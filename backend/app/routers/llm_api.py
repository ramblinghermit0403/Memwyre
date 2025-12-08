from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app.api import deps
from app.models.user import User
from app.models.memory import Memory
from app.models.audit import AuditLog
from app.schemas.llm import LLMMemoryCreate, LLMMemoryUpdate, LLMMemoryResponse, ContextRequest, ContextResponse
from app.services.vector_store import vector_store
from app.services.websocket import manager
from app.services.context_builder import context_builder
from app.services.dedupe_job import dedupe_service
import asyncio

router = APIRouter()

@router.post("/save_memory", response_model=LLMMemoryResponse)
def save_memory(
    memory_in: LLMMemoryCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Allow LLMs/Extensions to save memory. Respects Auto-Approve setting.
    """
    # 1. Determine Status
    auto_approve = True
    user_settings = current_user.settings
    if user_settings:
        if isinstance(user_settings, str):
            import json
            try:
                user_settings = json.loads(user_settings)
            except:
                user_settings = {}
        if isinstance(user_settings, dict):
            auto_approve = user_settings.get("auto_approve", True)
            
    status = "approved" if auto_approve else "pending"
    
    # 2. Determine Inbox Visibility
    # Logic:
    # - If Source is 'user-upload'/'manual', and auto-approved -> Don't show in inbox (it's implicit).
    # - If Source is 'user-upload', and pending -> Show in inbox.
    # - If Source is EXTERNAL (e.g. 'chatgpt', 'mcp'), -> ALWAYS show in inbox so user knows it happened (Notification).
    
    is_external = memory_in.source_llm not in ["user-upload", "user"]
    
    show_in_inbox = True 
    if not is_external and status == "approved":
        show_in_inbox = False # Skip inbox for manual approvals
        
    # 3. Create Memory
    memory = Memory(
        user_id=current_user.id,
        content=memory_in.content,
        title=f"Memory from {memory_in.source_llm}",
        source_llm=memory_in.source_llm,
        model_name=memory_in.model_name,
        status=status,
        tags=memory_in.tags,
        show_in_inbox=show_in_inbox,
        embedding_id=None # Will be updated if ingested
    )
    
    db.add(memory)
    
    # 3. Create Audit Log
    audit = AuditLog(
        actor=memory_in.source_llm,
        action="save_memory",
        details=f"Saved memory from {memory_in.url}",
        target_id=None # Will update after commit
    )
    db.add(audit)
    
    db.commit()
    db.refresh(memory)
    
    # Update audit with ID
    audit.target_id = str(memory.id)
    db.add(audit)
    db.commit()
    
    # Ingest if approved
    if status == "approved":
        from app.services.ingestion import ingestion_service
        try:
            ids, documents_content, metadatas = ingestion_service.process_text(
                text=memory_in.content,
                document_id=memory.id,
                title=memory.title,
                doc_type="memory",
                metadata={"user_id": current_user.id, "memory_id": memory.id, "tags": str(memory_in.tags) if memory_in.tags else "", "source": memory_in.source_llm}
            )
            if ids:
                memory.embedding_id = ids[0]
                db.commit()
                vector_store.add_documents(ids=ids, documents=documents_content, metadatas=metadatas)
        except Exception as e:
            print(f"Ingestion failed: {e}")

    # 4. Trigger Dedupe Job (Background)
    background_tasks.add_task(dedupe_service.check_duplicates, memory.id, db)
    
    # 5. Broadcast via Websocket
    asyncio.run(manager.broadcast({
        "type": "new_memory", 
        "data": {
            "id": f"mem_{memory.id}", 
            "status": memory.status,
            "source": memory.source_llm
        }
    }))
    
    return LLMMemoryResponse(
        id=f"mem_{memory.id}",
        status=memory.status,
        created_at=memory.created_at
    )

@router.put("/update_memory/{memory_id}", response_model=LLMMemoryResponse)
def update_memory(
    memory_id: str,
    memory_in: LLMMemoryUpdate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Update memory content or status.
    """
    try:
        mem_id_int = int(memory_id.replace("mem_", ""))
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID")

    memory = db.query(Memory).filter(Memory.id == mem_id_int, Memory.user_id == current_user.id).first()
    if not memory:
        raise HTTPException(status_code=404, detail="Memory not found")

    # Update fields
    if memory_in.content:
        # TODO: Create History entry
        memory.content = memory_in.content
        memory.version += 1
        
    if memory_in.status:
        memory.status = memory_in.status
        # If status becomes approved, trigger ingestion
        if memory_in.status == "approved" and not memory.embedding_id:
            # Trigger ingestion (TODO: refactor ingestion to be callable here)
            pass
            
    if memory_in.tags:
        memory.tags = memory_in.tags

    db.commit()
    db.refresh(memory)
    
    return LLMMemoryResponse(
        id=f"mem_{memory.id}",
        status=memory.status,
        created_at=memory.created_at
    )

@router.delete("/delete_memory/{memory_id}")
def delete_memory(
    memory_id: str,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    # Soft delete (status=archived) or hard delete? User request said "Soft-delete"
    try:
        mem_id_int = int(memory_id.replace("mem_", ""))
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID")
        
    memory = db.query(Memory).filter(Memory.id == mem_id_int, Memory.user_id == current_user.id).first()
    if not memory:
        raise HTTPException(status_code=404, detail="Memory not found")
        
    memory.status = "archived"
    
    # Remove from Vector DB if exists
    if memory.embedding_id:
        try:
            vector_store.delete(ids=[memory.embedding_id])
            memory.embedding_id = None
        except:
            pass
            
    db.commit()
    return {"status": "success", "message": "Memory archived"}

@router.post("/retrieve_context", response_model=ContextResponse)
def retrieve_context(
    request: ContextRequest,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    ctx = context_builder.build_context(
        query=request.query,
        user_id=current_user.id,
        limit_tokens=request.limit_tokens or 2000
    )
    
    return ContextResponse(
        context_text=ctx["text"],
        snippets=ctx["snippets"],
        token_count=ctx["token_count"]
    )
