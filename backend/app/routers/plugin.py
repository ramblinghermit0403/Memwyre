from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional, Any
from pydantic import BaseModel
from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.models.memory import Memory
from app.worker_router import process_plugin_transcript_task
import json

router = APIRouter()

class TranscriptCaptureRequest(BaseModel):
    session_id: str
    project_name: str
    cwd: str
    transcript: List[Any]

@router.get("/context")
async def get_plugin_context(
    project: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Fetch memories relevant to the project for Claude Code SessionStart hook.
    """
    # Simply fetch the latest memories containing the project name or general memories
    # In a fully fleshed out system, this would use semantic search on the vector DB.
    # For now, we do a basic ILIKE search in the DB to keep it fast.
    
    stmt = select(Memory).where(
        Memory.user_id == current_user.id
    ).filter(
        Memory.content.ilike(f"%{project}%")
    ).order_by(Memory.created_at.desc()).limit(10)
    
    result = await db.execute(stmt)
    memories = result.scalars().all()
    
    # Format for the plugin
    formatted_memories = [
        {"id": m.id, "content": m.content, "created_at": m.created_at.isoformat()}
        for m in memories
    ]
    
    return {"project": project, "memories": formatted_memories}

@router.post("/capture", status_code=202)
async def capture_plugin_session(
    request: TranscriptCaptureRequest,
    current_user: User = Depends(get_current_user)
):
    """
    Receive raw transcript from Claude Code plugin Stop hook.
    Returns 202 Accepted immediately and enqueues background processing.
    """
    
    # Enqueue Celery task for signal extraction
    process_plugin_transcript_task.delay(
        session_id=request.session_id,
        project_name=request.project_name,
        cwd=request.cwd,
        transcript=request.transcript,
        user_id=current_user.id
    )
    
    return {"message": "Transcript accepted for processing", "session_id": request.session_id}
