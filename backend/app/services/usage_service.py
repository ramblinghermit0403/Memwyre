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

class UsageService:
    async def track_usage(
        self, 
        user_id: int, 
        provider: str, 
        model_name: Optional[str], 
        tokens_in: int, 
        tokens_out: int
    ):
        """
        Log usage to DB.
        """
        async with AsyncSessionLocal() as db:
            cost = 0.0
            rates = COST_RATES.get(provider, {"in": 0, "out": 0})
            
            cost += (tokens_in / 1_000_000) * rates["in"]
            cost += (tokens_out / 1_000_000) * rates["out"]
            
            usage = UserUsage(
                user_id=user_id,
                provider=provider,
                model_name=model_name,
                tokens_in=tokens_in,
                tokens_out=tokens_out,
                estimated_cost=cost
            )
            db.add(usage)
            await db.commit()

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
