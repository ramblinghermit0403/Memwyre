"""
Migration Script: Assign all NULL project_id records to each user's 'default' workspace.

This script:
1. Finds or creates a 'default' project for every user in the database.
2. Updates all SQL records (Memory, Document, ChatSession, Fact, EntityProfile, 
   MemoryCluster) with NULL project_id to point to their owner's default project.
3. Batch-updates Pinecone vector metadata to include the correct project_id.

Usage:
    cd backend
    uv run python scripts/migrate_to_default_workspace.py
"""

import asyncio
import sys
import os

# Ensure backend is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, func, and_
from app.db.session import AsyncSessionLocal
from app.models.user import User
from app.models.project import Project
from app.models.memory import Memory
from app.models.document import Document
from app.models.chat import ChatSession
from app.models.fact import Fact


async def get_or_create_default_project(db: AsyncSession, user_id: int) -> int:
    """Find or create the 'default' project for a user."""
    result = await db.execute(
        select(Project).where(Project.user_id == user_id, Project.name == "default")
    )
    proj = result.scalars().first()
    if not proj:
        proj = Project(
            user_id=user_id,
            name="default",
            description="Default workspace project",
            color="#4f46e5"
        )
        db.add(proj)
        await db.flush()
    return proj.id


async def migrate_sql_records():
    """Migrate all NULL project_id SQL records to each user's default project."""
    print("=" * 60)
    print("MIGRATION: Assign NULL project_id records to 'default' workspace")
    print("=" * 60)

    async with AsyncSessionLocal() as db:
        # 1. Get all users
        result = await db.execute(select(User))
        users = result.scalars().all()
        print(f"\nFound {len(users)} users to process.\n")

        total_updated = {
            "memories": 0,
            "documents": 0,
            "chat_sessions": 0,
            "facts": 0,
        }

        for user in users:
            print(f"--- Processing user {user.id} ({user.email}) ---")

            # Get or create default project
            default_project_id = await get_or_create_default_project(db, user.id)
            print(f"  Default project ID: {default_project_id}")

            # Count NULL records per table
            mem_count = await db.scalar(
                select(func.count()).select_from(Memory).where(
                    Memory.user_id == user.id, Memory.project_id == None
                )
            )
            doc_count = await db.scalar(
                select(func.count()).select_from(Document).where(
                    Document.user_id == user.id, Document.project_id == None
                )
            )
            chat_count = await db.scalar(
                select(func.count()).select_from(ChatSession).where(
                    ChatSession.user_id == user.id, ChatSession.project_id == None
                )
            )
            fact_count = await db.scalar(
                select(func.count()).select_from(Fact).where(
                    Fact.user_id == user.id, Fact.project_id == None
                )
            )

            print(f"  NULL records: Memories={mem_count}, Documents={doc_count}, "
                  f"ChatSessions={chat_count}, Facts={fact_count}")

            # Update Memories
            if mem_count:
                await db.execute(
                    update(Memory)
                    .where(Memory.user_id == user.id, Memory.project_id == None)
                    .values(project_id=default_project_id)
                )
                total_updated["memories"] += mem_count

            # Update Documents
            if doc_count:
                await db.execute(
                    update(Document)
                    .where(Document.user_id == user.id, Document.project_id == None)
                    .values(project_id=default_project_id)
                )
                total_updated["documents"] += doc_count

            # Update ChatSessions
            if chat_count:
                await db.execute(
                    update(ChatSession)
                    .where(ChatSession.user_id == user.id, ChatSession.project_id == None)
                    .values(project_id=default_project_id)
                )
                total_updated["chat_sessions"] += chat_count

            # Update Facts
            if fact_count:
                await db.execute(
                    update(Fact)
                    .where(Fact.user_id == user.id, Fact.project_id == None)
                    .values(project_id=default_project_id)
                )
                total_updated["facts"] += fact_count

            # Try to update optional models (EntityProfile, MemoryCluster)
            try:
                from app.models.entity_profile import EntityProfile
                ep_count = await db.scalar(
                    select(func.count()).select_from(EntityProfile).where(
                        EntityProfile.user_id == user.id, EntityProfile.project_id == None
                    )
                )
                if ep_count:
                    await db.execute(
                        update(EntityProfile)
                        .where(EntityProfile.user_id == user.id, EntityProfile.project_id == None)
                        .values(project_id=default_project_id)
                    )
                    print(f"  Updated {ep_count} EntityProfiles")
            except Exception as e:
                print(f"  EntityProfile update skipped: {e}")

            try:
                from app.models.cluster import MemoryCluster
                mc_count = await db.scalar(
                    select(func.count()).select_from(MemoryCluster).where(
                        MemoryCluster.user_id == user.id, MemoryCluster.project_id == None
                    )
                )
                if mc_count:
                    await db.execute(
                        update(MemoryCluster)
                        .where(MemoryCluster.user_id == user.id, MemoryCluster.project_id == None)
                        .values(project_id=default_project_id)
                    )
                    print(f"  Updated {mc_count} MemoryClusters")
            except Exception as e:
                print(f"  MemoryCluster update skipped: {e}")

            print(f"  ✓ Done for user {user.id}")

        # Commit all changes
        await db.commit()
        print(f"\n{'=' * 60}")
        print("MIGRATION COMPLETE - SQL Records Updated:")
        for table, count in total_updated.items():
            print(f"  {table}: {count} records updated")
        print(f"{'=' * 60}")


