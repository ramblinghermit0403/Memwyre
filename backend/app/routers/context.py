from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import deps
from app.models.memory import Memory
from app.models.project import Project
from app.models.user import User

router = APIRouter()


class ContextComposeRequest(BaseModel):
    item_ids: List[str] = Field(default_factory=list)
    project_id: Optional[int] = None
    max_chars: int = 2800


class ContextComposeResponse(BaseModel):
    context_text: str
    suggested_title: str
    sources: List[dict]


@router.post("/compose", response_model=ContextComposeResponse)
async def compose_context(
    payload: ContextComposeRequest,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    if not payload.item_ids and payload.project_id is None:
        raise HTTPException(status_code=400, detail="Provide item_ids or project_id")

    memory_ids: List[int] = []
    for item in payload.item_ids:
        if item.startswith("mem_"):
            try:
                memory_ids.append(int(item.split("_")[1]))
            except (IndexError, ValueError):
                continue

    filters = [Memory.user_id == current_user.id, Memory.status == "approved"]
    if memory_ids:
        filters.append(Memory.id.in_(memory_ids))
    if payload.project_id is not None:
        filters.append(Memory.project_id == payload.project_id)

    result = await db.execute(select(Memory).where(*filters).order_by(Memory.created_at.desc()))
    memories = result.scalars().all()

    if not memories:
        return ContextComposeResponse(context_text="", suggested_title="MemWyre Context", sources=[])

    source_rows = []
    chunks: List[str] = []
    remaining = max(500, payload.max_chars)

    for mem in memories:
        project_name = None
        if mem.project_id:
            proj_result = await db.execute(
                select(Project).where(Project.id == mem.project_id, Project.user_id == current_user.id)
            )
            proj = proj_result.scalars().first()
            project_name = proj.name if proj else None

        header = f"### {mem.title or 'Untitled'}"
        body = mem.content or ""
        block = f"{header}\nSource: {mem.source_app or mem.source_llm or 'unknown'}"
        if project_name:
            block += f" | Project: {project_name}"
        block += f"\n{body.strip()}\n"

        if len(block) > remaining:
            block = block[:remaining]

        chunks.append(block)
        remaining -= len(block)
        source_rows.append(
            {
                "id": f"mem_{mem.id}",
                "title": mem.title,
                "source_app": mem.source_app or mem.source_llm or "unknown",
                "project_id": mem.project_id,
            }
        )

        if remaining <= 0:
            break

    context_text = "\n\n".join(chunks)
    suggested_title = memories[0].title or "MemWyre Context"

    return ContextComposeResponse(
        context_text=context_text,
        suggested_title=suggested_title,
        sources=source_rows,
    )
