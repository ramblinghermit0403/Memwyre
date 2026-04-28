# MemWyre Extension Publishing Checklist

Follow these steps precisely to submit your extension to the Chrome Web Store.

### 1. Pre-Publishing Setup
- [ ] Read and approve the `PrivacyPolicy.md` draft. Host it publicly (e.g., on a GitHub Gist, your personal site, or as a public page on your app website) so you can get a link to it.
- [ ] Review the `manifest.json` for production-only host permissions.
- [ ] Create your Promotional Images:
  - **Store Icon:** You already have `icon128.png` (Good!).
  - **Screenshots:** Take 1-5 screenshots of the extension working (Must be `1280x800` or `640x400`).
  - **Promo Tile (Optional but recommended):** A `440x280` image for the Web Store.

### 2. Prepare the ZIP file
- Once the AI finishes updating `manifest.json`, navigate to `c:\Users\himan\OneDrive\Documents\brain_vault\extension`.
- Select **all the files** *inside* this folder.
- Right-click, select **Compress to ZIP file** (name it `memwyre-v1.0.zip`).
*(Do not zip the outer `extension` folder itself, zip the contents)*

### 3. Chrome Web Store Developer Dashboard
1. Go to the [Developer Dashboard](https://chrome.google.com/webstore/devconsole/).
2. Pay the one-time $5 developer registration fee if this is your first time.
3. Click the **+ New Item** button and upload your `memwyre-v1.0.zip` file.

### 4. Store Listing Details
1. **Title:** MemWyre
2. **Summary:** (Will be pulled from manifest.json).
3. **Description:** Write a full description of the features.
4. **Category:** Productivity (or Tools).
5. **Language:** English.
6. Upload your `icon128.png` and your Screenshots.

### 5. Privacy Tab (Crucial!)
1. **Single Purpose:** "MemWyre connects users browsing and AI chats to their personal Brain Vault knowledge base."
2. **Permissions Justification:**
   - **`activeTab`:** Needed to extract the current AI chat context or page content to save as a memory in the Brain Vault.
   - **`storage`:** Needed to save the user's authentication token across sessions.
3. **Data Usage:**
   - Check the boxes indicating you collect "Website content" and "Authentication info".
   - Certify that you **do not** use this data for restricted purposes (no selling data, no unrelated use).
4. **Privacy Policy URL:** Paste the public link where you hosted the contents of `PrivacyPolicy.md`.

### 6. Submit
- Once all red asterisks are filled in both tabs, click **Submit for Review**.
- Wait 1-3 days for approval!

### 7. Reviewer Test Instructions (Chrome + Edge)
- Use the copy-ready instructions from: `store_reviewer_test_instructions.md`
- Replace placeholders before submission:
  - `{{REVIEWER_TEST_EMAIL}}`
  - `{{REVIEWER_TEST_PASSWORD}}`
