import json
import re
from typing import List, Dict, Any, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.entity_profile import EntityProfile
from langchain_core.messages import HumanMessage
from app.services.vector_store_v2 import vector_store_v2 as vector_store
import asyncio

class ProfileService:

    async def update_profiles(self, entity_facts: Dict[str, List[str]], user_id: int, db: AsyncSession, project_id: Optional[int] = None):
        from app.services.llm_service_v2 import llm_service_v2
        
        if not entity_facts:
            return
            
        llm = llm_service_v2._get_default_llm(temperature=0)
        
        # Normalize keys/names (capitalize)
        normalized_entity_facts = {}
        for entity_name, facts in entity_facts.items():
            if isinstance(entity_name, str) and len(entity_name.strip()) > 1:
                normalized_entity_facts[entity_name.strip().capitalize()] = facts
                
        entities = list(normalized_entity_facts.keys())
        entities.sort() # Alphabetical sorting prevents deadlocks under concurrent runs
        if not entities:
            return
            
        # Fetch all existing profiles in one query (with lock to prevent races)
        stmt = select(EntityProfile).where(
            EntityProfile.user_id == user_id,
            EntityProfile.entity_name.in_(entities)
        )
        if project_id is not None:
            stmt = stmt.where(EntityProfile.project_id == project_id)
        else:
            stmt = stmt.where(EntityProfile.project_id.is_(None))
            
        stmt = stmt.with_for_update()
        
        result = await db.execute(stmt)
        existing_profiles = {p.entity_name.capitalize(): p for p in result.scalars().all()}
        
        # Prepare LLM tasks
        llm_tasks = []
        entity_profile_map = {}
        
        for entity_name in entities:
            profile = existing_profiles.get(entity_name)
            if not profile:
                profile = EntityProfile(
                    user_id=user_id,
                    project_id=project_id,
                    entity_name=entity_name,
                    profile_data={
                        "demographics": {},
                        "activities_and_hobbies": [],
                        "relationships": {},
                        "pets": [],
                        "career_and_education": [],
                        "preferences": []
                    }
                )
                db.add(profile)
                
            entity_profile_map[entity_name] = profile
            current_json_str = json.dumps(profile.profile_data, indent=2)
            facts = normalized_entity_facts[entity_name]
            
            update_prompt = f"""
            You are a Profile Manager. You will be given a user's CURRENT JSON profile and a list of NEW facts.
            Your job is to extract relevant facts and merge them into the JSON profile for the entity: {entity_name}.
            
            Rules:
            1. Do not delete existing list items unless explicitly contradicted.
            2. Append new hobbies, pets, or friends to their respective arrays without duplicating.
            3. If there are facts that don't fit the existing keys, you may create new logical keys.
            4. Output ONLY the updated JSON.
            
            CURRENT JSON PROFILE:
            {current_json_str}
            
            NEW FACTS:
            {json.dumps(facts, indent=2)}
            """
            
            # Queue LLM invocation
            llm_tasks.append((entity_name, llm.ainvoke([HumanMessage(content=update_prompt)])))

        if not llm_tasks:
            return
            
        print(f"ProfileService: Calling LLM concurrently for {len(llm_tasks)} entities...")
        names, tasks = zip(*llm_tasks)
        llm_results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Process results sequentially to ensure safe DB transaction mapping
        vectors_to_add = []
        for entity_name, res in zip(names, llm_results):
            if isinstance(res, Exception):
                print(f"ProfileService: LLM update failed for {entity_name}: {res}")
                continue
                
            try:
                upd_clean_json = res.content.replace("```json", "").replace("```", "").strip()
                upd_match = re.search(r'\{.*\}', upd_clean_json, re.DOTALL)
                if upd_match:
                    updated_data = json.loads(upd_match.group())
                    profile = entity_profile_map[entity_name]
                    profile.profile_data = updated_data
                    
                    db.add(profile)
                    await db.flush() # Ensure we get profile.id if it's new
                    
                    # Prepare vector indexing string
                    profile_string = f"{entity_name} Profile:\n"
                    for k, v in updated_data.items():
                        profile_string += f"{k}: {json.dumps(v)}\n"
                        
                    meta = {
                        "type": "profile",
                        "entity_name": entity_name,
                        "user_id": str(user_id),
                        "profile_id": str(profile.id)
                    }
                    if project_id is not None:
                        meta["project_id"] = str(project_id)
                    
                    vectors_to_add.append((f"profile_{profile.id}", profile_string, meta))
                    print(f"ProfileService: Profile for {entity_name} processed.")
                else:
                    print(f"ProfileService: No JSON match found in LLM response for {entity_name}: {upd_clean_json[:200]}")
            except Exception as e:
                print(f"ProfileService: Failed to parse/save profile for {entity_name}: {e}")
        
        # Batch write all updated profiles to Vector Store
        if vectors_to_add:
            try:
                ids = [v[0] for v in vectors_to_add]
                docs = [v[1] for v in vectors_to_add]
                metas = [v[2] for v in vectors_to_add]
                await vector_store.add_documents(ids=ids, documents=docs, metadatas=metas)
                print(f"ProfileService: Batched indexed {len(vectors_to_add)} profiles to vector store.")
            except Exception as e:
                print(f"ProfileService: Failed to write profiles to vector store: {e}")

profile_service = ProfileService()
