import asyncio
import sys
import os
from typing import Any, List, Optional
from mcp.server.fastmcp import FastMCP

from app.services.vector_store import vector_store
from app.services.ingestion import ingestion_service
from app.db.session import SessionLocal
from app.models.document import Document
from app.models.user import User
from app.models.memory import Memory

# Initialize FastMCP Server
mcp = FastMCP("Brain Vault")

# Helper to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db):
    """
    Get the current user based on environment variables or fallback to first user.
    """
    # 1. Try env var for email
    user_email = os.environ.get("BRAIN_VAULT_USER_EMAIL")
    if user_email:
        user = db.query(User).filter(User.email == user_email).first()
        if user:
            return user
            
    # 2. Try env var for ID
    user_id = os.environ.get("BRAIN_VAULT_USER_ID")
    if user_id:
        user = db.query(User).filter(User.id == int(user_id)).first()
        if user:
            return user
            
    # 3. Fallback to first user (MVP/Single User mode)
    return db.query(User).first()

@mcp.tool()
async def search_memory(query: str, top_k: int = 5) -> str:
    """
    Search the Brain Vault memory for relevant context.
    Args:
        query: The search query.
        top_k: Number of results to return.
    """
    db = SessionLocal()
    try:
        user = get_current_user(db)
        if not user:
            return "Error: No user found."
            
        # Filter by user_id
        results = vector_store.query(query, n_results=top_k, where={"user_id": user.id})
        
        if not results["documents"] or not results["documents"][0]:
            return "No relevant memories found."
        
        # Format results
        formatted_results = []
        for i, doc in enumerate(results["documents"][0]):
            formatted_results.append(f"Result {i+1}:\n{doc}")
        
        return "\n\n---\n\n".join(formatted_results)
    finally:
        db.close()

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
        user = get_current_user(db)
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
        embedding_ids, chunk_texts, metadatas = ingestion_service.process_text(
            text=text,
            document_id=doc.id,
            title="MCP Memory",
            doc_type="memory",
            metadata={"source": "mcp", "tags": ",".join(tags or []), "user_id": user.id}
        )
        
        # FIX: Actually save to vector store
        vector_store.add_documents(
            ids=embedding_ids,
            documents=chunk_texts,
            metadatas=metadatas
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
        user = get_current_user(db)
        if not user:
            return "Error: No user found."
            
        doc = db.query(Document).filter(Document.id == doc_id).first()
        if not doc:
            return f"Document with ID {doc_id} not found."
            
        # Check ownership
        if doc.user_id != user.id:
             return f"Document with ID {doc_id} not found (Access Denied)."
             
        return doc.content
    finally:
        db.close()

@mcp.tool()
async def generate_prompt(query: str, template: str = "standard") -> str:
    """
    Generate a prompt with retrieved context from the vault.
    Args:
        query: The user's question or request.
        template: The template to use ("standard", "code", "summary").
    """
    db = SessionLocal()
    try:
        user = get_current_user(db)
        if not user:
            return "Error: No user found."
            
        # 1. Retrieve Context
        results = vector_store.query(query, n_results=10, where={"user_id": user.id})
        
        retrieved_texts = []
        if results["documents"]:
            retrieved_texts = results["documents"][0]
            
        # 2. Compact Context (Simple limit for MCP)
        context_str = "\n\n---\n\n".join(retrieved_texts[:5]) # Limit to top 5 chunks
        
        # 3. Apply Template
        if template == "code":
            prompt = f"""You are an expert coding assistant. Use the following context to answer the user's request.

CONTEXT:
{context_str}

USER REQUEST:
{query}

INSTRUCTIONS:
- Provide clear, efficient code.
- Explain your reasoning.
"""
        elif template == "summary":
            prompt = f"""Please summarize the following information based on the user's query.

CONTEXT:
{context_str}

QUERY:
{query}
"""
        else: # Standard
            prompt = f"""Use the following memory context to answer the question.

MEMORY CONTEXT:
{context_str}

QUESTION:
{query}
"""
        return prompt
    finally:
        db.close()

@mcp.tool()
async def update_memory(memory_id: str, content: str) -> str:
    """
    Update the content of an existing memory.
    Args:
        memory_id: The ID of the memory (must start with 'mem_').
        content: The new content.
    """
    if not memory_id.startswith("mem_"):
        return "Error: Only memories (starting with 'mem_') can be updated via this tool."

    db = SessionLocal()
    try:
        user = get_current_user(db)
        if not user:
            return "Error: No user found."

        try:
            mem_id = int(memory_id.split("_")[1])
        except ValueError:
            return "Error: Invalid ID format."

        memory = db.query(Memory).filter(Memory.id == mem_id, Memory.user_id == user.id).first()
        if not memory:
            return "Error: Memory not found."

        # Update DB
        memory.content = content
        db.commit()
        db.refresh(memory)

        # Update Vector Store
        if memory.embedding_id:
            try:
                vector_store.delete(ids=[memory.embedding_id])
            except:
                pass
        
        # Re-ingest
        ids, documents_content, metadatas = ingestion_service.process_text(
            text=memory.content,
            document_id=memory.id,
            title=memory.title,
            doc_type="memory",
            metadata={"user_id": user.id, "memory_id": memory.id, "tags": str(memory.tags) if memory.tags else "", "source": "mcp"}
        )
        
        if ids:
            memory.embedding_id = ids[0]
            db.commit()
            
            vector_store.add_documents(
                ids=ids,
                documents=documents_content,
                metadatas=metadatas
            )

        return f"Memory {memory_id} updated successfully."
    except Exception as e:
        return f"Error updating memory: {str(e)}"
    finally:
        db.close()

@mcp.tool()
async def delete_memory(memory_id: str) -> str:
    """
    Delete a memory or document by ID.
    Args:
        memory_id: The ID of the item (e.g., 'mem_1' or 'doc_5').
    """
    db = SessionLocal()
    try:
        user = get_current_user(db)
        if not user:
            return "Error: No user found."

        if memory_id.startswith("doc_"):
            # Handle Document Deletion
            try:
                doc_id = int(memory_id.split("_")[1])
            except ValueError:
                return "Error: Invalid ID format."

            document = db.query(Document).filter(Document.id == doc_id, Document.user_id == user.id).first()
            if not document:
                return "Error: Document not found."
            
            # Delete chunks from vector store
            for chunk in document.chunks:
                if chunk.embedding_id:
                    try:
                        vector_store.delete(ids=[chunk.embedding_id])
                    except:
                        pass # Ignore vector store errors
            
            db.delete(document)
            db.commit()
            return f"Document {memory_id} deleted successfully."
            
        elif memory_id.startswith("mem_"):
            # Handle Memory Deletion
            try:
                mem_id = int(memory_id.split("_")[1])
            except ValueError:
                return "Error: Invalid ID format."

            memory = db.query(Memory).filter(Memory.id == mem_id, Memory.user_id == user.id).first()
            if not memory:
                return "Error: Memory not found."
            
            if memory.embedding_id:
                try:
                    vector_store.delete(ids=[memory.embedding_id])
                except:
                    pass
                
            db.delete(memory)
            db.commit()
            return f"Memory {memory_id} deleted successfully."
        
        else:
            return "Error: ID must start with 'mem_' or 'doc_'."
    except Exception as e:
        return f"Error deleting item: {str(e)}"
    finally:
        db.close()

@mcp.tool()
async def list_memories(limit: int = 10, offset: int = 0) -> str:
    """
    List recent memories and documents in the vault.
    Args:
        limit: Number of items to return (default 10).
        offset: Pagination offset (default 0).
    """
    db = SessionLocal()
    try:
        user = get_current_user(db)
        if not user:
            return "Error: No user found."
            
        # Fetch Memories
        memories = db.query(Memory).filter(Memory.user_id == user.id).order_by(Memory.created_at.desc()).limit(limit).offset(offset).all()
        
        # Fetch Documents (simple logic, separate query for now)
        documents = db.query(Document).filter(Document.user_id == user.id).order_by(Document.created_at.desc()).limit(limit).offset(offset).all()
        
        results = []
        for mem in memories:
            results.append(f"[Memory] ID: mem_{mem.id} | Title: {mem.title} | Created: {mem.created_at}")
            
        for doc in documents:
            results.append(f"[Document] ID: doc_{doc.id} | Title: {doc.title} | Type: {doc.file_type} | Created: {doc.created_at}")
            
        if not results:
            return "No memories found."
            
        return "\n".join(results)
    finally:
        db.close()

if __name__ == "__main__":
    mcp.run()
