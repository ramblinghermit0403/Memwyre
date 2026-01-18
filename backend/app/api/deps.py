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
