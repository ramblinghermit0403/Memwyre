from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.sql import func
from app.db.base import Base

class WorkspaceConnection(Base):
    __tablename__ = "workspace_connections"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    service = Column(String, nullable=False)  # "notion", "gdrive", etc.
    access_token = Column(String, nullable=False)  # double-encrypted access token
    refresh_token = Column(String, nullable=True)  # double-encrypted refresh token (if applicable)
    token_expires_at = Column(DateTime(timezone=True), nullable=True)
    workspace_id = Column(String, nullable=True)
    workspace_name = Column(String, nullable=True)
    workspace_icon = Column(String, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    last_synced_at = Column(DateTime(timezone=True), nullable=True)
