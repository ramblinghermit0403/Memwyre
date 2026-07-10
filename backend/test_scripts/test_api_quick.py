"""Quick test: hit the live API with a proper JWT for user 4."""
import asyncio
import sys
import os
import json
from datetime import timedelta

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.db.session import AsyncSessionLocal
from app.models.user import User
from sqlalchemy import select
from app.core.security import create_access_token
from app.core.config import settings

import requests

def main():
    # Generate token synchronously using asyncio
    async def get_token():
        async with AsyncSessionLocal() as db:
            result = await db.execute(select(User).where(User.id == 4))
            user = result.scalars().first()
            token = create_access_token(user.id, expires_delta=timedelta(minutes=30))
            return token, user.email

    token, email = asyncio.run(get_token())
    print(f"Token for: {email}")

    try:
        response = requests.get(
            "http://localhost:8000/api/v1/memory/",
            headers={"Authorization": f"Bearer {token}"},
            timeout=10
        )
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Items returned: {len(data)}")
            for item in data[:3]:
                print(f"  {item.get('id')}: {item.get('title')[:50]}... type={item.get('type')}")
        else:
            print(f"Body: {response.text[:500]}")
    except requests.exceptions.Timeout:
        print("REQUEST TIMED OUT after 10s - backend is HUNG!")
    except requests.exceptions.ConnectionError as e:
        print(f"CONNECTION ERROR: {e}")

if __name__ == "__main__":
    main()
