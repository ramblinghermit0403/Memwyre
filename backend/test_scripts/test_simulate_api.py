"""Direct test: simulate read_memories logic against the DB for user 4."""
import asyncio
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
os.environ["PYTHONIOENCODING"] = "utf-8"

from app.db.session import AsyncSessionLocal
from app.models.memory import Memory
from app.models.document import Document
from app.models.project import Project
from sqlalchemy import select, and_, or_, cast, String, not_
from datetime import datetime

async def main():
    user_id = 4
    async with AsyncSessionLocal() as db:
        # Replicate exact read_memories logic
        filters = [
            Memory.user_id == user_id,
            Memory.status == "approved",
            or_(Memory.source_llm.is_(None), Memory.source_llm != "agent"),
            not_(cast(Memory.tags, String).contains("auto-fact")),
        ]
        
        result_mem = await db.execute(select(Memory).where(and_(*filters)))
        memories = result_mem.scalars().all()
        print(f"Memories for user {user_id}: {len(memories)}")

        # Now documents
        result_doc = await db.execute(select(Document).where(Document.user_id == user_id))
        documents = result_doc.scalars().all()
        print(f"Documents for user {user_id}: {len(documents)}")
        
        for doc in documents:
            print(f"  Doc ID={doc.id}, title={doc.title}, created_at={doc.created_at}, doc_type={doc.doc_type}, file_type={getattr(doc, 'file_type', 'N/A')}")

        # Now try to build the results list as the API does
        results = []
        for mem in memories:
            created = mem.created_at
            results.append({
                "id": f"mem_{mem.id}",
                "title": mem.title,
                "content": mem.content,
                "user_id": mem.user_id,
                "created_at": created,
                "updated_at": mem.updated_at,
                "source": mem.source_llm,
                "source_app": mem.source_app or mem.source_llm,
                "interaction_type": mem.interaction_type or "conversation",
                "project_id": mem.project_id,
                "project_name": None,
                "timeline_group": created.strftime("%Y-%m-%d") if created else None,
                "tags": mem.tags,
                "doc_type": "memory",
                "type": "memory",
            })

        for doc in documents:
            doc_type = "memory" if doc.doc_type == "memory" else "document"
            results.append({
                "id": f"doc_{doc.id}",
                "title": doc.title or "Untitled Document",
                "content": doc.content if doc.content else f"Uploaded Document: {doc.source} ({doc.file_type})",
                "user_id": doc.user_id,
                "created_at": doc.created_at or datetime.now(),
                "updated_at": None,
                "source": doc.source,
                "source_app": doc.source,
                "interaction_type": "document",
                "project_id": None,
                "project_name": None,
                "doc_type": doc_type,
                "type": doc_type,
                "tags": doc.tags if doc.tags is not None else [],
            })

        print(f"\nTotal results: {len(results)}")

        # Now try Pydantic validation
        from app.schemas.memory import Memory as MemorySchema
        print("\nTesting Pydantic validation on each result...")
        for i, r in enumerate(results):
            try:
                validated = MemorySchema(**r)
            except Exception as e:
                print(f"  VALIDATION FAILED for item {i} (id={r.get('id')}): {e}")

        print("\nDone!")

asyncio.run(main())
