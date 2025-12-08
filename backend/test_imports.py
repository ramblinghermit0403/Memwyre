import sys
import os

# Add the current directory to sys.path so 'app' module can be found
sys.path.append(os.getcwd())

print("Checking imports...")
try:
    print("Importing mcp.server.fastmcp...")
    from mcp.server.fastmcp import FastMCP
    print("Success.")

    print("Importing app.services.vector_store...")
    from app.services.vector_store import vector_store
    print("Success.")
    
    print("Importing app.services.ingestion...")
    from app.services.ingestion import ingestion_service
    print("Success.")

    print("Importing app.db.session...")
    from app.db.session import SessionLocal
    print("Success.")

    print("Importing models...")
    from app.models.document import Document
    from app.models.user import User
    from app.models.memory import Memory
    print("Success.")

    print("Importing context_builder...")
    from app.services.context_builder import context_builder
    print("Success.")

    print("ALL IMPORTS SUCCESSFUL")
except Exception as e:
    print(f"IMPORT ERROR: {e}")
    import traceback
    traceback.print_exc()
