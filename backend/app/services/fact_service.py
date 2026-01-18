from typing import List, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_, update
from datetime import datetime
from sqlalchemy.sql import func
from app.models.fact import Fact

class FactService:
    # Predicates that typically imply a single current state
    SINGLE_VALUE_PREDICATES = {
        "lives_in", "located_in", "current_role", "job_title", 
        "employer", "current_status", "location", "phone_number", 
        "email_address", "is_active", "age"
    }

    async def create_facts(
        self, 
        facts_data: List[Dict[str, Any]], 
        user_id: int, 
        memory_id: int, 
        chunk_id: int, 
        db: AsyncSession
    ):
        """
        Create facts concurrently (Phase 1) then write sequentially (Phase 2).
        """
        import asyncio
        
        # Phase 1: Parallel Decision Making (Read-Only / LLM)
        # We prefer to pass a cloned DB session? No, just ensure we don't write.
        # Ideally we use a new session, but session creation is expensive-ish.
        # Actually, if we just READ (vector store, simple selects), it might be okay?
        # Vector Store is HTTP (Safe).
        # DB 'get' for supersede might be an issue if interleaved.
        # Let's extract the "Check" logic that doesn't need DB or uses it minimally.
        # The Check needs Vector Store (Mainly).
        # If "Supersede" decision is made, we return the Target ID.
        
        tasks = [
            self._analyze_fact(f_data, user_id)
            for f_data in facts_data
        ]
        
        decisions = []
        if tasks:
            decisions = await asyncio.gather(*tasks)
            
        # Phase 2: Sequential Execution (DB Writes)
        from app.services.vector_store import vector_store
        
        for i, decision_res in enumerate(decisions):
            f_data = facts_data[i]
            decision = decision_res.get("decision", "NEW")
            target_id = decision_res.get("target_id")
            
            if decision == "DUPLICATE":
                continue
                
            if decision == "SUPERSEDE" and target_id:
                # Mark old as superseded
                try:
                    target_f = await db.get(Fact, target_id)
                    if target_f:
                        target_f.valid_until = func.now()
                        target_f.is_superseded = True
                        db.add(target_f)
                except Exception as e:
                    print(f"Error superseding fact {target_id}: {e}")
            
            # Create NEW Fact
            subject = f_data.get("subject", "Unknown")
            predicate = f_data.get("predicate", "related_to")
            obj = f_data.get("object", "Unknown")
            confidence = f_data.get("confidence", 1.0)
            valid_from = f_data.get("valid_from")
            location = f_data.get("location", None)
            
            new_fact = Fact(
                user_id=user_id,
                subject=subject,
                predicate=predicate,
                object=obj,
                location=location,
                confidence=confidence,
                source_memory_id=memory_id,
                source_chunk_id=chunk_id,
                is_superseded=False
            )
            
            if valid_from:
                if isinstance(valid_from, str):
                    try:
                        new_fact.valid_from = datetime.fromisoformat(valid_from.replace('Z', '+00:00'))
                    except:
                        pass 
                elif isinstance(valid_from, datetime):
                     new_fact.valid_from = valid_from
                     
            db.add(new_fact)
            await db.flush() # Get ID
            
            # Index immediately
            if new_fact.id:
                try:
                    fact_text = f"{subject} {predicate} {obj}"
                    meta = {
                        "type": "fact",
                        "fact_id": str(new_fact.id),
                        "user_id": str(user_id),
                        "valid_from": str(new_fact.valid_from),
                        "source": "ingestion"
                    }
                    # We can't await vector store here individually if we want speed?
                    # But vector store adds are fast-ish.
                    # Or collect them and batch add at end?
                    # Batch add is better.
                    await vector_store.add_documents(
                        ids=[f"fact_{new_fact.id}"],
                        documents=[fact_text],
                        metadatas=[meta]
                    )
                except Exception as e:
                    print(f"Error indexing fact {new_fact.id}: {e}")

    async def _analyze_fact(self, f_data, user_id):
        """
        Analyze a fact to decide if it's new, duplicate, or superseding.
        NO DB WRITES. Returns Decision Dict.
        """
        subject = f_data.get("subject", "Unknown")
        predicate = f_data.get("predicate", "related_to")
        obj = f_data.get("object", "Unknown")
        fact_text = f"{subject} {predicate} {obj}"
        
        from app.services.vector_store import vector_store
        import json
        import re
        from langchain_aws import ChatBedrock
        from app.core.aws_config import AWS_CONFIG
        from langchain_core.messages import HumanMessage
        
        try:
            results = await vector_store.query(
                query_texts=fact_text,
                n_results=3,
                where={"user_id": str(user_id), "type": "fact"}
            )
            
            existing_candidates = []
            if results and results["ids"] and results["ids"][0]:
                for i, dist in enumerate(results["distances"][0]):
                    cand_id = results["ids"][0][i]
                    cand_text = results["documents"][0][i] if results["documents"] else ""
                    cand_meta = results["metadatas"][0][i]
                    cand_date = cand_meta.get("valid_from", "Unknown")
                    existing_candidates.append(f"[{cand_id}] Date: {cand_date} | Text: {cand_text}")
            
            if not existing_candidates:
                return {"decision": "NEW"}
                
            # LLM Judge
            new_date_str = f_data.get("valid_from", "Unknown")
            judge_prompt = f"""
            Fact Gatekeeper:
            New Fact: "{fact_text}" (Date: {new_date_str})
            
            Existing Similar Facts:
            {chr(10).join(existing_candidates)}
            
            Decide:
            1. DUPLICATE: New Fact adds NO new info AND refers to the same time period.
            2. SUPERSEDE: New Fact is MORE detailed/current/corrected version of the Old Fact. (Output ID to supersede).
            3. NEW: Different fact entirely OR refers to a Different Time (e.g. valid_from is significantly newer/different).
            
            Output JSON: {{"decision": "DUPLICATE" | "SUPERSEDE" | "NEW", "target_id": "fact_123"}}
            """
            
            llm = ChatBedrock(model_id="apac.amazon.nova-pro-v1:0", model_kwargs={"temperature": 0}, config=AWS_CONFIG)
            res = await llm.ainvoke([HumanMessage(content=judge_prompt)])
            
            clean_json = res.content.replace("```json", "").replace("```", "").strip()
            match = re.search(r'\{.*\}', clean_json, re.DOTALL)
            if match:
                data = json.loads(match.group())
                
                # Normalize target_id
                target_id = None
                if data.get("target_id") and "fact_" in str(data.get("target_id")):
                     try:
                         target_id = int(str(data.get("target_id")).split("_")[1])
                     except:
                         pass
                
                return {
                    "decision": data.get("decision", "NEW"),
                    "target_id": target_id
                }
                
        except Exception as e:
            print(f"Fact Analysis Failed: {e}")
            
        return {"decision": "NEW"}

            
    async def _supersede_old_facts(self, user_id: int, subject: str, predicate: str, db: AsyncSession):
        """
        Mark old facts as superseded (valid_until = now).
        """
        # Find active facts matching S, P
        stmt = select(Fact).where(
            Fact.user_id == user_id,
            Fact.subject == subject,
            Fact.predicate == predicate,
            Fact.valid_until == None,
            Fact.is_superseded == False
        )
        result = await db.execute(stmt)
        old_facts = result.scalars().all()
        
        if old_facts:
            print(f"FactService: Superseding {len(old_facts)} old facts for {subject} {predicate}")
            for fact in old_facts:
                fact.valid_until = func.now()
                fact.is_superseded = True
                db.add(fact)

fact_service = FactService()
