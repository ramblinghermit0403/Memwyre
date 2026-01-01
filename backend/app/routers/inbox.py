from typing import Any, List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.api import deps
from app.models.user import User
from app.models.memory import Memory
from app.services.vector_store import vector_store
from app.services.ingestion import ingestion_service
from app.services.websocket import manager
from app.worker import ingest_memory_task
import asyncio
from pydantic import BaseModel

router = APIRouter()

class InboxItem(BaseModel):
    id: str
    content: str
    source: str
    created_at: Any
    status: str
    details: Optional[str] = None
    similarity_score: float = 0.0 
    task_type: Optional[str] = None
    tags: Optional[List[str]] = None
    
class InboxAction(BaseModel):
    action: str # "approve", "discard", "edit", "dismiss"
    payload: Any = None # If edit, new content

@router.get("/", response_model=List[InboxItem])
async def get_inbox(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    List pending memories.
    """
    result = await db.execute(
        select(Memory).where(
            Memory.user_id == current_user.id,
            Memory.show_in_inbox == True
        ).order_by(Memory.created_at.desc())
    )
    memories = result.scalars().all()
    
    results = []
    for mem in memories:
        results.append(InboxItem(
            id=f"mem_{mem.id}",
            content=mem.content,
            source=mem.source_llm or "unknown",
            created_at=mem.created_at,
            status=mem.status,
            details=mem.title,
            task_type=mem.task_type,
            tags=mem.tags
        ))
        
    return results

@router.post("/{memory_id}/action")
async def inbox_action(
    memory_id: str,
    action_in: InboxAction,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Approve, Discard or Edit a pending memory.
    """
    try:
        mem_id_int = int(memory_id.replace("mem_", ""))
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID")

    result = await db.execute(select(Memory).where(
        Memory.id == mem_id_int, 
        Memory.user_id == current_user.id
    ))
    memory = result.scalars().first()
    if not memory:
        raise HTTPException(status_code=404, detail="Memory not found")
        
    if action_in.action == "approve":
        memory.status = "approved"
        memory.show_in_inbox = False
        await db.commit()
        await db.refresh(memory)
        
        # ingest logic via Celery
        ingest_memory_task.delay(
            memory.id, 
            current_user.id, 
            memory.content, 
            memory.title,
            memory.tags,
            memory.source_llm
        )
        
        await manager.broadcast({"type": "inbox_update", "id": memory_id, "action": "approve"})
        return {"status": "approved", "id": memory_id}
        
    elif action_in.action == "discard":
        memory.status = "discarded"
        
        # Ensure it's removed from Vector DB
        if memory.embedding_id:
            try:
                vector_store.delete(ids=[memory.embedding_id])
                memory.embedding_id = None
            except:
                pass
                
        await db.commit()
        await manager.broadcast({"type": "inbox_update", "id": memory_id, "action": "discard"})
        return {"status": "discarded", "id": memory_id}
        
    elif action_in.action == "edit":
        if not action_in.payload or "content" not in action_in.payload:
            raise HTTPException(status_code=400, detail="Missing content for edit")
            
        memory.content = action_in.payload["content"]
        memory.status = "approved" 
        
        await db.commit()
        await db.refresh(memory)
        

        
        # ingest via Celery
        ingest_memory_task.delay(
            memory.id, 
            current_user.id, 
            memory.content, 
            memory.title,
            memory.tags,
            memory.source_llm
        )
            
        await manager.broadcast({"type": "inbox_update", "id": memory_id, "action": "edit"})
        return {"status": "approved_edited", "id": memory_id}
        
    elif action_in.action == "dismiss":
        # Just hide from inbox
        memory.show_in_inbox = False
        await db.commit()
        await manager.broadcast({"type": "inbox_update", "id": memory_id, "action": "dismiss"})
        return {"status": memory.status, "id": memory_id}
    
    else:
        raise HTTPException(status_code=400, detail="Invalid action")

@router.get("/{memory_id}", response_model=InboxItem)
async def get_inbox_item(
    memory_id: str,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get a single pending memory.
    """
    try:
        mem_id_int = int(memory_id.replace("mem_", ""))
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID")

    result = await db.execute(select(Memory).where(
        Memory.id == mem_id_int, 
        Memory.user_id == current_user.id
    ))
    memory = result.scalars().first()
    
    if not memory:
        raise HTTPException(status_code=404, detail="Memory not found")
        
    return InboxItem(
        id=f"mem_{memory.id}",
        content=memory.content,
        source=memory.source_llm or "unknown",
        created_at=memory.created_at,
        status=memory.status,
        details=memory.title,
        task_type=memory.task_type,
        tags=memory.tags
    )

class InboxUpdate(BaseModel):
    content: str
    title: Optional[str] = None
    tags: Optional[List[str]] = None

@router.put("/{memory_id}")
async def update_inbox_item(
    memory_id: str,
    data: InboxUpdate,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Update a pending memory content without approving.
    """
    try:
        mem_id_int = int(memory_id.replace("mem_", ""))
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID")

    result = await db.execute(select(Memory).where(
        Memory.id == mem_id_int, 
        Memory.user_id == current_user.id
    ))
    memory = result.scalars().first()
    
    if not memory:
        raise HTTPException(status_code=404, detail="Memory not found")
        
    memory.content = data.content
    if data.title:
        memory.title = data.title
    
    if data.tags is not None:
        memory.tags = data.tags
        
    await db.commit()
    await db.refresh(memory)
    
    # Broadcast update
    await manager.broadcast({"type": "inbox_update", "id": memory_id, "action": "update"})
    
    return {"status": "success", "id": memory_id}

from bs4 import BeautifulSoup
import time
from fastapi import Request

class AgentDropMetadata(BaseModel):
    model: Optional[str] = None
    runtime: Optional[str] = None
    duration_sec: Optional[float] = None

class AgentDropPayload(BaseModel):
    title: Optional[str] = None
    content: str
    confidence: Optional[float] = 0.0
    job_id: Optional[str] = None
    metadata: Optional[AgentDropMetadata] = None

# Simple in-memory rate limiter
# Map of IP -> list of timestamps
rate_limit_data = {}
RATE_LIMIT_WINDOW = 60 # seconds
RATE_LIMIT_MAX_REQUESTS = 10

def strip_html(text: str) -> str:
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

@router.post("/drop/{token}")
async def agent_drop(
    token: str,
    request: Request,
    payload: AgentDropPayload,
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Experimental endpoint for external AI agents to drop results.
    Uses unique user-specific token.
    """
    # 0. Token Check
    result = await db.execute(select(User).where(User.drop_token == token))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or missing drop token")

    # 1. Size Check
    body = await request.body()
    if len(body) > 50 * 1024:
        raise HTTPException(status_code=413, detail="Payload too large (max 50KB)")

    # 2. Rate Limit
    client_ip = request.client.host
    now = time.time()
    if client_ip not in rate_limit_data:
        rate_limit_data[client_ip] = []
    
    # Filter timestamps in window
    rate_limit_data[client_ip] = [t for t in rate_limit_data[client_ip] if now - t < RATE_LIMIT_WINDOW]
    
    if len(rate_limit_data[client_ip]) >= RATE_LIMIT_MAX_REQUESTS:
        raise HTTPException(status_code=429, detail="Too many requests. Try again later.")
    
    rate_limit_data[client_ip].append(now)

    # 3. Validation & Sanitization
    clean_content = strip_html(payload.content)
    if not clean_content.strip():
         raise HTTPException(status_code=400, detail="Content cannot be empty after stripping HTML")

    # 5. Create Inbox Item (Memory object with pending status)
    new_memory = Memory(
        user_id=user.id,
        title=payload.title or "AI Agent Drop",
        content=clean_content,
        source_llm="agent_drop",
        status="pending",
        show_in_inbox=True,
        trusted=False,
        task_type=payload.job_id # Reuse task_type for job_id if needed
    )
    
    db.add(new_memory)
    await db.commit()
    await db.refresh(new_memory)

    # 6. Notify UI
    await manager.broadcast({
        "type": "inbox_update", 
        "id": f"mem_{new_memory.id}", 
        "action": "new_drop",
        "title": new_memory.title
    })

    return {
        "status": "success",
        "id": f"mem_{new_memory.id}",
        "message": "Item added to inbox for review"
    }
