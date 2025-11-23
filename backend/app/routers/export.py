from typing import Any
from fastapi import APIRouter, Depends
from fastapi.responses import Response
from sqlalchemy.orm import Session
import json

from app.api import deps
from app.models.user import User
from app.models.memory import Memory
from app.models.document import Document

router = APIRouter()

@router.get("/json")
def export_json(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    memories = db.query(Memory).filter(Memory.user_id == current_user.id).all()
    documents = db.query(Document).filter(Document.user_id == current_user.id).all()
    
    data = {
        "memories": [
            {
                "id": m.id,
                "title": m.title,
                "content": m.content,
                "created_at": m.created_at.isoformat() if m.created_at else None
            } for m in memories
        ],
        "documents": [
            {
                "id": d.id,
                "title": d.title,
                "source": d.source,
                "file_type": d.file_type,
                "created_at": d.created_at.isoformat() if d.created_at else None
            } for d in documents
        ]
    }
    
    return Response(
        content=json.dumps(data, indent=2),
        media_type="application/json",
        headers={"Content-Disposition": "attachment; filename=brain_vault_export.json"}
    )

@router.get("/md")
def export_markdown(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    memories = db.query(Memory).filter(Memory.user_id == current_user.id).all()
    documents = db.query(Document).filter(Document.user_id == current_user.id).all()
    
    md_content = f"# Brain Vault Export for {current_user.email}\n\n"
    
    md_content += "## Memories\n\n"
    for m in memories:
        md_content += f"### {m.title}\n{m.content}\n\n"
        
    md_content += "## Documents\n\n"
    for d in documents:
        md_content += f"### {d.title}\nSource: {d.source}\n\n"
        # We could add chunk content here if we wanted
        
    return Response(
        content=md_content,
        media_type="text/markdown",
        headers={"Content-Disposition": "attachment; filename=brain_vault_export.md"}
    )
