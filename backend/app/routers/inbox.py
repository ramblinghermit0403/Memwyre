from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.models.user import User
from app.models.memory import Memory
from app.services.vector_store import vector_store
from app.services.ingestion import ingestion_service
from app.services.websocket import manager
import asyncio
from pydantic import BaseModel

router = APIRouter()

class InboxItem(BaseModel):
    id: str
    content: str
    source: str
    created_at: Any
    status: str
    details: str = None
    similarity_score: float = 0.0 # For duplicates?
    
class InboxAction(BaseModel):
    action: str # "approve", "discard", "edit", "dismiss"
    payload: Any = None # If edit, new content

@router.get("/", response_model=List[InboxItem])
def get_inbox(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    List pending memories.
    """
    memories = db.query(Memory).filter(
        Memory.user_id == current_user.id,
        Memory.show_in_inbox == True
    ).order_by(Memory.created_at.desc()).all()
    
    results = []
    for mem in memories:
        results.append(InboxItem(
            id=f"mem_{mem.id}",
            content=mem.content,
            source=mem.source_llm or "unknown",
            created_at=mem.created_at,
            status=mem.status,
            details=mem.title
        ))
        
    return results

@router.post("/{memory_id}/action")
async def inbox_action(
    memory_id: str,
    action_in: InboxAction,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Approve, Discard or Edit a pending memory.
    """
    try:
        mem_id_int = int(memory_id.replace("mem_", ""))
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID")

    memory = db.query(Memory).filter(Memory.id == mem_id_int, Memory.user_id == current_user.id).first()
    if not memory:
        raise HTTPException(status_code=404, detail="Memory not found")
        
    if action_in.action == "approve":
        memory.status = "approved"
        memory.show_in_inbox = False
        db.commit()
        db.refresh(memory)
        
        # Ingest
        # Note: In a real app, offload this to a background task to keep API fast
        ids, documents_content, metadatas = ingestion_service.process_text(
            text=memory.content,
            document_id=memory.id,
            title=memory.title,
            doc_type="memory",
            metadata={"user_id": current_user.id, "memory_id": memory.id, "tags": str(memory.tags) if memory.tags else "", "source": memory.source_llm}
        )
        
        if ids:
            memory.embedding_id = ids[0]
            db.commit()
            
            vector_store.add_documents(
                ids=ids,
                documents=documents_content,
                metadatas=metadatas
            )
        
        await manager.broadcast({"type": "inbox_update", "id": memory_id, "action": "approve"})
        return {"status": "approved", "id": memory_id}
        
    elif action_in.action == "discard":
        memory.status = "discarded"
        
        # Ensure it's removed from Vector DB if it was there (e.g. old memory or bug)
        if memory.embedding_id:
            try:
                vector_store.delete(ids=[memory.embedding_id])
                memory.embedding_id = None
            except:
                pass
                
        db.commit()
        await manager.broadcast({"type": "inbox_update", "id": memory_id, "action": "discard"})
        return {"status": "discarded", "id": memory_id}
        
    elif action_in.action == "edit":
        if not action_in.payload or "content" not in action_in.payload:
            raise HTTPException(status_code=400, detail="Missing content for edit")
            
        memory.content = action_in.payload["content"]
        memory.status = "approved" # approving on edit? Or keep pending? Let's approve for now as explicit user action.
        
        db.commit()
        db.refresh(memory)
        # Ingest logic same as approve... (Duplication here, refactor later)
        
        ids, documents_content, metadatas = ingestion_service.process_text(
            text=memory.content,
            document_id=memory.id,
            title=memory.title,
            doc_type="memory",
            metadata={"user_id": current_user.id, "memory_id": memory.id, "tags": str(memory.tags) if memory.tags else "", "source": memory.source_llm}
        )
        if ids:
            memory.embedding_id = ids[0]
            db.commit()
            vector_store.add_documents(ids=ids, documents=documents_content, metadatas=metadatas)
            
        await manager.broadcast({"type": "inbox_update", "id": memory_id, "action": "edit"})
        return {"status": "approved_edited", "id": memory_id}
        
    elif action_in.action == "dismiss":
        # Just hide from inbox, keep status (likely 'approved' if auto-approved)
        memory.show_in_inbox = False
        db.commit()
        await manager.broadcast({"type": "inbox_update", "id": memory_id, "action": "dismiss"})
        return {"status": memory.status, "id": memory_id}
    
    else:
        raise HTTPException(status_code=400, detail="Invalid action")

@router.get("/{memory_id}", response_model=InboxItem)
def get_inbox_item(
    memory_id: str,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get a single pending memory.
    """
    try:
        mem_id_int = int(memory_id.replace("mem_", ""))
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID")

    memory = db.query(Memory).filter(
        Memory.id == mem_id_int, 
        Memory.user_id == current_user.id
    ).first()
    
    if not memory:
        raise HTTPException(status_code=404, detail="Memory not found")
        
    return InboxItem(
        id=f"mem_{memory.id}",
        content=memory.content,
        source=memory.source_llm or "unknown",
        created_at=memory.created_at,
        status=memory.status,
        details=memory.title
    )

class InboxUpdate(BaseModel):
    content: str
    title: str = None

@router.put("/{memory_id}")
async def update_inbox_item(
    memory_id: str,
    data: InboxUpdate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Update a pending memory content without approving.
    """
    try:
        mem_id_int = int(memory_id.replace("mem_", ""))
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID")

    memory = db.query(Memory).filter(
        Memory.id == mem_id_int, 
        Memory.user_id == current_user.id
    ).first()
    
    if not memory:
        raise HTTPException(status_code=404, detail="Memory not found")
        
    memory.content = data.content
    if data.title:
        memory.title = data.title
        
    db.commit()
    db.refresh(memory)
    
    # Broadcast update
    await manager.broadcast({"type": "inbox_update", "id": memory_id, "action": "update"})
    
    return {"status": "success", "id": memory_id}
