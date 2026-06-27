from sqlalchemy import Column, Integer, String, JSON, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base import Base

class EntityProfile(Base):
    __tablename__ = "entity_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=True, index=True)
    entity_name = Column(String, index=True)

    project = relationship("Project", backref="entity_profiles")
    profile_data = Column(JSON, default=dict)
    last_updated = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
