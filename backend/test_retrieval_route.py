
from fastapi.testclient import TestClient
from app.main import app
from app.api import deps
from app.models.user import User

# Dummy User
mock_user = User(id=4, email="test@test.com")

# Dependency Override
async def override_get_current_user():
    return mock_user

app.dependency_overrides[deps.get_current_user] = override_get_current_user

client = TestClient(app)

def test_search_route():
    print("--- Testing /api/v1/retrieval/search ---")
    
    # Request Payload
    payload = {
        "query": "Caroline",
        "top_k": 5,
        "view": "state" # Force Fact Search
    }
    
    response = client.post("/api/v1/retrieval/search", json=payload)
    
    if response.status_code != 200:
        print(f"FAILED: {response.text}")
        return

    data = response.json()
    print(f"Status: {response.status_code}")
    print(f"Results Count: {len(data)}")
    
    for i, res in enumerate(data):
        chunk = res.get("chunk")
        fact_id = res['metadata'].get('fact_id')
        print(f"[{i}] Fact ID: {fact_id} | Chunk Present: {chunk is not None}")
        
        # Verify Structure
        if chunk:
            print(f"    Chunk ID: {chunk.get('id')}")
            print(f"    Chunk Text: {chunk.get('text')[:40]}...")
            
            # Check for keys that might have been filtered
            if 'metadata_json' in chunk:
                 print("    Chunk has metadata_json")
        else:
             print("    Chunk is NULL!")

if __name__ == "__main__":
    test_search_route()
