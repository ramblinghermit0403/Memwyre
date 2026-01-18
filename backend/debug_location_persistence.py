import asyncio
from app.db.session import AsyncSessionLocal
from app.services.llm_service import llm_service
from app.services.fact_service import fact_service
from app.models.fact import Fact
from sqlalchemy import select
from datetime import datetime

from app.models.user import User

async def test_location_persistence():
    text = "Caroline painted the painting on the beach today."
    
    async with AsyncSessionLocal() as db:
        result = await db.execute(select(User).limit(1))
        user = result.scalars().first()
        if not user:
            print("FAIL: No user found to test with.")
            return
        user_id = user.id
        print(f"Using User ID: {user_id}")
    
    print(f"1. Extracting from: '{text}'...")
    facts_data = await llm_service.extract_facts_from_text(text)
    
    if not facts_data:
        print("FAIL: No facts extracted.")
        return

    print(f"Extracted Data: {facts_data}")
    
    loc = facts_data[0].get("location")
    if not loc or "beach" not in loc.lower():
        print(f"FAIL: Location not extracted correctly. Got: {loc}")
        # Note: Depending on LLM, it might put it in Object still if confused, 
        # but we updated the prompt.
    else:
        print(f"SUCCESS: Extracted Location: {loc}")

    print("\n2. Saving to DB...")
    async with AsyncSessionLocal() as db:
        await fact_service.create_facts(facts_data, user_id, 1, 1, db)
        await db.commit()
        
        # 3. Validating
        print("\n3. Validating DB Persistence...")
        stmt = select(Fact).where(Fact.user_id == user_id, Fact.location.is_not(None)).order_by(Fact.created_at.desc()).limit(1)
        result = await db.execute(stmt)
        fact = result.scalar_one_or_none()
        
        if fact:
            print(f"DB Fact Found: ID={fact.id}")
            print(f"Subject: {fact.subject}")
            print(f"Predicate: {fact.predicate}")
            print(f"Object: {fact.object}")
            print(f"Location: {fact.location}")
            
            if "beach" in fact.location.lower():
                 print("PASS: Location successfully saved to SQL.")
            else:
                 print("FAIL: Location content mismatch in DB.")
        else:
            print("FAIL: Fact not found in DB.")

if __name__ == "__main__":
    asyncio.run(test_location_persistence())
