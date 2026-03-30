from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel, HttpUrl

from app.api import deps
from app.models.user import User
from app.models.memory import Memory
from app.services.web_ingestion import web_ingestion
from app.services.websocket import manager
from app.worker import ingest_memory_task, process_memory_metadata_task, dedupe_memory_task
import uuid

router = APIRouter()

class UrlIngestRequest(BaseModel):
    url: HttpUrl
    tags: list[str] = []

@router.post("/url")
async def ingest_url(
    request: UrlIngestRequest,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    """
    Ingest a webpage from a URL.
    Fetches content synchronously (API side) but processes embedding/vectorization in Celery.
    """
    url_str = str(request.url)
    
    # 1. Fetch Content (Async, non-blocking)
    try:
        data = await web_ingestion.fetch_url(url_str)
        
        if not data:
            raise HTTPException(status_code=400, detail="Could not extract content from URL")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to fetch URL: {str(e)}")

    # Content created directly from the UI is explicitly requested by the user,
    # so we should auto-approve it regardless of background scanning settings.
    auto_approve = True
                
    initial_status = "approved" if auto_approve else "pending"
    # Web ingests always appear in Inbox so the user is notified
    show_in_inbox = True
    
    # Enforce Usage Limits
    await deps.verify_usage_limits(doc_type="memory", content_len=len(data["content"]), current_user=current_user, db=db)
    
    # 3. Create Memory Record
    memory = Memory(
        title=data["title"],
        content=data["content"],
        # Normalized source fields for timeline & filter compatibility
        source_llm="web",
        source_app="web",
        interaction_type="webpage",
        user_id=current_user.id,
        tags=request.tags,
        embedding_id=str(uuid.uuid4()), # Placeholder
        status=initial_status,
        show_in_inbox=show_in_inbox
    )
    db.add(memory)
    await db.commit()
    await db.refresh(memory)
    
    # 4. Dispatch Celery Tasks
    # We always analyze metadata
    process_memory_metadata_task.delay(memory.id, current_user.id)
    
    # Only ingest (embed) if approved
    if initial_status == "approved":
        ingest_memory_task.delay(
            memory_id=memory.id,
            user_id=current_user.id,
            content=memory.content,
            title=memory.title,
            tags=request.tags,
            source="web"
        )
        # Dedupe check
        dedupe_memory_task.delay(memory.id)

    # 5. Broadcast so UI refreshes Inbox without full reload
    await manager.broadcast({
        "type": "inbox_update",
        "action": "new_ingest",
        "id": f"mem_{memory.id}",
        "title": memory.title
    })
        
    return {"status": "success", "memory_id": memory.id, "title": memory.title, "queued": True}
