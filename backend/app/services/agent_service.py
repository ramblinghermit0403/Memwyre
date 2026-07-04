import logging
import json
import re
from typing import List, Dict, Any, Optional, Callable, Awaitable
from datetime import datetime

# LangChain Imports
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory
from pydantic import BaseModel, Field
from langchain_core.tools import tool, StructuredTool
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_aws import ChatBedrock
from langgraph.prebuilt import create_react_agent


# App Imports
from app.core.config import settings
from app.db.session import AsyncSessionLocal
from app.models.chat import ChatMessage, ChatSession, MessageRole
from app.services.llm_service_v2 import llm_service_v2 as llm_service
from app.services.vector_store import vector_store
if settings.MEMORY_ENGINE_VERSION == "v2":
    from app.services.retrieval_service_v2 import retrieval_service
else:
    from app.services.retrieval_service import retrieval_service
from sqlalchemy.future import select

logger = logging.getLogger(__name__)

# --- 1. Custom Memory History ---
class SQLChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id: str, user_id: int):
        self.session_id = session_id
        self.user_id = user_id
        
    @property
    def messages(self) -> List[BaseMessage]:
        # Sync wrapper not ideal for async DB, but LangChain BaseChatMessageHistory is sync-ish.
        # We'll use a helper or run generic sync code if needed, 
        # BUT RunnableWithMessageHistory supports async methods if we implement `aget_messages`?
        # Actually standard practice in async FastAPI + LangChain is tricky.
        # We will use a hack: load messages effectively before calling agent, 
        # OR implementation aget_messages.
        raise NotImplementedError("Use aget_messages for async")

    async def aget_messages(self) -> List[BaseMessage]:
        async with AsyncSessionLocal() as db:
            result = await db.execute(
                select(ChatMessage)
                .where(ChatMessage.session_id == int(self.session_id))
                .order_by(ChatMessage.created_at.asc())
            )
            rows = result.scalars().all()
            
            messages = []
            for row in rows:
                if row.role == MessageRole.USER:
                    messages.append(HumanMessage(content=row.content))
                elif row.role == MessageRole.ASSISTANT:
                    messages.append(AIMessage(content=row.content))
                elif row.role == MessageRole.SYSTEM:
                    messages.append(SystemMessage(content=row.content))
            return messages

    async def add_message(self, message: BaseMessage, sources: List[Dict] = None) -> int:
        async with AsyncSessionLocal() as db:
            role = MessageRole.USER
            if isinstance(message, AIMessage):
                role = MessageRole.ASSISTANT
            elif isinstance(message, SystemMessage):
                role = MessageRole.SYSTEM
                
            db_msg = ChatMessage(
                session_id=int(self.session_id),
                role=role,
                content=message.content,
                created_at=datetime.utcnow()
            )
            
            # Save Sources/Metadata if provided
            if sources:
                import json
                db_msg.meta_info = json.dumps({"sources": sources})
                
            db.add(db_msg)
            await db.commit()
            await db.refresh(db_msg)
            return db_msg.id

# ... (rest of class)

# ... inside process_message ...

            # Save AI Response and get ID
            ai_message_id = await chat_history.add_message(AIMessage(content=output), sources=sources)
            
            return {
                "output": output,
                "sources": sources,
                "message_id": ai_message_id
            }
            
    async def clear(self) -> None:
        pass

# --- 2. Tools ---



class SaveFactInput(BaseModel):
    fact: str = Field(description="The generic fact or note to save.")
    
@tool("save_fact", args_schema=SaveFactInput)
def save_fact_tool(fact: str):
    """Save a precise fact or note to the Brain Vault for long-term memory."""
    # We call the existing API logic or service to save memory.
    # Since we are inside the backend, we can call a service methods.
    # But usually we need `user_id`. Tools don't natively have context.
    # We will need to bind user_id to the tool when creating the agent.
    return "Error: User context missing from tool execution."

# --- 3. Agent Service ---

