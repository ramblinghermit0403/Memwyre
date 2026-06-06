import asyncio
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.db.session import AsyncSessionLocal
from app.models.document import Document
from app.models.memory import Memory
from sqlalchemy import select

async def main():
    async with AsyncSessionLocal() as db:
        docs = await db.execute(select(Document))
        documents = docs.scalars().all()
        print(f"Total Documents in DB: {len(documents)}")
        for d in documents:
            print(f"Doc {d.id} User: {d.user_id} Title: {d.title}")

        mems = await db.execute(select(Memory))
        memories = mems.scalars().all()
        print(f"Total Memories in DB: {len(memories)}")
        for m in memories:
            print(f"Mem {m.id} User: {m.user_id} Title: {m.title}")

asyncio.run(main())
