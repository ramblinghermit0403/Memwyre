from datetime import datetime, timedelta, timezone
from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy import String, cast, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import deps
from app.models.chat import ChatMessage, ChatSession
from app.models.document import Document
from app.models.memory import Memory
from app.models.usage import UserUsage
from app.models.user import User
from app.routers.admin_bypass import get_admin_user

router = APIRouter()


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _as_iso(value: datetime | None) -> str | None:
    return value.isoformat() if value else None


def _as_date_key(value: datetime | None) -> str | None:
    return value.date().isoformat() if value else None


def _empty_series(days: int) -> list[dict[str, Any]]:
    today = _utc_now().date()
    start = today - timedelta(days=days - 1)
    return [
        {
            "date": (start + timedelta(days=offset)).isoformat(),
            "users": 0,
            "memories": 0,
            "documents": 0,
            "chat_sessions": 0,
        }
        for offset in range(days)
    ]


async def _count(db: AsyncSession, stmt) -> int:
    return int(await db.scalar(stmt) or 0)


async def _sum(db: AsyncSession, stmt) -> float:
    return float(await db.scalar(stmt) or 0)


async def _distinct_user_ids(db: AsyncSession, stmt) -> set[int]:
    result = await db.execute(stmt)
    return {int(row[0]) for row in result.all() if row[0] is not None}


