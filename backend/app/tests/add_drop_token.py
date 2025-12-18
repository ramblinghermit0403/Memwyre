import asyncio
from sqlalchemy import text
from app.db.session import engine

async def add_drop_token_column():
    async with engine.begin() as conn:
        try:
            await conn.execute(text("ALTER TABLE users ADD COLUMN drop_token VARCHAR UNIQUE"))
            print("Successfully added 'drop_token' column to 'users' table.")
        except Exception as e:
            print(f"Error adding column (maybe it exists?): {e}")

if __name__ == "__main__":
    asyncio.run(add_drop_token_column())
