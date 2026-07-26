import asyncio
import subprocess
import sys
import os

# Add the parent directory to sys.path so we can import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.ext.asyncio import create_async_engine
from app.core.config import settings
from app.db.base import Base
# Import models to ensure they are registered with Base.metadata
import app.models

async def init_db():
    url = settings.assemble_db_url
    if url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+asyncpg://", 1)
    
    engine = create_async_engine(url)
    async with engine.begin() as conn:
        from sqlalchemy import text
        # Check if users table exists
        res = await conn.execute(text("SELECT to_regclass('public.users');"))
        table_exists = res.scalar() is not None
        
        if not table_exists:
            print("Fresh database detected. Creating tables...")
            await conn.run_sync(Base.metadata.create_all)
            print("Stamping alembic head...")
            subprocess.run(["uv", "run", "alembic", "stamp", "head"], check=True)
            print("Database initialized successfully.")
        else:
            print("Database already initialized. Passing to migrations.")
            
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(init_db())
