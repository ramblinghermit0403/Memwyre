import logging
from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from app.api import deps
from app.models.user import User
from app.services.bypass import redeem_invite_token

logger = logging.getLogger(__name__)
router = APIRouter()

class RedeemRequest(BaseModel):
    token: str

@router.post("/redeem")
async def redeem_invite(
    request: RedeemRequest,
    current_user: User = Depends(deps.get_current_authenticated_user),
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Redeem an invite token to grant Pro subscription.
    """
    try:
        await redeem_invite_token(request.token, current_user, db)
        return {"message": "Token redeemed successfully. Subscription upgraded to Pro."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
