import asyncio
import os
from app.services.vector_store import VectorStore
from app.core.config import settings

async def debug_upsert():
    print("--- Debugging Sparse Upsert ---")
    
    if not settings.PINECONE_SPARSE_HOST:
        print("SKIP: PINECONE_SPARSE_HOST not set.")
        return

    vs = VectorStore()
    
    # Try omitting dense values
    # zero_vec = [0.0] * dense_dim
    
    sparse_vec = {
        "indices": [10, 20, 30],
        "values": [0.5, 0.5, 0.5]
    }
    
    vector = {
        "id": "debug_test_id_no_dense",
        "values": [], # Sending EMPTY dense values
        "sparse_values": sparse_vec,
        "metadata": {"type": "debug"}
    }
    
    print(f"Attempting Upsert to Sparse Index (Values=[]): {settings.PINECONE_SPARSE_HOST}")

    print(f"Payload ID: {vector['id']}")
    # print(f"Payload Dense Dim: {len(zero_vec)}")
    
    try:
        # Direct upsert to sparse index
        resp = await asyncio.to_thread(
            vs.sparse_index.upsert,
            vectors=[vector]
        )
        print(f"Upsert Success! Response: {resp}")
        
    except Exception as e:
        print(f"### UPSERT FAILED ###")
        print(e)
        
        # Try finding out why
        if "dimension" in str(e).lower():
            print("HINT: Dimension mismatch. Check if Sparse Index was created with dim=1024.")
            
    # Cleanup
    # ...

if __name__ == "__main__":
    asyncio.run(debug_upsert())
