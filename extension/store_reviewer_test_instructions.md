# Store Reviewer Test Instructions (Chrome + Edge)

Use this exact text in your store submission **Test instructions** field (replace placeholders):

1. Install the extension and pin it to the toolbar.
2. Click the extension icon. The MemWyre side panel opens.
3. In the side panel, click **Login**. This opens: `https://memwyre.tech/login?source=extension`.
4. Sign in with this reviewer test account:
   - Email: `{{REVIEWER_TEST_EMAIL}}`
   - Password: `{{REVIEWER_TEST_PASSWORD}}`
5. After successful login, return to the previous tab and open the extension side panel again. You should see tabs: **Inbox, Timeline, Search, Save**.
6. Go to **Save** tab:
   - Title: `Reviewer Test Memory`
   - Content: `This is a reviewer test memory from extension.`
   - Click **Save Memory**
   - Expected: success toast/status appears.
7. Go to **Search** tab:
   - Query: `reviewer test memory`
   - Click search icon
   - Expected: saved memory appears in results.
8. Go to **Inbox** tab:
   - Click **Refresh**
   - Expected: list renders (or shows empty-state message cleanly if no pending items).
9. Go to **Timeline** tab:
   - Click **Refresh**
   - Expected: timeline list renders; source filter dropdown works.
10. Test context menu permission:
   - Open any normal webpage.
   - Right-click page and click **Save Page to MemWyre**.
   - Expected: extension badge briefly shows success (`OK`) and page is ingested.
11. Test logout:
   - Open extension settings (gear icon) -> **Logout**.
   - Expected: extension returns to Login view.
12. Optional supported-site verification:
   - Visit one supported AI site (`chatgpt.com`, `claude.ai`, `gemini.google.com/app`, or `perplexity.ai`).
   - Expected: MemWyre action UI appears for saving prompt/response content.

## Test Coverage Checklist
- Auth handoff from web app to extension token storage.
- Side panel UI and tab navigation.
- Memory save + memory search end-to-end API path.
- Inbox/Timeline retrieval.
- Context menu (`contextMenus`, `activeTab`) behavior.
- Session clear/logout behavior.

## Assumptions
- Submission build uses production endpoints (`memwyre.tech` / `server.memwyre.tech`).
- Provided reviewer account is email-verified and has required access level for save/search features.
- Same instructions are used for both Chrome and Edge (behavior is identical for this extension).
