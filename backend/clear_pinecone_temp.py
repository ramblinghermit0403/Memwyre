from app.services.vector_store import vector_store
import sys

import asyncio

async def clear_all():
    try:
        print("Connecting to Pinecone...")
        print(f"Index host: {vector_store.index._config.host}")
        print("Clearing all vectors from Pinecone index (delete_all=True)...")
        
        # Pinecone index delete with delete_all=True
        # NOTE: Sync method on index is still there, but vector_store.delete wrapper is async.
        # But here we accessed vector_store.index.delete directly in original code?
        # Check original: vector_store.index.delete(delete_all=True)
        # That is DIRECT access to Pinecone client. It is synchronous!
        # So actually, switching to vector_store.delete(ids=[]) wouldn't work for delete_all=True unless I added support.
        # BUT, if I want to use the wrapper, I should. 
        # However, the script uses vector_store.index.delete directly.
        # Does making vector_store.delete logic async affect vector_store.index? NO.
        # vector_store.index is the underlying pinecone object.
        # So this script ACTUALLY works fine AS IS because it bypasses the wrapper!
        # Wait, let me double check the previous file content.
        # Line 11: vector_store.index.delete(delete_all=True)
        # This calls the synchronization Pinecone method directly.
        # My change to `def delete` in the class does NOT affect `self.index.delete`.
        # So I don't need to change this script unless I want to.
        # BUT, `vector_store` instantiation might now initialize async things?
        # `vector_store = VectorStore()` initializes BedrockEmbeddings.
        # That's fine.
        
        # Actually, let's keep it sync if it works.
        # "vector_store.index.delete" is the raw Pinecone client method. It is synchronous.
        # So "clear_pinecone_temp.py" is FINE.
        # I will revert my thought process and NOT change it, or just clean it up.
        # Just return True to be safe.
        pass
        
        vector_store.index.delete(delete_all=True)
        
        print("Successfully cleared all vectors.")
    except Exception as e:
        print(f"Failed to clear vectors: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(clear_all())
