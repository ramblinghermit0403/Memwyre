import logging
import secrets
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.config import settings
from app.models.user import User
from app.models.subscription import Subscription
from app.models.invite import InviteToken

logger = logging.getLogger(__name__)

async def apply_direct_bypass(user: User, db: AsyncSession) -> bool:
    """
    Directly force a user into an active 'pro' subscription,
    bypassing the Dodo Payments requirement.
    """
    result = await db.execute(
        select(Subscription).where(Subscription.user_id == user.id)
    )
    sub = result.scalars().first()

    if not sub:
        # Create a mock active subscription
        sub = Subscription(
            user_id=user.id,
            dodo_subscription_id=f"sub_bypass_{user.id}_{secrets.token_hex(4)}",
            dodo_customer_id=f"cus_bypass_{user.id}",
            status="active",
            plan="pro"
        )
        db.add(sub)
    else:
        # Update existing
        sub.status = "active"
        sub.plan = "pro"
        sub.updated_at = datetime.utcnow()

    await db.commit()
    return True

async def check_and_apply_domain_whitelist(user: User, db: AsyncSession) -> bool:
    """
    Checks if a user's email matches the WHITELISTED_DOMAINS.
    If it does, automatically bumps their account to Pro.
    Returns True if bypassed.
    """
    if not settings.whitelisted_domain_list:
        return False

    domain = user.email.split("@")[-1].lower()
    if domain in settings.whitelisted_domain_list:
        logger.info(f"Auto-bypassing payment for {user.email} (Whitelisted Domain: {domain})")
        return await apply_direct_bypass(user, db)
    
    return False

async def create_invite_token(admin_user: User, db: AsyncSession, target_email: str = None) -> InviteToken:
    """
    Generate a new secure invite token.
    """
    # Verify admin permission just in case
    if admin_user.email.lower() not in settings.admin_email_list:
        raise ValueError("User is not authorized to generate invite tokens.")

    token_str = secrets.token_urlsafe(32)
    invite = InviteToken(
        token=token_str,
        created_by_id=admin_user.id,
        target_email=target_email.lower() if target_email else None
    )
    db.add(invite)
    await db.commit()
    await db.refresh(invite)
    return invite

async def redeem_invite_token(token_str: str, user: User, db: AsyncSession) -> bool:
    """
    Validate and redeem an invite token to grant Pro access.
    """
    result = await db.execute(
        select(InviteToken).where(InviteToken.token == token_str)
    )
    invite = result.scalars().first()

    if not invite:
        raise ValueError("Invalid or expired invite token.")

    if invite.is_used:
        raise ValueError("This invite token has already been used.")

    if invite.target_email and invite.target_email.lower() != user.email.lower():
        raise ValueError("This invite token is bound to a different email address.")

    # Mark as used and apply bypass
    invite.is_used = True
    db.add(invite)
    
    logger.info(f"User {user.email} successfully redeemed invite token {invite.id}")
    await apply_direct_bypass(user, db)
    
    return True
