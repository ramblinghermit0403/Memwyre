from typing import Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.token_tracker import token_tracker

router = APIRouter()

class TokenCountRequest(BaseModel):
    text: str
    provider: Optional[str] = "openai" # "openai", "azure", "bedrock", "gcp"
    model_name: Optional[str] = "gpt-4o"

class TokenCountResponse(BaseModel):
    tokens_count: int
    estimated_cost: float
    provider: str
    model_name: str
    normalized_model: str

@router.post("/count", response_model=TokenCountResponse)
async def count_tokens(request: TokenCountRequest):
    """
    Compute exact token counts and estimated costs for any cloud provider and model.
    Supports Azure OpenAI, AWS Bedrock, GCP (Gemini/Vertex), and OpenAI/Anthropic.
    """
    if request.text is None:
        raise HTTPException(status_code=400, detail="Text field is required.")

    provider = request.provider or "openai"
    model_name = request.model_name or "gpt-4o"

    tokens = token_tracker.count_tokens(request.text, provider=provider, model_name=model_name)
    cost = token_tracker.calculate_cost(tokens_in=tokens, tokens_out=0, provider=provider, model_name=model_name)
    normalized = token_tracker.normalize_model(provider, model_name)

    return TokenCountResponse(
        tokens_count=tokens,
        estimated_cost=cost,
        provider=provider,
        model_name=model_name,
        normalized_model=normalized
    )
