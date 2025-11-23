document.addEventListener('DOMContentLoaded', async () => {
    const loginView = document.getElementById('login-view');
    const mainView = document.getElementById('main-view');
    const tokenInput = document.getElementById('token-input');
    const saveTokenBtn = document.getElementById('save-token');
    const queryInput = document.getElementById('query-input');
    const generateBtn = document.getElementById('generate-btn');
    const resultDiv = document.getElementById('result');
    const copyBtn = document.getElementById('copy-btn');
    const logoutBtn = document.getElementById('logout-btn');

    // Check auth
    const { token } = await chrome.storage.local.get('token');
    if (token) {
        showMain();
    } else {
        showLogin();
    }

    // Save Token
    saveTokenBtn.addEventListener('click', async () => {
        const token = tokenInput.value.trim();
        if (token) {
            await chrome.storage.local.set({ token });
            showMain();
        }
    });

    // Logout
    logoutBtn.addEventListener('click', async () => {
        await chrome.storage.local.remove('token');
        showLogin();
    });

    // Generate Prompt
    generateBtn.addEventListener('click', async () => {
        const query = queryInput.value.trim();
        if (!query) return;

        generateBtn.textContent = 'Generating...';
        generateBtn.disabled = true;
        resultDiv.classList.add('hidden');
        copyBtn.classList.add('hidden');

        try {
            const response = await chrome.runtime.sendMessage({
                action: 'generatePrompt',
                data: { query }
            });

            if (response.success) {
                resultDiv.textContent = response.data.prompt;
                resultDiv.classList.remove('hidden');
                copyBtn.classList.remove('hidden');
            } else {
                resultDiv.textContent = 'Error: ' + response.error;
                resultDiv.classList.remove('hidden');
            }
        } catch (err) {
            resultDiv.textContent = 'Error: ' + err.message;
            resultDiv.classList.remove('hidden');
        } finally {
            generateBtn.textContent = 'Generate Prompt';
            generateBtn.disabled = false;
        }
    });

    // Copy
    copyBtn.addEventListener('click', () => {
        navigator.clipboard.writeText(resultDiv.textContent);
        copyBtn.textContent = 'Copied!';
        setTimeout(() => copyBtn.textContent = 'Copy to Clipboard', 2000);
    });

    function showLogin() {
        loginView.classList.remove('hidden');
        mainView.classList.add('hidden');
    }

    function showMain() {
        loginView.classList.add('hidden');
        mainView.classList.remove('hidden');
    }
});
