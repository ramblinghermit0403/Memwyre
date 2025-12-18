from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.api import deps
from app.models.user import User
from app.models.api_key import ApiKey
from pydantic import BaseModel
from datetime import datetime
import secrets
import hashlib

router = APIRouter()

class ApiKeyCreate(BaseModel):
    name: str

class ApiKeyResponse(BaseModel):
    id: int
    name: str
    prefix: str
    created_at: datetime
    last_used_at: datetime | None
    is_active: bool
    
    class Config:
        from_attributes = True

class ApiKeyCreatedResponse(ApiKeyResponse):
    key: str # Show full key only once

def hash_key(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()

@router.post("/api-keys", response_model=ApiKeyCreatedResponse)
async def create_api_key(
    key_in: ApiKeyCreate,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Generate a new persistent API Key.
    """
    # Generate secure key
    # Format: bv_sk_<32_hex_chars>
    random_part = secrets.token_hex(32)
    raw_key = f"bv_sk_{random_part}"
    
    hashed = hash_key(raw_key)
    
    api_key = ApiKey(
        user_id=current_user.id,
        name=key_in.name,
        key_hash=hashed,
        prefix=raw_key[:10] + "...",
        is_active=True
    )
    
    db.add(api_key)
    await db.commit()
    await db.refresh(api_key)
    
    # Return raw key attached to response object (not stored in DB)
    response = ApiKeyCreatedResponse.model_validate(api_key)
    response.key = raw_key
    
    return response

@router.get("/api-keys", response_model=List[ApiKeyResponse])
async def list_api_keys(
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    List active API keys.
    """
    result = await db.execute(
        select(ApiKey).filter(ApiKey.user_id == current_user.id).order_by(ApiKey.created_at.desc())
    )
    keys = result.scalars().all()
    return keys

@router.delete("/api-keys/{key_id}")
async def revoke_api_key(
    key_id: int,
    db: AsyncSession = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Revoke (delete) an API key.
    """
    result = await db.execute(
        select(ApiKey).filter(ApiKey.id == key_id, ApiKey.user_id == current_user.id)
    )
    key = result.scalars().first()
    
    if not key:
        raise HTTPException(status_code=404, detail="API Key not found")
        
    await db.delete(key)
    await db.commit()
    
    return {"status": "success", "message": "Key revoked"}
