from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.memory import Memory
from app.models.cluster import MemoryCluster
from app.services.vector_store_v2 import vector_store_v2 as vector_store
from app.services.websocket import manager
from app.db.session import AsyncSessionLocal
import asyncio
import json
from redis import asyncio as aioredis
from app.core.config import settings

class DedupeService:
    async def check_duplicates(self, memory_id: int, db: AsyncSession = None):
        """
        Check if a new memory is duplicate of existing ones.
        If db is provided, use it. Otherwise create a new session.
        Warning: If running in background task after request, do NOT pass request-scoped db.
        """
        if db:
            await self._process_dedupe(memory_id, db)
        else:
            async with AsyncSessionLocal() as session:
                await self._process_dedupe(memory_id, session)

    async def _publish_update(self, payload: dict, user_id: str = None):
        """
        Publish update to Redis channel for Uvicorn to broadcast.
        """
        if not settings.CELERY_BROKER_URL:
            return

        try:
            redis = aioredis.from_url(settings.CELERY_BROKER_URL)
            message = {
                "type": "message",
                "target_type": "personal" if user_id else "broadcast",
                "user_id": str(user_id) if user_id else None,
                "payload": payload
            }
            await redis.publish("brain_vault_updates", json.dumps(message))
            await redis.close()
        except Exception as e:
            print(f"Dedupe: Failed to publish Redis update: {e}")

    async def _process_dedupe(self, memory_id: int, db: AsyncSession):
        try:
            print(f"Dedupe Service: Checking updates/conflicts for memory {memory_id}")
            result = await db.execute(select(Memory).where(Memory.id == memory_id))
            memory = result.scalars().first()
            if not memory:
                return
            
            print("Dedupe: Querying vector store for potential conflicts...")
            try:
                # Query only against existing facts
                where_dict = {"user_id": str(memory.user_id), "type": "fact"}
                if memory.project_id is not None:
                    where_dict["project_id"] = str(memory.project_id)
                results = await vector_store.query(memory.content, n_results=5, where=where_dict)
                num_matches = len(results.get('ids', [[]])[0]) if results.get('ids') else 0
                print(f"Dedupe: Vector store returned {num_matches} candidate facts")
            except Exception as vs_e:
                print(f"Dedupe: Vector store query failed: {vs_e}")
                raise vs_e
            
            existing_facts = []
            
            if results.get("ids") and results["ids"][0]:
                for i, doc_id in enumerate(results["ids"][0]):
                    dist = results["distances"][0][i] if results.get("distances") else 0.0
                    metadata = results["metadatas"][0][i] if results.get("metadatas") else {}
                    text = results["documents"][0][i] if results.get("documents") else ""
                    
                    # Ensure we don't match against self if doc_id somehow equals memory_id
                    match_id_val = metadata.get("memory_id")
                    if str(match_id_val) == str(memory_id):
                        continue
                        
                    similarity = dist * 100
                    if similarity > 40: 
                        fact_id = doc_id.replace("fact_", "") if str(doc_id).startswith("fact_") else metadata.get("fact_id") or metadata.get("source_id") or doc_id
                        if fact_id and text:
                            existing_facts.append({
                                "id": str(fact_id),
                                "text": text
                            })
                            
            if existing_facts:
                print(f"Dedupe: Evaluating {len(existing_facts)} existing facts for conflicts...")
                from app.services.llm_service_v2 import llm_service_v2 as llm_service
                evaluations = await llm_service.evaluate_memory_relations(memory.content, existing_facts)
                
                superseded_fact_ids = []
                for eval_res in evaluations:
                    if eval_res.get("relationship") == "UPDATES":
                        fid = eval_res.get("fact_id")
                        if fid:
                            try:
                                superseded_fact_ids.append(int(fid))
                            except ValueError:
                                pass
                                
                if superseded_fact_ids:
                    from app.models.fact import Fact
                    from sqlalchemy import update
                    await db.execute(
                        update(Fact)
                        .where(Fact.id.in_(superseded_fact_ids))
                        .values(is_superseded=True)
                    )
                    await db.commit()
                    print(f"Dedupe: Superseded old facts: {superseded_fact_ids}")
                    
                    current_tags = memory.tags or []
                    if "update" not in current_tags:
                        new_tags = list(current_tags)
                        new_tags.append("update")
                        memory.tags = new_tags
                        await db.commit()
            
            await self._publish_update({
                "type": "inbox_update", 
                "id": f"mem_{memory.id}", 
                "action": "analyzed"
            })
                    
        except Exception as e:
            print(f"Dedupe job failed: {e}")

    async def run_periodic_check(self, db_session_factory):
        """
        Periodically run dedupe checks or other background maintenance.
        """
        while True:
            try:
                await asyncio.sleep(60) 
            except Exception as e:
                print(f"Background job error: {e}")
                await asyncio.sleep(60)

dedupe_service_v2 = DedupeService()
