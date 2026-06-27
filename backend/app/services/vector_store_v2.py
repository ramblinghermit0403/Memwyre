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
        
        # Initialize Azure Embeddings Locally
        try:
            from langchain_openai import AzureOpenAIEmbeddings
            
            api_key = getattr(settings, "AZURE_OPENAI_API_KEY", None) or getattr(settings, "OPENAI_API_KEY", None) or os.environ.get("AZURE_OPENAI_API_KEY")
            if not api_key:
                logger.error("Missing Azure OpenAI API Key. Embeddings will fail.")
            
            self.embeddings = AzureOpenAIEmbeddings(
                api_key=api_key,
                azure_endpoint=getattr(settings, "AZURE_OPENAI_ENDPOINT", "https://memwyre.cognitiveservices.azure.com/"),
                api_version=getattr(settings, "AZURE_OPENAI_API_VERSION", "2024-12-01-preview"),
                azure_deployment=getattr(settings, "AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-small"),
                dimensions=512
            )
            logger.info("Initialized Azure OpenAI Embeddings locally.")
        except Exception as e:
            import traceback
            logger.error(f"Failed to load Azure embeddings: {e}")
            logger.error(traceback.format_exc())
            self.embeddings = None
        
    from tenacity import retry, stop_after_attempt, wait_exponential
    
    @retry(stop=stop_after_attempt(4), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def _async_get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings locally using Azure OpenAI (Batched to save RPM).
        """
        if not self.embeddings:
            raise Exception("Azure embeddings not initialized")
            
        # Use batched documents embedding (1 API request instead of N)
        return await self.embeddings.aembed_documents(texts)

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
            if not self.embeddings:
                 return {"ids": [[]], "distances": [[]], "metadatas": [[]], "documents": [[]], "embeddings": [[]]}

            # Azure OpenAI embedding is synchronous call usually fast or we can async it too?
            # Let's wrap it just in case, or use aembed_query if available.
            # aembed_query was used above.
            
            query_embedding = await self.embeddings.aembed_query(query_texts)
            
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

vector_store_v2 = VectorStore()
