from typing import List, Any, Dict, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime, timezone
from sqlalchemy.orm import selectinload
from app.models.document import Chunk
from app.services.vector_store import vector_store

class RetrievalService:
    async def search_memories(
        self, 
        query: str, 
        user_id: int, 
        db: AsyncSession, 
        top_k: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Search for relevant document chunks with re-ranking based on feedback.
        Returns a list of dictionaries with text, score, and metadata.
        """
        # 1. Vector Search
        results = vector_store.query(query, n_results=top_k, where={"user_id": user_id})
        
        if not results["ids"] or not results["ids"][0]:
            return []
            
        # 2. Fetch Rich Metadata from DB (Chunks)
        top_ids = results["ids"][0]
        distances = results["distances"][0] if results["distances"] else [0.0] * len(top_ids)
        
        # Async fetch with Eager Loading for Recency Calculation
        query_stmt = (
            select(Chunk)
            .options(selectinload(Chunk.memory), selectinload(Chunk.document))
            .where(Chunk.embedding_id.in_(top_ids))
        )
        db_res = await db.execute(query_stmt)
        chunks = db_res.scalars().all()
        chunk_map = {c.embedding_id: c for c in chunks}
        
        formatted_results = []
        
        for i, emb_id in enumerate(top_ids):
            chunk = chunk_map.get(emb_id)
            distance = distances[i]
            base_score = max(0, 1 - distance) # Simple conversion
            
            if chunk:
                # 3. Apply Re-ranking modifiers
                feedback_mod = 1 + (chunk.feedback_score or 0.0)
                trust_mod = chunk.trust_score or 0.5
                
                # Recency Logic
                recency_mod = 1.0
                created_at = None
                if chunk.memory:
                    created_at = chunk.memory.created_at
                elif chunk.document:
                    created_at = chunk.document.created_at
                
                if created_at:
                    # ensure timezone awareness
                    if created_at.tzinfo is None:
                        created_at = created_at.replace(tzinfo=timezone.utc)
                    
                    now = datetime.now(timezone.utc)
                    days_diff = (now - created_at).days
                    # Boost: +10% for today/yesterday, decays to ~0% after a month
                    # Formula: 1 + (0.1 / max(1, days_diff))
                    recency_mod = 1 + (0.1 / max(1, days_diff))
                
                final_score = base_score * feedback_mod * (0.5 + trust_mod) * recency_mod
                
                # Enrich response
                meta = results["metadatas"][0][i]
                meta["summary"] = chunk.summary
                meta["generated_qas"] = chunk.generated_qas
                meta["trust_score"] = chunk.trust_score
                meta["memory_id"] = chunk.id # Add DB ID for reference
                meta["recency_boost"] = round(recency_mod, 2)
                
                formatted_results.append({
                    "text": chunk.text, # Return DB text which is reliable
                    "score": final_score,
                    "metadata": meta,
                    "chunk": chunk # Return actual chunk object if needed
                })
            else:
                # Fallback if DB sync issue
                formatted_results.append({
                    "text": results["documents"][0][i],
                    "score": base_score,
                    "metadata": results["metadatas"][0][i],
                    "chunk": None
                })
                
        # Sort by final score desc
        formatted_results.sort(key=lambda x: x["score"], reverse=True)
        
        return formatted_results

retrieval_service = RetrievalService()
