import asyncio
import uuid
from sqlalchemy import select
from app.db.session import AsyncSessionLocal
from app.models.user import User

async def populate():
    async with AsyncSessionLocal() as db:
        result = await db.execute(select(User).where(User.drop_token == None))
        users = result.scalars().all()
        print(f"Updating {len(users)} users with UUID v4 drop tokens...")
        for u in users:
            u.drop_token = str(uuid.uuid4())
            print(f"- {u.email} -> {u.drop_token}")
        await db.commit()
        print("Done.")

if __name__ == "__main__":
    asyncio.run(populate())
