import asyncio
import os
from sqlalchemy.future import select
from app.db.session import AsyncSessionLocal
from app.models.user import User
from app.models.memory import Memory
from app.models.project import Project
from app.models.fact import Fact
from app.services.retrieval_service_v2 import retrieval_service
from app.services.fact_service import fact_service
from app.services.dedupe_job_v2 import dedupe_service_v2

async def run_test():
    async with AsyncSessionLocal() as db:
        # 1. Get any user
        result = await db.execute(select(User))
        user = result.scalars().first()
        if not user:
            print("No users found in database.")
            return

        print(f"Testing Workspace Isolation with User ID: {user.id} ({user.email})")

        # 2. Create two test projects
        proj_a = Project(user_id=user.id, name="Project_Alpha", description="Test Project Alpha")
        proj_b = Project(user_id=user.id, name="Project_Beta", description="Test Project Beta")
        db.add(proj_a)
        db.add(proj_b)
        await db.commit()
        await db.refresh(proj_a)
        await db.refresh(proj_b)
        print(f"Created Projects: Alpha (ID: {proj_a.id}), Beta (ID: {proj_b.id})")

        # 3. Create facts under Project Alpha and Project Beta
        fact_alpha = Fact(
            user_id=user.id,
            project_id=proj_a.id,
            subject="Application",
            predicate="uses",
            object="PostgreSQL",
            is_superseded=False
        )
        fact_beta = Fact(
            user_id=user.id,
            project_id=proj_b.id,
            subject="Application",
            predicate="uses",
            object="SQLite",
            is_superseded=False
        )
        db.add(fact_alpha)
        db.add(fact_beta)
        await db.commit()
        await db.refresh(fact_alpha)
        await db.refresh(fact_beta)
        print(f"Created Facts: Alpha Fact (ID: {fact_alpha.id}), Beta Fact (ID: {fact_beta.id})")

        # Index in vector store
        from app.services.vector_store_v2 import vector_store_v2 as vector_store
        await vector_store.add_documents(
            ids=[f"fact_{fact_alpha.id}", f"fact_{fact_beta.id}"],
            documents=["Application uses PostgreSQL", "Application uses SQLite"],
            metadatas=[
                {
                    "user_id": str(user.id),
                    "type": "fact",
                    "project_id": str(proj_a.id)
                },
                {
                    "user_id": str(user.id),
                    "type": "fact",
                    "project_id": str(proj_b.id)
                }
            ]
        )
        print("Indexed facts in vector store.")

        # 4. Test State (Fact) search scoping for Project Alpha
        print("\n--- Testing search scoping for Project Alpha ---")
        results_alpha = await retrieval_service.search_memories(
            query="Which database does the application use?",
            user_id=user.id,
            db=db,
            top_k=5,
            view="state",
            project_id=proj_a.id
        )
        print("Alpha search results:")
        for r in results_alpha:
            print(f" - {r['text']} (Score: {r['score']})")

        # 5. Test State (Fact) search scoping for Project Beta
        print("\n--- Testing search scoping for Project Beta ---")
        results_beta = await retrieval_service.search_memories(
            query="Which database does the application use?",
            user_id=user.id,
            db=db,
            top_k=5,
            view="state",
            project_id=proj_b.id
        )
        print("Beta search results:")
        for r in results_beta:
            print(f" - {r['text']} (Score: {r['score']})")

        # 6. Test Deduplication / Conflict Isolation
        # Create a new memory in Project Alpha stating "Application uses PostgreSQL"
        # and verify it does NOT mark Project Beta's fact ("uses SQLite") as superseded.
        print("\n--- Testing Deduplication / Conflict Isolation ---")
        conflict_mem = Memory(
            user_id=user.id,
            project_id=proj_a.id,
            title="Database Update",
            content="Confirm that application uses PostgreSQL",
            source_llm="test_script",
            status="approved"
        )
        db.add(conflict_mem)
        await db.commit()
        await db.refresh(conflict_mem)

        # Run deduplication check
        await dedupe_service_v2.check_duplicates(conflict_mem.id, db)
        
        # Verify facts status
        await db.refresh(fact_alpha)
        await db.refresh(fact_beta)
        print(f"Alpha Fact is_superseded: {fact_alpha.is_superseded}")
        print(f"Beta Fact is_superseded: {fact_beta.is_superseded}")

        # Cleanup
        try:
            await vector_store.delete([f"fact_{fact_alpha.id}", f"fact_{fact_beta.id}"])
            print("Deleted facts from vector store.")
        except Exception as e:
            print(f"Error deleting vector docs: {e}")

        await db.delete(conflict_mem)
        await db.delete(fact_alpha)
        await db.delete(fact_beta)
        await db.delete(proj_a)
        await db.delete(proj_b)
        await db.commit()
        print("\nCleanup completed.")

if __name__ == "__main__":
    asyncio.run(run_test())
