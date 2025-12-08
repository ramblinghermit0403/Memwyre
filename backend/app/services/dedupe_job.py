from sqlalchemy.orm import Session
from app.models.memory import Memory
from app.models.cluster import MemoryCluster
from app.services.vector_store import vector_store
from app.services.websocket import manager
import asyncio
import json

class DedupeService:
    def check_duplicates(self, memory_id: int, db: Session):
        """
        Check if a new memory is duplicate of existing ones.
        """
        try:
            # Get new memory
            memory = db.query(Memory).filter(Memory.id == memory_id).first()
            if not memory:
                return
                
            # If it has no embedding yet (pending), we might need to generate one specifically for search
            # But the requirement says "compute embedding for new memory".
            # For MVP, let's assume if it's pending it might not be in vector store yet?
            # Actually, `save_memory` didn't put it in Vector Store if pending.
            # So we can't query Vector Store *with* it, but we can query *for* it using its text.
            
            results = vector_store.query(memory.content, n_results=5, where={"user_id": memory.user_id})
            
            # Check distances/similarities
            # Chroma returns distances. Lower is better.
            # Convert to similarity? 
            # Let's assume a threshold for distance. (e.g. < 0.3 for cosine distance)
            
            similar_ids = []
            if results["ids"]:
                for i, _ in enumerate(results["ids"][0]):
                    dist = results["distances"][0][i] if results["distances"] else 1.0
                    metadata = results["metadatas"][0][i] if results["metadatas"] else {}
                    
                    if dist < 0.3: # Threshold
                        # Extract memory_id from metadata
                        mem_id_val = metadata.get("memory_id")
                        if mem_id_val:
                            try:
                                similar_ids.append(int(mem_id_val))
                            except:
                                pass
                        
            if similar_ids:
                # Remove duplicates and self
                similar_ids = list(set([sid for sid in similar_ids if sid != memory_id]))
                
                if similar_ids:
                    # Create Cluster Suggestion
                    cluster = MemoryCluster(
                        user_id=memory.user_id,
                        memory_ids=json.dumps(similar_ids + [memory.id]),
                        representative_text=f"Cluster centered on: {memory.title}",
                        status="pending"
                    )
                    db.add(cluster)
                    db.commit()
                    
                    # Notify User via Inbox
                    # Use personal message
                    asyncio.create_task(manager.send_personal_message({
                        "type": "new_cluster", 
                        "cluster_id": cluster.id,
                        "count": len(similar_ids) + 1
                    }, user_id=str(memory.user_id)))
                    
        except Exception as e:
            print(f"Dedupe job failed: {e}")

    async def run_periodic_check(self, db_session_factory):
        """
        Periodically run dedupe checks or other background maintenance.
        For MVP, we might just sleep and check "pending" memories or clusters.
        Realistically, dedupe triggers on insertion. 
        This background job could be for batch processing or reprocessing.
        """
        while True:
            try:
                # Example: Check for pending clusters that need auto-merging (if we had that feature)
                # Or just keep alive.
                # For now, we do nothing but sleep to simulate a background worker available for future tasks
                await asyncio.sleep(60) 
            except Exception as e:
                print(f"Background job error: {e}")
                await asyncio.sleep(60)

dedupe_service = DedupeService()
