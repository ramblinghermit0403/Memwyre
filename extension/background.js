// Background script for context menus and other background tasks
chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
        id: "saveToVault",
        title: "Save selection to Brain Vault",
        contexts: ["selection"]
    });
});

chrome.contextMenus.onClicked.addListener(async (info, tab) => {
    if (info.menuItemId === "saveToVault") {
        const text = info.selectionText;
        const { token } = await chrome.storage.local.get('token');

        if (!token) {
            console.error("Not logged in");
            return;
        }

        const API_URL = 'http://localhost:8000/api/v1';
        const blob = new Blob([text], { type: 'text/plain' });
        const formData = new FormData();
        formData.append('file', blob, `Selection from ${tab.title}.txt`);

        try {
            await fetch(`${API_URL}/documents/upload`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`
                },
                body: formData
            });
            console.log("Saved to vault");
        } catch (error) {
            console.error("Failed to save", error);
        }
    }
});
