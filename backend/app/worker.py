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
            # Fetch Memory created_at for Date Context
            reference_date = None
            async with AsyncSessionLocal() as db:
                 result = await db.execute(select(Memory).where(Memory.id == memory_id))
                 mem = result.scalars().first()
                 if mem:
                     reference_date = mem.created_at

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
                    "source": source,
                    "created_at": str(reference_date) if reference_date else ""
                }
            )
            
            if ids:
                # 2. Add to Vector Store (Use Enriched Text)
                try:
                    await vector_store.add_documents(
                        ids=ids,
                        documents=enriched_chunk_texts, # Embed ENRICHED text
                        metadatas=metadatas
                    )
                except Exception as e:
                    print(f"Worker Error Adding to Vector Store: {e}")
                    return

                # 3. Parallel Fact Extraction (Optimized with Semaphore)
                from app.services.llm_service import llm_service
                from app.services.fact_service import fact_service
                
                print(f"Worker: Starting parallel fact extraction for {len(documents_content)} chunks with date context {reference_date}...")
                
                # Limit concurrency to prevent Rate Limits and DB Pool Exhaustion
                # 5-10 is a safe sweet spot for Bedrock/LLM APIs per worker thread
                sem = asyncio.Semaphore(10) 

                async def _bounded_extraction(txt, ref_dt):
                    async with sem:
                        return await llm_service.extract_facts_from_text(txt, reference_date=ref_dt)

                extraction_tasks = [_bounded_extraction(text, reference_date) for text in documents_content]
                # Execute all LLM calls concurrently (throttled)
                all_facts_results = await asyncio.gather(*extraction_tasks, return_exceptions=True)

                # 4. Update DB with embedding_id AND Save Chunks/Facts
                async with AsyncSessionLocal() as db:
                     # Update Memory
                     result = await db.execute(select(Memory).where(Memory.id == memory_id))
                     memory = result.scalars().first()
                     if memory:
                         memory.embedding_id = ids[0]
                         db.add(memory)

                     # Save Chunks first to get IDs
                     saved_chunks = []
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
                        saved_chunks.append(chunk)

                     await db.flush() # Get all Chunk IDs at once
                     await db.commit() # Commit so parallel sessions can see Chunks

                     # Parallel Fact Processing for ALL chunks
                     # Helper to run fact saving in its own session to avoid sharing collision
                     async def _save_facts_safe(facts_res, c_id, u_id, m_id):
                         async with sem: # Reuse semaphore to limit DB connections
                             async with AsyncSessionLocal() as local_db:
                                 await fact_service.create_facts(
                                     facts_data=facts_res,
                                     user_id=u_id,
                                     memory_id=m_id,
                                     chunk_id=c_id,
                                     db=local_db
                                 )
                                 await local_db.commit()

                     fact_tasks = []
                     for i, chunk in enumerate(saved_chunks):
                        facts_result = all_facts_results[i]
                        
                        if isinstance(facts_result, list) and facts_result:
                            fact_tasks.append(
                                _save_facts_safe(facts_result, chunk.id, user_id, memory_id)
                            )
                        elif isinstance(facts_result, Exception):
                            print(f"Worker Fact Extraction Failed for Chunk {i}: {facts_result}")

                     if fact_tasks:
                         print(f"Worker: processing {len(fact_tasks)} chunks of facts concurrently (throttled)...")
                         await asyncio.gather(*fact_tasks)
                     
                     print(f"Worker: Ingestion complete for memory {memory_id}")
            else:
                 print(f"Worker: No chunks generated for memory {memory_id}")

        except Exception as e:
            print(f"Worker Ingestion Failed: {e}")

    run_async(_ingest())
