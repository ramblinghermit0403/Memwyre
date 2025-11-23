import asyncio
import sys
from typing import Any, List, Optional
from mcp.server.fastmcp import FastMCP

from app.services.vector_store import vector_store
from app.services.ingestion import ingestion_service
from app.db.session import SessionLocal
from app.models.document import Document
from app.models.user import User

# Initialize FastMCP Server
mcp = FastMCP("Brain Vault")

# Helper to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@mcp.tool()
async def search_memory(query: str, top_k: int = 5) -> str:
    """
    Search the Brain Vault memory for relevant context.
    Args:
        query: The search query.
        top_k: Number of results to return.
    """
    results = vector_store.query(query, n_results=top_k)
    if not results["documents"]:
        return "No relevant memories found."
    
    # Format results
    formatted_results = []
    for i, doc in enumerate(results["documents"][0]):
        formatted_results.append(f"Result {i+1}:\n{doc}")
    
    return "\n\n---\n\n".join(formatted_results)

@mcp.tool()
async def save_memory(text: str, tags: Optional[List[str]] = None) -> str:
    """
    Save a new memory snippet to the Brain Vault.
    Args:
        text: The content of the memory.
        tags: Optional list of tags.
    """
    # For MVP, we'll assume a default user or require user_id in a real scenario
    # Here we just use the ingestion service to process the text
    # Note: In a real multi-user app, we'd need to handle auth context here
    
    # We need to create a Document record first to get an ID
    db = SessionLocal()
    try:
        # Create a dummy user for the MCP context if needed, or assume single user MVP
        # For now, we'll just process the text directly into vector store
        # But to be consistent with our app, we should create a Document
        
        # Fetch the first user for MVP (assuming single user)
        user = db.query(User).first()
        if not user:
            return "Error: No user found in database to attach memory to."

        doc = Document(
            title="MCP Memory",
            content=text,
            doc_type="memory",
            user_id=user.id
        )
        db.add(doc)
        db.commit()
        db.refresh(doc)
        
        # Ingest
        ingestion_service.process_text(
            text=text,
            doc_id=doc.id,
            doc_type="memory",
            metadata={"source": "mcp", "tags": tags or []}
        )
        
        return f"Memory saved successfully with ID: {doc.id}"
    except Exception as e:
        return f"Error saving memory: {str(e)}"
    finally:
        db.close()

@mcp.tool()
async def get_document(doc_id: int) -> str:
    """
    Retrieve the full content of a specific document by ID.
    Args:
        doc_id: The ID of the document.
    """
    db = SessionLocal()
    try:
        doc = db.query(Document).filter(Document.id == doc_id).first()
        if not doc:
            return f"Document with ID {doc_id} not found."
        return doc.content
    finally:
        db.close()

if __name__ == "__main__":
    mcp.run()
