print("Loading app.worker module...")
from app.celery_app import celery_app
from app.services.metadata_extraction import metadata_service
from app.services.dedupe_job import dedupe_service
from app.services.ingestion import ingestion_service
from app.services.vector_store import vector_store
from app.db.session import AsyncSessionLocal
from app.models.memory import Memory
from app.models.document import Chunk
# Import ChatSession to ensure relationship mapper works
from app.models.chat import ChatSession
from sqlalchemy.future import select
import asyncio
import json

# Helper to run async code in sync Celery task
def run_async(coro):
    loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(coro)
    finally:
        loop.close()

@celery_app.task(acks_late=True)
def process_memory_metadata_task(memory_id: int, user_id: int):
    """
    Background task for auto-tagging and metadata extraction.
    """
    print(f"Worker: Starting metadata extraction for memory {memory_id}")
    
    async def _process_metadata():
        async with AsyncSessionLocal() as db:
            await metadata_service.process_memory_metadata(memory_id, user_id, db)
            
    run_async(_process_metadata())

@celery_app.task(acks_late=True)
def dedupe_memory_task(memory_id: int):
    """
    Background task for duplicate detection.
    """
    print(f"Worker: Starting dedupe check for memory {memory_id}")
    
    async def _dedupe():
        async with AsyncSessionLocal() as db:
            await dedupe_service.check_duplicates(memory_id, db)

    run_async(_dedupe())

@celery_app.task(acks_late=True)
def ingest_memory_task(memory_id: int, user_id: int, content: str, title: str, tags: list = None, source: str = None):
    """
    Background task for ingestion (Chunking + Vector Store).
    Doing this in worker prevents blocking API during heavy embedding generation.
    """
    print(f"Worker: Starting ingestion for memory {memory_id}")
    
    # We pass content/title explicitly to avoid fetching if possible, 
    # but we need to update the DB with embedding_id, so we'll need a session anyway.
    
    async def _ingest():
        try:
            # 1. Process Text (CPU bound, maybe API bound for embeddings)
            ids, documents_content, enriched_chunk_texts, metadatas = await ingestion_service.process_text(
                text=content,
                document_id=memory_id,
                title=title,
                doc_type="memory",
                metadata={
                    "user_id": user_id, 
                    "memory_id": memory_id, 
                    "tags": str(tags) if tags else "", 
                    "source": source
                }
            )
            
            if ids:
                # 2. Add to Vector Store (Use Enriched Text)
                try:
                    vector_store.add_documents(
                        ids=ids,
                        documents=enriched_chunk_texts, # Embed ENRICHED text
                        metadatas=metadatas
                    )
                except Exception as e:
                    print(f"Worker Error Adding to Vector Store: {e}")
                    return

                # 3. Update DB with embedding_id AND Save Chunks (Async)
                async with AsyncSessionLocal() as db:
                     # Update Memory
                     result = await db.execute(select(Memory).where(Memory.id == memory_id))
                     memory = result.scalars().first()
                     if memory:
                         memory.embedding_id = ids[0]
                         db.add(memory)

                     # NEW: Save Chunks
                     for i, (embedding_id, chunk_content) in enumerate(zip(ids, documents_content)):
                        meta = metadatas[i]
                        
                        # Parse JSON fields safely
                        qas = []
                        if meta.get("generated_qas"):
                             try:
                                 qas = json.loads(meta.get("generated_qas"))
                             except:
                                 pass
                        
                        entities = []
                        if meta.get("entities"):
                             try:
                                 entities = json.loads(meta.get("entities"))
                             except:
                                 pass

                        chunk = Chunk(
                            memory_id=memory_id, # Link to Memory
                            chunk_index=i,
                            text=chunk_content,
                            embedding_id=embedding_id,
                            summary=meta.get("summary"),
                            generated_qas=qas,
                            entities=entities,
                            metadata_json=meta
                        )
                        db.add(chunk)
                     
                     await db.commit()
                     print(f"Worker: Ingestion complete for memory {memory_id}")
            else:
                 print(f"Worker: No chunks generated for memory {memory_id}")

        except Exception as e:
            print(f"Worker Ingestion Failed: {e}")

    run_async(_ingest())
