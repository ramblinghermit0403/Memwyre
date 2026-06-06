from fastapi.testclient import TestClient
from app.main import app
from app.api.deps import get_current_user
from app.models.user import User

def override_get_current_user():
    return User(id=1, email="test@example.com", is_active=True)

app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)

response = client.get("/api/v1/memory/")
if response.status_code == 200:
    data = response.json()
    print(f"Total returned: {len(data)}")
    for d in data[:10]:
        print(f"{d.get('id')} - {d.get('type')} - {d.get('title')}")
else:
    print(f"Error {response.status_code}: {response.text}")
