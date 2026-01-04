from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from app.models.document import Chunk

from app.api import deps
from app.models.user import User
from app.services.vector_store import vector_store

router = APIRouter()

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5

class SearchResult(BaseModel):
    text: str
    score: float
    metadata: Any

@router.post("/search", response_model=List[SearchResult])
async def search_documents(
    request: SearchRequest,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Search for relevant document chunks with re-ranking based on feedback.
    """
    try:
        from app.services.retrieval_service import retrieval_service
        
        results = await retrieval_service.search_memories(
            query=request.query,
            user_id=current_user.id,
            db=db,
            top_k=request.top_k
        )
        
        # Transform to response model
        formatted_results = []
        for res in results:
            formatted_results.append(SearchResult(
                text=res["text"],
                score=res["score"],
                metadata=res["metadata"]
            ))
            
        return formatted_results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")
