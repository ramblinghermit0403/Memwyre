import os
import httpx
import base64
from datetime import datetime, timedelta
from jose import jwt
from fastapi import APIRouter, Depends, HTTPException, Query, BackgroundTasks
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from app.api import deps
from app.core.config import settings
from app.core.encryption import encryption_service
from app.models.workspace_connection import WorkspaceConnection

router = APIRouter(prefix="/connectors", tags=["connectors"])

def create_state_token(user_id: int, project_id: int) -> str:
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode = {
        "exp": expire,
        "user_id": user_id,
        "project_id": project_id
    }
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def verify_state_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except Exception:
        return None

@router.get("/status")
async def get_connectors_status(
    current_user = Depends(deps.get_current_user),
    db: AsyncSession = Depends(deps.get_db)
):
    stmt = select(WorkspaceConnection).where(WorkspaceConnection.user_id == current_user.id)
    result = await db.execute(stmt)
    connections = result.scalars().all()
    
    status_dict = {
        "notion": {"connected": False, "workspace_name": None, "last_synced_at": None, "workspace_icon": None},
        "gdrive": {"connected": False, "workspace_name": None, "last_synced_at": None, "workspace_icon": None}
    }
    
    for conn in connections:
        if conn.service in status_dict and conn.is_active:
            status_dict[conn.service] = {
                "connected": True,
                "workspace_name": conn.workspace_name,
                "workspace_icon": conn.workspace_icon,
                "last_synced_at": conn.last_synced_at.isoformat() if conn.last_synced_at else None
            }
            
    return status_dict

@router.get("/notion/auth")
async def notion_auth(
    token: str = Query(..., description="User access token"),
    project_id: int = Query(None, description="Optional target project ID"),
    db: AsyncSession = Depends(deps.get_db)
):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = int(payload.get("sub"))
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

    if not project_id:
        project_id = await deps.resolve_project_id(db, user_id)

    state = create_state_token(user_id, project_id)

    notion_client_id = os.environ.get("NOTION_CLIENT_ID") or getattr(settings, "NOTION_CLIENT_ID", None)
    if not notion_client_id:
        raise HTTPException(status_code=400, detail="Notion Client ID not configured on server")

    redirect_uri = f"{settings.BACKEND_URL}{settings.API_V1_STR}/connectors/notion/callback"
    auth_url = (
        f"https://api.notion.com/v1/oauth/authorize"
        f"?client_id={notion_client_id}"
        f"&response_type=code"
        f"&owner=user"
        f"&redirect_uri={redirect_uri}"
        f"&state={state}"
    )
    return RedirectResponse(auth_url)

