import asyncio
import os
import sys
from sqlalchemy import text, inspect

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.db.session import engine

async def migrate_schema():
    print("Starting Chunk Schema Migration...")
    
    async with engine.begin() as conn:
        # Check current dialect
        dialect = conn.dialect.name
        print(f"Detected Database Dialect: {dialect}")
        
        if dialect == "sqlite":
            await migrate_sqlite(conn)
        elif dialect == "postgresql":
            await migrate_postgres(conn)
        else:
            print("Unsupported dialect.")

async def migrate_postgres(conn):
    print("Applying Postgres Changes...")
    try:
        # 1. Add memory_id
        await conn.execute(text("ALTER TABLE chunks ADD COLUMN IF NOT EXISTS memory_id INTEGER REFERENCES memories(id);"))
        print("- Added memory_id column")
        
        # 2. Make document_id nullable
        await conn.execute(text("ALTER TABLE chunks ALTER COLUMN document_id DROP NOT NULL;"))
        print("- Made document_id nullable")
        
    except Exception as e:
        print(f"Error: {e}")

async def migrate_sqlite(conn):
    print("Applying SQLite Changes (Table Rebuild)...")
    # SQLite requires table recreation to change nullability
    try:
        # 1. Check if memory_id already exists to avoid double run
        # Implementation via raw SQL check is safer than inspect in async for simple check
        try:
             await conn.execute(text("SELECT memory_id FROM chunks LIMIT 1"))
             print("memory_id already exists. Skipping.")
             return
        except:
             pass

        # 2. Rename old table
        await conn.execute(text("ALTER TABLE chunks RENAME TO chunks_old;"))
        
        # 3. Create new table (Based on current app/models/document.py definition logic + changes)
        # We define it manually here to ensure it matches what we want
        create_sql = """
        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER REFERENCES documents(id),
            memory_id INTEGER REFERENCES memories(id),
            chunk_index INTEGER,
            text TEXT NOT NULL,
            embedding_id VARCHAR,
            metadata_json JSON,
            summary TEXT,
            generated_qas JSON,
            tokens_count INTEGER,
            trust_score FLOAT DEFAULT 0.5,
            last_validated_at TIMESTAMP,
            feedback_score FLOAT DEFAULT 0.0,
            entities JSON,
            tags JSON
        );
        """
        await conn.execute(text(create_sql))
        print("- Created new chunks table")
        
        # 4. Copy data
        # We only copy rows where document_id is not null (which is all of them currently)
        copy_sql = """
        INSERT INTO chunks (id, document_id, chunk_index, text, embedding_id, metadata_json, summary, generated_qas, tokens_count, trust_score, last_validated_at, feedback_score, entities, tags)
        SELECT id, document_id, chunk_index, text, embedding_id, metadata_json, summary, generated_qas, tokens_count, trust_score, last_validated_at, feedback_score, entities, tags
        FROM chunks_old;
        """
        await conn.execute(text(copy_sql))
        print("- Copied data")
        
        # 5. Drop old table
        await conn.execute(text("DROP TABLE chunks_old;"))
        print("- Dropped old table")
        
    except Exception as e:
        print(f"Error in SQLite migration: {e}")
        # Try to rollback rename if needed? Transaction should handle it.

if __name__ == "__main__":
    asyncio.run(migrate_schema())
