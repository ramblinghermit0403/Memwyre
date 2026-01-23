from typing import List, Any, Optional
from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.api import deps
from app.models.user import User
from app.services.vector_store import vector_store
from app.services.llm_service import llm_service
from app.services.usage_service import usage_service
from app.core.guardrails import guardrails

router = APIRouter()
from app.core.rate_limiter import limiter

class ChatRequest(BaseModel):
    query: str
    provider: str = "openai"
    api_key: str
    top_k: int = 5
    filter: Optional[dict] = None

class ChatResponse(BaseModel):
    response: str
    context: List[str]

from app.models.memory import Memory
from app.models.document import Document

@router.post("/chat", response_model=ChatResponse)
@limiter.limit("15/minute")
async def chat_with_llm(
    request: Request,
    chat_request: ChatRequest,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Chat with LLM using retrieved context.
    """
    try:
        # -1. Guard Rails
        guardrails.validate_input(chat_request.query)

        # 0. Check Budget
        if not await usage_service.check_budget(current_user.id):
             raise HTTPException(status_code=429, detail="Daily LLM budget exceeded.")

        # 1. Retrieve context
        where_clause = {"user_id": current_user.id}
        if chat_request.filter:
            # Ensure IDs are integers
            if "document_id" in chat_request.filter:
                try:
                    chat_request.filter["document_id"] = int(chat_request.filter["document_id"])
                except:
                    pass
            if "memory_id" in request.filter:
                try:
                    chat_request.filter["memory_id"] = int(chat_request.filter["memory_id"])
                except:
                    pass
            
            # ChromaDB/Pinecone filter adaptation
            # Pinecone uses $and for multiple conditions filter={"$and": [...]}
            # But specific "document_id" is simple scalar.
            # Only use $and if we have multiple keys.
            if len(chat_request.filter) > 0:
                where_clause.update(chat_request.filter)
            
        results = await vector_store.query(chat_request.query, n_results=chat_request.top_k, where=where_clause)
        
        context = []
        if results["documents"] and results.get("distances"):
            # Filter by relevance (Distance Threshold)
            # Threshold depends on metric. Chroma default is L2. 
            # Lower is better. < 1.0 is usually good, > 1.5 is often irrelevant.
            threshold = 1.5 
            
            for i, doc in enumerate(results["documents"][0]):
                distance = results["distances"][0][i]
                
                # Fallback: If doc text is missing (e.g. from old migration), fetch from DB
                if not doc and results["metadatas"][0][i]:
                    meta = results["metadatas"][0][i]
                    try:
                        if meta.get("memory_id"):
                            result = await db.execute(select(Memory).where(Memory.id == int(meta["memory_id"])))
                            mem = result.scalars().first()
                            if mem:
                                doc = mem.content
                        elif meta.get("document_id"):
                             result = await db.execute(select(Document).where(Document.id == int(meta["document_id"])))
                             doc_obj = result.scalars().first()
                             if doc_obj:
                                 # This might be full content, but better than nothing
                                 doc = doc_obj.content
                    except Exception as e:
                        print(f"Fallback fetch failed: {e}")

                if distance < threshold:
                    if doc:
                        context.append(doc)
        elif results["documents"]:
             # Fallback if no distances returned (unlikely)
             context = results["documents"][0]

        # 2. Generate response
        response = await llm_service.generate_response(
            query=chat_request.query,
            context=context,
            provider=chat_request.provider,
            api_key=chat_request.api_key,
            user_id=current_user.id
        )
        
        return ChatResponse(response=response, context=context)

    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat failed: {str(e)}")

class SuggestTagsRequest(BaseModel):
    content: str
    existing_tags: List[str] = []
    
@router.post("/suggest_tags", response_model=List[str])
async def suggest_tags(
    request: SuggestTagsRequest,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Generate AI tags for the provided content on demand.
    """
    from app.models.client import AIClient
    from app.core.encryption import encryption_service
    
    # Fetch API Key (Gemini preferred for speed/cost)
    provider = "gemini"
    result = await db.execute(select(AIClient).where(AIClient.user_id == current_user.id, AIClient.provider == provider))
    client = result.scalars().first()
    
    if not client:
        provider = "openai"
        result = await db.execute(select(AIClient).where(AIClient.user_id == current_user.id, AIClient.provider == provider))
        client = result.scalars().first()
    
    api_key = None
    if client:
        try:
            api_key = encryption_service.decrypt(client.encrypted_api_key)
        except:
             # Log warning but continue, maybe Bedrock works
             pass
    
    # We no longer strictly raise HTTPException if client is missing, 
    # because the system might be using Bedrock (Nova Pro) credentials from the environment.
        
    metadata = await llm_service.extract_metadata(
        content=request.content,
        existing_tags=request.existing_tags,
        api_key=api_key
    )
    
    return metadata.get("tags", [])