async def migrate_vector_metadata():
    """
    Batch-update Pinecone vectors that have no project_id metadata.
    This is optional and should be run after the SQL migration.
    """
    print("\n" + "=" * 60)
    print("VECTOR STORE MIGRATION: Update metadata for orphaned vectors")
    print("=" * 60)

    try:
        from app.services.vector_store import vector_store
    except Exception as e:
        print(f"Could not import vector_store: {e}")
        print("Skipping vector metadata migration.")
        return

    async with AsyncSessionLocal() as db:
        # Get all users and their default project IDs
        result = await db.execute(select(User))
        users = result.scalars().all()

        for user in users:
            default_project_id = await get_or_create_default_project(db, user.id)

            # Query vectors for this user that lack project_id
            # Note: Pinecone filtering for "field does not exist" is tricky.
            # We query by user_id and then check metadata client-side.
            try:
                results = await vector_store.query(
                    query_texts="general query",
                    n_results=100,
                    where={"user_id": str(user.id)}
                )

                if not results or not results.get("ids") or not results["ids"][0]:
                    continue

                vectors_to_update = []
                for i, meta in enumerate(results["metadatas"][0]):
                    if "project_id" not in meta or not meta.get("project_id"):
                        vid = results["ids"][0][i]
                        vectors_to_update.append(vid)

                if vectors_to_update:
                    print(f"  User {user.id}: Found {len(vectors_to_update)} vectors without project_id")
                    # Update metadata in batches
                    batch_size = 50
                    for batch_start in range(0, len(vectors_to_update), batch_size):
                        batch_ids = vectors_to_update[batch_start:batch_start + batch_size]
                        try:
                            await vector_store.update_metadata(
                                ids=batch_ids,
                                metadata={"project_id": str(default_project_id)}
                            )
                            print(f"    Updated batch of {len(batch_ids)} vectors")
                        except AttributeError:
                            print(f"    Warning: vector_store does not support update_metadata. "
                                  f"Skipping vector updates for user {user.id}.")
                            break
                        except Exception as e:
                            print(f"    Error updating vectors: {e}")

            except Exception as e:
                print(f"  Error querying vectors for user {user.id}: {e}")

        await db.commit()

    print("Vector metadata migration complete.")


async def main():
    print("\n🚀 Starting Workspace Containerization Migration\n")

    # Phase 1: SQL Records
    await migrate_sql_records()

    # Phase 2: Vector Store (optional, best-effort)
    try:
        await migrate_vector_metadata()
    except Exception as e:
        print(f"\nVector migration failed (non-critical): {e}")
        print("You can re-run this script later to retry.")

    print("\n✅ Migration complete!\n")


if __name__ == "__main__":
    asyncio.run(main())
