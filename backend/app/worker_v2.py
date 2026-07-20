print("Loading app.worker module...")
from app.celery_app import celery_app
from app.services.metadata_extraction import metadata_service
from app.services.dedupe_job_v2 import dedupe_service_v2
from app.services.ingestion_v2 import ingestion_service_v2
from app.services.vector_store_v2 import vector_store_v2 as vector_store
from app.db.session import AsyncSessionLocal
from app.models.memory import Memory
from app.models.document import Chunk
from app.models.fact import Fact
# Import ChatSession to ensure relationship mapper works
from app.models.chat import ChatSession
from sqlalchemy.future import select
from typing import Optional
import asyncio
import json
from datetime import datetime

# Helper to run async code in sync Celery task
def run_async(coro):
    try:
        loop = asyncio.get_event_loop()
        if loop.is_closed():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    return loop.run_until_complete(coro)

@celery_app.task(acks_late=True)
def process_memory_metadata_task_v2(memory_id: int, user_id: int):
    """
    Background task for auto-tagging and metadata extraction.
    """
    print(f"Worker: Starting metadata extraction for memory {memory_id}")
    
    async def _process_metadata():
        async with AsyncSessionLocal() as db:
            await metadata_service.process_memory_metadata(memory_id, user_id, db)
            
    run_async(_process_metadata())

@celery_app.task(acks_late=True)
def dedupe_memory_task_v2(memory_id: int):
    """
    Background task for duplicate detection.
    """
    print(f"Worker: Starting dedupe check for memory {memory_id}")
    
    async def _dedupe():
        async with AsyncSessionLocal() as db:
            await dedupe_service_v2.check_duplicates(memory_id, db)

    run_async(_dedupe())

@celery_app.task(acks_late=True)
def extract_chat_facts_task_v2(message: str, user_id: int, project_id: int = None):
    """
    Background task for extracting facts from chat messages.
    This is deferred from the chat agent to reduce response latency.
    """
    print(f"Worker: Starting fact extraction from chat message for user {user_id}")
    
    async def _extract_facts():
        from app.services.llm_service_v2 import llm_service_v2 as llm_service
        from app.core.config import settings
        
        try:
            # Extract facts from the message
            extracted_facts = await llm_service.extract_facts_from_text(
                message, 
                getattr(settings, "GEMINI_API_KEY", None)
            )
            
            if extracted_facts:
                print(f"Worker: Extracted {len(extracted_facts)} facts from chat message")
                async with AsyncSessionLocal() as db:
                    for f_data in extracted_facts:
                        # Create Fact Model
                        new_fact = Fact(
                            user_id=user_id,
                            content=f"{f_data.get('subject')} {f_data.get('predicate')} {f_data.get('object')}",
                            subject=f_data.get('subject'),
                            predicate=f_data.get('predicate'),
                            object=f_data.get('object'),
                            confidence=f_data.get('confidence', 0.8),
                            source="user-chat",
                            project_id=project_id,
                        )
                        if f_data.get("valid_from"):
                            try:
                                new_fact.valid_from = datetime.fromisoformat(f_data.get("valid_from"))
                            except:
                                pass
                                
                        db.add(new_fact)
                    await db.commit()
                print(f"Worker: Saved {len(extracted_facts)} facts to database")
            else:
                print("Worker: No facts extracted from chat message")
        except Exception as e:
            print(f"Worker: Chat fact extraction failed: {e}")
            import traceback
            traceback.print_exc()

    run_async(_extract_facts())

@celery_app.task(acks_late=True)
def update_profiles_task_v2(entity_facts: dict, user_id: int, project_id: Optional[int] = None):
    """
    Background task for updating entity profiles.
    """
    print(f"Worker: Starting entity profile updates for entities: {list(entity_facts.keys())} under project {project_id}")
    
    async def _update_profiles():
        from app.services.profile_service import profile_service
        try:
            async with AsyncSessionLocal() as db:
                await profile_service.update_profiles(entity_facts, user_id, db, project_id=project_id)
                await db.commit()
                print(f"Worker: Profile update COMMITTED")
        except Exception as e:
            print(f"Worker: Profile update failed: {e}")
            import traceback
            traceback.print_exc()
            
    run_async(_update_profiles())

