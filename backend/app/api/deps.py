from typing import AsyncGenerator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import AsyncSessionLocal
from app.core.config import settings
from app.models.user import User
from app.core import security

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()

async def get_current_user(
    db: AsyncSession = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Check for API Key (starts with bv_sk_)
    if token.startswith("bv_sk_"):
        import hashlib
        from app.models.api_key import ApiKey
        from datetime import datetime
        
        hashed = hashlib.sha256(token.encode()).hexdigest()
        
        result = await db.execute(select(ApiKey).where(ApiKey.key_hash == hashed, ApiKey.is_active == True))
        api_key_obj = result.scalars().first()
        
        if not api_key_obj:
             raise credentials_exception
             
        # Update usage stats
        api_key_obj.last_used_at = datetime.now()
        await db.commit()
        
        # Get user
        result_user = await db.execute(select(User).where(User.id == api_key_obj.user_id))
        user = result_user.scalars().first()
        if not user:
            raise credentials_exception
        return user

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # Async query
    result = await db.execute(select(User).where(User.id == int(user_id)))
    user = result.scalars().first()
    
    if user is None:
        raise credentials_exception
    return user


async def require_subscription(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> User:
    """
    Feature gate: requires an active subscription OR dev mode.
    Use this as a dependency on routers/endpoints that should be paywalled.
    """
    if settings.DEV_MODE:
        return current_user

    from app.models.subscription import Subscription

    result = await db.execute(
        select(Subscription).where(Subscription.user_id == current_user.id)
    )
    sub = result.scalars().first()

    if not sub or sub.status != "active":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Active subscription required. Please upgrade to Pro.",
            headers={"X-Requires-Subscription": "true"},
        )
    return current_user

async def verify_usage_limits(
    doc_type: str,     # 'memory' or 'document'
    content_len: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> bool:
    """Verifies that the user has not exceeded their quotas and content limits."""
    if settings.DEV_MODE:
        return True
    
    from app.models.subscription import Subscription
    from sqlalchemy import func

    # Check subscription
    result = await db.execute(select(Subscription).where(Subscription.user_id == current_user.id))
    sub = result.scalars().first()
    is_pro = sub and sub.status == "active"

    # Enforce Character Size Limits
    if doc_type == "memory":
        if content_len > settings.MAX_CHARS_PER_MEMORY:
            raise HTTPException(status_code=413, detail=f"Memory exceeds token limit. Max {settings.MAX_CHARS_PER_MEMORY} characters allowed.")
    else:  # Document
        max_doc_chars = settings.MAX_CHARS_PER_DOC_PRO if is_pro else settings.MAX_CHARS_PER_DOC_FREE
        if content_len > max_doc_chars:
            raise HTTPException(status_code=413, detail=f"Document exceeds token limit. Max {max_doc_chars} characters allowed.")

    # Enforce Quantity Limits for Free Tier
    if not is_pro:
        if doc_type == "memory":
            from app.models.memory import Memory
            count = await db.scalar(select(func.count()).select_from(Memory).where(Memory.user_id == current_user.id))
            if count and count >= settings.FREE_MEMORY_LIMIT:
                raise HTTPException(
                    status_code=403, 
                    detail="Free tier limit reached: 10 Memories max. Please upgrade to Pro.",
                    headers={"X-Requires-Subscription": "true"}
                )
        else: # Document
            from app.models.document import Document
            count = await db.scalar(select(func.count()).select_from(Document).where(Document.user_id == current_user.id))
            if count and count >= settings.FREE_DOCUMENT_LIMIT:
                raise HTTPException(
                    status_code=403, 
                    detail="Free tier limit reached: 5 Documents max. Please upgrade to Pro.",
                    headers={"X-Requires-Subscription": "true"}
                )
    
    return True
