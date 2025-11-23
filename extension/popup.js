const API_URL = 'http://localhost:8000/api/v1';

document.addEventListener('DOMContentLoaded', async () => {
    const loginSection = document.getElementById('login-section');
    const mainSection = document.getElementById('main-section');
    const statusDiv = document.getElementById('status');

    // Check if logged in
    const { token } = await chrome.storage.local.get('token');

    if (token) {
        showMain();
    } else {
        showLogin();
    }

    document.getElementById('login-btn').addEventListener('click', async () => {
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        try {
            statusDiv.textContent = 'Logging in...';
            const response = await fetch(`${API_URL}/auth/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: new URLSearchParams({ username: email, password })
            });

            if (!response.ok) throw new Error('Login failed');

            const data = await response.json();
            await chrome.storage.local.set({ token: data.access_token });
            statusDiv.textContent = '';
            showMain();
        } catch (error) {
            statusDiv.textContent = error.message;
        }
    });

    document.getElementById('logout-btn').addEventListener('click', async () => {
        await chrome.storage.local.remove('token');
        showLogin();
    });

    document.getElementById('clip-selection').addEventListener('click', async () => {
        clipContent('selection');
    });

    document.getElementById('clip-page').addEventListener('click', async () => {
        clipContent('page');
    });

    function showLogin() {
        loginSection.classList.remove('hidden');
        mainSection.classList.add('hidden');
    }

    function showMain() {
        loginSection.classList.add('hidden');
        mainSection.classList.remove('hidden');
    }

    async function clipContent(type) {
        statusDiv.textContent = 'Clipping...';
        const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

        try {
            const response = await chrome.tabs.sendMessage(tab.id, { action: 'getContent', type });

            if (!response || !response.content) {
                throw new Error('No content found');
            }

            const { token } = await chrome.storage.local.get('token');

            // Create a text file blob to upload
            const blob = new Blob([response.content], { type: 'text/plain' });
            const formData = new FormData();
            formData.append('file', blob, `${response.title}.txt`);

            const uploadRes = await fetch(`${API_URL}/documents/upload`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`
                },
                body: formData
            });

            if (!uploadRes.ok) throw new Error('Upload failed');

            statusDiv.textContent = 'Saved to Vault!';
            setTimeout(() => statusDiv.textContent = '', 2000);
        } catch (error) {
            statusDiv.textContent = 'Error: ' + error.message;
        }
    }
});
