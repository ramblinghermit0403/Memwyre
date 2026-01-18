import logging
import os
import asyncio
from typing import List, Dict, Any
from pinecone import Pinecone
from app.core.config import settings

# Configure logging
logger = logging.getLogger(__name__)

class VectorStore:
    def __init__(self):
        # Initialize Pinecone Client
        api_key = settings.PINECONE_API_KEY
        if not api_key:
            logger.warning("PINECONE_API_KEY not set. Vector store will fail.")
            
        self.pc = Pinecone(api_key=api_key)
        
        # Connect to Index
        # We use the host provided in settings to connect to the specific index
        self.index = self.pc.Index(host=settings.PINECONE_HOST)
        
        # Initialize Bedrock Embeddings Locally (Titan v2)
        try:
            from langchain_aws import BedrockEmbeddings
            self.bedrock_embeddings = BedrockEmbeddings(
                model_id="amazon.titan-embed-text-v2:0",
                region_name=os.getenv("AWS_REGION", "us-east-1")
            )
            logger.info("Initialized Bedrock Titan v2 Embeddings locally.")
        except Exception as e:
            logger.error(f"Failed to load Bedrock embeddings: {e}")
            self.bedrock_embeddings = None
        
    async def _async_get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings locally using Bedrock (Parallel).
        """
        import asyncio
        if not self.bedrock_embeddings:
            raise Exception("Bedrock embeddings not initialized")
            
        try:
            # Parallel execution for Titan v2
            tasks = [self.bedrock_embeddings.aembed_query(t) for t in texts]
            return await asyncio.gather(*tasks)
        except Exception as e:
            logger.error(f"Bedrock Async Embedding Failed: {e}")
            # Fallback
            return self.bedrock_embeddings.embed_documents(texts)

    async def add_documents(self, ids: List[str], documents: List[str], metadatas: List[Dict[str, Any]]):
        if not documents:
            return True

        vectors = []
        try:
            # Batch generate embeddings (Parallel)
            embeddings = await self._async_get_embeddings(documents)
            
            for i, doc in enumerate(documents):
                # Clean metadata
                clean_meta = {k: v for k, v in metadatas[i].items() if v is not None}
                # Add text to metadata for retrieval
                clean_meta["text_content"] = documents[i] 
    
                vectors.append({
                    "id": ids[i], 
                    "values": embeddings[i], 
                    "metadata": clean_meta
                })
            
            # Offload blocking IO to thread
            await asyncio.to_thread(self.index.upsert, vectors=vectors)
            return True
        except Exception as e:
            print(f"Pinecone Upsert Failed: {e}")
            return False

    async def query(self, query_texts: str, n_results: int = 5, where: Dict = None, include_values: bool = False) -> Dict:
        """
        Query Pinecone index asynchronously.
        """
        try:
            # 1. Generate embedding for query locally
            if not self.bedrock_embeddings:
                 return {"ids": [[]], "distances": [[]], "metadatas": [[]], "documents": [[]], "embeddings": [[]]}

            # Bedrock embedding is synchronous call usually fast or we can async it too?
            # embed_query is sync in BedrockEmbeddings? Titan v2 client is sync here?
            # Actually self.bedrock_embeddings.embed_query is blocking too if it uses boto3 sync client!
            # Let's wrap it just in case, or use aembed_query if available.
            # aembed_query was used above.
            
            query_embedding = await self.bedrock_embeddings.aembed_query(query_texts)
            
            if not query_embedding:
                return {"ids": [[]], "distances": [[]], "metadatas": [[]], "documents": [[]], "embeddings": [[]]}

            # 2. Query Pinecone (Blocking IO -> Thread)
            search_results = await asyncio.to_thread(
                self.index.query,
                vector=query_embedding,
                top_k=n_results,
                include_metadata=True,
                filter=where,
                include_values=include_values
            )
            
            # ... (rest of logic)
            
            # 3. Format results to match ChromaDB format
            ids = []
            distances = []
            metadatas = []
            documents = []
            embeddings = []

            for match in search_results["matches"]:
                ids.append(match["id"])
                # Pinecone returns similarity score (cosine). 
                distances.append(match["score"]) 
                
                meta = match["metadata"] if match["metadata"] else {}
                metadatas.append(meta)
                
                # Retrieve text from metadata
                documents.append(meta.get("text_content", ""))
                
                # Retrieve values if requested
                if include_values and match.get("values"):
                    embeddings.append(match["values"])

            return {
                "ids": [ids],
                "distances": [distances],
                "metadatas": [metadatas],
                "documents": [documents],
                "embeddings": [embeddings] if include_values else []
            }
            
        except Exception as e:
            print(f"Pinecone Query Failed: {e}")
            return {"ids": [[]], "distances": [[]], "metadatas": [[]], "documents": [[]], "embeddings": [[]]}

    async def delete(self, ids: List[str]):
        if not ids:
            return
        await asyncio.to_thread(self.index.delete, ids=ids)

vector_store = VectorStore()
