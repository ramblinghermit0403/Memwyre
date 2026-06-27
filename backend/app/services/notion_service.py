import httpx
import re
from datetime import datetime
from sqlalchemy import select
from app.db.session import AsyncSessionLocal
from app.models.document import Document
from app.models.workspace_connection import WorkspaceConnection
from app.worker import ingest_memory_task

class NotionService:
    def extract_rich_text(self, rich_text_list: list) -> str:
        if not rich_text_list:
            return ""
        return "".join(t.get("plain_text", "") for t in rich_text_list)

    def block_to_markdown(self, block: dict) -> str:
        b_type = block.get("type")
        if not b_type:
            return ""
            
        data = block.get(b_type, {})
        rich_text = data.get("rich_text", [])
        text = self.extract_rich_text(rich_text)
        
        if b_type == "paragraph":
            return text + "\n\n"
        elif b_type == "heading_1":
            return f"# {text}\n\n"
        elif b_type == "heading_2":
            return f"## {text}\n\n"
        elif b_type == "heading_3":
            return f"### {text}\n\n"
        elif b_type == "bulleted_list_item":
            return f"* {text}\n"
        elif b_type == "numbered_list_item":
            return f"1. {text}\n"
        elif b_type == "to_do":
            checked = data.get("checked", False)
            checkbox = "[x]" if checked else "[ ]"
            return f"{checkbox} {text}\n"
        elif b_type == "code":
            lang = data.get("language", "text")
            return f"```{lang}\n{text}\n```\n\n"
        elif b_type == "quote":
            return f"> {text}\n\n"
        elif b_type == "divider":
            return "---\n\n"
        return ""

    async def get_page_content(self, page_id: str, access_token: str) -> str:
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Notion-Version": "2022-06-28"
        }
        
        url = f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=100"
        markdown_content = ""
        
        async with httpx.AsyncClient() as client:
            try:
                has_more = True
                start_cursor = None
                
                while has_more:
                    req_url = url
                    if start_cursor:
                        req_url += f"&start_cursor={start_cursor}"
                        
                    resp = await client.get(req_url, headers=headers)
                    resp.raise_for_status()
                    res_data = resp.json()
                    
                    for block in res_data.get("results", []):
                        markdown_content += self.block_to_markdown(block)
                        
                    has_more = res_data.get("has_more", False)
                    start_cursor = res_data.get("next_cursor")
            except Exception as e:
                print(f"Error fetching blocks for page {page_id}: {e}")
                
        return markdown_content

    async def sync_notion(self, user_id: int, project_id: int, access_token: str):
        print(f"Starting Notion sync for user {user_id}")
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Notion-Version": "2022-06-28"
        }
        
        search_url = "https://api.notion.com/v1/search"
        search_body = {
            "filter": {
                "value": "page",
                "property": "object"
            },
            "page_size": 100
        }
        
        pages = []
        async with httpx.AsyncClient() as client:
            try:
                resp = await client.post(search_url, json=search_body, headers=headers)
                resp.raise_for_status()
                data = resp.json()
                pages = data.get("results", [])
            except Exception as e:
                print(f"Notion search failed: {e}")
                return

        print(f"Found {len(pages)} pages in Notion for user {user_id}")
        
        for page in pages:
            page_id = page.get("id")
            properties = page.get("properties", {})
            title = "Untitled Notion Page"
            
            for prop_name, prop_val in properties.items():
                if prop_val.get("type") == "title":
                    title_list = prop_val.get("title", [])
                    title = self.extract_rich_text(title_list) or "Untitled Notion Page"
                    break
            
            content = await self.get_page_content(page_id, access_token)
            
            if not content.strip():
                print(f"Skipping empty page: {title} ({page_id})")
                continue
                
            notion_url = page.get("url") or f"https://notion.so/{page_id.replace('-', '')}"
            
            async with AsyncSessionLocal() as db:
                stmt = select(Document).where(
                    Document.user_id == user_id,
                    Document.source == notion_url
                )
                result = await db.execute(stmt)
                doc = result.scalars().first()
                
                if doc:
                    doc.title = title
                    doc.content = content
                    doc.updated_at = datetime.utcnow()
                    mode = "replace"
                else:
                    doc = Document(
                        user_id=user_id,
                        project_id=project_id,
                        title=title,
                        content=content,
                        source=notion_url,
                        file_type="md",
                        doc_type="file",
                        tags=["notion", "sync"]
                    )
                    db.add(doc)
                    mode = "append"
                    
                await db.commit()
                await db.refresh(doc)
                
            ingest_memory_task.delay(
                memory_id=doc.id,
                user_id=user_id,
                content=content,
                title=title,
                tags=["notion", "sync"],
                source=notion_url,
                doc_type="file",
                mode=mode
            )
            print(f"Queued ingestion for Notion page: {title}")

        async with AsyncSessionLocal() as db:
            stmt = select(WorkspaceConnection).where(
                WorkspaceConnection.user_id == user_id,
                WorkspaceConnection.service == "notion"
            )
            result = await db.execute(stmt)
            conn = result.scalars().first()
            if conn:
                conn.last_synced_at = datetime.utcnow()
                await db.commit()
                
        print(f"Notion sync completed for user {user_id}")

notion_service = NotionService()
