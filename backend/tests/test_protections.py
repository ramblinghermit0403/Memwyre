import pytest
import sys
import os
from pathlib import Path

# Add backend directory to sys.path
backend_path = str(Path(__file__).parent.parent)
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

from httpx import AsyncClient, ASGITransport
from app.main import app
from app.core.config import settings

# Mock User and Dependency Override
from app.api import deps
from app.models.user import User

async def override_get_current_user():
    return User(id=1, email="test@example.com", is_active=True, drop_token="test_token")

app.dependency_overrides[deps.get_current_user] = override_get_current_user

# Mock Rate Limiter (Since Redis might not be available in test env)
from app.core.rate_limiter import limiter
limiter.enabled = False 

@pytest.mark.asyncio
async def test_guardrails_input_too_long():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        long_text = "a" * 10001
        response = await ac.post(
            f"{settings.API_V1_STR}/llm/chat",
            json={"query": long_text, "provider": "openai", "api_key": "sk-fake"}
        )
        if response.status_code != 400:
             with open("debug_test_fail.txt", "w") as f:
                 f.write(f"Status: {response.status_code}\nBody: {response.text}")
        assert response.status_code == 400
        assert "too long" in response.json()["detail"]

@pytest.mark.asyncio
async def test_budget_check_rejection():
    # Mock UsageService to return False (Budget Exceeded)
    from app.services.usage_service import usage_service
    
    # Store original method
    original_check = usage_service.check_budget
    
    # Mock
    async def mock_check_budget(user_id):
        return False
        
    usage_service.check_budget = mock_check_budget
    
    try:
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.post(
                f"{settings.API_V1_STR}/llm/chat",
                json={"query": "test", "provider": "openai", "api_key": "sk-fake"}
            )
            if response.status_code != 429:
                 with open("debug_test_fail_budget.txt", "w") as f:
                     f.write(f"Status: {response.status_code}\nBody: {response.text}")
            assert response.status_code == 429
            assert "budget exceeded" in response.json()["detail"]
    finally:
        # Restore
        usage_service.check_budget = original_check

