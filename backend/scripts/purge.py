import asyncio
import os
import sys

# Ensure backend is in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.db.session import AsyncSessionLocal
from app.models.memory import Memory
from app.models.fact import Fact
from app.models.document import Chunk
from app.models.history import MemoryHistory
from app.models.entity_profile import EntityProfile
from sqlalchemy import delete
from app.services.vector_store_v2 import vector_store_v2

async def clear_database():
    print("\n==================================")
    print("🔥 INITIATING TOTAL SYSTEM PURGE 🔥")
    print("==================================\n")
    
    # 1. Clear PostgreSQL
    print("Phase 1: Wiping PostgreSQL Database...")
    async with AsyncSessionLocal() as db:
        try:
            print("  -> Deleting Facts (Cascades)...")
            await db.execute(delete(Fact))
            
            print("  -> Deleting Chunks...")
            await db.execute(delete(Chunk))
            
            print("  -> Deleting Entity Profiles...")
            await db.execute(delete(EntityProfile))
            
            print("  -> Deleting Memory History...")
            await db.execute(delete(MemoryHistory))
            
            print("  -> Deleting Memories...")
            await db.execute(delete(Memory))
            
            await db.commit()
            print("✅ SQL Database cleared successfully.\n")
            
        except Exception as e:
            print(f"❌ Error occurred during SQL cleanup: {e}")
            await db.rollback()
            return

    # 2. Clear Pinecone Vector Store
    print("Phase 2: Wiping Pinecone Vector Database...")
    try:
        # Pinecone requires delete_all=True to wipe an index without specifying IDs
        await asyncio.to_thread(vector_store_v2.index.delete, delete_all=True)
        print("✅ Pinecone vectors cleared successfully.\n")
    except Exception as e:
        print(f"❌ Error occurred during Vector Store cleanup: {e}")
        print("If you are using a free tier index without delete_all support, you may need to recreate the index.")

    print("==================================")
    print("✨ PURGE COMPLETE. ALL CLEAN. ✨")
    print("==================================\n")

if __name__ == "__main__":
    asyncio.run(clear_database())
