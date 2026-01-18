from typing import List, Any
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import uuid
import random
from datetime import datetime, timedelta
from sqlalchemy import or_
from sqlalchemy.orm import selectinload

from app.api import deps
from app.models.user import User
from app.models.memory import Memory
from app.schemas.memory import Memory as MemorySchema, MemoryCreate, MemoryUpdate
from app.services.vector_store import vector_store
from app.services.ingestion import ingestion_service
from app.services.metadata_extraction import metadata_service
from app.db.session import AsyncSessionLocal
from app.worker import process_memory_metadata_task, ingest_memory_task, dedupe_memory_task


router = APIRouter()

@router.get("/agent-facts", response_model=List[MemorySchema])
async def get_agent_facts(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Retrieve memories created by agents (source_llm='agent' or tags=['auto-fact']).
    """
    from sqlalchemy import cast, String
    result = await db.execute(
        select(Memory).where(
            Memory.user_id == current_user.id,
            or_(
                Memory.source_llm == "agent",
                cast(Memory.tags, String).contains("auto-fact")
            )
        ).order_by(Memory.created_at.desc())
    )
    return result.scalars().all()

@router.get("/tags", response_model=List[str])
async def get_all_tags(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get all unique tags used by the current user.
    """
    # Fetch all memories with tags for this user
    result = await db.execute(select(Memory.tags).where(
        Memory.user_id == current_user.id, 
        Memory.tags != None
    ))
    memories = result.all()
    
    unique_tags = set()
    for mem in memories:
        # mem is a Row
        tags_val = mem.tags if hasattr(mem, 'tags') else mem[0]
        if tags_val:
            for tag in tags_val:
                if tag:
                    unique_tags.add(tag)
                    
    return sorted(list(unique_tags))



@router.post("/", response_model=MemorySchema)
async def create_memory(
    memory_in: MemoryCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Create new memory.
    """
    print(f"Creating memory for user: {current_user.id}")
    print(f"Memory data: {memory_in}")
    
    # Generate embedding ID
    embedding_id = str(uuid.uuid4())
    
    # Check Auto-Approve Setting
    auto_approve = True
    user_settings = current_user.settings
    # ... Same logic ...
    
    if user_settings:
        if isinstance(user_settings, str):
            import json
            try:
                user_settings = json.loads(user_settings)
            except:
                user_settings = {}
                
        if isinstance(user_settings, dict):
            auto_approve = user_settings.get("auto_approve", True)
            
    initial_status = "approved" if auto_approve else "pending"
    
    is_extension = "extension" in (memory_in.tags or [])
    
    show_in_inbox = True 
    if initial_status == "approved" and not is_extension:
        show_in_inbox = False
        
    memory = Memory(
        title=memory_in.title,
        content=memory_in.content,
        user_id=current_user.id,
        tags=memory_in.tags,
        embedding_id=embedding_id,
        status=initial_status,
        show_in_inbox=show_in_inbox
    )
    
    # MemoryBench Patch: Allow backdating if explicitly tagged
    normalized_tags = [t.lower() for t in (memory_in.tags or [])]
    if "memorybench" in normalized_tags and memory_in.created_at:
        print(f"Applying MemoryBench backdate: {memory_in.created_at}")
        memory.created_at = memory_in.created_at
    else:
        print(f"No backdate applied. Tags: {memory_in.tags}, CreatedAt: {memory_in.created_at}")
        
    db.add(memory)
    try:
        await db.commit()
        print("Memory committed to DB")
    except Exception as e:
        print(f"Error committing to DB: {e}")
        await db.rollback()
        raise e
        
    await db.refresh(memory)
    print(f"Memory ID: {memory.id}")
    
    # Trigger Background Analysis (Auto-Tagging + Similarity) via Celery
    process_memory_metadata_task.delay(memory.id, current_user.id)
    
    # Ingest and Add to Vector DB via Celery
    if initial_status == "approved":
        ingest_memory_task.delay(
            memory.id,
            current_user.id,
            memory_in.content,
            memory_in.title,
            memory_in.tags,
            "user"
        )

    # Trigger Dedupe Job (Background Celery)
    dedupe_memory_task.delay(memory.id)

    
    return memory

from app.models.document import Document

class CheckDuplicateRequest(BaseModel):
    content: str

@router.post("/check-duplicate", response_model=Any)
async def check_duplicate(
    request: CheckDuplicateRequest,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Check if content is similar to existing memories (Real-time check).
    """
    if not request.content or len(request.content) < 10:
        return {"is_duplicate": False, "percent": 0.0}
        
    try:
        results = await vector_store.query(request.content, n_results=1, where={"user_id": current_user.id})
        
        if results["ids"] and results["distances"]:
             dist = results["distances"][0][0]
             similarity = (1 - dist) * 100
             
             if similarity > 70:
                 metadata = results["metadatas"][0][0]
                 return {
                     "is_duplicate": True,
                     "percent": round(similarity, 1),
                     "existing_id": metadata.get("memory_id"),
                     "title": metadata.get("source_id", "Unknown") # Or fetch title from DB if needed
                 }
                 
        return {"is_duplicate": False, "percent": 0.0}
    except Exception as e:
        print(f"Check duplicate failed: {e}")
        return {"is_duplicate": False, "percent": 0.0}

@router.get("/", response_model=List[MemorySchema])
async def read_memories(
    skip: int = 0,
    limit: int = 100,
    tag: str | None = None,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Retrieve memories and documents.
    """
    from sqlalchemy import not_, cast, String, and_
    
    # Build query filters
    filters = [
        Memory.user_id == current_user.id,
        Memory.status == "approved",
        or_(Memory.source_llm.is_(None), Memory.source_llm != "agent"),
        not_(cast(Memory.tags, String).contains("auto-fact"))
    ]
    
    if tag:
        filters.append(cast(Memory.tags, String).contains(tag))

    # Fetch Memories
    result_mem = await db.execute(select(Memory).where(and_(*filters)))
    memories = result_mem.scalars().all()
    
    # Fetch Documents
    result_doc = await db.execute(select(Document).where(Document.user_id == current_user.id))
    documents = result_doc.scalars().all()
    
    results = []
    
    for mem in memories:
        results.append({
            "id": f"mem_{mem.id}",
            "title": mem.title,
            "content": mem.content,
            "user_id": mem.user_id,
            "created_at": mem.created_at,
            "updated_at": mem.updated_at,
            "tags": mem.tags,
            "type": "memory"
        })
        
    for doc in documents:
        # Check if document is actually a memory
        doc_type = "memory" if doc.doc_type == "memory" else "document"
        
        results.append({
            "id": f"doc_{doc.id}",
            "title": doc.title,
            "content": doc.content if doc.content else f"Uploaded Document: {doc.source} ({doc.file_type})",
            "user_id": doc.user_id,
            "created_at": doc.created_at,
            "updated_at": None,
            "type": doc_type,
            "tags": doc.tags
        })
    
    # Sort by created_at desc
    results.sort(key=lambda x: x["created_at"], reverse=True)
    
    # Apply pagination
    return results[skip : skip + limit]

@router.get("/review", response_model=Any)
async def get_daily_review(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get the previous 5 memories for review.
    """
    # Simply fetch the 5 most recent approved memories
    result = await db.execute(
        select(Memory).where(
            Memory.user_id == current_user.id,
            Memory.status == "approved"
        ).order_by(Memory.created_at.desc()).limit(5)
    )
    memories = result.scalars().all()
    
    results = []
    for mem in memories:
        results.append({
            "id": f"mem_{mem.id}",
            "title": mem.title,
            "content": mem.content,
            "created_at": mem.created_at,
            "tags": mem.tags,
            "reason": "recent"
        })
        
    return results

@router.put("/{memory_id}", response_model=MemorySchema)
async def update_memory(
    memory_id: str,
    memory_in: MemoryUpdate,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Update a memory.
    """
    if memory_id.startswith("doc_"):
        raise HTTPException(status_code=400, detail="Cannot edit documents via memory editor")
        
    if "_" in memory_id:
        real_id = int(memory_id.split("_")[1])
    else:
        try:
            real_id = int(memory_id)
        except ValueError:
             raise HTTPException(status_code=400, detail="Invalid ID format")
    
    result = await db.execute(select(Memory).where(Memory.id == real_id, Memory.user_id == current_user.id))
    memory = result.scalars().first()
    if not memory:
        raise HTTPException(status_code=404, detail="Memory not found")
    
    memory.title = memory_in.title
    memory.content = memory_in.content
    memory.tags = memory_in.tags
    await db.commit()
    await db.refresh(memory)
    
    # Update Vector DB (Delete old, add new)
    if memory.embedding_id:
        # If we have a single embedding_id stored, delete it. 
        # But if we switch to chunking, we might have multiple.
        # The Memory model only has one embedding_id column.
        # This implies the original design didn't support chunking for memories properly, 
        # or it stored the ID of the first chunk?
        # create_memory generates one embedding_id for the Memory object, 
        # but ingestion_service generates new IDs for chunks.
        # We should probably delete by metadata filter if possible, but vector_store.delete takes IDs.
        # For now, let's delete the one we know.
        await vector_store.delete(ids=[memory.embedding_id])
    
    # Chunk and process
    # Chunk and process
    # Chunk and process
    ids, documents_content, enriched_chunk_texts, metadatas, sparse_values = await ingestion_service.process_text(
        text=memory.content,
        document_id=memory.id, # Using memory.id as document_id for ingestion
        title=memory.title,
        doc_type="memory",
        metadata={"user_id": current_user.id, "memory_id": memory.id, "tags": str(memory.tags) if memory.tags else ""}
    )
    
    
    # Update memory with the first embedding ID
    if ids:
        memory.embedding_id = ids[0]
        # Save Chunks to DB
        from app.models.document import Chunk
        import json
        
        # Delete existing chunks for this memory first?
        # Ideally yes, if we are re-processing content.
        # But 'chunks' relationship defaults to append unless we clear.
        # memory.chunks is a relationship.
        # Let's delete old ones manually to be safe.
        # But wait, Chunk model has memory_id.
        await db.execute(select(Chunk).where(Chunk.memory_id == memory.id).execution_options(synchronize_session=False))
        # Logic to delete? 'delete(Chunk).where...'
        from sqlalchemy import delete
        await db.execute(delete(Chunk).where(Chunk.memory_id == memory.id))
        
        for i, (embedding_id, chunk_content) in enumerate(zip(ids, documents_content)):
            meta = metadatas[i]
            
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
                memory_id=memory.id,
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

    try:
        await vector_store.add_documents(
            ids=ids,
            documents=enriched_chunk_texts,
            metadatas=metadatas,
            sparse_values=sparse_values
        )
    except Exception as e:
        # Log the error or handle it as appropriate. For now, we'll just print.
        print(f"Error adding documents to vector store: {e}")
        # Decide how to proceed if adding to vector store fails.
        # For example, you might want to revert the DB commit or raise an HTTPException.
        # For this change, we'll let the function continue and return the memory.

    # Return with prefix
    return {
        "id": f"mem_{memory.id}",
        "title": memory.title,
        "content": memory.content,
        "user_id": memory.user_id,
        "created_at": memory.created_at,
        "updated_at": memory.updated_at,
        "tags": memory.tags,
        "type": "memory"
    }

@router.delete("/{memory_id}", response_model=Any)
async def delete_memory(
    memory_id: str,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Delete a memory or document.
    """
    if memory_id.startswith("doc_"):
        # Handle Document Deletion
        doc_id = int(memory_id.split("_")[1])
        result = await db.execute(
            select(Document)
            .where(Document.id == doc_id, Document.user_id == current_user.id)
            .options(selectinload(Document.chunks))
        )
        document = result.scalars().first()
        if not document:
            raise HTTPException(status_code=404, detail="Document not found")
        
        # Delete chunks from vector store?
        for chunk in document.chunks:
            if chunk.embedding_id:
                await vector_store.delete(ids=[chunk.embedding_id])
        
        await db.delete(document)
        await db.commit()
        return {"status": "success", "id": memory_id}
        
    elif memory_id.startswith("mem_"):
        # Handle Memory Deletion
        mem_id = int(memory_id.split("_")[1])
        result = await db.execute(select(Memory).where(Memory.id == mem_id, Memory.user_id == current_user.id))
        memory = result.scalars().first()
        if not memory:
            raise HTTPException(status_code=404, detail="Memory not found")
        
        if memory.embedding_id:
            await vector_store.delete(ids=[memory.embedding_id])
            
        await db.delete(memory)
        await db.commit()
        return {"status": "success", "id": memory_id}
    
    else:
        # Fallback for old int IDs if any
        try:
            mem_id = int(memory_id)
            result = await db.execute(select(Memory).where(Memory.id == mem_id, Memory.user_id == current_user.id))
            memory = result.scalars().first()
            if not memory:
                raise HTTPException(status_code=404, detail="Memory not found")
            if memory.embedding_id:
                await vector_store.delete(ids=[memory.embedding_id])
            await db.delete(memory)
            await db.commit()
            return {"status": "success", "id": memory_id}
        except ValueError:
             raise HTTPException(status_code=400, detail="Invalid ID format")
