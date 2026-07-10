import re
import sys

filepath = r"C:\Users\himan\OneDrive\Documents\brain_vault\backend\app\routers\memory.py"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# We want to replace everything from `def read_memories(` down to `return results[skip : skip + limit]`
# Let's find the start and end carefully.

start_str = "async def read_memories("
end_str = "    return results[skip : skip + limit]"

start_idx = content.find(start_str)
end_idx = content.find(end_str) + len(end_str)

if start_idx == -1 or end_idx == -1:
    print("Could not find boundaries!")
    sys.exit(1)

new_func = """async def read_memories(
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

    if view != "timeline":
        result_doc = await db.execute(select(Document).where(Document.user_id == current_user.id))
        documents = result_doc.scalars().all()
        for doc in documents:
            doc_type = "memory" if doc.doc_type == "memory" else "document"
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
                    "project_id": None,
                    "project_name": None,
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
    return results[skip : skip + limit]"""

new_content = content[:start_idx] + new_func + content[end_idx:]

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Fixed memory.py successfully.")
