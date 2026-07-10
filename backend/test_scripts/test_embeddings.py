import asyncio
import sys
import os

# Add the backend directory to sys.path so we can import from app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.core.rate_limiter import get_embeddings_instance

async def main():
    print("Testing embeddings model with 10 requests...")
    try:
        embeddings = get_embeddings_instance()
        if not embeddings:
            print("Failed to get embeddings instance.")
            return

        for i in range(1, 11):
            text = f"This is test document number {i}."
            print(f"Request {i}: Embedding text: '{text}'")
            # Try to embed
            try:
                if hasattr(embeddings, 'aembed_query'):
                    vector = await embeddings.aembed_query(text)
                else:
                    vector = embeddings.embed_query(text)
                
                if vector and isinstance(vector, list) and len(vector) > 0:
                    print(f"  -> Success! Vector length: {len(vector)}")
                    # print first 3 floats
                    print(f"  -> Preview: {vector[:3]}")
                else:
                    print(f"  -> Failed: Return value is not a valid vector: {vector}")
            except Exception as e:
                print(f"  -> Exception on request {i}: {e}")
                
    except Exception as e:
        print(f"Fatal error during testing: {e}")

if __name__ == "__main__":
    asyncio.run(main())
