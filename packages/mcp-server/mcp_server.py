import asyncio
import sys
import os
import contextlib
import logging
import builtins
from typing import Any, List, Optional
from mcp.server.fastmcp import FastMCP
from sqlalchemy.future import select
from sqlalchemy import delete
from sqlalchemy.orm import selectinload

# --- STDOUT PROTECTION ---
# Force all logging to stderr
logging.basicConfig(level=logging.ERROR, stream=sys.stderr, force=True)

# Explicitly silence noisy libraries
logging.getLogger("sentence_transformers").setLevel(logging.ERROR)
logging.getLogger("transformers").setLevel(logging.ERROR)

# Override print to write to stderr by default to prevent accidental protocol corruption
# Keep a reference to the real stdout for the MCP server to use if it needs explicitly
_original_stdout = sys.stdout

def safe_print(*args, **kwargs):
    # If no file is specified, default to stderr
    if "file" not in kwargs:
        kwargs["file"] = sys.stderr
    builtins._original_print(*args, **kwargs)

# Save original print and replace
if not hasattr(builtins, "_original_print"):
    builtins._original_print = builtins.print
    builtins.print = safe_print

# Context manager to redirect stdout to stderr (doubly ensuring imports don't leak)
@contextlib.contextmanager
def redirect_stdout_to_stderr():
    old_stdout = sys.stdout
    sys.stdout = sys.stderr
    try:
        yield
    finally:
        sys.stdout = old_stdout

# Perform imports and initialization with stdout redirected
# This prevents libraries (like ChromaDB) from printing to stdout and breaking the MCP protocol
with redirect_stdout_to_stderr():
    from app.services.vector_store import vector_store
    from app.services.ingestion import ingestion_service
    from app.db.session import AsyncSessionLocal
    from app.models.document import Document
    from app.models.user import User
    from app.models.memory import Memory
    # Import ChatSession to ensure relationship mapper works
    from app.models.chat import ChatSession
    from app.services.context_builder import context_builder
    from app.services.memory_service import memory_service
    # Worker tasks imported lazily to avoid Celery/Redis connection at startup

# Setup File Logging for Debugging (since stdout is redirected)
import logging
file_handler = logging.FileHandler("mcp_debug.log")
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger = logging.getLogger("mcp_server")
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

# Initialize FastMCP Server with DNS rebinding protection configured
# to allow the production domain (otherwise 421 "Invalid Host header")
from mcp.server.transport_security import TransportSecuritySettings

mcp = FastMCP(
    "MemWyre",
    transport_security=TransportSecuritySettings(
        allowed_hosts=["server.memwyre.tech", "localhost", "127.0.0.1"],
    ),
)

# Import Context and ApiKey
from mcp.server.fastmcp import Context
from app.models.api_key import ApiKey
from app.core.config import settings
from jose import jwt, JWTError
import hashlib

