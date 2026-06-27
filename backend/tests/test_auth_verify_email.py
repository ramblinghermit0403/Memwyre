import sys
from pathlib import Path
from datetime import datetime, timedelta, timezone

import pytest
from fastapi import HTTPException

backend_path = str(Path(__file__).parent.parent)
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

from app.models.token import VerificationToken
from app.models.user import User
from app.routers.auth import VerifyEmailRequest, verify_email_endpoint


class _ScalarResult:
    def __init__(self, obj):
        self._obj = obj

    def first(self):
        return self._obj


class _ExecuteResult:
    def __init__(self, obj):
        self._obj = obj

    def scalars(self):
        return _ScalarResult(self._obj)


class FakeAsyncSession:
    def __init__(self, execute_results):
        self._execute_results = list(execute_results)
        self.added = []
        self.deleted = []
        self.committed = False

    async def execute(self, _):
        if not self._execute_results:
            raise AssertionError("Unexpected execute() call in test")
        return _ExecuteResult(self._execute_results.pop(0))

    def add(self, obj):
        self.added.append(obj)

    async def delete(self, obj):
        self.deleted.append(obj)

    async def commit(self):
        self.committed = True


class FakeBackgroundTasks:
    def add_task(self, func, *args, **kwargs):
        pass


@pytest.mark.asyncio
async def test_verify_email_success_returns_metadata_only():
    user = User(id=123, email="user@example.com", hashed_password="x", is_verified=False)
    token = VerificationToken(
        token="token-123",
        user_id=123,
        token_type="email_verify",
        expires_at=datetime.now(timezone.utc) + timedelta(hours=1),
    )
    db = FakeAsyncSession([token, user])

    response = await verify_email_endpoint(
        VerifyEmailRequest(token="token-123"),
        background_tasks=FakeBackgroundTasks(),
        db=db
    )

    assert response["message"] == "Email verified successfully."
    assert "verified_at" in response
    assert "access_token" not in response
    assert "refresh_token" not in response
    assert user.is_verified is True
    assert db.deleted == [token]
    assert db.committed is True


@pytest.mark.asyncio
async def test_verify_email_invalid_token_raises_400():
    db = FakeAsyncSession([None])

    with pytest.raises(HTTPException) as exc:
        await verify_email_endpoint(
            VerifyEmailRequest(token="missing"),
            background_tasks=FakeBackgroundTasks(),
            db=db
        )

    assert exc.value.status_code == 400
    assert exc.value.detail == "Invalid or expired token"


@pytest.mark.asyncio
async def test_verify_email_expired_token_raises_400():
    user = User(id=99, email="user@example.com", hashed_password="x", is_verified=False)
    expired = VerificationToken(
        token="expired-token",
        user_id=99,
        token_type="email_verify",
        expires_at=datetime.now(timezone.utc) - timedelta(minutes=1),
    )
    db = FakeAsyncSession([expired, user])

    with pytest.raises(HTTPException) as exc:
        await verify_email_endpoint(
            VerifyEmailRequest(token="expired-token"),
            background_tasks=FakeBackgroundTasks(),
            db=db
        )

    assert exc.value.status_code == 400
    assert exc.value.detail == "Token has expired"
