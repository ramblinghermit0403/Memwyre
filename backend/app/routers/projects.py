from datetime import datetime, timezone
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import deps
from app.models.project import Project
from app.models.user import User
from app.schemas.project import ProjectCreate, ProjectOut, ProjectUpdate

router = APIRouter()


@router.get("/", response_model=List[ProjectOut])
async def list_projects(
    include_archived: bool = False,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    q = select(Project).where(Project.user_id == current_user.id)
    if not include_archived:
        q = q.where(Project.archived_at.is_(None))
    q = q.order_by(Project.created_at.desc())
    result = await db.execute(q)
    return result.scalars().all()


@router.post("/", response_model=ProjectOut)
async def create_project(
    payload: ProjectCreate,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    project = Project(
        user_id=current_user.id,
        name=payload.name,
        description=payload.description,
        color=payload.color,
        icon=payload.icon,
    )
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return project


@router.put("/{project_id}", response_model=ProjectOut)
async def update_project(
    project_id: int,
    payload: ProjectUpdate,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.user_id == current_user.id)
    )
    project = result.scalars().first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if payload.name is not None:
        project.name = payload.name
    if payload.description is not None:
        project.description = payload.description
    if payload.color is not None:
        project.color = payload.color
    if payload.icon is not None:
        project.icon = payload.icon
    if payload.archived is True:
        project.archived_at = datetime.now(timezone.utc)
    elif payload.archived is False:
        project.archived_at = None

    await db.commit()
    await db.refresh(project)
    return project


@router.delete("/{project_id}")
async def archive_project(
    project_id: int,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.user_id == current_user.id)
    )
    project = result.scalars().first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project.archived_at = datetime.now(timezone.utc)
    await db.commit()
    return {"status": "archived", "project_id": project_id}
