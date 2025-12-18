from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func

from app.core import security
from app.core.config import settings
from app.api import deps
from app.schemas.user import UserCreate, User as UserSchema, UserLogin
from app.models.user import User

router = APIRouter()

@router.post("/register", response_model=UserSchema)
async def register(
    user_in: UserCreate,
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Create new user.
    """
    # Normalize email
    user_in.email = user_in.email.lower()
    
    result = await db.execute(select(User).where(func.lower(User.email) == user_in.email))
    user = result.scalars().first()
    
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    
    hashed_password = security.get_password_hash(user_in.password)
    user = User(
        email=user_in.email,
        name=user_in.name,
        hashed_password=hashed_password,
        is_active=True,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

@router.post("/login")
async def login(
    db: AsyncSession = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    # Normalize input
    email = form_data.username.lower()
    
    # Case-insensitive lookup to handle legacy mixed-case data
    result = await db.execute(select(User).where(func.lower(User.email) == email))
    user = result.scalars().first()
    
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
        
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires, extra_claims={"email": user.email, "name": user.name}
        ),
        "refresh_token": security.create_refresh_token(
            user.id, expires_delta=refresh_token_expires
        ),
        "token_type": "bearer",
    }

@router.get("/verify", response_model=UserSchema)
def verify_token(
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Verify current token validity.
    """
    return current_user

from pydantic import BaseModel

class RefreshTokenRequest(BaseModel):
    refresh_token: str

@router.post("/refresh")
async def refresh_token(
    request: RefreshTokenRequest,
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Refresh access token using refresh token.
    """
    from jose import jwt, JWTError
    from app.core.config import settings
    
    try:
        payload = jwt.decode(request.refresh_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        token_type: str = payload.get("type")
        
        if user_id is None or token_type != "refresh":
            raise HTTPException(status_code=401, detail="Invalid refresh token")
            
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
        
    # Check if user still exists/active
    result = await db.execute(select(User).where(User.id == int(user_id)))
    user = result.scalars().first()
    
    if not user or not user.is_active:
         raise HTTPException(status_code=401, detail="User not found or inactive")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    # We can perform refresh token rotation here if desired, for now just new access token
    
    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires, extra_claims={"email": user.email, "name": user.name}
        ),
        "token_type": "bearer",
        "refresh_token": request.refresh_token # Return same or a new one
    }
