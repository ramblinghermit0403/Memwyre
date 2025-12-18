import asyncio
from app.db.session import AsyncSessionLocal
from app.models.user import User
from sqlalchemy.future import select

async def check():
    async with AsyncSessionLocal() as db:
        res = await db.execute(select(User))
        users = res.scalars().all()
        print(f"Users found: {len(users)}")
        for u in users:
            print(f"- {u.email} (id: {u.id})")

if __name__ == "__main__":
    asyncio.run(check())
