from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.db.base import Base

class ApiKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False) # e.g. "Laptop", "Claude"
    key_hash = Column(String, unique=True, index=True, nullable=False)
    prefix = Column(String, nullable=False) # Store first few chars for display (e.g. "bv_sk_a1b2...")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_used_at = Column(DateTime(timezone=True), nullable=True)
    is_active = Column(Boolean, default=True)

    user = relationship("app.models.user.User", back_populates="api_keys")
