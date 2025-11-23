// Background script for Brain Vault Extension

const API_BASE_URL = 'http://localhost:8000/api/v1';

// Listen for messages from popup or content script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'generatePrompt') {
        generatePrompt(request.data)
            .then(response => sendResponse({ success: true, data: response }))
            .catch(error => sendResponse({ success: false, error: error.message }));
        return true; // Will respond asynchronously
    }
});

async function generatePrompt(data) {
    // 1. Get Token from Storage
    const { token } = await chrome.storage.local.get('token');
    if (!token) {
        throw new Error('Not authenticated. Please login via the popup.');
    }

    // 2. Call Backend API
    const response = await fetch(`${API_BASE_URL}/prompts/generate`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
            query: data.query,
            template_id: data.templateId || 'standard',
            context_size: 2000
        })
    });

    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to generate prompt');
    }

    return await response.json();
}
