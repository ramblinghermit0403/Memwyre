from datetime import datetime
from typing import Any, List

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import and_, cast, not_, or_, String, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.api import deps
from app.models.document import Document
from app.models.memory import Memory
from app.models.project import Project
from app.models.user import User
from app.schemas.memory import Memory as MemorySchema, MemoryCreate, MemoryUpdate
from app.services.memory_service import memory_service
from app.services.vector_store import vector_store
from app.worker_router import ingest_memory_task

router = APIRouter()


@router.get("/agent-facts", response_model=List[MemorySchema])
async def get_agent_facts(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    result = await db.execute(
        select(Memory)
        .where(
            Memory.user_id == current_user.id,
            or_(
                Memory.source_llm == "agent",
                cast(Memory.tags, String).contains("auto-fact"),
            ),
        )
        .order_by(Memory.created_at.desc())
    )
    return result.scalars().all()


@router.get("/tags", response_model=List[str])
async def get_all_tags(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    result = await db.execute(
        select(Memory.tags).where(Memory.user_id == current_user.id, Memory.tags.is_not(None))
    )
    memories = result.all()

    unique_tags = set()
    for mem in memories:
        tags_val = mem.tags if hasattr(mem, "tags") else mem[0]
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
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    is_extension = "extension" in (memory_in.tags or [])
    await deps.verify_usage_limits(
        doc_type="memory",
        content_len=len(memory_in.content),
        current_user=current_user,
        db=db,
    )

    # Resolve project_id to ensure workspace containerization
    project_id = await deps.resolve_project_id(db, current_user.id, memory_in.project_id)

    memory = await memory_service.create_memory(
        db=db,
        user=current_user,
        content=memory_in.content,
        title=memory_in.title,
        source="extension" if is_extension else "web-app",
        tags=memory_in.tags,
        created_at=memory_in.created_at,
        project_id=project_id,
        interaction_type=memory_in.interaction_type,
        source_app=memory_in.source_app,
    )

    project_name = None
    if memory.project_id:
        project_result = await db.execute(
            select(Project).where(Project.id == memory.project_id, Project.user_id == current_user.id)
        )
        project = project_result.scalars().first()
        project_name = project.name if project else None

    return {
        "id": memory.id,
        "title": memory.title,
        "content": memory.content,
        "user_id": memory.user_id,
        "created_at": memory.created_at,
        "updated_at": memory.updated_at,
        "source": memory.source_llm,
        "source_app": memory.source_app or memory.source_llm,
        "interaction_type": memory.interaction_type,
        "project_id": memory.project_id,
        "project_name": project_name,
        "tags": memory.tags,
        "doc_type": "memory",
        "type": "memory",
    }


class CheckDuplicateRequest(BaseModel):
    content: str


@router.post("/check-duplicate", response_model=Any)
async def check_duplicate(
    request: CheckDuplicateRequest,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
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
                    "title": metadata.get("source_id", "Unknown"),
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
    view: str | None = None,
    project_id: int | None = None,
    source_app: str | None = None,
    interaction_type: str | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    filters = [
        Memory.user_id == current_user.id,
        Memory.status == "approved",
        or_(Memory.source_llm.is_(None), Memory.source_llm != "agent"),
        not_(cast(Memory.tags, String).contains("auto-fact")),
    ]

    if tag:
        filters.append(cast(Memory.tags, String).contains(tag))
    if project_id is not None:
        filters.append(Memory.project_id == project_id)
    if source_app:
        filters.append(Memory.source_app == source_app)
    if interaction_type:
        if interaction_type == "webpage":
            filters.append(Memory.interaction_type.in_(["webpage", "web_snippet"]))
        else:
            filters.append(Memory.interaction_type == interaction_type)
    if date_from:
        try:
            filters.append(Memory.created_at >= datetime.fromisoformat(date_from))
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid date_from format")
    if date_to:
        try:
            filters.append(Memory.created_at <= datetime.fromisoformat(date_to))
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid date_to format")

    result_mem = await db.execute(select(Memory).where(and_(*filters)))
    memories = result_mem.scalars().all()

    project_ids = {m.project_id for m in memories if m.project_id is not None}
    project_map = {}
    if project_ids:
        project_result = await db.execute(
            select(Project).where(Project.user_id == current_user.id, Project.id.in_(project_ids))
        )
        project_map = {p.id: p for p in project_result.scalars().all()}

    results = []
    for mem in memories:
        project = project_map.get(mem.project_id)
        created = mem.created_at
        results.append(
            {
                "id": f"mem_{mem.id}",
                "title": mem.title,
                "content": mem.content,
                "user_id": mem.user_id,
                "created_at": created,
                "updated_at": mem.updated_at,
                "source": mem.source_llm,
                "source_app": mem.source_app or mem.source_llm,
                "interaction_type": mem.interaction_type or "conversation",
                "project_id": mem.project_id,
                "project_name": project.name if project else None,
                "timeline_group": created.strftime("%Y-%m-%d") if created else None,
                "tags": mem.tags,
                "doc_type": "memory",
                "type": "memory",
            }
        )

    doc_filters = [Document.user_id == current_user.id]
    if project_id is not None:
        doc_filters.append(Document.project_id == project_id)
    if date_from:
        try:
            doc_filters.append(Document.created_at >= datetime.fromisoformat(date_from))
        except ValueError:
            pass
    if date_to:
        try:
            doc_filters.append(Document.created_at <= datetime.fromisoformat(date_to))
        except ValueError:
            pass

    result_doc = await db.execute(select(Document).where(and_(*doc_filters)))
    documents = result_doc.scalars().all()
    
    for doc in documents:
        doc_type = "memory" if doc.doc_type == "memory" else "document"
        
        # If activeType filter is used for "conversation", "prompt", "memory", "webpage" on frontend,
        # documents should be returned if interaction_type is not provided OR matches.
        # But documents don't have interaction_type in DB, they have doc_type.
        # So we'll map their interaction_type to "document".
        if interaction_type and interaction_type != "document":
            continue
            
        results.append(
            {
                "id": f"doc_{doc.id}",
                "title": doc.title or "Untitled Document",
                "content": doc.content if doc.content else f"Uploaded Document: {doc.source} ({doc.file_type})",
                "user_id": doc.user_id,
                "created_at": doc.created_at or datetime.now(),
                "updated_at": None,
                "source": doc.source,
                "source_app": doc.source,
                "interaction_type": "document",
                "project_id": doc.project_id,
                "project_name": project_map.get(doc.project_id).name if doc.project_id and project_map.get(doc.project_id) else None,
                "timeline_group": (doc.created_at or datetime.now()).strftime("%Y-%m-%d"),
                "doc_type": doc_type,
                "type": doc_type,
                "tags": doc.tags if doc.tags is not None else [],
            }
        )

    def get_sort_key(x):
        dt = x.get("created_at")
        if not dt:
            return 0
        try:
            return dt.timestamp()
        except Exception:
            return 0

    results.sort(key=get_sort_key, reverse=True)
    return results[skip : skip + limit]


@router.get("/review", response_model=Any)
async def get_daily_review(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    result = await db.execute(
        select(Memory)
        .where(Memory.user_id == current_user.id, Memory.status == "approved")
        .order_by(Memory.created_at.desc())
        .limit(5)
    )
    memories = result.scalars().all()

    results = []
    for mem in memories:
        results.append(
            {
                "id": f"mem_{mem.id}",
                "title": mem.title,
                "content": mem.content,
                "created_at": mem.created_at,
                "tags": mem.tags,
                "reason": "recent",
            }
        )

    return results


@router.put("/{memory_id}", response_model=MemorySchema)
async def update_memory(
    memory_id: str,
    memory_in: MemoryUpdate,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    if memory_id.startswith("doc_"):
        doc_id = int(memory_id.split("_")[1])
        result = await db.execute(select(Document).where(Document.id == doc_id, Document.user_id == current_user.id))
        document = result.scalars().first()
        if not document:
            raise HTTPException(status_code=404, detail="Document not found")

        document.title = memory_in.title
        document.content = memory_in.content
        document.tags = memory_in.tags

        await db.commit()
        await db.refresh(document)

        ingest_memory_task.delay(
            memory_id=document.id,
            user_id=current_user.id,
            content=document.content,
            title=document.title,
            tags=document.tags,
            source="document-update",
            doc_type="document",
            mode="replace",
        )

        return {
            "id": f"doc_{document.id}",
            "title": document.title,
            "content": document.content,
            "user_id": document.user_id,
            "created_at": document.created_at,
            "updated_at": document.updated_at,
            "tags": document.tags,
            "type": "document",
        }

    if "_" in memory_id:
        try:
            real_id = int(memory_id.split("_")[1])
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid ID format")
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
    # Resolve project_id: use provided value, or keep existing, or fall back to default
    if memory_in.project_id is not None:
        memory.project_id = await deps.resolve_project_id(db, current_user.id, memory_in.project_id)
    elif memory.project_id is None:
        memory.project_id = await deps.resolve_project_id(db, current_user.id)
    memory.interaction_type = memory_in.interaction_type
    memory.source_app = memory_in.source_app or memory.source_app
    await db.commit()
    await db.refresh(memory)

    ingest_memory_task.delay(
        memory_id=memory.id,
        user_id=current_user.id,
        content=memory.content,
        title=memory.title,
        tags=memory.tags,
        source="memory-update",
        doc_type="memory",
        mode="replace",
    )

    project_name = None
    if memory.project_id:
        project_result = await db.execute(
            select(Project).where(Project.id == memory.project_id, Project.user_id == current_user.id)
        )
        project = project_result.scalars().first()
        project_name = project.name if project else None

    return {
        "id": memory.id,
        "title": memory.title,
        "content": memory.content,
        "user_id": memory.user_id,
        "created_at": memory.created_at,
        "updated_at": memory.updated_at,
        "tags": memory.tags,
        "project_id": memory.project_id,
        "project_name": project_name,
        "interaction_type": memory.interaction_type,
        "source_app": memory.source_app or memory.source_llm,
        "type": "memory",
    }


@router.delete("/{memory_id}", response_model=Any)
async def delete_memory(
    memory_id: str,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    if memory_id.startswith("doc_"):
        doc_id = int(memory_id.split("_")[1])
        result = await db.execute(
            select(Document)
            .where(Document.id == doc_id, Document.user_id == current_user.id)
            .options(selectinload(Document.chunks))
        )
        document = result.scalars().first()
        if not document:
            raise HTTPException(status_code=404, detail="Document not found")

        for chunk in document.chunks:
            if chunk.embedding_id:
                await vector_store.delete(ids=[chunk.embedding_id])

        await db.delete(document)
        await db.commit()
        return {"status": "success", "id": memory_id}

    if memory_id.startswith("mem_"):
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