@router.get("/notion/callback")
async def notion_callback(
    code: str = None,
    state: str = None,
    error: str = None,
    db: AsyncSession = Depends(deps.get_db),
    background_tasks: BackgroundTasks = None
):
    if error:
        return HTMLResponse(
            f"<html><body style='font-family: sans-serif; text-align: center; padding-top: 50px; background: #1a1a1a; color: white;'><h3>Authentication failed: {error}</h3><script>setTimeout(window.close, 3000);</script></body></html>"
        )
    if not code or not state:
        raise HTTPException(status_code=400, detail="Missing code or state")

    payload = verify_state_token(state)
    if not payload:
        raise HTTPException(status_code=400, detail="Invalid state token")

    user_id = payload["user_id"]
    project_id = payload["project_id"]

    notion_client_id = os.environ.get("NOTION_CLIENT_ID") or getattr(settings, "NOTION_CLIENT_ID", None)
    notion_client_secret = os.environ.get("NOTION_CLIENT_SECRET") or getattr(settings, "NOTION_CLIENT_SECRET", None)

    if not notion_client_id or not notion_client_secret:
        raise HTTPException(status_code=500, detail="Notion OAuth credentials not configured")

    token_url = "https://api.notion.com/v1/oauth/token"
    credentials = f"{notion_client_id}:{notion_client_secret}"
    b64_credentials = base64.b64encode(credentials.encode()).decode()
    headers = {
        "Authorization": f"Basic {b64_credentials}",
        "Content-Type": "application/json"
    }
    body = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": f"{settings.BACKEND_URL}{settings.API_V1_STR}/connectors/notion/callback"
    }

    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(token_url, json=body, headers=headers)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            error_detail = resp.text if 'resp' in locals() else str(e)
            return HTMLResponse(
                f"<html><body style='font-family: sans-serif; text-align: center; padding-top: 50px; background: #1a1a1a; color: white;'><h3>Token exchange failed: {error_detail}</h3></body></html>"
            )

    access_token = data.get("access_token")
    workspace_name = data.get("workspace_name")
    workspace_id = data.get("workspace_id")
    workspace_icon = data.get("workspace_icon")

    encrypted_token = encryption_service.encrypt(access_token)

    stmt = select(WorkspaceConnection).where(
        WorkspaceConnection.user_id == user_id,
        WorkspaceConnection.service == "notion"
    )
    result = await db.execute(stmt)
    connection = result.scalars().first()

    if connection:
        connection.access_token = encrypted_token
        connection.workspace_name = workspace_name
        connection.workspace_id = workspace_id
        connection.workspace_icon = workspace_icon
        connection.is_active = True
        connection.updated_at = datetime.utcnow()
    else:
        connection = WorkspaceConnection(
            user_id=user_id,
            service="notion",
            access_token=encrypted_token,
            workspace_name=workspace_name,
            workspace_id=workspace_id,
            workspace_icon=workspace_icon,
            is_active=True
        )
        db.add(connection)

    await db.commit()

    from app.services.notion_service import notion_service
    background_tasks.add_task(notion_service.sync_notion, user_id, project_id, access_token)

    html_content = """
    <html>
      <body style="font-family: sans-serif; text-align: center; padding-top: 50px; background: #1a1a1a; color: white;">
        <h2>Notion connected successfully!</h2>
        <p>Syncing your workspace in the background...</p>
        <script>
          if (window.opener) {
            window.opener.postMessage("notion_connected", "*");
          }
          setTimeout(window.close, 1500);
        </script>
      </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@router.delete("/{service}")
async def disconnect_connector(
    service: str,
    current_user = Depends(deps.get_current_user),
    db: AsyncSession = Depends(deps.get_db)
):
    if service not in ["notion", "gdrive"]:
        raise HTTPException(status_code=400, detail="Invalid service")
        
    stmt = delete(WorkspaceConnection).where(
        WorkspaceConnection.user_id == current_user.id,
        WorkspaceConnection.service == service
    )
    await db.execute(stmt)
    await db.commit()
    return {"status": "success", "message": f"{service.capitalize()} disconnected"}

@router.post("/{service}/sync")
async def sync_connector(
    service: str,
    background_tasks: BackgroundTasks,
    current_user = Depends(deps.get_current_user),
    db: AsyncSession = Depends(deps.get_db)
):
    if service != "notion":
        raise HTTPException(status_code=400, detail="Only Notion sync is supported currently")
        
    stmt = select(WorkspaceConnection).where(
        WorkspaceConnection.user_id == current_user.id,
        WorkspaceConnection.service == "notion",
        WorkspaceConnection.is_active == True
    )
    result = await db.execute(stmt)
    conn = result.scalars().first()
    
    if not conn:
        raise HTTPException(status_code=404, detail="Notion connection not found or inactive")
        
    access_token = encryption_service.decrypt(conn.access_token)
    project_id = await deps.resolve_project_id(db, current_user.id)
    
    from app.services.notion_service import notion_service
    background_tasks.add_task(notion_service.sync_notion, current_user.id, project_id, access_token)
    
    return {"status": "success", "message": "Sync started in background"}
