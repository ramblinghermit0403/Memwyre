import asyncio
import os
from sqlalchemy.future import select
from app.db.session import AsyncSessionLocal
from app.models.user import User
from app.models.memory import Memory
from mcp_server import approve_memory, discard_memory

async def run_test():
    async with AsyncSessionLocal() as db:
        # 1. Get any user
        result = await db.execute(select(User))
        user = result.scalars().first()
        if not user:
            print("No users found in database.")
            return

        print(f"Testing with User ID: {user.id} ({user.email})")
        os.environ["BRAIN_VAULT_USER_ID"] = str(user.id)

        # 2. Create a pending memory
        memory = Memory(
            user_id=user.id,
            title="Test Memory for MCP",
            content="This is a temporary test memory to verify approve and discard tools.",
            source_llm="test_script",
            status="pending",
            show_in_inbox=True
        )
        db.add(memory)
        await db.commit()
        await db.refresh(memory)
        mem_id_str = f"mem_{memory.id}"
        print(f"Created pending memory: {mem_id_str}")

    # 3. Test approve_memory
    print("Testing approve_memory...")
    approve_result = await approve_memory(mem_id_str, None)
    print(f"Approve Result: {approve_result}")

    # 4. Verify status updated to approved
    async with AsyncSessionLocal() as db:
        result = await db.execute(select(Memory).filter(Memory.id == memory.id))
        mem_check = result.scalars().first()
        print(f"Status after approve: {mem_check.status} (show_in_inbox: {mem_check.show_in_inbox})")

    # 5. Reset status to pending to test discard
    async with AsyncSessionLocal() as db:
        result = await db.execute(select(Memory).filter(Memory.id == memory.id))
        mem_check = result.scalars().first()
        mem_check.status = "pending"
        mem_check.show_in_inbox = True
        await db.commit()
    
    # 6. Test discard_memory
    print("Testing discard_memory...")
    discard_result = await discard_memory(mem_id_str, None)
    print(f"Discard Result: {discard_result}")

    # 7. Verify status updated to discarded
    async with AsyncSessionLocal() as db:
        result = await db.execute(select(Memory).filter(Memory.id == memory.id))
        mem_check = result.scalars().first()
        print(f"Status after discard: {mem_check.status} (show_in_inbox: {mem_check.show_in_inbox})")

if __name__ == "__main__":
    asyncio.run(run_test())
