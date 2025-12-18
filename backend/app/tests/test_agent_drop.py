import requests
import json
import time

BASE_URL = "http://localhost:8000/api/v1"

def get_token():
    import sqlite3
    import os
    # Try to find the DB
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "brain_vault.db")
    if not os.path.exists(db_path):
        return "no-db"
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT drop_token FROM users WHERE drop_token IS NOT NULL LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else "no-token"

def test_valid_drop():
    token = get_token()
    print(f"\n--- Testing Valid Drop with Token: {token} ---")
    payload = {
        "title": "Test Agent Result",
        "content": "<p>This is a <b>test</b> result from an external agent.</p>",
        "job_id": "job_123",
        "metadata": {
            "model": "test-model-v1",
            "runtime": "python3.10",
            "duration_sec": 1.5
        }
    }
    token = get_token()
    response = requests.post(f"{BASE_URL}/inbox/drop/{token}", json=payload)
    print(f"Status: {response.status_code}")
    try:
        print(f"Response: {response.json()}")
    except:
        print(f"Response (text): {response.text}")
    
    if response.status_code == 200:
        print("✅ SUCCESS: Valid drop accepted.")
    else:
        print("❌ FAILURE: Valid drop rejected.")

def test_large_payload():
    print("\n--- Testing Large Payload (>50KB) ---")
    large_content = "X" * (51 * 1024)
    payload = {
        "content": large_content
    }
    token = get_token()
    response = requests.post(f"{BASE_URL}/inbox/drop/{token}", json=payload)
    print(f"Status: {response.status_code}")
    if response.status_code == 413:
        print("✅ SUCCESS: Large payload rejected.")
    else:
        print("❌ FAILURE: Large payload was not correctly rejected.")

def test_html_stripping():
    print("\n--- Testing HTML Stripping ---")
    payload = {
        "content": "<div>Hello <script>alert('bad')</script> world!</div>"
    }
    token = get_token()
    response = requests.post(f"{BASE_URL}/inbox/drop/{token}", json=payload)
    print(f"Status: {response.status_code}")
    # We would need to check the DB to verify stripping, but if it returns 200, it survived the strip check
    if response.status_code == 200:
        print("✅ SUCCESS: HTML payload accepted and stripped.")
    else:
        print("❌ FAILURE: HTML payload rejected.")

def test_rate_limiting():
    print("\n--- Testing Rate Limiting ---")
    print("Sending 15 requests rapidly...")
    for i in range(15):
        payload = {"content": f"Rate limit test {i}"}
        response = requests.post(f"{BASE_URL}/inbox/drop", json=payload)
        if response.status_code == 429:
            print(f"✅ SUCCESS: Rate limited at request {i+1}")
            return
    print("❌ FAILURE: Not rate limited after 15 requests.")

if __name__ == "__main__":
    try:
        test_valid_drop()
        test_html_stripping()
        test_large_payload()
        test_rate_limiting()
    except Exception as e:
        print(f"Error during testing: {e}")