class AgentService:
    def __init__(self):
        # Allow overriding provider via settings? for now default to configured.
        pass

    def _normalize_markdown_block(self, text: str) -> str:
        if not text:
            return ""

        lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
        normalized_lines: List[str] = []
        previous_heading: Optional[str] = None
        previous_was_separator = False
        blank_count = 0

        for raw_line in lines:
            line = raw_line.rstrip()

            if not line.strip():
                blank_count += 1
                if blank_count <= 1 and normalized_lines and normalized_lines[-1] != "":
                    normalized_lines.append("")
                continue

            blank_count = 0
            heading_match = re.match(r"^\s{0,3}(#{1,6}\s+.+?)\s*$", line)
            strong_heading_match = re.match(r"^\s*\*\*([^*].+?)\*\*\s*$", line)

            heading_key = None
            if heading_match:
                heading_key = heading_match.group(1).strip().lower()
            elif strong_heading_match:
                heading_key = strong_heading_match.group(1).strip().lower()

            if heading_key and heading_key == previous_heading:
                continue
            previous_heading = heading_key if heading_key else None

            if re.match(r"^\s*([-*_]){3,}\s*$", line):
                if previous_was_separator:
                    continue
                previous_was_separator = True
                normalized_lines.append("---")
                continue
            previous_was_separator = False

            normalized_lines.append(line)

        text_out = "\n".join(normalized_lines).strip()
        text_out = re.sub(r"(?im)^\s*(answer|final answer)\s*:\s*$", "", text_out)
        text_out = re.sub(r"(?is)\s*(?:<\|/?\w+\|>|<end>|END_OF_RESPONSE)\s*$", "", text_out).strip()
        text_out = re.sub(r"\n{3,}", "\n\n", text_out).strip()
        return text_out

    def _normalize_agent_output(self, text: str) -> str:
        if not text:
            return ""

        normalized = text.replace("\r\n", "\n").replace("\r", "\n").strip()

        think_match = re.search(r"(?is)<(think|thinking)>\s*(.*?)\s*</\1>", normalized)
        reasoning_text = self._normalize_markdown_block(think_match.group(2)) if think_match else ""

        answer_text = re.sub(r"(?is)<(think|thinking)>\s*.*?\s*</\1>", "", normalized)
        answer_text = re.sub(r"(?is)<(think|thinking)>[\s\S]*$", "", answer_text)
        answer_text = re.sub(r"(?is)</?(think|thinking)>", "", answer_text)
        answer_text = self._normalize_markdown_block(answer_text)

        if reasoning_text and answer_text:
            return f"<think>\n{reasoning_text}\n</think>\n\n{answer_text}"
        if reasoning_text:
            return f"<think>\n{reasoning_text}\n</think>"
        return answer_text

    def _build_memwyre_context(self, results: List[Dict[str, Any]]) -> str:
        """
        Format retrieved context using Memwyre standards (Time-Aware).
        Separates Entity Profiles from regular chunks/facts.
        """
        profile_snippets = []
        result_snippets = []
        result_counter = 0
        
        for r in results:
            meta = r.get("metadata", {})
            result_type = meta.get("type", "")
            
            # Entity Profiles go into a separate section
            if result_type == "profile":
                entity_name = meta.get("entity_name", "Unknown")
                profile_snippets.append(f"[{entity_name}]\n{r.get('text', '')}")
                continue
            
            result_counter += 1
            chunk = r.get("chunk", None)
            
            # Extract Temporal Signals
            valid_from = meta.get("valid_from")
            valid_until = meta.get("valid_until")
            created_at = meta.get("created_at")
            
            # Fallback
            generic_date = meta.get("date") or meta.get("timestamp")
            
            # Construct Temporal Line
            vals = []
            if valid_from: vals.append(f"Event Date: {valid_from}")
            if valid_until: vals.append(f"| Valid Until: {valid_until}")
            if created_at: vals.append(f"| Recorded: {created_at}")
            
            date_str = " ".join(vals)
            if not date_str and generic_date: date_str = f"Date: {generic_date}"
            if not date_str: date_str = "Date: Unknown"
            
            # Content Construction
            content = r.get("text", "")
            if chunk:
               if hasattr(chunk, 'text') and chunk.text and chunk.text != content:
                   content = f"Fact: {content}\nChunk: {chunk.text}"
            
            result_snippets.append(f"[Result {result_counter}] ({date_str.strip()})\nContent: {content}")
        
        # Assemble final context string
        sections = []
        if profile_snippets:
            sections.append("=== ENTITY PROFILES ===\n" + "\n\n".join(profile_snippets))
        if result_snippets:
            sections.append("=== RETRIEVED FACTS & MEMORIES ===\n" + "\n\n---\n\n".join(result_snippets))
        
        return "\n\n".join(sections)
        
    async def process_message(
        self, 
        session_id: int, 
        user_id: int, 
        message: str, 
        model: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
        max_tokens: int = 2800,
        progress_callback: Optional[Callable[[str, str, Optional[Dict[str, Any]]], Awaitable[None]]] = None
    ) -> Dict[str, Any]:
        temperature = min(max(float(temperature), 0.0), 1.0)
        max_tokens = int(min(max(int(max_tokens), 128), 8192))
        
        # 1. Setup Chat History
        chat_history = SQLChatMessageHistory(session_id=str(session_id), user_id=user_id)

        # Get project_id from ChatSession
        project_id = None
        async with AsyncSessionLocal() as db:
            result_sess = await db.execute(select(ChatSession).where(ChatSession.id == session_id))
            session_obj = result_sess.scalars().first()
            if session_obj:
                project_id = getattr(session_obj, "project_id", None)

        async def emit_progress(step: str, status: str, meta: Optional[Dict[str, Any]] = None):
            if not progress_callback:
                return
            try:
                await progress_callback(step, status, meta or {})
            except Exception as e:
                logger.warning(f"Progress callback failed for step '{step}': {e}")
        
        # 2. Setup LLM based on requested model
        llm = None
        
        def get_llm(model_name):
            from app.services.llm_service_v2 import llm_service_v2
            
            provider = getattr(settings, "DEFAULT_LLM_PROVIDER", "openai").lower()
            if provider == "bedrock":
                return llm_service_v2._get_default_llm(temperature=temperature)
                
            google_key = settings.GEMINI_API_KEY
            
            if "gemini" in model_name.lower():
                if google_key:
                    return ChatGoogleGenerativeAI(
                        google_api_key=google_key, 
                        model=model_name,
                        temperature=temperature,
                        max_output_tokens=max_tokens
                    )
                raise ValueError("Google API Key not configured.")
            elif "gpt" in model_name.lower():
                if settings.OPENAI_API_KEY:
                    return ChatOpenAI(
                        api_key=settings.OPENAI_API_KEY, 
                        model=model_name,
                        temperature=temperature,
                        max_tokens=max_tokens
                    )
                raise ValueError("OpenAI API Key not configured.")
            else:
                return llm_service_v2._get_default_llm(temperature=temperature)

        try:
            llm = get_llm(model)
        except ValueError as e:
            await emit_progress("llm_generation_completed", "failed", {"error": str(e), "model": model})
            return {
                "output": f"Configuration Error: {str(e)} Please check your API keys in Settings.",
                "sources": [],
                "message_id": 0,
                "turn_status": "failed",
                "error": str(e)
            }
             
        # 3. Setup Tools
        
        # 3.1 Search Tool (DynamicWrapper)
        class SearchMemoryInput(BaseModel):
             query: str = Field(description="The query to search for in the brain vault.")
             
        async def search_memory_wrapper(query: str):
            """Search for relevant memories."""
            if settings.MEMORY_ENGINE_VERSION == "v2":
                from app.services.retrieval_service_v2 import retrieval_service
            else:
                from app.services.retrieval_service import retrieval_service
            from app.db.session import AsyncSessionLocal
            
            async with AsyncSessionLocal() as db:
                results = await retrieval_service.search_memories(
                    query=query,
                    user_id=user_id,
                    db=db,
                    top_k=5,
                    project_id=project_id
                )

            # Fix #7: Log hop mismatches
            # If answer_mode is EXTRACTIVE (Single Hop) and we found > 1 fact, it might be a misroute or purity issue.
            if results and results[0]["metadata"].get("answer_mode") == "EXTRACTIVE" and len(results) > 1:
                logger.warning(f"LocoMo Misroute: Query '{query}' classified as SINGLE but retrieved {len(results)} facts.")
            
            if not results:
                return "No relevant memories found."
            
            formatted = []
            for res in results:
                # Format: Source: Title [ID: 123]\nContent: ...
                meta = res["metadata"]
                
                doc_id = "unknown"
                if meta.get("memory_id"): doc_id = meta.get("memory_id")
                elif meta.get("document_id"): doc_id = meta.get("document_id")
                elif meta.get("fact_id"): doc_id = f"fact-{meta.get('fact_id')}"
                
                title = meta.get("title", "Untitled")
                if meta.get("type") == "fact":
                    title = "Fact"
                    
                content = res["text"]
                
                # Append enrichment info if available
                if meta.get("summary"):
                     content = f"Summary: {meta['summary']}\nDetails: {content}"
                
                formatted.append(f"Source: {title} [ID: {doc_id}]\nContent: {content}")
                
            return "\n\n---\n\n".join(formatted)

        search_memory_tool_instance = StructuredTool.from_function(
            func=search_memory_wrapper,
            name="search_memory",
            description="Search for relevant memories, notes, and documents in the Brain Vault.",
            args_schema=SearchMemoryInput,
            coroutine=search_memory_wrapper
        )
        
        # 3.2 Save Tool REMOVED (Side-car extraction used instead)
        # async def save_fact_wrapper(fact: str): ... 
        
        # Only Search Tool remains available to the Agent
        tools = [search_memory_tool_instance]
        
        # 4. Create Agent (LangGraph)
        # This creates a compiled state graph (Runnable)
        app = create_react_agent(llm, tools)
        
        # 5. Prepare Input for LangGraph
        
        # 5.0 Update History with User Message
        await chat_history.add_message(HumanMessage(content=message))
        history_messages = await chat_history.aget_messages()
        
        # 5.1 PRE-FETCH CONTEXT (Smart RAG)
        # Instead of waiting for tool use, we proactively fetch relevant context
        context_str = ""
        results: List[Dict[str, Any]] = []
        await emit_progress("memory_search_started", "started")
        try:
            async with AsyncSessionLocal() as db:
                results = await retrieval_service.search_memories(
                    query=message,
                    user_id=user_id,
                    db=db,
                    top_k=3,
                    project_id=project_id
                )
                if results:
                    # Use Memwyre Context Builder
                    formatted_ctx_str = self._build_memwyre_context(results)
                    context_str = formatted_ctx_str
            await emit_progress("memory_search_completed", "completed", {"result_count": len(results)})
        except Exception as e:
            logger.error(f"Context pre-fetch failed: {e}")
            await emit_progress("memory_search_completed", "failed", {"result_count": 0, "error": str(e)})

        # ---------------------------------------------------------
        # 5.2 SIDE-CAR FACT EXTRACTION (DEFERRED TO BACKGROUND)
        # Moved to Celery worker to reduce response latency.
        # The task is dispatched AFTER the agent responds (see below).
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        # 5.2 SIDE-CAR FACT EXTRACTION (DEFERRED TO BACKGROUND)
        # Moved to Celery worker to reduce response latency.
        # The task is dispatched AFTER the agent responds (see below).
        # ---------------------------------------------------------

        # Define System Instruction (Memwyre Prompt Logic)
        question_date_str = datetime.now().strftime('%Y-%m-%d')
        
        instruction = f"""You are a question-answering system. Based on the retrieved context below, answer the question.

Question: {message}
Question Date: {question_date_str}

Retrieved Context:
{context_str}

**Understanding the Context:**
The context has two sections:

1. **ENTITY PROFILES** (if present): High-level structured summaries of known people, places, or things. These profiles contain aggregated knowledge (demographics, hobbies, relationships, career info, etc.) about each entity. Use profiles to get a broad overview of an entity and to cross-reference details that individual facts may not cover alone.

2. **RETRIEVED FACTS & MEMORIES**: Granular search results with specific dates and details. Each result has:
   - **Content**: The text content found in relevant documents or memories.
   - **Dates & Timing**:
   - **Event Date**: This is the **PRE-RESOLVED Absolute Date** of the event (derived from 'valid_from').
     * **Start Date Rule**: If the text suggests a duration (e.g. "last week", "camping trip", "picnic week"), treat this date as the **START** of that period.
     * **Timezone Tolerance**: Stored dates are in UTC. If your calculated answer seems off by 1 day (e.g. June 1st vs June 2nd), acknowledge that the event likely occurred **around** this date or **starting** this week.
     * **Trust the System**: Do NOT try to re-calculate "last week" from the current date. The system has done it for you and put it here.
   - **Valid Until**: The **End Date** of the event.
   - **Range**: If 'Valid Until' is present, the event covers the [Event Date, Valid Until] range. Use this range in your answer.

**How to Answer:**
1. **Analyze Temporal Context**:
   - Does the text refer to a "Day" (e.g. "On Friday") or a "Period" (e.g. "last week")?
2. **Formulate Date**:
   - **For Periods**: Answer with "The week of [Event Date]" or "Starting [Event Date]". Avoid asserting strictly "On [Event Date]" if the event is a week long.
   - **For Specific Days**: Use the Event Date.
3. **Address Mismatches**:
   - If the Question expects a range ("When did she...") and facts are broad, use a Range.
   - **Missing by a Day**: If the date falls on a boundary (e.g. 1st vs 30th), be inclusive. "The week before X" often implies the week *ending* on X or *starting* 7 days prior. If your date is June 1st and target is June 9th, "Week of June 1st" is the right answer.
4. **Multi-Hop Reasoning (CRITICAL)**:
   - If the question asks about a relationship that requires bridging multiple facts (e.g., "Where does the person who owns a dog work?"), you MUST trace the entities step-by-step.
   - Fact 1: [Person] owns [Dog]. Fact 2: [Person] works at [Company].
   - Combine these facts to form a single coherent answer. Do not get confused by irrelevant facts.

Instructions:
- First, think through the problem step by step. Show your reasoning process.
- **Explicitly cite the dates** found.
- **Trace entities carefully** for multi-hop questions.
- **Prioritize Ranges/Periods** over single dates for broad events.
- When answering "when" questions, if specific date references (e.g., "The week before 9 June 2023", "The Friday before 15 July 2023") are found in the context, return them directly along with the date in the answer.
- If you find references like "last week" or "two weekends ago" while resolving temporal context, return them as "week before ${{questionDate || "the conversation date"}}" or "2 weekends before ${{questionDate || "the conversation date"}}".
- Base your answer ONLY on the provided context.

**Response Format (strict):**
- Output ONLY Markdown.
- Start with an optional reasoning block only if needed, using STRICT tags:
  <think>
  your reasoning
  </think>
- After reasoning, provide the final answer directly. Do not prefix with "Answer:".
- Keep output concise and scannable: short paragraphs and optional brief bullets.
- Do not repeat headings, separators, or boilerplate preambles.

ADDITIONAL AGENT INSTRUCTIONS:
1. This is your primary directive for answering based on the provided context.
2. Facts are extracted automatically by the system. You do NOT need to call tools to save facts.
3. If context is insufficient, you CAN call 'search_memory', but prefer the provided Retrieved Context."""

        instruction_msg = SystemMessage(content=instruction)
        
        # history_messages already includes the current user message (added at L245)
        input_messages = [instruction_msg] + history_messages
        
        try:
            await emit_progress("llm_generation_started", "started", {"model": model})
            # invoke returns a dict with keys like 'messages' (list of BaseMessage)
            result = await app.ainvoke({"messages": input_messages})
            
            # Extract final response from the last AI message
            messages_out = result.get("messages", [])
            output = ""
            if messages_out and isinstance(messages_out[-1], AIMessage):
                output = messages_out[-1].content
            else:
                output = "No response generated."
            output = self._normalize_agent_output(output)
            await emit_progress("llm_generation_completed", "completed", {"model": model})

            # Extract Sources from tool executions in message history
            sources = []
            # We scan messages for ToolMessage or AIMessage with tool_calls
            # But our specific source logic relied on "observation" strings from "search_memory"
            # In LangGraph, tool outputs are ToolMessages.
            from langchain_core.messages import ToolMessage
            
            # No logic needed for tool messages since we use SideCar/PreFetch mostly.
            # But keeping it just in case:
            for msg in messages_out:
                if isinstance(msg, ToolMessage) and msg.name == "search_memory":
                     # Legacy parsing - minimal validation needed as we prefer PreFetch logic
                     pass

            # Fix: Add Pre-Fetched Context items to Sources
            # Since we now inject context in System Prompt, the tool is often not called.
            # We must report these "implicit" sources to the UI.
            # Reuse 'results' from earlier scope (L327) if available
            if results:
                from app.schemas.document import Chunk as ChunkSchema
                for res in results:
                    meta = res["metadata"]
                    
                    # USER REQ: No Facts in Context List
                    if meta.get("type") == "fact":
                        continue

                    doc_id = "unknown"
                    if meta.get("memory_id"): doc_id = meta.get("memory_id")
                    elif meta.get("document_id"): doc_id = meta.get("document_id")
                    
                    title = meta.get("title", "Untitled")

                    # Construct Rich Source Object expected by Frontend
                    # { "title": str, "id": str, "content": str, "metadata": dict, "chunk": dict }
                    
                    chunk_data = None
                    if res.get("chunk"):
                        try:
                            # Use Pydantic Schema to serialize SQL Model
                            chunk_model = ChunkSchema.model_validate(res["chunk"])
                            chunk_data = chunk_model.model_dump()
                        except Exception as e:
                            # logger.warning(f"Chunk serialization failed: {e}")
                            pass
                            
                    source_obj = {
                        "title": title,
                        "id": str(doc_id),
                        "content": res["text"],
                        "metadata": meta,
                        "chunk": chunk_data
                    }

                    # Dedupe (ID or Title)
                    exists = False
                    for s in sources:
                        # Match by ID if valid
                        if doc_id != "unknown" and s.get("id") == str(doc_id):
                            exists = True
                            break
                        # Match by Title if same (and ID might be unknown or match)
                        if s.get("title") == title:
                            exists = True
                            break
                    
                    if not exists:
                        sources.append(source_obj)

            await emit_progress("sources_attached", "completed", {"source_count": len(sources)})

            # Save AI Response and get ID
            ai_message_id = await chat_history.add_message(AIMessage(content=output), sources=sources)
            await emit_progress("response_saved", "completed", {"message_id": ai_message_id})
            
            # ---------------------------------------------------------
            # DEFERRED FACT EXTRACTION: Dispatch to Celery worker
            # This runs in the background AFTER the response is ready
            # ---------------------------------------------------------
            try:
                from app.worker_router import extract_chat_facts_task
                extract_chat_facts_task.delay(message, user_id, project_id=project_id)
                logger.info(f"Dispatched fact extraction task for user {user_id} with project_id {project_id}")
            except Exception as e:
                # Non-critical: log and continue
                logger.warning(f"Failed to dispatch fact extraction task: {e}")
            # ---------------------------------------------------------
            
            return {
                "output": output,
                "sources": sources,
                "message_id": ai_message_id,
                "turn_status": "completed"
            }
            
        except Exception as e:
            logger.error(f"Agent failed: {e}")
            await emit_progress("llm_generation_completed", "failed", {"model": model, "error": str(e)})
            return {
                "output": "I'm sorry, I encountered an error while thinking.",
                "sources": [],
                "message_id": 0,
                "turn_status": "failed",
                "error": str(e)
            }

agent_service = AgentService()
