"""
Dodo Payments subscription service.

Wraps the Dodo Payments Python SDK for checkout sessions,
subscription management, and webhook processing.
"""

import hashlib
import hmac
import logging
from datetime import datetime
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.config import settings
from app.models.subscription import Subscription
from app.models.user import User

logger = logging.getLogger(__name__)


def get_dodo_client():
    """Get an async Dodo Payments client."""
    from dodopayments import AsyncDodoPayments

    return AsyncDodoPayments(
        bearer_token=settings.DODO_PAYMENTS_API_KEY,
        environment=settings.DODO_ENVIRONMENT,
    )


async def create_checkout_session(user: User, db: AsyncSession) -> dict:
    """
    Create a Dodo Payments checkout session for the $5/month Pro plan.
    Returns dict with checkout_url and session_id.
    """
    client = get_dodo_client()

    checkout = await client.checkout_sessions.create(
        product_cart=[
            {
                "product_id": settings.DODO_PRODUCT_ID,
                "quantity": 1,
            }
        ],
        customer={
            "email": user.email,
            "name": user.name or user.email.split("@")[0],
        },
        metadata={
            "user_id": str(user.id),
        },
        return_url=f"{settings.FRONTEND_URL}/billing?status=success",
    )

    return {
        "checkout_url": checkout.checkout_url,
        "session_id": checkout.session_id,
    }


async def get_subscription_status(user: User, db: AsyncSession) -> dict:
    """Get the current subscription status for a user."""
    # Dev mode bypass
    if settings.DEV_MODE:
        return {
            "plan": "pro",
            "status": "dev_mode_active",
            "is_active": True,
            "current_period_end": None,
        }

    result = await db.execute(
        select(Subscription).where(Subscription.user_id == user.id)
    )
    sub = result.scalars().first()

    if not sub or sub.status != "active":
        return {
            "plan": "free",
            "status": sub.status if sub else "inactive",
            "is_active": False,
            "current_period_end": sub.current_period_end.isoformat() if sub and sub.current_period_end else None,
        }

    return {
        "plan": sub.plan,
        "status": sub.status,
        "is_active": True,
        "current_period_end": sub.current_period_end.isoformat() if sub.current_period_end else None,
    }


async def is_user_subscribed(user: User, db: AsyncSession) -> bool:
    """Check if user has an active subscription (or dev mode is on)."""
    if settings.DEV_MODE:
        return True

    result = await db.execute(
        select(Subscription).where(Subscription.user_id == user.id)
    )
    sub = result.scalars().first()
    return sub is not None and sub.status == "active"


def verify_webhook_signature(payload: bytes, signature: str) -> bool:
    """Verify the Dodo Payments webhook signature."""
    if not settings.DODO_WEBHOOK_SECRET:
        logger.warning("DODO_WEBHOOK_SECRET not set — skipping signature verification")
        return True

    expected = hmac.new(
        settings.DODO_WEBHOOK_SECRET.encode(),
        payload,
        hashlib.sha256,
    ).hexdigest()

    logger.warning(f"Webhook sig check -> received: {signature}, calculated: {expected}")
    return hmac.compare_digest(expected, signature)


async def handle_webhook_event(event_type: str, data: dict, db: AsyncSession) -> None:
    """
    Process a Dodo Payments webhook event.
    
    Events:
    - subscription.active     → subscription is now active
    - subscription.on_hold    → payment issues, grace period
    - subscription.failed     → payment failed
    - subscription.cancelled  → user cancelled
    - subscription.renewed    → subscription renewed for new period
    """
    dodo_sub_id = data.get("subscription_id") or data.get("id")
    metadata = data.get("metadata", {})
    user_id = metadata.get("user_id")
    customer = data.get("customer", {})
    dodo_customer_id = customer.get("customer_id")

    if not dodo_sub_id:
        logger.error(f"Webhook {event_type}: missing subscription_id in payload")
        return

    # Try to find existing subscription by Dodo ID
    result = await db.execute(
        select(Subscription).where(Subscription.dodo_subscription_id == dodo_sub_id)
    )
    sub = result.scalars().first()

    # If not found, try to find by user_id from metadata
    if not sub and user_id:
        result = await db.execute(
            select(Subscription).where(Subscription.user_id == int(user_id))
        )
        sub = result.scalars().first()

    # Create new subscription record if it doesn't exist
    if not sub:
        if not user_id:
            logger.error(f"Webhook {event_type}: cannot create subscription — no user_id in metadata")
            return
        sub = Subscription(
            user_id=int(user_id),
            dodo_subscription_id=dodo_sub_id,
            dodo_customer_id=dodo_customer_id,
        )
        db.add(sub)

    # Always update the Dodo IDs
    sub.dodo_subscription_id = dodo_sub_id
    if dodo_customer_id:
        sub.dodo_customer_id = dodo_customer_id

    # Map event type to status
    status_map = {
        "subscription.active": "active",
        "subscription.on_hold": "on_hold",
        "subscription.failed": "failed",
        "subscription.cancelled": "cancelled",
        "subscription.renewed": "active",
    }

    new_status = status_map.get(event_type)
    if new_status:
        sub.status = new_status
        sub.plan = "pro" if new_status == "active" else sub.plan

    # Update period dates if available
    if data.get("current_period_start"):
        try:
            sub.current_period_start = datetime.fromisoformat(data["current_period_start"])
        except (ValueError, TypeError):
            pass
    if data.get("current_period_end"):
        try:
            sub.current_period_end = datetime.fromisoformat(data["current_period_end"])
        except (ValueError, TypeError):
            pass

    sub.updated_at = datetime.utcnow()
    await db.commit()

    logger.info(f"Webhook {event_type}: user_id={sub.user_id}, status={sub.status}")


async def cancel_subscription(user: User, db: AsyncSession) -> dict:
    """Cancel a user's subscription at the end of the current billing period."""
    result = await db.execute(
        select(Subscription).where(Subscription.user_id == user.id)
    )
    sub = result.scalars().first()

    if not sub or not sub.dodo_subscription_id:
        return {"error": "No active subscription found"}

    client = get_dodo_client()

    try:
        await client.subscriptions.update(
            sub.dodo_subscription_id,
            status="cancelled",
        )
        sub.status = "cancelled"
        await db.commit()
        return {"status": "cancelled", "message": "Subscription will end at the current billing period"}
    except Exception as e:
        logger.error(f"Failed to cancel subscription: {e}")
        return {"error": str(e)}
