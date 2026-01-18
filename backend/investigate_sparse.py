import asyncio
import os
from app.services.vector_store import VectorStore
from app.services.ingestion import ingestion_service
from app.core.config import settings

async def investigate_ingestion():
    print("--- Investigating Sparse Index Population ---")
    
    # Check Settings
    print(f"PINECONE_SPARSE_HOST: {settings.PINECONE_SPARSE_HOST}")
    
    # Mock Document
    text = "The quick brown fox jumps over the lazy dog."
    doc_id = 999
    
    try:
        # 1. Test Ingestion Service (Sparse Generation)
        print("\n1. Testing Ingestion Service Generation...")
        ids, contents, enriched_chunks, metadatas, sparse_values = await ingestion_service.process_text(
            text=text,
            document_id=doc_id,
            title="Investigation Doc",
            doc_type="test",
            metadata={}
        )
        
        print(f"   Generated {len(ids)} chunks.")
        
        has_sparse = all(sv is not None and len(sv['indices']) > 0 for sv in sparse_values)
        if has_sparse:
             print(f"   Success! Sparse Values Generated: {sparse_values[0].keys()} (indices, values)")
             print(f"   Sample Sparse: {sparse_values[0]}")
        else:
             print("   FAILURE: Sparse values are empty or None!")
             return

        # 2. Test Vector Store Upsert
        print("\n2. Testing Vector Store Upsert...")
        vs = VectorStore()
        
        if not vs.sparse_index:
            print("   FAILURE: VectorStore.sparse_index is None!")
            return
            
        success = await vs.add_documents(
            ids=ids,
            documents=enriched_chunks,
            metadatas=metadatas,
            sparse_values=sparse_values
        )
        
        if success:
            print("   Vector Store Upsert returned True.")
        else:
            print("   Vector Store Upsert returned False.")
            
        # 3. Verify Upsert in Pinecone
        print("\n3. Verifying Persistence in Sparse Index...")
        # Fetch the vector back
        fetch_id = ids[0]
        resp = await asyncio.to_thread(vs.sparse_index.fetch, ids=[fetch_id])
        
        if resp and resp.get("vectors") and fetch_id in resp["vectors"]:
             vec = resp["vectors"][fetch_id]
             print(f"   Success! Vector found in Sparse Index.")
             print(f"   Values (Dense Placeholder): {vec.get('values')}")
             print(f"   Sparse Values: {vec.get('sparse_values')}")
        else:
             print(f"   FAILURE: Vector {fetch_id} NOT found in Sparse Index.")

        # Cleanup
        await vs.delete(ids=ids)
        print("\nCleanup: Deleted test vector.")

    except Exception as e:
        print(f"CRITICAL FAILURE: {e}")

if __name__ == "__main__":
    asyncio.run(investigate_ingestion())