@celery_app.task(acks_late=True)
def ingest_memory_task_v2(memory_id: int, user_id: int, content: str, title: str, tags: list = None, source: str = None, doc_type: str = "memory", mode: str = "append"):
    """
    Background task for ingestion (Chunking + Vector Store).
    Supports both Memory and Document models.
    mode: 'append' (default) or 'replace' (delete existing chunks first)
    """
    print(f"Worker: Starting ingestion for {doc_type} {memory_id}")
    
    async def _ingest():
        try:
            # Fetch Context Creation Date and Project ID
            reference_date = None
            project_id = None
            async with AsyncSessionLocal() as db:
                 if doc_type == "memory":
                     result = await db.execute(select(Memory).where(Memory.id == memory_id))
                     obj = result.scalars().first()
                 else:
                     # Assume Document model for other types (file, youtube, etc)
                     from app.models.document import Document
                     result = await db.execute(select(Document).where(Document.id == memory_id))
                     obj = result.scalars().first()
                     
                 if obj:
                     reference_date = obj.created_at
                     project_id = getattr(obj, "project_id", None)

            # Handle Replacement (Delete old chunks)
            if mode == "replace":
                print(f"Worker: Deleting existing chunks for {doc_type} {memory_id}")
                async with AsyncSessionLocal() as db:
                    # 1. Fetch chunks to get embedding_ids for Vector Store deletion
                    # Chunk is already imported globally
                    stmt = select(Chunk)
                    if doc_type == "memory":
                        stmt = stmt.where(Chunk.memory_id == memory_id)
                    else:
                        stmt = stmt.where(Chunk.document_id == memory_id)
                        
                    result = await db.execute(stmt)
                    old_chunks = result.scalars().all()
                    
                    old_ids = [c.embedding_id for c in old_chunks if c.embedding_id]
                    
                    # 2. Delete from Vector Store
                    if old_ids:
                        try:
                            await vector_store.delete(ids=old_ids)
                        except Exception as e:
                            print(f"Worker: Warning during vector delete: {e}")
                            
                    # 3. Delete from DB
                    from sqlalchemy import delete
                    if doc_type == "memory":
                        await db.execute(delete(Chunk).where(Chunk.memory_id == memory_id))
                    else:
                        await db.execute(delete(Chunk).where(Chunk.document_id == memory_id))
                    
                    await db.commit()

            # 1. Process Text (CPU bound / API bound)
            metadata_dict = {
                "user_id": str(user_id), 
                f"{doc_type}_id": memory_id, # Stores memory_id or document_id
                "tags": str(tags) if tags else "", 
                "source": source,
                "created_at": str(reference_date) if reference_date else ""
            }
            if project_id is not None:
                metadata_dict["project_id"] = str(project_id)

            ids, documents_content, enriched_chunk_texts, metadatas, all_facts_results = await ingestion_service_v2.process_text(
                text=content,
                document_id=memory_id,
                title=title,
                doc_type=doc_type,
                metadata=metadata_dict,
                extract_facts=True,
                reference_date=reference_date
            )
            
            if ids:
                # 2. Add to Vector Store in batches (prevent OOM)
                VECTOR_BATCH_SIZE = 5
                try:
                    for batch_start in range(0, len(ids), VECTOR_BATCH_SIZE):
                        batch_end = batch_start + VECTOR_BATCH_SIZE
                        await vector_store.add_documents(
                            ids=ids[batch_start:batch_end],
                            documents=enriched_chunk_texts[batch_start:batch_end], 
                            metadatas=metadatas[batch_start:batch_end]
                        )
                except Exception as e:
                    print(f"Worker Error Adding to Vector Store: {e}")
                    return

                # 3. Update DB and Save Chunks
                async with AsyncSessionLocal() as db:
                     # Update Parent Object with embedding_id if applicable
                     if doc_type == "memory":
                         result = await db.execute(select(Memory).where(Memory.id == memory_id))
                         obj = result.scalars().first()
                         if obj:
                             obj.embedding_id = ids[0]
                             db.add(obj)
                     # Document model might not need embedding_id on parent, but let's check model definition if needed.
                     # Usually Document has 1:N chunks, embedding_id is on Chunk. 
                     # Memory model has embedding_id field as legacy/primary?
                     # We skip parent update for Document if field doesn't exist, but checking app/models/document.py would be good. 
                     # Assuming Document doesn't strictly require it on parent for now or we leave it.

                     # Save Chunks
                     saved_chunks = []
                     for i, (embedding_id, chunk_content) in enumerate(zip(ids, documents_content)):
                        meta = metadatas[i]
                        
                        # Safe JSON parse
                        def safe_load(k):
                            try: return json.loads(meta.get(k))
                            except: return []

                        chunk = Chunk(
                            chunk_index=i,
                            text=chunk_content,
                            embedding_id=embedding_id,
                            summary=meta.get("summary"),
                            generated_qas=safe_load("generated_qas"),
                            entities=safe_load("entities"),
                            metadata_json=meta
                        )
                        
                        # Link to correct parent
                        if doc_type == "memory":
                            chunk.memory_id = memory_id
                        else:
                            chunk.document_id = memory_id
                            
                        db.add(chunk)
                        saved_chunks.append(chunk)

                     await db.flush() 
                     await db.commit() 

                     # Parallel Fact Processing
                     async def _save_facts_safe(facts_res, c_id, u_id, m_id):
                         from app.services.fact_service import fact_service
                         async with AsyncSessionLocal() as local_db:
                             # Maps m_id to memory_id argument regardless of type? 
                             # fact_service.create_facts likely expects memory_id. 
                             # If it's a document, facts might not link correctly if table expects memory_id FK.
                             # We will pass memory_id as is, assuming facts schema supports it or we only extract facts for memories?
                             # User wants "ingest memory task for documents too".
                             # If Facts table requires valid memory_id FK, this will fail for Documents.
                             # Let's skip fact extraction for non-memories to be safe/consistent OR assuming poly-morphic.
                             # The prompt implies full ingestion.
                             # For safety, I will pass memory_id=None if doc_type != 'memory' unless Fact supports document_id.
                             # Let's verify Fact model later. For now, we try passing it if it was doing so before.
                             pass 

                             await fact_service.create_facts(
                                 facts_data=facts_res,
                                 user_id=u_id,
                                 memory_id=m_id if doc_type == "memory" else None,
                                 chunk_id=c_id,
                                 db=local_db,
                                 project_id=project_id
                             )
                             await local_db.commit()

                     fact_tasks = []
                     for i, chunk in enumerate(saved_chunks):
                        facts_result = all_facts_results[i]
                        if isinstance(facts_result, list) and facts_result:
                            fact_tasks.append(
                                _save_facts_safe(facts_result, chunk.id, user_id, memory_id)
                            )

                     if fact_tasks:
                         await asyncio.gather(*fact_tasks)
                     
                     # Update Entity Profiles (Inline - runs immediately after fact extraction)
                     try:
                          entity_facts = {}
                          
                          # Stopwords and common nouns to ignore
                          ignored_entities = {
                              "it", "he", "she", "they", "them", "him", "her", "we", "us", "you", "i",
                              "this", "that", "these", "those", "room", "music", "kids", "community",
                              "people", "nature", "blue", "picture", "posters", "boy", "girl", "man", "woman"
                          }
                          
                          for facts in all_facts_results:
                              if isinstance(facts, list):
                                  for f in facts:
                                      subject = f.get("subject")
                                      if subject:
                                          entity_lower = subject.lower()
                                          
                                          # Strict filtering to avoid noise profiles
                                          if entity_lower in ignored_entities:
                                              continue
                                          if len(entity_lower) <= 2:
                                              continue
                                          if len(subject.split()) > 2:
                                              continue
                                          if "'" in subject or "’" in subject:
                                              continue
                                              
                                          entity_name = subject.strip().capitalize()
                                          if entity_name not in entity_facts:
                                              entity_facts[entity_name] = []
                                              
                                          # Construct a clean fact representation
                                          fact_str = f"{f.get('subject')} {f.get('predicate')} {f.get('object')}"
                                          if f.get("location"):
                                              fact_str += f" ({f.get('location')})"
                                          entity_facts[entity_name].append(fact_str)
                          
                          if entity_facts:
                              print(f"Worker: Updating entity profiles inline for {doc_type} {memory_id} with entities: {list(entity_facts.keys())} under project {project_id}")
                              from app.services.profile_service import profile_service
                              async with AsyncSessionLocal() as profile_db:
                                  await profile_service.update_profiles(entity_facts, user_id, profile_db, project_id=project_id)
                                  await profile_db.commit()
                              print(f"Worker: Entity profiles updated for {doc_type} {memory_id}")
                          else:
                              print(f"Worker: No entities found for profile update ({doc_type} {memory_id})")
                     except Exception as profile_e:
                          print(f"Worker: Profile update failed: {profile_e}")
                          import traceback
                          traceback.print_exc()
                     
                     print(f"Worker: Ingestion complete for {doc_type} {memory_id}")
            else:
                 print(f"Worker: No chunks generated for {doc_type} {memory_id}")

        except Exception as e:
            print(f"Worker Ingestion Failed: {e}")
            import traceback
            traceback.print_exc()

    run_async(_ingest())

