from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, index=True, nullable=False)

    # Dodo Payments identifiers
    dodo_subscription_id = Column(String, unique=True, index=True, nullable=True)
    dodo_customer_id = Column(String, nullable=True)

    # Subscription state (source of truth: Dodo webhooks)
    status = Column(String, default="inactive")  # active | on_hold | cancelled | failed | inactive
    plan = Column(String, default="free")         # free | pro

    # Billing period
    current_period_start = Column(DateTime(timezone=True), nullable=True)
    current_period_end = Column(DateTime(timezone=True), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User", back_populates="subscription")
