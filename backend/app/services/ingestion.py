"""
Ingestion Service: Handle text chunking and embedding generation
"""
from typing import List, Dict
from langchain_text_splitters import RecursiveCharacterTextSplitter
import uuid
import numpy as np
import numpy as np
import os
from langchain_aws import BedrockEmbeddings
import re
import json
import asyncio
from app.services.llm_service import llm_service
from app.core.aws_config import AWS_CONFIG
import boto3

class IngestionService:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Initialize the ingestion service with a text splitter.
        
        Args:
            chunk_size: Maximum size of each chunk
            chunk_overlap: Number of characters to overlap between chunks
        """
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        # Initialize semantic model
        try:
            # Create a boto3 client with custom config
            client = boto3.client("bedrock-runtime", region_name=os.getenv("AWS_REGION", "us-east-1"), config=AWS_CONFIG)
            
            self.bedrock_embeddings = BedrockEmbeddings(
                model_id="amazon.titan-embed-text-v2:0",
                client=client
            )
        except Exception as e:
            print(f"Warning: Failed to load Bedrock embeddings: {e}")
            self.bedrock_embeddings = None
    
    def chunk_text(self, text: str) -> List[str]:
        """
        Chunk text using RecursiveCharacterTextSplitter.
        """
        return self.text_splitter.split_text(text)
    
    async def process_text(
        self, 
        text: str, 
        document_id: int, 
        title: str, 
        doc_type: str = "memory",
        metadata: Dict = None,
        enrich: bool = True
    ) -> tuple[List[str], List[str], List[str], List[Dict]]:
        """
        Process text into chunks with metadata for vector store.
        Uses Semantic Chunking and LLM Enrichment.
        Now optimized with parallel processing.
        """
        # 1. Chunking (Wait for this, it's CPU + Embedding bound)
        if len(text) < 500:
             chunks = [text] 
        elif len(text) < 3000:
             chunks = self.text_splitter.split_text(text)
        else:
             chunks = await self.semantic_chunk_text(text) # Now Async!
        
        base_metadata = {
            "document_id": document_id,
            "title": title,
            "type": doc_type
        }
        if metadata:
            base_metadata.update(metadata)
        
        # 2. Enrichment (Parallelized)
        enrichment_tasks = []
        if enrich:
            for chunk_text in chunks:
                enrichment_tasks.append(llm_service.generate_chunk_enrichment(chunk_text))
        
        # Execute Enrichment concurrently
        enrichment_results = []
        if enrichment_tasks:
            # return_exceptions=True prevents one failure from killing others immediately,
            # but we want to inspect them and potentially fail the batch.
            enrichment_results = await asyncio.gather(*enrichment_tasks, return_exceptions=True)
        else:
            enrichment_results = [None] * len(chunks)

        embedding_ids = []
        chunk_texts = []
        metadatas = []
        
        # Check for failures before processing
        for res in enrichment_results:
            if isinstance(res, Exception):
                # If ANY chunk failed enrichment, fail the whole batch to trigger Celery retry.
                # This prevents "Ghost Chunks" (chunks with no metadata).
                print(f"Enrichment failed: {res}. Raising exception to trigger retry.")
                raise res
        enriched_chunk_texts = [] # Text to be embedded
        
        # Assemble Results
        for i, chunk_text in enumerate(chunks):
            embedding_id = str(uuid.uuid4())
            embedding_ids.append(embedding_id)
            chunk_texts.append(chunk_text)
            
            chunk_metadata = base_metadata.copy()
            chunk_metadata["chunk_index"] = i
            
            # Process Enrichment Result
            result = enrichment_results[i] if i < len(enrichment_results) else None
            
            summary = ""
            qas = []
            entities = []
            
            if isinstance(result, Exception):
                print(f"Enrichment failed for chunk {i}: {result}")
            elif result:
                summary = result.get("summary", "")
                qas = result.get("generated_qas", [])
                entities = result.get("entities", [])
            
            chunk_metadata["summary"] = summary
            chunk_metadata["generated_qas"] = json.dumps(qas)
            chunk_metadata["entities"] = json.dumps(entities)
            
            # Construct Enriched Text
            enriched_text = chunk_text
            if summary or qas:
                enrichment_context = f"\n\n-- Context --\nSummary: {summary}\n"
                if qas:
                    enrichment_context += "Q&A:\n"
                    for qa in qas:
                            if isinstance(qa, dict):
                                enrichment_context += f"Q: {qa.get('question', '')}\nA: {qa.get('answer', '')}\n"
                            elif isinstance(qa, str):
                                enrichment_context += f"{qa}\n"
                enriched_text += enrichment_context
            
            enriched_chunk_texts.append(enriched_text)
            metadatas.append(chunk_metadata)
        
        return embedding_ids, chunk_texts, enriched_chunk_texts, metadatas

    async def semantic_chunk_text(self, text: str, threshold: float = 0.5) -> List[str]:
        """
        Split text semantically using cosine similarity of adjacent sentences.
        Parallelized embedding generation.
        """
        # Split sentences
        sentences = re.split(r'(?<=[.?!])\s+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if not sentences: return []
        if len(sentences) == 1: return sentences
        
        # Optimized Parallel Embedding Generation
        try:
            # Create concurrent tasks for each sentence
            # Titan v2 requires single inputs, so we fire them all at once.
            tasks = [self.bedrock_embeddings.aembed_query(s) for s in sentences]
            embeddings = await asyncio.gather(*tasks)
        except Exception as e:
            print(f"Bedrock Parallel Embedding failed: {e}")
            # Fallback to sync call if async fails for some reason
            try:
                embeddings = self.bedrock_embeddings.embed_documents(sentences)
            except Exception as inner_e:
                print(f"Fallback Embedding failed: {inner_e}")
                return self.text_splitter.split_text(text)
            
        # Optimization: Vectorized Cosine Similarity
        embeddings_np = np.array(embeddings) # Shape: (N, D)
        
        # Compute Norms
        norms = np.linalg.norm(embeddings_np, axis=1) # Shape: (N,)
        
        # Compute Dot Products for adjacent pairs
        # dot(v[i-1], v[i]) for i=1..N-1
        vec_a = embeddings_np[:-1]
        vec_b = embeddings_np[1:]
        dots = np.sum(vec_a * vec_b, axis=1)
        
        # Compute Cosine Similarities
        norm_products = norms[:-1] * norms[1:]
        similarities = np.zeros_like(dots)
        
        # Avoid division by zero
        nonzero = norm_products > 1e-9
        similarities[nonzero] = dots[nonzero] / norm_products[nonzero]
        
        # Form Chunks
        chunks = []
        current_chunk = [sentences[0]]
        
        for i in range(1, len(sentences)):
            sim = similarities[i-1] 
            
            if sim < threshold and len(" ".join(current_chunk)) > 150: 
                chunks.append(" ".join(current_chunk))
                current_chunk = [sentences[i]]
            else:
                if len(" ".join(current_chunk)) + len(sentences[i]) > 2000:
                     chunks.append(" ".join(current_chunk))
                     current_chunk = [sentences[i]]
                else:
                    current_chunk.append(sentences[i])
                
        if current_chunk:
            chunks.append(" ".join(current_chunk))
            
        return chunks

    def count_tokens(self, text: str) -> int:
        """
        Estimate token count (approx 4 chars per token).
        """
        if not text:
            return 0
        return len(text) // 4

ingestion_service = IngestionService()
