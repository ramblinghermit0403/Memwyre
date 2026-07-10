from app.schemas.memory import Memory as MemorySchema
from datetime import datetime

data = {
    "id": "doc_1",
    "title": "Untitled Document",
    "content": "Uploaded Document: test_doc.txt (txt)",
    "user_id": 1,
    "created_at": datetime.now(),
    "updated_at": None,
    "source": "test_doc.txt",
    "source_app": "test_doc.txt",
    "interaction_type": "document",
    "project_id": None,
    "project_name": None,
    "doc_type": "document",
    "type": "document",
    "tags": [],
}

try:
    memory = MemorySchema(**data)
    print("Success:", memory.model_dump())
except Exception as e:
    print("Validation Error:", e)
