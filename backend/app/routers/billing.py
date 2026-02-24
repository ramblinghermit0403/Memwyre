"""
Billing router — Dodo Payments checkout, webhook, and subscription status.
"""

import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import deps
from app.models.user import User
from app.services.subscription import (
    create_checkout_session,
    get_subscription_status,
    cancel_subscription,
    handle_webhook_event,
    verify_webhook_signature,
)

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/checkout")
async def create_checkout(
    current_user: User = Depends(deps.get_current_user),
    db: AsyncSession = Depends(deps.get_db),
) -> Any:
    """
    Create a Dodo Payments checkout session for the Pro plan.
    Returns a checkout_url to redirect the user to.
    """
    from app.core.config import settings

    if not settings.DODO_PAYMENTS_API_KEY or not settings.DODO_PRODUCT_ID:
        raise HTTPException(
            status_code=503,
            detail="Payment system not configured",
        )

    try:
        result = await create_checkout_session(current_user, db)
        return result
    except Exception as e:
        logger.error(f"Checkout creation failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to create checkout session")


@router.get("/status")
async def subscription_status(
    current_user: User = Depends(deps.get_current_user),
    db: AsyncSession = Depends(deps.get_db),
) -> Any:
    """Get the current user's subscription status."""
    return await get_subscription_status(current_user, db)


@router.post("/cancel")
async def cancel_sub(
    current_user: User = Depends(deps.get_current_user),
    db: AsyncSession = Depends(deps.get_db),
) -> Any:
    """Cancel the current user's subscription at end of period."""
    result = await cancel_subscription(current_user, db)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


@router.post("/webhook")
async def dodo_webhook(request: Request) -> Any:
    """
    Receive and process Dodo Payments webhook events.
    This endpoint is NOT authenticated via JWT — it uses Dodo's webhook signature.
    """
    from app.db.session import AsyncSessionLocal
    from app.services.subscription import get_dodo_client
    from app.core.config import settings
    import json

    body = await request.body()
    headers = dict(request.headers)

    client = get_dodo_client()
    
    # Let the SDK handle the verification, it supports headers parsing out-of-the-box
    try:
        if settings.DODO_WEBHOOK_SECRET:
            event = client.webhooks.unwrap(
                payload=body.decode("utf-8"), 
                headers=headers,
                key=settings.DODO_WEBHOOK_SECRET
            )
            # The SDK returns a typed model, let's dump it back to a generic dict to feed our handler 
            payload = event.model_dump() if hasattr(event, "model_dump") else event.dict()
        else:
            logger.warning("DODO_WEBHOOK_SECRET not set — skipping signature verification (Development only)")
            payload = json.loads(body)
    except Exception as e:
        logger.error(f"Webhook verification failed: {e}")
        raise HTTPException(status_code=401, detail="Invalid webhook signature")

    event_type = payload.get("data", {}).get("event_type") or payload.get("data", {}).get("type") or payload.get("type", payload.get("event_type"))
    data = payload.get("data", payload)

    if not event_type:
        logger.error(f"Missing event type in payload: {payload.keys()}")
        raise HTTPException(status_code=400, detail="Missing event type")

    logger.info(f"Dodo webhook received: {event_type}")

    # Process in a fresh DB session (webhook has no user auth context)
    async with AsyncSessionLocal() as db:
        try:
            await handle_webhook_event(event_type, data, db)
        except Exception as e:
            logger.error(f"Webhook processing error: {e}")
            raise HTTPException(status_code=500, detail="Webhook processing failed")

    return {"status": "ok"}
