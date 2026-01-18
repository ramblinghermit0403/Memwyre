from typing import List, Any, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from app.models.document import Chunk
from app.schemas.document import Chunk as ChunkSchema

from app.api import deps
from app.models.user import User
from app.services.vector_store import vector_store

router = APIRouter()

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5
    view: str = "auto"

class SearchResult(BaseModel):
    text: str
    score: float
    metadata: Any
    chunk: Optional[ChunkSchema] = None

@router.post("/search", response_model=List[SearchResult])
async def search_documents(
    request: SearchRequest,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Search for relevant document chunks with re-ranking based on feedback.
    """
    print(f"DEBUG: Incoming Search Request top_k={request.top_k} query='{request.query}'")
    try:
        from app.services.retrieval_service import retrieval_service
        
        results = await retrieval_service.search_memories(
            query=request.query,
            user_id=current_user.id,
            db=db,
            top_k=request.top_k,
            view=request.view
        )
        
        # Transform to response model
        formatted_results = []
        for res in results:
            chunk_data = None
            if res.get("chunk"):
                try:
                    chunk_data = ChunkSchema.model_validate(res.get("chunk"))
                except Exception as val_err:
                    print(f"CRITICAL: Chunk serialization FAILED for ID {res['chunk'].id}")
                    print(f"Error: {val_err}")
                    # import traceback
                    # traceback.print_exc()
                    pass

            formatted_results.append(SearchResult(
                text=res["text"],
                score=res["score"],
                metadata=res["metadata"],
                chunk=chunk_data
            ))
            
        return formatted_results
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")
