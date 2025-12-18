import asyncio
from sqlalchemy import text
from app.db.session import engine

async def add_trusted_column():
    async with engine.begin() as conn:
        try:
            await conn.execute(text("ALTER TABLE memories ADD COLUMN trusted BOOLEAN DEFAULT TRUE"))
            print("Successfully added 'trusted' column to 'memories' table.")
        except Exception as e:
            print(f"Error adding column (maybe it exists?): {e}")

if __name__ == "__main__":
    asyncio.run(add_trusted_column())
