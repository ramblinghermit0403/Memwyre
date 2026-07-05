"""
Ingestion Service: Handle text chunking and embedding generation
"""
from typing import List, Dict, Any
from langchain_text_splitters import RecursiveCharacterTextSplitter
import uuid
import numpy as np
import numpy as np
import os
import re
import json
import asyncio
from app.services.llm_service_v2 import llm_service_v2 as llm_service
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
            from app.core.rate_limiter import get_embeddings_instance
            self.embeddings = get_embeddings_instance()
        except Exception as e:
            print(f"Warning: Failed to load embeddings: {e}")
            self.embeddings = None
    
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
        enrich: bool = True,
        extract_facts: bool = False,
        reference_date = None
    ) -> tuple[List[str], List[str], List[str], List[Dict], List[Any]]:
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
        
        # 2. Enrichment & Fact Extraction (Fully concurrent, managed by global semaphore)
        enrichment_results = []
        fact_results = []
        
        if enrich or extract_facts:
            from app.services.llm_service_v2 import llm_service_v2 as llm_service
            all_tasks = []
            
            # Queue enrichment tasks
            if enrich:
                for chunk_text in chunks:
                    all_tasks.append(llm_service.generate_chunk_enrichment(chunk_text))
            
            # Queue fact extraction tasks
            if extract_facts:
                for chunk_text in chunks:
                    all_tasks.append(llm_service.extract_facts_from_text(chunk_text, reference_date=reference_date))
                    
            # Run everything concurrently (controlled by the global semaphore)
            results = await asyncio.gather(*all_tasks, return_exceptions=True)
            
            # Separate the results back into enrichment and facts
            if enrich:
                enrichment_results = results[:len(chunks)]
                if extract_facts:
                    fact_results = results[len(chunks):]
                else:
                    fact_results = [None] * len(chunks)
            else:
                enrichment_results = [None] * len(chunks)
                if extract_facts:
                    fact_results = results
                else:
                    fact_results = [None] * len(chunks)
        else:
            enrichment_results = [None] * len(chunks)
            fact_results = [None] * len(chunks)

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
        
        return embedding_ids, chunk_texts, enriched_chunk_texts, metadatas, fact_results

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
        
        # Batched Embedding Generation (25 at a time to prevent OOM)
        EMBED_BATCH_SIZE = 25
        try:
            embeddings = []
            for batch_start in range(0, len(sentences), EMBED_BATCH_SIZE):
                batch = sentences[batch_start:batch_start + EMBED_BATCH_SIZE]
                batch_results = await self.embeddings.aembed_documents(batch)
                embeddings.extend(batch_results)
        except Exception as e:
            print(f"Azure Batched Embedding failed: {e}")
            # Fallback to sync call if async fails for some reason
            try:
                embeddings = self.embeddings.embed_documents(sentences)
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

ingestion_service_v2 = IngestionService()