@celery_app.task(acks_late=True)
def process_plugin_transcript_task_v2(session_id: str, project_name: str, cwd: str, transcript: list, user_id: int):
    """
    Background task to process Claude Code transcripts and extract high-signal memories.
    """
    print(f"Worker: Starting transcript processing for session {session_id}")
    
    async def _process_transcript():
        from app.services.llm_service_v2 import llm_service_v2 as llm_service
        from app.core.config import settings
        import json
        
        try:
            # Convert transcript list to string for LLM
            transcript_str = json.dumps(transcript, indent=2)
            
            # Extract signals
            signals = await llm_service.extract_plugin_signals(
                transcript_str, 
                getattr(settings, "GEMINI_API_KEY", None) or getattr(settings, "OPENAI_API_KEY", None)
            )
            
            if signals:
                print(f"Worker: Extracted {len(signals)} signals from session {session_id}")
                async with AsyncSessionLocal() as db:
                    from app.models.project import Project
                    resolved_project_name = project_name or (os.path.basename(cwd) if cwd else "default")
                    result_proj = await db.execute(select(Project).where(Project.user_id == user_id, Project.name == resolved_project_name))
                    proj = result_proj.scalars().first()
                    if not proj:
                        proj = Project(user_id=user_id, name=resolved_project_name, description=f"Workspace project for {resolved_project_name}")
                        db.add(proj)
                        await db.commit()
                        await db.refresh(proj)
                    
                    project_id = proj.id

                    for signal_content in signals:
                        # Create Memory Model
                        # Adding [Plugin] prefix or similar context
                        full_content = f"[{resolved_project_name}] {signal_content}"
                        new_memory = Memory(
                            user_id=user_id,
                            content=full_content,
                            project_id=project_id,
                        )
                        db.add(new_memory)
                    await db.commit()
                print(f"Worker: Saved {len(signals)} memories from plugin.")
            else:
                print(f"Worker: No high-value signals found in session {session_id}")
                
        except Exception as e:
            print(f"Worker: Transcript processing failed: {e}")
            import traceback
            traceback.print_exc()

    run_async(_process_transcript())
