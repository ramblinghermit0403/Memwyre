import asyncio
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.db.session import AsyncSessionLocal
from app.models.document import Document
from app.models.memory import Memory
from sqlalchemy import select, and_, or_, cast, String, not_
from datetime import datetime

async def main():
    user_id = 11
    async with AsyncSessionLocal() as db:
        filters = [
            Memory.user_id == user_id,
            Memory.status == "approved",
            or_(Memory.source_llm.is_(None), Memory.source_llm != "agent"),
            not_(cast(Memory.tags, String).contains("auto-fact")),
        ]
        
        result_mem = await db.execute(select(Memory).where(and_(*filters)))
        memories = result_mem.scalars().all()
        print(f"Total Memories for User 11: {len(memories)}")
        for m in memories:
            print(f"Mem: {m.id}, {m.title}")

        result_doc = await db.execute(select(Document).where(Document.user_id == user_id))
        documents = result_doc.scalars().all()
        print(f"Total Documents for User 11: {len(documents)}")
        for d in documents:
            print(f"Doc: {d.id}, {d.title}")

asyncio.run(main())