def hash_key(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()

# Helper to get current user async
async def get_current_user(db, ctx: Context = None, required_scope: str = None):
    """
    Get the current user based on:
    1. HTTP Headers (Multi-Tenant via Context)
    2. Environment Variables (Single-Tenant fallback)
    Also validates required scopes if provided.
    Returns a tuple of (User, client_source) where client_source is determined from protocol or API key name.
    """
    api_key = None
    protocol_client_name = None

    # 0. Check Protocol Client Info (MCP standard initialize params)
    if ctx:
        try:
            if hasattr(ctx, 'session'):
                session = ctx.session
                # Attempt to extract from standard mcp python SDK internals
                # Different versions of the SDK store it in different places
                if hasattr(session, '_client_info') and hasattr(session._client_info, 'name'):
                    protocol_client_name = session._client_info.name
                elif hasattr(session, 'client_info') and hasattr(session.client_info, 'name'):
                    protocol_client_name = session.client_info.name
                elif hasattr(session, 'init_options') and hasattr(session.init_options, 'clientInfo'):
                    protocol_client_name = session.init_options.clientInfo.name
            
                if protocol_client_name:
                    logger.info(f"Detected MCP protocol client name: {protocol_client_name}")
                else:
                    logger.debug(f"Session attrs (could not find client info): {[a for a in dir(session) if not a.startswith('_')]}")
        except Exception as e:
            logger.error(f"Error extracting protocol client info: {e}")

    # Explicit environment variable source override
    env_client_name = os.environ.get("BRAIN_VAULT_CLIENT_NAME")

    # 1. Check Context for Headers (HTTP Mode)
    if ctx and hasattr(ctx, 'request_context'):
        try:
            rc = ctx.request_context
            logger.info(f"request_context type: {type(rc)}, attrs: {[a for a in dir(rc) if not a.startswith('_')]}")
            
            # Try multiple ways to get headers (varies by transport)
            headers = {}
            if hasattr(rc, 'headers'):
                headers = rc.headers
            elif hasattr(rc, 'request') and hasattr(rc.request, 'headers'):
                headers = rc.request.headers
            elif isinstance(rc, dict):
                headers = rc.get('headers', {})
            
            # Convert to dict if it's a special headers object
            if hasattr(headers, 'items'):
                header_dict = dict(headers.items()) if not isinstance(headers, dict) else headers
            else:
                header_dict = {}
            
            logger.info(f"Extracted headers keys: {list(header_dict.keys())}")
            
            # Check Custom Headers for explicit client name
            for key, value in header_dict.items():
                if key.lower() == 'x-mcp-client-name':
                    protocol_client_name = protocol_client_name or value
            
            # Check Authorization Header (case-insensitive)
            auth_header = None
            for key, value in header_dict.items():
                if key.lower() == 'authorization':
                    auth_header = value
                    break

            if auth_header:
                logger.info(f"Found auth header: {auth_header[:20]}...")
                if auth_header.startswith("Bearer "):
                    token = auth_header.split(" ")[1]
                    if token.startswith("bv_sk_"):
                        api_key = token
                elif auth_header.startswith("bv_sk_"):
                    api_key = auth_header
            
            # Check Custom Header (case-insensitive)
            if not api_key:
                for key, value in header_dict.items():
                    if key.lower() in ('x-brain-vault-key', 'x-api-key'):
                        api_key = value
                        break
        except Exception as e:
            logger.error(f"Error extracting headers from context: {e}", exc_info=True)

    # 2. Check Environment Variables (Stdio Mode / Single User)
    if not api_key:
        api_key = os.environ.get("BRAIN_VAULT_API_KEY")

    key_record_name = None

    # 3. Authenticate
    user = None
    if api_key:
        # A. Persistent API Key
        if api_key.startswith("bv_sk_"):
            hashed = hash_key(api_key)
            result = await db.execute(select(ApiKey).filter(ApiKey.key_hash == hashed, ApiKey.is_active == True))
            key_record = result.scalars().first()
            if key_record:
                
                # Check scopes, default to allowing read/write if scopes aren't set (legacy keys)
                scopes = key_record.scopes or ["mcp:read", "mcp:write"]
                if required_scope and required_scope not in scopes:
                    raise Exception(f"Permission denied: Missing required scope '{required_scope}'")
                
                result_user = await db.execute(select(User).filter(User.id == key_record.user_id))
                user = result_user.scalars().first()
                key_record_name = key_record.name
        
        # B. OAuth2 Access Token (JWT)
        else:
            try:
                # Verify JWT
                payload = jwt.decode(api_key, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
                user_id: str = payload.get("sub")
                
                # For JWT, assume full user access within MCP for now, or decode scopes if added to JWT later
                if user_id:
                    result = await db.execute(select(User).filter(User.id == int(user_id)))
                    user = result.scalars().first()
            except JWTError:
                # Invalid or expired token
                pass

    # 4. Fallback Legacy Auth (Env Vars for ID/Email)
    # Only if NO API KEY was provided/found (to prevent accidental bypass)
    if not user and not api_key:
        # Fallback assume full access for local dev
        user_email = os.environ.get("BRAIN_VAULT_USER_EMAIL")
        if user_email:
            result = await db.execute(select(User).filter(User.email == user_email))
            user = result.scalars().first()
            
        user_id = os.environ.get("BRAIN_VAULT_USER_ID")
        if not user and user_id:
            result = await db.execute(select(User).filter(User.id == int(user_id)))
            user = result.scalars().first()

    # Determine priority for client_source
    client_source = protocol_client_name or env_client_name or key_record_name
    return (user, client_source)



@mcp.tool()
async def save_memory(text: str, ctx: Context, source: str = "mcp", tags: Optional[List[str]] = None) -> str:
    """
    Save a new memory snippet to the MemWyre Vault. Use this tool when the user explicitly asks you to 'remember' something, 'save' a note, or when you encounter important information that should be persisted for future reference.
    Args:
        text: The content of the memory.
        source: Source of memory (default 'mcp').
        tags: Optional list of tags.
    """
    async with AsyncSessionLocal() as db:
        try:
            logger.info(f"MCP save_memory called. Source: {source}. Text length: {len(text)}")
            user, key_name = await get_current_user(db, ctx, required_scope="mcp:write")
            if not user:
                logger.error("No user found during save_memory")
                return "Error: No user found."

            # Use the dynamically identified client source if the tool caller just used "mcp"
            effective_source = source
            if source == "mcp" and key_name:
                effective_source = key_name
            
            logger.info(f"Effective source: {effective_source} (identified source: {key_name})")

            memory = await memory_service.create_memory(
                db=db,
                user=user,
                content=text,
                source=effective_source,
                tags=tags
            )
            
            logger.info(f"Memory saved successfully: mem_{memory.id}")
            return f"Memory saved to Inbox with ID: mem_{memory.id} (Status: {memory.status})"
        except Exception as e:
            logger.error(f"Error saving memory: {e}", exc_info=True)
            return f"Error saving memory: {str(e)}"

@mcp.tool()
async def search_memwyre(query: str, ctx: Context, purpose: str = "general") -> str:
    """
    The PRIMARY tool for searching the user's "MemWyre". Use this to retrieve relevant context, notes, code snippets, or past conversations from the MemWyre Vault.
    ALWAYS use this before answering questions that might require personal context.
    Args:
        query: The semantic search query (e.g., "python fastapi project structure", "notes on meeting with Bob", or "auth system specs").
        purpose: Optional hint for context formatting ("general", "code", "summary").
    """
    async with AsyncSessionLocal() as db:
        try:
            user, _ = await get_current_user(db, ctx, required_scope="mcp:read")
            if not user:
                return "Error: No user found."
                
            # Context builder uses vector store (network/sync)
            ctx = context_builder.build_context(query=query, user_id=user.id, limit_tokens=2000)
            return ctx["text"]
        except Exception as e:
            return f"Error searching vault: {str(e)}"

@mcp.tool()
async def get_inbox(ctx: Context) -> str:
    """
    Get list of pending memories in the MemWyre Inbox.
    """
    async with AsyncSessionLocal() as db:
        try:
            user, _ = await get_current_user(db, ctx, required_scope="mcp:read")
            if not user:
                return "Error: No user found."
                
            result = await db.execute(
                select(Memory).filter(
                    Memory.user_id == user.id,
                    Memory.status == "pending"
                ).order_by(Memory.created_at.desc())
            )
            memories = result.scalars().all()
            
            if not memories:
                return "Inbox is empty."
                
            results = []
            for mem in memories:
                results.append(f"ID: mem_{mem.id} | Content: {mem.content[:50]}... | Source: {mem.source_llm}")
                
            return "\n".join(results)
        except Exception as e:
            return f"Error getting inbox: {str(e)}"

@mcp.tool()
async def get_document(doc_id: int, ctx: Context) -> str:
    """
    Retrieve the full content of a specific document by ID from MemWyre.
    Args:
        doc_id: The ID of the document.
    """
    async with AsyncSessionLocal() as db:
        try:
            user, _ = await get_current_user(db, ctx, required_scope="mcp:read")
            if not user:
                return "Error: No user found."
                
            result = await db.execute(
                select(Document).filter(Document.id == doc_id)
            )
            doc = result.scalars().first()
            
            if not doc:
                return f"Document with ID {doc_id} not found."
                
            # Check ownership
            if doc.user_id != user.id:
                 return f"Document with ID {doc_id} not found (Access Denied)."
                 
            return doc.content
        except Exception as e:
            return f"Error getting document: {str(e)}"

@mcp.tool()
async def generate_prompt(query: str, ctx: Context, template: str = "standard") -> str:
    """
    Generate a prompt with retrieved context from MemWyre.
    Args:
        query: The user's question or request.
        template: The template to use ("standard", "code", "summary").
    """
    async with AsyncSessionLocal() as db:
        try:
            user, _ = await get_current_user(db, ctx, required_scope="mcp:read")
            if not user:
                return "Error: No user found."
            
            # 1. Retrieve Context using ContextBuilder (Standardized)
            ctx = context_builder.build_context(query=query, user_id=user.id, limit_tokens=2000)
            context_str = ctx["text"]
            
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
        except Exception as e:
            return f"Error generating prompt: {str(e)}"

@mcp.tool()
async def update_memory(memory_id: str, content: str, ctx: Context) -> str:
    """
    Update the content of an existing memory in MemWyre.
    Args:
        memory_id: The ID of the memory (must start with 'mem_').
        content: The new content.
    """
    if not memory_id.startswith("mem_"):
        return "Error: Only memories (starting with 'mem_') can be updated via this tool."

    async with AsyncSessionLocal() as db:
        try:
            user, _ = await get_current_user(db, ctx, required_scope="mcp:write")
            if not user:
                return "Error: No user found."

            try:
                mem_id = int(memory_id.split("_")[1])
            except ValueError:
                return "Error: Invalid ID format."

            result = await db.execute(
                select(Memory).filter(Memory.id == mem_id, Memory.user_id == user.id)
            )
            memory = result.scalars().first()
            if not memory:
                return "Error: Memory not found."

            # Update DB
            memory.content = content
            await db.commit()
            await db.refresh(memory)

            # Update Vector Store
            if memory.embedding_id:
                try:
                    vector_store.delete(ids=[memory.embedding_id])
                except:
                    pass
            
            # Re-ingest
            ids, raw_chunks, enriched_chunks, metadatas = await ingestion_service.process_text(
                text=memory.content,
                document_id=memory.id,
                title=memory.title,
                doc_type="memory",
                metadata={"user_id": user.id, "memory_id": memory.id, "tags": str(memory.tags) if memory.tags else "", "source": "mcp"}
            )
            
            if ids:
                memory.embedding_id = ids[0]
                await db.commit()
                
                vector_store.add_documents(
                    ids=ids,
                    documents=enriched_chunks,
                    metadatas=metadatas
                )

            return f"Memory {memory_id} updated successfully."
        except Exception as e:
            return f"Error updating memory: {str(e)}"

@mcp.tool()
async def delete_memory(memory_id: str, ctx: Context) -> str:
    """
    Delete a memory or document by ID from MemWyre.
    Args:
        memory_id: The ID of the item (e.g., 'mem_1' or 'doc_5').
    """
    async with AsyncSessionLocal() as db:
        try:
            user, _ = await get_current_user(db, ctx, required_scope="mcp:write")
            if not user:
                return "Error: No user found."

            if memory_id.startswith("doc_"):
                # Handle Document Deletion
                try:
                    doc_id = int(memory_id.split("_")[1])
                except ValueError:
                    return "Error: Invalid ID format."

                # Eager load chunks because they are accessed
                result = await db.execute(
                    select(Document).options(selectinload(Document.chunks)).filter(Document.id == doc_id, Document.user_id == user.id)
                )
                document = result.scalars().first()

                if not document:
                    return "Error: Document not found."
                
                # Delete chunks from vector store
                for chunk in document.chunks:
                    if chunk.embedding_id:
                        try:
                            vector_store.delete(ids=[chunk.embedding_id])
                        except:
                            pass # Ignore vector store errors
                
                await db.delete(document)
                await db.commit()
                return f"Document {memory_id} deleted successfully."
                
            elif memory_id.startswith("mem_"):
                # Handle Memory Deletion
                try:
                    mem_id = int(memory_id.split("_")[1])
                except ValueError:
                    return "Error: Invalid ID format."

                result = await db.execute(select(Memory).filter(Memory.id == mem_id, Memory.user_id == user.id))
                memory = result.scalars().first()
                if not memory:
                    return "Error: Memory not found."
                
                if memory.embedding_id:
                    try:
                        vector_store.delete(ids=[memory.embedding_id])
                    except:
                        pass
                    
                await db.delete(memory)
                await db.commit()
                return f"Memory {memory_id} deleted successfully."
            
            else:
                return "Error: ID must start with 'mem_' or 'doc_'."
        except Exception as e:
            return f"Error deleting item: {str(e)}"

@mcp.tool()
async def list_memories(ctx: Context, limit: int = 10, offset: int = 0) -> str:
    """
    List recent memories and documents in MemWyre.
    Args:
        limit: Number of items to return (default 10).
        offset: Pagination offset (default 0).
    """
    async with AsyncSessionLocal() as db:
        try:
            user, _ = await get_current_user(db, ctx, required_scope="mcp:read")
            if not user:
                return "Error: No user found."
                
            # Fetch Memories
            result = await db.execute(
                select(Memory).filter(Memory.user_id == user.id).order_by(Memory.created_at.desc()).limit(limit).offset(offset)
            )
            memories = result.scalars().all()
            
            # Fetch Documents (simple logic, separate query for now)
            result_docs = await db.execute(
                select(Document).filter(Document.user_id == user.id).order_by(Document.created_at.desc()).limit(limit).offset(offset)
            )
            documents = result_docs.scalars().all()
            
            results = []
            for mem in memories:
                results.append(f"[Memory] ID: mem_{mem.id} | Title: {mem.title} | Created: {mem.created_at}")
                
            for doc in documents:
                results.append(f"[Document] ID: doc_{doc.id} | Title: {doc.title} | Type: {doc.file_type} | Created: {doc.created_at}")
                
            if not results:
                return "No memories found."
                
            return "\n".join(results)
        except Exception as e:
            return f"Error listing memories: {str(e)}"

# --- RESOURCES ---
@mcp.resource("brain://inbox")
async def get_inbox_resource() -> str:
    """
    Read the current contents of the Inbox directly as a resource.
    """
    async with AsyncSessionLocal() as db:
        try:
            user, _ = await get_current_user(db, None, required_scope="mcp:read")
            if not user:
                return "Error: No user found."
                
            result = await db.execute(
                select(Memory).filter(
                    Memory.user_id == user.id,
                    Memory.status == "pending"
                ).order_by(Memory.created_at.desc())
            )
            memories = result.scalars().all()
            
            if not memories:
                return "Inbox is empty."
                
            results = ["# MemWyre Inbox"]
            for mem in memories:
                results.append(f"- [ID: mem_{mem.id}] ({mem.source_llm}): {mem.content[:100]}...")
                
            return "\n".join(results)
        except Exception as e:
            return f"Error reading inbox resource: {str(e)}"

# --- PROMPTS ---
@mcp.prompt()
def daily_briefing() -> str:
    """
    Generate a briefing prompt based on recent memories from MemWyre.
    """
    return "Please review my recent memories from MemWyre and provide a summary of what I've been working on and any outstanding tasks in my Inbox."

@mcp.prompt()
def project_context(project_name: str) -> str:
    """
    Generate a prompt to focus on a specific project using MemWyre.
    """
    return f"Please search MemWyre for all information related to '{project_name}'. Summarize the key points, technical decisions, and current status."

@mcp.tool()
async def search_by_date(start_date: str, ctx: Context, end_date: Optional[str] = None) -> str:
    """
    Find memories in MemWyre created within a specific date range.
    Args:
        start_date: Start date in YYYY-MM-DD format.
        end_date: End date in YYYY-MM-DD format (optional, defaults to end of start_date).
    """
    async with AsyncSessionLocal() as db:
        try:
            user, _ = await get_current_user(db, ctx, required_scope="mcp:read")
            if not user:
                return "Error: No user found."
                
            from datetime import datetime, timedelta
            
            try:
                start = datetime.strptime(start_date, "%Y-%m-%d")
                if end_date:
                    end = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=1) # Inclusive of end date
                else:
                    end = start + timedelta(days=1)
            except ValueError:
                return "Error: Invalid date format. Use YYYY-MM-DD."
                
            result = await db.execute(
                select(Memory).filter(
                    Memory.user_id == user.id,
                    Memory.created_at >= start,
                    Memory.created_at < end
                ).order_by(Memory.created_at.asc())
            )
            memories = result.scalars().all()
            
            if not memories:
                return f"No memories found between {start_date} and {end_date or start_date}."
                
            results = []
            for mem in memories:
                results.append(f"[{mem.created_at.strftime('%Y-%m-%d %H:%M')}] {mem.title}: {mem.content[:200]}...")
                
            return "\n".join(results)
        except Exception as e:
            return f"Error searching by date: {str(e)}"

@mcp.tool()
async def get_all_tags(ctx: Context) -> str:
    """
    Get a list of all tags currently used in MemWyre. 
    Use this to understand the taxonomy of the user's knowledge.
    """
    async with AsyncSessionLocal() as db:
        try:
            user, _ = await get_current_user(db, ctx, required_scope="mcp:read")
            if not user:
                return "Error: No user found."
            
            # Inefficient but valid for MVP: Fetch all and aggregate
            result = await db.execute(select(Memory).filter(Memory.user_id == user.id))
            memories = result.scalars().all()
            
            all_tags = set()
            for mem in memories:
                if mem.tags:
                    try:
                        # mem.tags might be a list or a string repr of list depending on SQLite/JSON handling
                        tags_list = mem.tags if isinstance(mem.tags, list) else eval(mem.tags)
                        for tag in tags_list:
                            all_tags.add(tag)
                    except:
                        pass
                        
            sorted_tags = sorted(list(all_tags))
            
            if not sorted_tags:
                return "No tags found."
                
            return "Current Tags:\n" + ", ".join([f"#{t}" for t in sorted_tags])
        except Exception as e:
            return f"Error getting tags: {str(e)}"

if __name__ == "__main__":
    mcp.run()
