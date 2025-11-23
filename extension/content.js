// Content script for Brain Vault Extension

console.log('Brain Vault Extension loaded');

// Listen for messages
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'injectPrompt') {
        injectText(request.text);
        sendResponse({ success: true });
    }
});

function injectText(text) {
    // Try to find the active element or common LLM input selectors
    const activeElement = document.activeElement;

    if (activeElement && (activeElement.tagName === 'TEXTAREA' || activeElement.getAttribute('contenteditable') === 'true')) {
        // Standard textarea or contenteditable
        if (activeElement.tagName === 'TEXTAREA') {
            activeElement.value += text;
            activeElement.dispatchEvent(new Event('input', { bubbles: true }));
        } else {
            activeElement.textContent += text;
            activeElement.dispatchEvent(new Event('input', { bubbles: true }));
        }
    } else {
        // Fallback: Copy to clipboard
        navigator.clipboard.writeText(text).then(() => {
            alert('Brain Vault: Prompt copied to clipboard (could not find input box).');
        });
    }
}
