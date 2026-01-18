import asyncio
import sys
import os
import logging
from dotenv import load_dotenv

# Add backend to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()

from app.services.retrieval_service import retrieval_service
from app.services.fact_service import fact_service
from app.db.session import AsyncSessionLocal
from app.models.fact import Fact
from sqlalchemy.future import select

# Enable logging
logging.basicConfig(level=logging.INFO)

async def test_proposition():
    print("--- Testing Memory Proposition Architecture ---")
    
    async with AsyncSessionLocal() as db:
        # 1. Setup User
        # Fetch any user
        from app.models.user import User
        result = await db.execute(select(User).limit(1))
        user = result.scalars().first()
        if not user:
            print("No user found. Skipping test.")
            return

        user_id = user.id
        print(f"Testing with User ID: {user_id}")

        # 2. Setup Dummy Memory/Chunk for FK constraints
        from app.models.memory import Memory
        from app.models.document import Chunk
        
        dummy_mem = Memory(user_id=user_id, content="Dummy Memory", title="Dummy")
        db.add(dummy_mem)
        await db.commit()
        await db.refresh(dummy_mem)
        
        dummy_chunk = Chunk(memory_id=dummy_mem.id, text="Dummy Chunk", chunk_index=0)
        db.add(dummy_chunk)
        await db.commit()
        await db.refresh(dummy_chunk)
        
        mem_id = dummy_mem.id
        chunk_id = dummy_chunk.id

        # 3. Test Supersession (lives_in)
        print("\n[Test 1] Supersession Logic:")
        
        # Fact 1: I live in Berlin
        fact1_data = [{"subject": "User", "predicate": "lives_in", "object": "Berlin", "confidence": 1.0}]
        await fact_service.create_facts(fact1_data, user_id, mem_id, chunk_id, db)
        await db.commit()
        print("  Created Fact: User lives_in Berlin")
        
        # Fact 2: I live in Tokyo (Should supersede Berlin)
        fact2_data = [{"subject": "User", "predicate": "lives_in", "object": "Tokyo", "confidence": 1.0}]
        await fact_service.create_facts(fact2_data, user_id, mem_id, chunk_id, db)
        await db.commit()
        print("  Created Fact: User lives_in Tokyo")
        
        # Verify Database State
        stmt = select(Fact).where(Fact.user_id == user_id, Fact.predicate == "lives_in").order_by(Fact.created_at)
        facts = (await db.execute(stmt)).scalars().all()
        
        passed_supersession = False
        for f in facts:
            status = "CURRENT" if f.valid_until is None else f"SUPERSEDED (until {f.valid_until})"
            print(f"    - {f.object}: {status}")
            if f.object == "Berlin" and f.valid_until is not None:
                passed_supersession = True
            elif f.object == "Tokyo" and f.valid_until is None:
                pass # Expected
                
        if passed_supersession:
            print("  SUCCESS: Old fact was superseded.")
        else:
            print("  FAILURE: Old fact was NOT superseded.")

        # 3. Test Retrieval (State View)
        print("\n[Test 2] State Retrieval View:")
        query = "Where do I live?"
        results = await retrieval_service.search_memories(query, user_id, db, top_k=5, view="state")
        
        print("  Results for 'Where do I live?':")
        passed_retrieval = False
        for res in results:
            print(f"    - {res['text']} (Score: {res['score']})")
            if "Tokyo" in res['text']:
                passed_retrieval = True
                
        if passed_retrieval:
            print("  SUCCESS: Retrieved current state (Tokyo).")
        else:
            print("  FAILURE: Did not retrieve Tokyo.")
            
        # Clean up (Optional, but good for repeatability)
        # Delete facts created
        # await db.delete(facts...)
        
if __name__ == "__main__":
    asyncio.run(test_proposition())
