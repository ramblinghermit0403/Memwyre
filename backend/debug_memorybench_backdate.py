import asyncio
import requests
from datetime import datetime

BASE_URL = "http://localhost:8000/api/v1"
# Hardcoded token or login flow needed. 
# Since this is a test script running locally, I might need to simulate a login or use a known token.
# Assuming I can't easily login without creds. 
# I will use the app code directly to test the logic if API is blocked.
# Actually, I can use `app/main.py` context or just use `AsyncSessionLocal` directly? 
# The logic is in the ROUTER, so I must test via Router or mocking the request. 
# Testing via router needs dependencies override. 

# Alternative: Test directly using dependency overrides or simply manually inspecting logic?
# I'll try to run a python script that imports the router function? No, dependencies issues.
# I'll assume the API is running (uvicorn is running). I need a token.
# I will try to login first.

EMAIL = "test@example.com" # Hopefully exists or I can register
PASSWORD = "password"

async def test_backdate():
    # 1. Login
    # Note: Need to know a valid user.
    # If I can't login, I will inspect code logic.
    # But I see 'uvicorn' running on 8000.
    # I'll try to read `debug_location_persistence.py` to see how it got user.
    # It queried DB.
    
    # Direct DB + Logic Test is easier than HTTP if I don't have creds.
    # But the logic is in the ROUTER.
    
    # Let's try HTTP with a made up token? No.
    # I'll rely on a unit test style:
    
    from app.schemas.memory import MemoryCreate
    from app.routers.memory import create_memory
    from app.models.user import User
    from app.db.session import AsyncSessionLocal
    from sqlalchemy import select
    from fastapi import BackgroundTasks
    
    print("Testing create_memory logic directly...")
    
    async with AsyncSessionLocal() as db:
        # Get user
        result = await db.execute(select(User).limit(1))
        user = result.scalars().first()
        if not user:
            print("No user found.")
            return

        # Case 1: With Tag + Date
        input_1 = MemoryCreate(
            title="Backdate Test",
            content="This happened in 2020",
            tags=["memorybench", "test"],
            created_at=datetime(2020, 1, 1, 12, 0, 0)
        )
        
        # Mock background tasks
        bg = BackgroundTasks()
        
        # Call router function directly (bypassing auth/dependencies injection, passing manually)
        try:
            mem_1 = await create_memory(
                memory_in=input_1,
                background_tasks=bg,
                db=db,
                current_user=user
            )
            # Need to refresh to see DB state if not returned updated
            # mem_1 is the ORM object returned
            print("\nTest 1 (Tag='memorybench', Date='2020'):")
            print(f"Result Created At: {mem_1.created_at}")
            
            if mem_1.created_at.year == 2020:
                print("PASS: Backdating worked.")
            else:
                print("FAIL: Backdating ignored.")
                
        except Exception as e:
            print(f"Error test 1: {e}")

        # Case 2: Without Tag
        input_2 = MemoryCreate(
            title="Normal Test",
            content="This happened today",
            tags=["other"],
            created_at=datetime(2020, 1, 1, 12, 0, 0) # Should be ignored
        )
        
        try:
             mem_2 = await create_memory(
                memory_in=input_2,
                background_tasks=bg,
                db=db,
                current_user=user
            )
             print("\nTest 2 (Tag='other', Date='2020'):")
             print(f"Result Created At: {mem_2.created_at}")
             
             if mem_2.created_at.year != 2020:
                 print("PASS: Date ignored as expected (no tag).")
             else:
                 print("FAIL: Date was used but tag was missing!")
                 
        except Exception as e:
            print(f"Error test 2: {e}")

if __name__ == "__main__":
    asyncio.run(test_backdate())
