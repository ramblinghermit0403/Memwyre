import logging
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from app.api import deps
from app.core.config import settings
from app.models.user import User
from app.services.bypass import create_invite_token, apply_direct_bypass
from sqlalchemy.future import select

logger = logging.getLogger(__name__)
router = APIRouter()

def get_admin_user(current_user: User = Depends(deps.get_current_authenticated_user)) -> User:
    """Dependency to check if current user is an admin."""
    if current_user.email.lower() not in settings.admin_email_list:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Requires administrator privileges.",
        )
    return current_user

class InviteRequest(BaseModel):
    target_email: str | None = None

@router.post("/invite")
async def generate_invite(
    request: InviteRequest,
    admin_user: User = Depends(get_admin_user),
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Generate a payment bypass invite token.
    """
    try:
        invite = await create_invite_token(admin_user, db, request.target_email)
        return {"token": invite.token, "target_email": invite.target_email}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

class DirectBypassRequest(BaseModel):
    email: str

@router.post("/apply")
async def apply_direct_bypass_endpoint(
    request: DirectBypassRequest,
    admin_user: User = Depends(get_admin_user),
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Directly apply payment bypass to an existing user by email.
    """
    result = await db.execute(select(User).where(User.email == request.email.lower()))
    target_user = result.scalars().first()
    
    if not target_user:
        raise HTTPException(status_code=404, detail="User not found")
        
    await apply_direct_bypass(target_user, db)
    return {"message": f"Successfully upgraded {target_user.email} to Pro."}
