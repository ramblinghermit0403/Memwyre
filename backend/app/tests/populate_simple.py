import sqlite3
import uuid
import os

def populate():
    db_path = os.path.join(os.getcwd(), "brain_vault.db")
    if not os.path.exists(db_path):
        print(f"DB not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check if column exists (optional since we did it, but safe)
    try:
        cursor.execute("SELECT email, drop_token FROM users")
        rows = cursor.fetchall()
        for email, token in rows:
            if not token:
                new_token = str(uuid.uuid4())
                cursor.execute("UPDATE users SET drop_token = ? WHERE email = ?", (new_token, email))
                print(f"Updated {email} with token {new_token}")
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    populate()