@router.get("/insights")
async def get_admin_insights(
    _admin_user: User = Depends(get_admin_user),
    db: AsyncSession = Depends(deps.get_db),
) -> Any:
    """
    Operational dashboard data for admins.

    This intentionally keeps the endpoint read-only and aggregate-focused so the
    frontend can expose app health without leaking full user content.
    """
    now = _utc_now()
    day_ago = now - timedelta(days=1)
    week_ago = now - timedelta(days=7)
    series_days = 14
    series_start = now - timedelta(days=series_days - 1)

    extension_filter = or_(
        func.lower(func.coalesce(Memory.source_llm, "")).like("%extension%"),
        func.lower(func.coalesce(Memory.source_app, "")).like("%extension%"),
        func.lower(cast(Memory.tags, String)).like("%extension%"),
    )

    user_ids_24h = set()
    user_ids_7d = set()
    for cutoff, target in ((day_ago, user_ids_24h), (week_ago, user_ids_7d)):
        target.update(
            await _distinct_user_ids(
                db,
                select(Memory.user_id).where(Memory.created_at >= cutoff).distinct(),
            )
        )
        target.update(
            await _distinct_user_ids(
                db,
                select(Document.user_id).where(Document.created_at >= cutoff).distinct(),
            )
        )
        target.update(
            await _distinct_user_ids(
                db,
                select(ChatSession.user_id).where(ChatSession.created_at >= cutoff).distinct(),
            )
        )
        target.update(
            await _distinct_user_ids(
                db,
                select(UserUsage.user_id).where(UserUsage.timestamp >= cutoff).distinct(),
            )
        )

    overview = {
        "total_users": await _count(db, select(func.count()).select_from(User)),
        "verified_users": await _count(db, select(func.count()).select_from(User).where(User.is_verified.is_(True))),
        "active_users_24h": len(user_ids_24h),
        "active_users_7d": len(user_ids_7d),
        "total_memories": await _count(db, select(func.count()).select_from(Memory)),
        "approved_memories": await _count(db, select(func.count()).select_from(Memory).where(Memory.status == "approved")),
        "pending_memories": await _count(db, select(func.count()).select_from(Memory).where(Memory.status == "pending")),
        "conversation_memories": await _count(
            db,
            select(func.count()).select_from(Memory).where(func.lower(func.coalesce(Memory.interaction_type, "")).like("%conversation%")),
        ),
        "extension_memories": await _count(db, select(func.count()).select_from(Memory).where(extension_filter)),
        "total_documents": await _count(db, select(func.count()).select_from(Document).where(Document.doc_type != "memory")),
        "chat_sessions": await _count(db, select(func.count()).select_from(ChatSession)),
        "chat_messages": await _count(db, select(func.count()).select_from(ChatMessage)),
        "tokens_in": await _count(db, select(func.coalesce(func.sum(UserUsage.tokens_in), 0))),
        "tokens_out": await _count(db, select(func.coalesce(func.sum(UserUsage.tokens_out), 0))),
        "estimated_cost": round(await _sum(db, select(func.coalesce(func.sum(UserUsage.estimated_cost), 0.0))), 4),
    }

    series = _empty_series(series_days)
    series_by_date = {item["date"]: item for item in series}
    series_queries = (
        ("users", select(User.created_at).where(User.created_at >= series_start)),
        ("memories", select(Memory.created_at).where(Memory.created_at >= series_start)),
        ("documents", select(Document.created_at).where(Document.created_at >= series_start, Document.doc_type != "memory")),
        ("chat_sessions", select(ChatSession.created_at).where(ChatSession.created_at >= series_start)),
    )
    for key, stmt in series_queries:
        result = await db.execute(stmt)
        for (created_at,) in result.all():
            date_key = _as_date_key(created_at)
            if date_key in series_by_date:
                series_by_date[date_key][key] += 1

    source_expr = func.coalesce(Memory.source_app, Memory.source_llm, "unknown")
    source_result = await db.execute(
        select(
            source_expr.label("source"),
            func.count(Memory.id),
        )
        .group_by(source_expr)
        .order_by(func.count(Memory.id).desc())
        .limit(10)
    )
    source_breakdown = [
        {"source": source or "unknown", "count": int(count)}
        for source, count in source_result.all()
    ]

    interaction_result = await db.execute(
        select(func.coalesce(Memory.interaction_type, "unknown"), func.count(Memory.id))
        .group_by(Memory.interaction_type)
        .order_by(func.count(Memory.id).desc())
    )
    interaction_breakdown = [
        {"type": interaction_type or "unknown", "count": int(count)}
        for interaction_type, count in interaction_result.all()
    ]

    users_result = await db.execute(select(User).order_by(User.created_at.desc()).limit(250))
    users = users_result.scalars().all()
    user_ids = [user.id for user in users]

    async def grouped_counts(column, *filters):
        if not user_ids:
            return {}
        result = await db.execute(
            select(column, func.count()).where(column.in_(user_ids), *filters).group_by(column)
        )
        return {int(user_id): int(count) for user_id, count in result.all()}

    async def grouped_latest(model, user_column, date_column):
        if not user_ids:
            return {}
        result = await db.execute(
            select(user_column, func.max(date_column)).where(user_column.in_(user_ids)).group_by(user_column)
        )
        return {int(user_id): latest for user_id, latest in result.all()}

    memory_counts = await grouped_counts(Memory.user_id)
    document_counts = await grouped_counts(Document.user_id, Document.doc_type != "memory")
    chat_counts = await grouped_counts(ChatSession.user_id)
    usage_counts = await grouped_counts(UserUsage.user_id)
    latest_memories = await grouped_latest(Memory, Memory.user_id, Memory.created_at)
    latest_documents = await grouped_latest(Document, Document.user_id, Document.created_at)
    latest_chats = await grouped_latest(ChatSession, ChatSession.user_id, ChatSession.updated_at)
    latest_usage = await grouped_latest(UserUsage, UserUsage.user_id, UserUsage.timestamp)

    user_rows = []
    for user in users:
        latest_values = [
            value
            for value in (
                latest_memories.get(user.id),
                latest_documents.get(user.id),
                latest_chats.get(user.id),
                latest_usage.get(user.id),
            )
            if value is not None
        ]
        last_activity = max(latest_values) if latest_values else user.created_at
        user_rows.append(
            {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "is_verified": bool(user.is_verified),
                "onboarding_completed": bool(user.onboarding_completed),
                "created_at": _as_iso(user.created_at),
                "last_activity_at": _as_iso(last_activity),
                "memories": memory_counts.get(user.id, 0),
                "documents": document_counts.get(user.id, 0),
                "chat_sessions": chat_counts.get(user.id, 0),
                "usage_events": usage_counts.get(user.id, 0),
            }
        )
    user_rows.sort(key=lambda item: item["last_activity_at"] or "", reverse=True)

    recent_items: list[dict[str, Any]] = []
    recent_memory_result = await db.execute(
        select(Memory, User.email)
        .join(User, User.id == Memory.user_id)
        .order_by(Memory.created_at.desc())
        .limit(15)
    )
    for memory, email in recent_memory_result.all():
        recent_items.append(
            {
                "kind": "memory",
                "title": memory.title or "Untitled memory",
                "user_email": email,
                "created_at": _as_iso(memory.created_at),
                "meta": memory.source_app or memory.source_llm or memory.interaction_type or "memory",
            }
        )

    recent_chat_result = await db.execute(
        select(ChatSession, User.email)
        .join(User, User.id == ChatSession.user_id)
        .order_by(ChatSession.updated_at.desc())
        .limit(15)
    )
    for session, email in recent_chat_result.all():
        recent_items.append(
            {
                "kind": "chat",
                "title": session.title or "Untitled chat",
                "user_email": email,
                "created_at": _as_iso(session.updated_at or session.created_at),
                "meta": "chat session",
            }
        )

    recent_document_result = await db.execute(
        select(Document, User.email)
        .join(User, User.id == Document.user_id)
        .where(Document.doc_type != "memory")
        .order_by(Document.created_at.desc())
        .limit(15)
    )
    for document, email in recent_document_result.all():
        recent_items.append(
            {
                "kind": "document",
                "title": document.title or document.source or "Untitled document",
                "user_email": email,
                "created_at": _as_iso(document.created_at),
                "meta": document.file_type or document.doc_type or "document",
            }
        )
    recent_items.sort(key=lambda item: item["created_at"] or "", reverse=True)

    return {
        "generated_at": _as_iso(now),
        "overview": overview,
        "series": series,
        "source_breakdown": source_breakdown,
        "interaction_breakdown": interaction_breakdown,
        "users": user_rows[:50],
        "recent_activity": recent_items[:20],
    }
