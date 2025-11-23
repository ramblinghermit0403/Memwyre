"""
Quick script to update the database schema
"""
from app.db.session import engine
from app.db.base import Base

# This will create any missing columns
Base.metadata.create_all(bind=engine)

print("Database schema updated successfully!")
