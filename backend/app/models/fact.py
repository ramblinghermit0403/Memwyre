from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Fact(Base):
    """
    Atomic Fact Model (Subject-Predicate-Object).
    Represents a specific, atomic unit of knowledge extracted from text.
    Implements Proposition Point 4 (Time) and Point 5 (State).
    """
    __tablename__ = "facts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # The Atomic Triple
    subject = Column(String, index=True, nullable=False)   # e.g. "User"
    predicate = Column(String, index=True, nullable=False) # e.g. "likes"
    object = Column(String, index=True, nullable=False)    # e.g. "Python"
    
    # Metadata
    confidence = Column(Float, default=1.0)
    source_memory_id = Column(Integer, ForeignKey("memories.id"), nullable=True)
    source_chunk_id = Column(Integer, ForeignKey("chunks.id"), nullable=True)
    
    # Temporal Validity (Proposition Point 4)
    # When did this become true? (Defaults to ingestion time, or extracted time)
    valid_from = Column(DateTime(timezone=True), server_default=func.now())
    
    # When did this stop being true? (Null = Currently True)
    valid_until = Column(DateTime(timezone=True), nullable=True)
    
    # Location Metadata (Proposition: Spatial Context)
    location = Column(String, nullable=True)
    
    # Has this been explicitly superseded by a newer fact?
    is_superseded = Column(Boolean, default=False)
    
    # Audit
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", backref="facts")
    memory = relationship("Memory", backref="facts")
    chunk = relationship("Chunk", backref="facts")
