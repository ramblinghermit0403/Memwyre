import asyncio
import httpx
import sys
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

# First, get a user token
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.db.session import engine
from app.models.user import User
from sqlalchemy import select
from app.core.security import create_access_token
from datetime import timedelta
from app.core.config import settings

async def main():
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as db:
        result = await db.execute(select(User).limit(1))
        user = result.scalars().first()
        if not user:
            print("No user found!")
            return
        
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        token = create_access_token(
            user.id, expires_delta=access_token_expires
        )
        print(f"User: {user.email}")
        
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "http://localhost:8000/api/v1/memory/",
            headers={"Authorization": f"Bearer {token}"}
        )
        print(f"Status: {response.status_code}")
        data = response.json()
        print(f"Response body: {data}")
        if isinstance(data, list):
            print(f"Returned items: {len(data)}")
            for d in data[:5]:
                print(f" - {d.get('id')}: {d.get('title')} ({d.get('type')})")

asyncio.run(main())
