import asyncio
from app.services.vector_store_v2 import vector_store_v2

async def main():
    # 1. Set your test parameters here
    query_text = "adoption agency"
    user_id = "4" # e.g., "1"
    top_k = 10 # Number of raw results to fetch
    
    print(f"Generating embedding for: '{query_text}'...")
    print(f"Querying Pinecone for user_id: {user_id}...")
    
    # 2. Query Pinecone directly (bypassing Cross-Encoder and MMR)
    # This calls the exact same vector_store query method used in the app
    results = await vector_store_v2.query(
        query_texts=query_text,
        n_results=top_k,
        where={"user_id": user_id},
        include_values=False # Set to True if you want to see the giant vector arrays
    )
    
    # 3. Print the raw results
    print("\n--- RAW PINECONE RESULTS (Pre-Reranking) ---")
    
    if not results.get("ids") or not results["ids"][0]:
        print("No results found in Pinecone for this query and user_id.")
        return

    ids = results["ids"][0]
    distances = results["distances"][0]
    docs = results["documents"][0]
    metas = results["metadatas"][0]
    
    for i in range(len(ids)):
        chunk_type = metas[i].get("type", "unknown")
        print(f"\n[Result {i+1}] ID: {ids[i]} | Type: {chunk_type} | Score/Distance: {distances[i]:.4f}")
        print(f"Metadata: {metas[i]}")
        print(f"Text Snippet: {docs[i][:200]}...")

if __name__ == "__main__":
    asyncio.run(main())
