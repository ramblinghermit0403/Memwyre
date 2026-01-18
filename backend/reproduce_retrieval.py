
import asyncio
import sys
import os

# Add backend to path
sys.path.append(os.getcwd())

from app.db.session import AsyncSessionLocal
from app.services.retrieval_service import retrieval_service
from app.models.user import User
from sqlalchemy.future import select

async def main():
    async with AsyncSessionLocal() as db:
        # Get a user (Assuming ID 1 or 4 based on logs)
        # Log showed user_id=4
        user_id = 4
        
        print(f"--- Searching for 'Caroline' (Facts) for User {user_id} ---")
        results = await retrieval_service.search_memories(
            query="Caroline",
            user_id=user_id,
            db=db,
            top_k=5,
            view="state"
        )
        
        print(f"Found {len(results)} results.")
        for i, res in enumerate(results):
            chunk = res.get("chunk")
            fact_id = res['metadata'].get('fact_id')
            print(f"[{i}] Fact ID: {fact_id} | Chunk Present: {chunk is not None}")
            if chunk:
                print(f"    Chunk ID: {chunk.id}")
                print(f"    Chunk Text: {chunk.text[:50]}...")
            else:
                print("    Chunk is NULL!")

if __name__ == "__main__":
    asyncio.run(main())
