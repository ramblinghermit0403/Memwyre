import asyncio
from app.db.session import AsyncSessionLocal
from app.routers.memory import read_memories
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

async def main():
    async with AsyncSessionLocal() as db:
        # Get first user
        result = await db.execute(select(User).limit(1))
        user = result.scalars().first()
        if not user:
            print("No users found.")
            return

        print(f"Testing with user: {user.email}")
        
        try:
            memories = await read_memories(
                skip=0, limit=100, tag=None, view=None,
                project_id=None, source_app=None, interaction_type=None,
                date_from=None, date_to=None, db=db, current_user=user
            )
            print(f"Returned {len(memories)} items.")
            for m in memories:
                print(f"ID: {m['id']} | Title: {m['title']} | Type: {m.get('type')}")
        except Exception as e:
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
