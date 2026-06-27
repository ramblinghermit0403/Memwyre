from datetime import timedelta, datetime, timezone
from typing import Any
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from sqlalchemy.orm import selectinload
from pydantic import BaseModel
from urllib.parse import urlencode
import httpx
import secrets

from app.core import security
from app.core.config import settings
from app.api import deps
from app.schemas.user import UserCreate, User as UserSchema, UserLogin
from app.models.user import User
from app.models.token import VerificationToken
from app.services.bypass import check_and_apply_domain_whitelist
from app.services.email import send_verification_email, send_password_reset_email, send_otp_email, send_welcome_email


async def verify_turnstile(token: str) -> bool:
    if settings.DEV_MODE:
        return True
    if not settings.TURNSTILE_SECRET_KEY:
        return True
    if not token:
        return False

    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://challenges.cloudflare.com/turnstile/v0/siteverify",
            data={
                "secret": settings.TURNSTILE_SECRET_KEY,
                "response": token
            }
        )
        data = res.json()
        return data.get("success", False)


router = APIRouter()


class RegisterResponse(BaseModel):
    message: str
    email: str
    is_verified: bool


@router.post("/register", response_model=RegisterResponse)
async def register(
    user_in: UserCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Create new user. Sends a 6-digit OTP to verify their email.
    """
    # Normalize email
    user_in.email = user_in.email.lower()

    result = await db.execute(select(User).where(func.lower(User.email) == user_in.email))
    user = result.scalars().first()

    if not await verify_turnstile(user_in.turnstile_token):
        raise HTTPException(status_code=400, detail="Invalid Turnstile token (Bot protection)")

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

    # Create default workspace project for new user
    await deps.resolve_project_id(db, user.id)

    # Auto-upgrade if domain is whitelisted
    bypassed = await check_and_apply_domain_whitelist(user, db)

    if bypassed:
        user.is_verified = True
        db.add(user)
        await db.commit()
        background_tasks.add_task(send_welcome_email, user.email, user.name)
        return {"message": "Account created and verified.", "email": user.email, "is_verified": True}

    # Generate 6-digit OTP and send via email
    import random
    otp = str(random.randint(100000, 999999))

    # Delete any existing OTPs for this user
    await db.execute(
        VerificationToken.__table__.delete().where(
            VerificationToken.user_id == user.id,
            VerificationToken.token_type == "email_otp"
        )
    )
    v_token = VerificationToken(
        token=otp,
        user_id=user.id,
        token_type="email_otp",
        expires_at=datetime.now(timezone.utc) + timedelta(minutes=10)
    )
    db.add(v_token)
    await db.commit()

    background_tasks.add_task(send_otp_email, user.email, otp)

    return {"message": "OTP sent to your email. Please verify to continue.", "email": user.email, "is_verified": False}


@router.post("/login")
async def login(
    request: Request,
    db: AsyncSession = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    form = await request.form()
    turnstile_token = form.get("turnstile_token")

    if not await verify_turnstile(turnstile_token):
        raise HTTPException(status_code=400, detail="Invalid Turnstile token (Bot protection)")
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
            user.id, expires_delta=access_token_expires, extra_claims={"email": user.email, "name": user.name, "is_verified": user.is_verified}
        ),
        "refresh_token": security.create_refresh_token(
            user.id, expires_delta=refresh_token_expires
        ),
        "token_type": "bearer",
    }


@router.get("/verify", response_model=UserSchema)
def verify_token(
    current_user: User = Depends(deps.get_current_authenticated_user)
) -> Any:
    """
    Verify current token validity.
    """
    return current_user


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

    return {
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires, extra_claims={"email": user.email, "name": user.name, "is_verified": user.is_verified}
        ),
        "token_type": "bearer",
        "refresh_token": request.refresh_token  # Return same or a new one
    }


@router.get("/oauth/{provider}/login")
async def oauth_login(provider: str):
    if provider == "google":
        params = {
            "client_id": settings.GOOGLE_CLIENT_ID,
            "redirect_uri": f"{settings.BACKEND_URL}{settings.API_V1_STR}/auth/oauth/google/callback",
            "response_type": "code",
            "scope": "openid email profile",
            "access_type": "offline",
            "prompt": "consent"
        }
        url = f"https://accounts.google.com/o/oauth2/v2/auth?{urlencode(params)}"
        return RedirectResponse(url)
    elif provider == "github":
        params = {
            "client_id": settings.GITHUB_CLIENT_ID,
            "redirect_uri": f"{settings.BACKEND_URL}{settings.API_V1_STR}/auth/oauth/github/callback",
            "scope": "user:email"
        }
        url = f"https://github.com/login/oauth/authorize?{urlencode(params)}"
        return RedirectResponse(url)
    else:
        raise HTTPException(status_code=400, detail="Unsupported provider")


@router.get("/oauth/{provider}/callback")
async def oauth_callback(
    provider: str,
    code: str,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(deps.get_db)
):
    try:
        user_email = None
        user_name = None

        async with httpx.AsyncClient() as client:
            if provider == "google":
                token_url = "https://oauth2.googleapis.com/token"
                data = {
                    "client_id": settings.GOOGLE_CLIENT_ID,
                    "client_secret": settings.GOOGLE_CLIENT_SECRET,
                    "code": code,
                    "grant_type": "authorization_code",
                    "redirect_uri": f"{settings.BACKEND_URL}{settings.API_V1_STR}/auth/oauth/google/callback",
                }
                response = await client.post(token_url, data=data)
                response.raise_for_status()
                access_token = response.json()["access_token"]

                user_info_resp = await client.get(
                    "https://www.googleapis.com/oauth2/v1/userinfo",
                    headers={"Authorization": f"Bearer {access_token}"}
                )
                user_info = user_info_resp.json()
                user_email = user_info.get("email")
                user_name = user_info.get("name")

            elif provider == "github":
                token_url = "https://github.com/login/oauth/access_token"
                headers = {"Accept": "application/json"}
                data = {
                    "client_id": settings.GITHUB_CLIENT_ID,
                    "client_secret": settings.GITHUB_CLIENT_SECRET,
                    "code": code,
                    "redirect_uri": f"{settings.BACKEND_URL}{settings.API_V1_STR}/auth/oauth/github/callback",
                }
                response = await client.post(token_url, data=data, headers=headers)
                response.raise_for_status()
                access_token = response.json().get("access_token")

                user_resp = await client.get(
                    "https://api.github.com/user",
                    headers={"Authorization": f"Bearer {access_token}"}
                )
                user_data = user_resp.json()
                user_name = user_data.get("name") or user_data.get("login")

                emails_resp = await client.get(
                    "https://api.github.com/user/emails",
                    headers={"Authorization": f"Bearer {access_token}"}
                )
                emails = emails_resp.json()
                primary_email = next((e for e in emails if e.get("primary")), None)
                if primary_email:
                    user_email = primary_email["email"]
                else:
                    user_email = emails[0]["email"] if emails else None

        if not user_email:
            raise HTTPException(status_code=400, detail="Could not retrieve email from provider")

        result = await db.execute(select(User).where(func.lower(User.email) == user_email.lower()))
        user = result.scalars().first()

        if not user:
            random_password = secrets.token_urlsafe(16)
            hashed_passwd = security.get_password_hash(random_password)
            user = User(
                email=user_email,
                name=user_name,
                hashed_password=hashed_passwd,
                is_active=True,
                is_verified=True  # OAuth providers verify email; skip OTP
            )
            db.add(user)
            await db.commit()
            await db.refresh(user)

            # Create default workspace project for new user
            await deps.resolve_project_id(db, user.id)

            await check_and_apply_domain_whitelist(user, db)
            background_tasks.add_task(send_welcome_email, user.email, user.name)
        else:
            # Existing user signing in via OAuth — auto-verify if not already
            if not user.is_verified:
                user.is_verified = True
                db.add(user)
                await db.commit()

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token_expires = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

        access_token = security.create_access_token(
            user.id, expires_delta=access_token_expires, extra_claims={"email": user.email, "name": user.name, "is_verified": user.is_verified}
        )
        refresh_token = security.create_refresh_token(
            user.id, expires_delta=refresh_token_expires
        )

        redirect_url = f"{settings.FRONTEND_URL}/login?access_token={access_token}&refresh_token={refresh_token}"
        return RedirectResponse(redirect_url)

    except Exception as e:
        return RedirectResponse(f"{settings.FRONTEND_URL}/login?error=OAuth_Failed")


class GoogleOneTapRequest(BaseModel):
    credential: str


@router.post("/google-one-tap")
async def google_one_tap_login(
    request: GoogleOneTapRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(deps.get_db)
) -> Any:
    """
    Login using Google One Tap credential (ID Token)
    """
    try:
        from google.oauth2 import id_token
        from google.auth.transport import requests as google_requests

        id_info = id_token.verify_oauth2_token(
            request.credential,
            google_requests.Request(),
            settings.GOOGLE_CLIENT_ID
        )

        email = id_info['email']
        name = id_info.get('name', email.split('@')[0])

        if not id_info.get('email_verified'):
            raise HTTPException(status_code=400, detail="Google email not verified")

        result = await db.execute(select(User).where(func.lower(User.email) == email.lower()))
        user = result.scalars().first()

        if not user:
            random_password = secrets.token_urlsafe(16)
            hashed_passwd = security.get_password_hash(random_password)
            user = User(
                email=email,
                name=name,
                hashed_password=hashed_passwd,
                is_active=True,
                is_verified=True  # Google One Tap confirms email_verified
            )
            db.add(user)
            await db.commit()
            await db.refresh(user)

            # Create default workspace project for new user
            await deps.resolve_project_id(db, user.id)

            await check_and_apply_domain_whitelist(user, db)
            background_tasks.add_task(send_welcome_email, user.email, user.name)
        else:
            # Existing user — auto-verify if not already
            if not user.is_verified:
                user.is_verified = True
                db.add(user)
                await db.commit()

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token_expires = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

        return {
            "access_token": security.create_access_token(
                user.id, expires_delta=access_token_expires, extra_claims={"email": user.email, "name": user.name, "is_verified": user.is_verified}
            ),
            "refresh_token": security.create_refresh_token(
                user.id, expires_delta=refresh_token_expires
            ),
            "token_type": "bearer",
        }

    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid Google Token")
    except Exception as e:
        print(f"Google One Tap Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))


class VerifyEmailRequest(BaseModel):
    token: str


class VerifyEmailResponse(BaseModel):
    message: str
    verified_at: datetime | None = None


@router.post("/verify-email", response_model=VerifyEmailResponse)
async def verify_email_endpoint(
    request: VerifyEmailRequest, 
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(deps.get_db)
):
    result = await db.execute(
        select(VerificationToken).where(
            VerificationToken.token == request.token,
            VerificationToken.token_type == "email_verify"
        )
    )
    v_token = result.scalars().first()

    if not v_token:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    result = await db.execute(select(User).where(User.id == v_token.user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    if v_token.expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=400, detail="Token has expired")

    verified_at = datetime.now(timezone.utc)
    user.is_verified = True
    db.add(user)
    await db.delete(v_token)
    await db.commit()

    background_tasks.add_task(send_welcome_email, user.email, user.name)

    return {
        "message": "Email verified successfully.",
        "verified_at": verified_at,
    }


class VerifyOTPRequest(BaseModel):
    email: str
    otp: str


@router.post("/verify-otp")
async def verify_otp_endpoint(
    request: VerifyOTPRequest, 
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(deps.get_db)
):
    """
    Verify the 6-digit OTP sent after registration.
    On success, marks the user as verified and returns JWT tokens for immediate login.
    """
    email = request.email.lower()
    result = await db.execute(select(User).where(func.lower(User.email) == email))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=400, detail="No account found for this email.")

    result = await db.execute(
        select(VerificationToken).where(
            VerificationToken.user_id == user.id,
            VerificationToken.token_type == "email_otp"
        )
    )
    v_token = result.scalars().first()

    if not v_token:
        raise HTTPException(status_code=400, detail="No OTP found. Please request a new one.")

    if v_token.expires_at < datetime.now(timezone.utc):
        await db.delete(v_token)
        await db.commit()
        raise HTTPException(status_code=400, detail="OTP has expired. Please request a new one.")

    if v_token.token != request.otp:
        raise HTTPException(status_code=400, detail="Incorrect OTP. Please try again.")

    # Mark user as verified
    user.is_verified = True
    db.add(user)
    await db.delete(v_token)
    await db.commit()

    background_tasks.add_task(send_welcome_email, user.email, user.name)

    # Return JWT tokens so user is immediately logged in
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

    return {
        "message": "Email verified successfully.",
        "access_token": security.create_access_token(
            user.id, expires_delta=access_token_expires,
            extra_claims={"email": user.email, "name": user.name, "is_verified": True}
        ),
        "refresh_token": security.create_refresh_token(
            user.id, expires_delta=refresh_token_expires
        ),
        "token_type": "bearer",
    }


class ResendOTPRequest(BaseModel):
    email: str


@router.post("/resend-otp")
async def resend_otp(
    request: ResendOTPRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(deps.get_db)
):
    """
    Resend a new 6-digit OTP to the given email (for unverified accounts).
    """
    email = request.email.lower()
    result = await db.execute(select(User).where(func.lower(User.email) == email))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=400, detail="No account found for this email.")

    if user.is_verified:
        raise HTTPException(status_code=400, detail="Email is already verified.")

    import random
    otp = str(random.randint(100000, 999999))

    await db.execute(
        VerificationToken.__table__.delete().where(
            VerificationToken.user_id == user.id,
            VerificationToken.token_type == "email_otp"
        )
    )
    v_token = VerificationToken(
        token=otp,
        user_id=user.id,
        token_type="email_otp",
        expires_at=datetime.now(timezone.utc) + timedelta(minutes=10)
    )
    db.add(v_token)
    await db.commit()

    background_tasks.add_task(send_otp_email, user.email, otp)

    return {"message": "A new OTP has been sent to your email."}


@router.post("/resend-verification")
async def resend_verification(
    background_tasks: BackgroundTasks,
    current_user: User = Depends(deps.get_current_authenticated_user),
    db: AsyncSession = Depends(deps.get_db)
):
    if current_user.is_verified:
        raise HTTPException(status_code=400, detail="Email is already verified")

    await db.execute(
        VerificationToken.__table__.delete().where(
            VerificationToken.user_id == current_user.id,
            VerificationToken.token_type == "email_verify"
        )
    )

    token_str = secrets.token_urlsafe(32)
    v_token = VerificationToken(
        token=token_str,
        user_id=current_user.id,
        token_type="email_verify",
        expires_at=datetime.now(timezone.utc) + timedelta(hours=24)
    )
    db.add(v_token)
    await db.commit()

    verify_url = f"{settings.FRONTEND_URL}/verify-email?token={token_str}"
    background_tasks.add_task(send_verification_email, current_user.email, verify_url)

    return {"message": "Verification email resent successfully."}


class ForgotPasswordRequest(BaseModel):
    email: str
    turnstile_token: str | None = None


@router.post("/forgot-password")
async def forgot_password_endpoint(
    request: ForgotPasswordRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(deps.get_db)
):
    if not await verify_turnstile(request.turnstile_token):
        raise HTTPException(status_code=400, detail="Invalid Turnstile token (Bot protection)")

    result = await db.execute(select(User).where(func.lower(User.email) == request.email.lower()))
    user = result.scalars().first()

    if not user:
        return {"message": "If an account exists, a reset link has been sent."}

    token_str = secrets.token_urlsafe(32)
    v_token = VerificationToken(
        token=token_str,
        user_id=user.id,
        token_type="password_reset",
        expires_at=datetime.now(timezone.utc) + timedelta(hours=1)
    )
    db.add(v_token)
    await db.commit()

    reset_url = f"{settings.FRONTEND_URL}/reset-password?token={token_str}"
    background_tasks.add_task(send_password_reset_email, user.email, reset_url)

    return {"message": "If an account exists, a reset link has been sent."}


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str


@router.post("/reset-password")
async def reset_password_endpoint(request: ResetPasswordRequest, db: AsyncSession = Depends(deps.get_db)):
    result = await db.execute(
        select(VerificationToken).where(
            VerificationToken.token == request.token,
            VerificationToken.token_type == "password_reset"
        )
    )
    v_token = result.scalars().first()

    if not v_token:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    if v_token.expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=400, detail="Token has expired")

    result = await db.execute(select(User).where(User.id == v_token.user_id))
    user = result.scalars().first()

    user.hashed_password = security.get_password_hash(request.new_password)
    db.add(user)
    await db.delete(v_token)
    await db.commit()

    return {"message": "Password has been reset successfully. You can now log in."}
