from typing import Optional
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import func
from datetime import datetime, timedelta
from app.models.usage import UserUsage
from app.db.session import AsyncSessionLocal
from app.core.config import settings

# Simple cost estimation (approximate per 1M tokens)
# These are rough averages as of 2024
COST_RATES = {
    "openai": {"in": 0.50, "out": 1.50}, # gpt-3.5
    "gemini": {"in": 0.10, "out": 0.30}, 
    "bedrock": {"in": 0.80, "out": 2.40},
}

from app.services.token_tracker import token_tracker

class UsageService:
    async def track_usage(
        self, 
        user_id: int, 
        provider: str, 
        model_name: Optional[str], 
        tokens_in: int, 
        tokens_out: int,
        resource_type: Optional[str] = None,
        resource_id: Optional[int] = None
    ):
        """
        Log granular usage to DB with model & resource context.
        """
        async with AsyncSessionLocal() as db:
            cost = token_tracker.calculate_cost(
                tokens_in=tokens_in,
                tokens_out=tokens_out,
                provider=provider,
                model_name=model_name or "gpt-4o"
            )
            
            usage = UserUsage(
                user_id=user_id,
                provider=provider,
                model_name=model_name,
                resource_type=resource_type,
                resource_id=resource_id,
                tokens_in=tokens_in,
                tokens_out=tokens_out,
                estimated_cost=cost
            )
            db.add(usage)
            await db.commit()
            return usage

    async def check_budget(self, user_id: int) -> bool:
        """
        Check if user has exceeded daily budget.
        Returns True if SAFE, False if EXCEEDED.
        """
        # Hardcoded daily limit for MVP: 100,000 tokens or $1.00
        MAX_DAILY_TOKENS = getattr(settings, "MAX_DAILY_TOKENS", 100_000)
        
        async with AsyncSessionLocal() as db:
            # Check usage in last 24h
            since = datetime.now() - timedelta(days=1)
            
            result = await db.execute(
                select(
                    func.sum(UserUsage.tokens_in) + func.sum(UserUsage.tokens_out)
                ).where(
                    UserUsage.user_id == user_id,
                    UserUsage.timestamp >= since
                )
            )
            total_tokens = result.scalar() or 0
            
            if total_tokens > MAX_DAILY_TOKENS:
                return False
                
            return True

usage_service = UsageService()
