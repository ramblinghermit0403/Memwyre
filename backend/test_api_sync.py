import sys
import os
import requests
import asyncio
from datetime import timedelta

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.db.session import AsyncSessionLocal
from app.models.user import User
from sqlalchemy import select
from app.core.security import create_access_token
from app.core.config import settings

async def get_token(user_id: int):
    async with AsyncSessionLocal() as db:
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalars().first()
        if not user:
            print("No user found!")
            return None
        
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        token = create_access_token(
            user.id, expires_delta=access_token_expires
        )
        print(f"Generated token for user {user.email}")
        return token

def main():
    token = asyncio.run(get_token(4)) # User 4
    if not token:
        return
        
    response = requests.get(
        "http://localhost:8000/api/v1/memory/",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    print(f"Status Code: {response.status_code}")
    data = response.json()
    if isinstance(data, list):
        print(f"Total returned: {len(data)}")
        for item in data[:5]:
            print(f" - {item.get('id')}: {item.get('title')} ({item.get('type')})")
    else:
        print(f"Response: {data}")

if __name__ == "__main__":
    main()
