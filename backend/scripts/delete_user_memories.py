import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.db.base import SessionLocal
from app.models.user import User
from app.models.memory import Memory

def delete_user_memories(email: str):
    """Delete all memories for a user by email"""
    db = SessionLocal()
    
    try:
        # Find the user
        user = db.query(User).filter(User.email == email).first()
        
        if not user:
            print(f"User with email '{email}' not found.")
            return
        
        # Count memories
        memory_count = db.query(Memory).filter(Memory.user_id == user.id).count()
        
        if memory_count == 0:
            print(f"No memories found for user '{email}'.")
            return
        
        print(f"Found {memory_count} memories for user '{email}' (ID: {user.id}).")
        
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete all {memory_count} memories? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Deletion cancelled.")
            return
        
        # Delete all memories
        deleted = db.query(Memory).filter(Memory.user_id == user.id).delete()
        db.commit()
        
        print(f"Successfully deleted {deleted} memories for user '{email}'.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python delete_user_memories.py <user_email>")
        sys.exit(1)
    
    user_email = sys.argv[1]
    delete_user_memories(user_email)
