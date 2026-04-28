// Content script for Memwyre Extension
// Self-contained with all adapters bundled (no ES modules in content scripts)

console.log('Memwyre Extension loaded');

// ============================================================================
// BASE UTILITIES
// ============================================================================

/**
 * Shows a floating tooltip near a button
 */
function showFloatingFeedback(btn, message, type = 'info') {
    const existing = document.getElementById('memwyre-tooltip-' + btn.dataset.mwId);
    if (existing) existing.remove();

    if (!btn.dataset.mwId) btn.dataset.mwId = Math.random().toString(36).substr(2, 9);

    const tooltip = document.createElement('div');
    tooltip.id = 'memwyre-tooltip-' + btn.dataset.mwId;
    tooltip.textContent = message;

    let bg = 'rgba(0, 0, 0, 0.8)';
    let color = '#fff';
    if (type === 'error') bg = 'rgba(220, 53, 69, 0.9)';
    if (type === 'success') bg = 'rgba(25, 135, 84, 0.9)';

    tooltip.style.cssText = `
        position: absolute;
        background: ${bg};
        color: ${color};
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        pointer-events: none;
        z-index: 10001;
        opacity: 0;
        transition: opacity 0.2s ease, transform 0.2s ease;
        white-space: nowrap;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    `;

    document.body.appendChild(tooltip);

    const rect = btn.getBoundingClientRect();
    const scrollX = window.scrollX;
    const scrollY = window.scrollY;
    const tipWidth = tooltip.offsetWidth;
    const top = rect.top + scrollY - 30;
    const left = rect.left + scrollX + (rect.width / 2) - (tipWidth / 2);

    tooltip.style.top = `${top}px`;
    tooltip.style.left = `${left}px`;

    requestAnimationFrame(() => {
        tooltip.style.opacity = '1';
        tooltip.style.transform = 'translateY(-5px)';
    });

    setTimeout(() => {
        tooltip.style.opacity = '0';
        tooltip.style.transform = 'translateY(0)';
        setTimeout(() => tooltip.remove(), 200);
    }, 3000);
}

function createSpinner() {
    const spinner = document.createElement('div');
    spinner.style.cssText = `
        width: 14px; height: 14px;
        border: 2px solid rgba(100,100,100,0.3);
        border-top: 2px solid #007bff;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    `;
    return spinner;
}

function createCheckmark() {
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("fill", "none");
    svg.setAttribute("stroke", "#666666");
    svg.setAttribute("stroke-width", "3");
    svg.setAttribute("stroke-linecap", "round");
    svg.setAttribute("stroke-linejoin", "round");
    svg.style.width = "20px";
    svg.style.height = "20px";
    const polyline = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
    polyline.setAttribute("points", "20 6 9 17 4 12");
    svg.appendChild(polyline);
    return svg;
}

function createErrorIcon() {
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("fill", "none");
    svg.setAttribute("stroke", "#666666");
    svg.setAttribute("stroke-width", "3");
    svg.setAttribute("stroke-linecap", "round");
    svg.setAttribute("stroke-linejoin", "round");
    svg.style.width = "20px";
    svg.style.height = "20px";
    const line1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
    line1.setAttribute("x1", "18"); line1.setAttribute("y1", "6");
    line1.setAttribute("x2", "6"); line1.setAttribute("y2", "18");
    const line2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
    line2.setAttribute("x1", "6"); line2.setAttribute("y1", "6");
    line2.setAttribute("x2", "18"); line2.setAttribute("y2", "18");
    svg.appendChild(line1);
    svg.appendChild(line2);
    return svg;
}

function getLogoUrl() {
    return chrome.runtime.getURL('logo.png');
}

function createLogoImage(options = {}) {
    const { width = '16px', height = '16px', opacity = '0.9', filter = '' } = options;
    const img = document.createElement('img');
    img.src = getLogoUrl();
    img.style.width = width;
    img.style.height = height;
    img.style.display = 'block';
    img.style.opacity = opacity;
    if (filter) img.style.filter = filter;
    return img;
}

function queryWithFallback(selectors) {
    for (const selector of selectors) {
        try {
            const element = document.querySelector(selector);
            if (element) return element;
        } catch (e) {
            console.warn(`Memwyre: Invalid selector "${selector}"`, e);
        }
    }
    return null;
}

function queryAllWithFallback(selectors) {
    for (const selector of selectors) {
        try {
            const elements = document.querySelectorAll(selector);
            if (elements.length > 0) return Array.from(elements);
        } catch (e) {
            console.warn(`Memwyre: Invalid selector "${selector}"`, e);
        }
    }
    return [];
}

function buildSystemPrompt() {
    return `[SYSTEM: The following context is retrieved from the user's Brain Vault. Use it to answer the request if relevant.

**Understanding the Context:**
The context contains search results from a memory system. Each result has multiple components.

**How to Answer:**
- First, think through the problem step by step.
- **Explicitly cite the dates** found.
- **Prioritize Ranges/Periods** over single dates for broad events.
- Base your answer ONLY on the provided context.

**Response Format:** Think step by step, then provide your answer.]`;
}

function createSaveButton(contentGetter, source) {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'brain-vault-save-btn';
    btn.appendChild(createLogoImage({ width: '16px', height: '16px' }));
    btn.title = 'Save to Memwyre';
    btn.style.cssText = `
        display: inline-flex; align-items: center; justify-content: center;
        width: 32px; height: 32px; background-color: transparent; color: #333;
        border: none; border-radius: 6px; cursor: pointer; opacity: 0.9;
        transition: all 0.2s ease; margin-right: 4px;
    `;

    btn.onmouseover = () => {
        btn.style.opacity = '1';
        btn.style.backgroundColor = 'rgba(128,128,128,0.15)';
    };
    btn.onmouseout = () => {
        btn.style.opacity = '0.9';
        btn.style.backgroundColor = 'transparent';
    };

    btn.onclick = async (e) => {
        e.stopPropagation();
        const originalIcon = btn.querySelector('img')?.cloneNode(true);
        btn.replaceChildren(createSpinner());
        btn.disabled = true;
        btn.style.cursor = 'default';

        try {
            let response;
            if (source === 'youtube') {
                response = await chrome.runtime.sendMessage({
                    action: 'ingestYouTube',
                    data: { url: window.location.href }
                });
            } else {
                const content = typeof contentGetter === 'function'
                    ? await Promise.resolve(contentGetter())
                    : contentGetter;
                response = await chrome.runtime.sendMessage({
                    action: 'saveLLMMemory',
                    data: { content, source, model: 'unknown', url: window.location.href }
                });
            }

            if (response.success) {
                btn.replaceChildren(createCheckmark());
                showFloatingFeedback(btn, 'Saved to Memwyre!', 'success');
                setTimeout(() => {
                    if (!btn.isConnected) return;
                    btn.replaceChildren(originalIcon || createLogoImage({ width: '16px', height: '16px' }));
                    btn.disabled = false;
                    btn.style.cursor = 'pointer';
                }, 2000);
            } else {
                throw new Error(response.error || 'Failed to save');
            }
        } catch (err) {
            console.error('Memwyre save error:', err);
            btn.replaceChildren(createErrorIcon());
            showFloatingFeedback(btn, 'Error: ' + err.message, 'error');
            setTimeout(() => {
                if (!btn.isConnected) return;
                btn.replaceChildren(createLogoImage({ width: '16px', height: '16px' }));
                btn.disabled = false;
                btn.style.cursor = 'pointer';
            }, 3000);
        }
    };

    return btn;
}

function createInjectButton(getInputAreaFn) {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'brain-vault-inject-btn';
    btn.appendChild(createLogoImage({ width: '20px', height: '20px' }));
    btn.title = 'Insert Context from Memwyre';
    btn.style.cssText = `
        display: flex; align-items: center; justify-content: center;
        width: 32px; height: 32px; border-radius: 50%; background-color: transparent;
        border: none; cursor: pointer; z-index: 1000; transition: all 0.2s ease; opacity: 0.9;
    `;

    btn.onmouseover = () => {
        btn.style.backgroundColor = 'rgba(128,128,128,0.1)';
        btn.style.transform = 'scale(1.05)';
        btn.style.opacity = '1';
    };
    btn.onmouseout = () => {
        btn.style.backgroundColor = 'transparent';
        btn.style.transform = 'scale(1)';
        btn.style.opacity = '0.9';
    };

    btn.onclick = async () => {
        btn.replaceChildren(createSpinner());

        try {
            const inputArea = typeof getInputAreaFn === 'function' ? getInputAreaFn() : getInputAreaFn;
            let query = '';
            if (inputArea) {
                query = inputArea.tagName === 'TEXTAREA' ? inputArea.value : inputArea.innerText;
            }

            if (!query || query.trim().length < 2) {
                showFloatingFeedback(btn, 'Please type a query first', 'error');
                btn.replaceChildren(createLogoImage({ width: '20px', height: '20px' }));
                return;
            }

            const response = await chrome.runtime.sendMessage({
                action: 'searchMemory',
                data: { query }
            });

            if (response?.success && response.data?.length > 0) {
                const jsonContent = JSON.stringify(response.data, null, 2);
                const fullInjection = `\n\n${buildSystemPrompt()}\n\n${jsonContent}\n\n[END CONTEXT]\n\n`;

                if (inputArea.tagName === 'TEXTAREA') {
                    const start = inputArea.selectionStart || inputArea.value.length;
                    const end = inputArea.selectionEnd || inputArea.value.length;
                    inputArea.value = inputArea.value.substring(0, start) + fullInjection + inputArea.value.substring(end);
                } else {
                    inputArea.textContent += fullInjection;
                }
                inputArea.dispatchEvent(new Event('input', { bubbles: true }));

                btn.replaceChildren(createCheckmark());
                showFloatingFeedback(btn, 'Context Injected!', 'success');
            } else {
                btn.textContent = '⚠️';
                if (response?.error?.includes('Not authenticated')) {
                    showFloatingFeedback(btn, 'Please Login to Memwyre', 'error');
                } else if (response?.error?.includes('free tier is currently disabled')) {
                    showFloatingFeedback(btn, 'Free tier disabled. Upgrade to Pro.', 'error');
                } else if (response?.error) {
                    showFloatingFeedback(btn, 'Error: ' + response.error, 'error');
                } else {
                    showFloatingFeedback(btn, 'No relevant memories found', 'info');
                }
            }

            setTimeout(() => {
                btn.replaceChildren(createLogoImage({ width: '20px', height: '20px' }));
            }, 2000);

        } catch (err) {
            console.error('Memwyre injection error:', err);
            btn.replaceChildren(createErrorIcon());
            showFloatingFeedback(btn, 'Error: ' + err.message, 'error');
            setTimeout(() => {
                btn.replaceChildren(createLogoImage({ width: '20px', height: '20px' }));
            }, 2000);
        }
    };

    return btn;
}

// ============================================================================
// SITE ADAPTERS - Loaded from separate config files at runtime
// ============================================================================

const ADAPTERS = {
    chatgpt: {
        name: 'chatgpt',
        match: (host) => host === 'chatgpt.com' || host === 'www.chatgpt.com',
        selectors: {
            assistantMessage: [
                'div[data-message-author-role="assistant"]',
                'article[data-role="assistant"]',
                '[data-testid*="conversation-turn-assistant"]'
            ],
            messageToolbar: [
                '.flex.flex-wrap.items-center.gap-y-4',
                '[class*="message-actions"]'
            ],
            conversationTurn: [
                'div.group\\/conversation-turn',
                '[data-testid*="conversation-turn"]'
            ],
            inputArea: [
                '#prompt-textarea',
                'textarea[data-id="root"]',
                'div[contenteditable="true"][role="textbox"]'
            ],
            inputActions: [
                'div[class*="[grid-area:trailing]"]',
                '.flex.items-center.gap-2'
            ]
        },
        async injectSaveButtons() {
            const messages = queryAllWithFallback(this.selectors.assistantMessage);
            for (const msg of messages) {
                let row = null;
                for (const sel of this.selectors.conversationTurn) {
                    row = msg.closest(sel);
                    if (row) break;
                }
                if (!row) row = msg.parentElement?.parentElement;
                if (!row) continue;

                const toolbars = queryAllWithFallback(this.selectors.messageToolbar).filter(bar => row.contains(bar));
                for (const bar of toolbars) {
                    if (bar.querySelector('.brain-vault-save-btn')) continue;
                    requestAnimationFrame(() => bar.appendChild(createSaveButton(() => msg.innerText, this.name)));
                }
            }
        },
        async injectUserPromptSaveButtons() {
            // User turns: find the div.z-0 action bar that appears on hover
            const userTurns = document.querySelectorAll('[data-message-author-role="user"]');
            for (const turn of userTurns) {
                // The text content of the prompt
                const textEl = turn.querySelector('[data-message-id]') || turn;
                // The action button bar beside the user message
                const actionBar = turn.closest('[data-testid*="conversation-turn"]')?.querySelector('.flex.flex-wrap.items-center.gap-y-4') ||
                    turn.parentElement?.querySelector('.flex.flex-wrap.items-center.gap-y-4');
                if (!actionBar || actionBar.querySelector('.brain-vault-save-btn')) continue;

                const btn = createSaveButton(() => turnText, this.name);
                const turnText = turn.innerText || textEl?.innerText || '';
                btn.onclick = async (e) => {
                    e.stopPropagation();
                    const text = turn.innerText;
                    const resp = await chrome.runtime.sendMessage({ action: 'saveMemory', data: { title: 'ChatGPT Prompt', content: text, source: 'chatgpt', interaction_type: 'prompt', tags: ['prompt', 'chatgpt'] } });
                    const originalIcon = btn.querySelector('img')?.cloneNode(true);
                    if (resp?.success) {
                        btn.replaceChildren(createCheckmark());
                        showFloatingFeedback(btn, 'Prompt saved!', 'success');
                    } else {
                        btn.replaceChildren(createErrorIcon());
                        showFloatingFeedback(btn, resp?.error || 'Error', 'error');
                    }
                    setTimeout(() => { if (btn.isConnected) btn.replaceChildren(originalIcon || createLogoImage({ width: '16px', height: '16px' })); }, 2000);
                };
                actionBar.prepend(btn);
            }
        },
        async injectContextButton() {
            const actionContainer = queryWithFallback(this.selectors.inputActions);
            if (!actionContainer || actionContainer.querySelector('.brain-vault-inject-btn')) return;

            const btn = createInjectButton(() => queryWithFallback(this.selectors.inputArea));
            btn.style.cssText = `
                display: flex; align-items: center; justify-content: center;
                width: 32px; height: 32px; border-radius: 50%; background-color: transparent;
                border: none; cursor: pointer; opacity: 0.9; transition: all 0.2s ease;
                margin-right: 4px; color: currentColor;
            `;
            btn.onmouseover = () => { btn.style.backgroundColor = 'rgba(128,128,128,0.15)'; btn.style.opacity = '1'; };
            btn.onmouseout = () => { btn.style.backgroundColor = 'transparent'; btn.style.opacity = '0.9'; };
            actionContainer.prepend(btn);
        }
    },

    claude: {
        name: 'claude',
        match: (host) => host === 'claude.ai' || host === 'www.claude.ai',
        selectors: {
            assistantMessage: [
                '.font-claude-message',
                '[data-testid="assistant-message"]',
                '[class*="claude-message"]'
            ],
            messageToolbar: [
                '.flex.items-center.gap-1',
                '[class*="message-toolbar"]'
            ],
            inputArea: [
                'div[contenteditable="true"][role="textbox"]',
                'div[contenteditable="true"]',
                '.ProseMirror'
            ]
        },
        async injectSaveButtons() {
            // Find all Copy buttons across both User and Assistant messages
            const copyBtns = document.querySelectorAll('button[data-testid="action-bar-copy"], button[aria-label="Copy"]');
            
            for (const copyBtn of copyBtns) {
                // Find the wrapper of the copy button
                const wrapper = copyBtn.closest('.w-fit') || copyBtn;
                // Find the action bar container
                const toolbar = wrapper.parentElement;
                if (!toolbar || toolbar.querySelector('.brain-vault-save-btn') || wrapper.previousElementSibling?.classList.contains('brain-vault-save-btn')) continue;

                // Find the message container to get the text. Claude wraps messages in [data-testid="...-message"] typically.
                const messageWrap = copyBtn.closest('[data-testid="user-message"], [data-testid="assistant-message"]') || 
                                    copyBtn.closest('.group') || 
                                    document.body;

                const textEl = messageWrap.querySelector('.font-claude-message, .font-user-message, .prose') || messageWrap;
                
                const isUser = messageWrap.getAttribute('data-testid') === 'user-message' || !!messageWrap.querySelector('.font-user-message');
                const sourceTitle = isUser ? 'Claude Prompt' : 'Claude Response';
                const interactionType = isUser ? 'prompt' : 'conversation';
                const tag = isUser ? 'prompt' : 'response';

                const btn = createSaveButton(() => textEl?.innerText || '', this.name);
                
                btn.onclick = async (e) => {
                    e.stopPropagation();
                    const text = textEl?.innerText || '';
                    const originalIcon = btn.querySelector('img')?.cloneNode(true);
                    const resp = await chrome.runtime.sendMessage({ 
                        action: 'saveMemory', 
                        data: { 
                            title: sourceTitle, 
                            content: text, 
                            source: 'claude', 
                            interaction_type: interactionType, 
                            tags: [tag, 'claude'] 
                        } 
                    });
                    if (resp?.success) {
                        btn.replaceChildren(createCheckmark());
                        showFloatingFeedback(btn, 'Saved!', 'success');
                    } else {
                        btn.replaceChildren(createErrorIcon());
                        showFloatingFeedback(btn, resp?.error || 'Error', 'error');
                    }
                    setTimeout(() => { if (btn.isConnected) btn.replaceChildren(originalIcon || createLogoImage({ width: '16px', height: '16px' })); }, 2000);
                };

                // Style the button to match Claude's ghost buttons
                btn.className = 'brain-vault-save-btn w-fit';
                btn.style.cssText = `
                    display: inline-flex; align-items: center; justify-content: center;
                    width: 32px; height: 32px; border-radius: 6px;
                    background-color: transparent; border: none; cursor: pointer;
                    color: currentColor; opacity: 0.7; transition: all 0.2s ease;
                `;
                btn.onmouseover = () => { btn.style.backgroundColor = 'rgba(128,128,128,0.1)'; btn.style.opacity = '1'; };
                btn.onmouseout = () => { btn.style.backgroundColor = 'transparent'; btn.style.opacity = '0.7'; };
                
                // Insert depending on user vs agent
                if (isUser) {
                    toolbar.prepend(btn); // Leftmost
                } else {
                    toolbar.appendChild(btn); // Rightmost
                }
            }
        },
        async injectUserPromptSaveButtons() { /* Handled comprehensively in injectSaveButtons */ },
        async injectContextButton() {
            // Claude's input toolbar has the model dropdown [data-testid="model-selector-dropdown"]
            const modelDropdowns = document.querySelectorAll('button[data-testid="model-selector-dropdown"]');
            
            for (const dropdown of modelDropdowns) {
                // The immediate container of the dropdown or its parent wrapper
                const dropdownWrapper = dropdown.closest('.transition-all.duration-200.ease-out') || dropdown.parentElement;
                const container = dropdownWrapper.parentElement;
                
                if (!container || container.querySelector('.brain-vault-inject-btn')) continue;

                const btn = createInjectButton(() => queryWithFallback(this.selectors.inputArea));
                
                btn.className = 'brain-vault-inject-btn inline-flex items-center justify-center relative shrink-0 h-8 w-8 rounded-md active:scale-95 transition duration-300 ease-out hover:bg-bg-200 mr-1';
                btn.style.cssText = `
                    color: currentColor; opacity: 0.7; cursor: pointer; border: none; background: transparent;
                `;
                btn.onmouseover = () => { btn.style.backgroundColor = 'rgba(128,128,128,0.1)'; btn.style.opacity = '1'; };
                btn.onmouseout = () => { btn.style.backgroundColor = 'transparent'; btn.style.opacity = '0.7'; };
                
                // Insert directly to the left of the model selector
                container.insertBefore(btn, dropdownWrapper);
            }
        }
    },

    gemini: {
        name: 'gemini',
        match: (host) => (host === 'gemini.google.com' || host === 'www.gemini.google.com') && window.location.pathname.startsWith('/app'),
        selectors: {
            modelResponseText: [
                '.model-response-text',
                '[class*="response-text"]',
                '.markdown-content'
            ],
            buttonsContainer: [
                '.buttons-container-v2',
                '.buttons-container',
                '[class*="action-buttons"]'
            ],
            modelTurn: [
                'model-turn-component',
                '[class*="model-turn"]',
                '.conversation-container'
            ],
            inputArea: [
                'rich-textarea textarea',
                'textarea[aria-label*="prompt"]',
                'div[contenteditable="true"]'
            ],
            inputActions: [
                '.model-picker-container',
                '.input-buttons-wrapper-bottom'
            ]
        },
        async injectSaveButtons() {
            const toolbars = queryAllWithFallback(this.selectors.buttonsContainer);
            for (const toolbar of toolbars) {
                if (toolbar.querySelector('.brain-vault-save-btn')) continue;
                let container = null;
                for (const sel of this.selectors.modelTurn) {
                    container = toolbar.closest(sel);
                    if (container) break;
                }
                if (!container) continue;
                const textEl = container.querySelector(this.selectors.modelResponseText[0]);
                if (!textEl) continue;

                const btn = createSaveButton(() => textEl.innerText, this.name);
                const spacer = toolbar.querySelector('.spacer');
                if (spacer) toolbar.insertBefore(btn, spacer);
                else toolbar.appendChild(btn);
            }
        },
        async injectUserPromptSaveButtons() {
            // Gemini: .query-content wraps the Copy/Edit buttons + the query bubble
            // Prepend directly to it so our button appears as first child (leftmost)
            const queryContainers = document.querySelectorAll('.query-content');
            for (const container of queryContainers) {
                if (container.querySelector('.brain-vault-save-btn')) continue;
                // Only proceed if this container has action buttons (confirms it's a user query turn)
                const copyBtn = container.querySelector('button[aria-label="Copy prompt"]');
                if (!copyBtn) continue;

                const textEl = container.querySelector('.query-text') || container;
                const btn = createSaveButton(() => textEl.innerText || '', this.name);
                btn.onclick = async (e) => {
                    e.stopPropagation();
                    const text = textEl.innerText;
                    const originalIcon = btn.querySelector('img')?.cloneNode(true);
                    const resp = await chrome.runtime.sendMessage({ action: 'saveMemory', data: { title: 'Gemini Prompt', content: text, source: 'gemini', interaction_type: 'prompt', tags: ['prompt', 'gemini'] } });
                    if (resp?.success) {
                        btn.replaceChildren(createCheckmark());
                        showFloatingFeedback(btn, 'Prompt saved!', 'success');
                    } else {
                        btn.replaceChildren(createErrorIcon());
                        showFloatingFeedback(btn, resp?.error || 'Error', 'error');
                    }
                    setTimeout(() => { if (btn.isConnected) btn.replaceChildren(originalIcon || createLogoImage({ width: '16px', height: '16px' })); }, 2000);
                };
                btn.style.cssText = `
                    display: inline-flex; align-items: center; justify-content: center;
                    width: 40px; height: 40px; border-radius: 50%; background-color: transparent;
                    border: none; cursor: pointer; opacity: 0.8; transition: all 0.2s;
                `;
                btn.onmouseover = () => { btn.style.backgroundColor = 'rgba(128,128,128,0.15)'; btn.style.opacity = '1'; };
                btn.onmouseout = () => { btn.style.backgroundColor = 'transparent'; btn.style.opacity = '0.8'; };
                // Prepend to .query-content so it is the very first element (leftmost)
                container.prepend(btn);
            }
        },
        async injectContextButton() {
            const actionContainer = queryWithFallback(this.selectors.inputActions);
            if (!actionContainer || actionContainer.querySelector('.brain-vault-inject-btn')) return;

            const btn = createInjectButton(() => queryWithFallback(this.selectors.inputArea));
            btn.style.cssText = `
                display: flex; align-items: center; justify-content: center;
                width: 36px; height: 36px; border-radius: 50%; background-color: transparent;
                border: none; cursor: pointer; opacity: 0.9; transition: all 0.2s ease; margin-right: 8px;
            `;
            btn.onmouseover = () => { btn.style.backgroundColor = 'rgba(128,128,128,0.1)'; btn.style.opacity = '1'; };
            btn.onmouseout = () => { btn.style.backgroundColor = 'transparent'; btn.style.opacity = '0.9'; };
            actionContainer.prepend(btn);
        }
    },

    youtube: {
        name: 'youtube',
        match: (host) => host.includes('youtube'),
        selectors: {
            videoMenu: [
                '#menu > ytd-menu-renderer',
                '#menu-container ytd-menu-renderer'
            ],
            videoTitle: [
                '#title > h1 > yt-formatted-string',
                'h1.ytd-video-primary-info-renderer'
            ],
            shortsActions: [
                'ytd-reel-player-overlay-renderer #actions',
                '#actions.ytd-reel-player-overlay-renderer'
            ],
            shortsVideo: ['ytd-reel-video-renderer'],
            shortsTitle: ['#overlay .metadata h2', '.yt-reel-metadatam-renderer h2']
        },
        // YouTube extraction hidden — coming soon with client-side transcript support
        async injectSaveButtons() { /* Hidden: YouTube extraction coming soon */ },
        async injectContextButton() { /* No-op for YouTube */ }
    },

    perplexity: {
        name: 'perplexity',
        match: (host) => host === 'perplexity.ai' || host === 'www.perplexity.ai',
        selectors: {
            // Input area - contenteditable div
            inputArea: [
                '#ask-input',
                'div[contenteditable="true"][role="textbox"]',
                'div[data-lexical-editor="true"]'
            ],
            // Container for inject button - left of model selector
            inputActionsRight: [
                '.flex.items-center.justify-self-end.col-start-3',
                'div.col-start-3.row-start-2',
                '.grid-rows-1fr-auto .col-start-3'
            ],
            // Model selector button to insert before
            modelSelector: [
                'button[aria-label="Choose a model"]',
                'button:has-text("Model")',
                'span:has-text("Model")'
            ],
            // Response action toolbar (left division with Share, Download, Copy, Rewrite)
            responseToolbarLeft: [
                '.flex.items-center.justify-between > div:first-child',
                '.-ml-sm.gap-xs.flex.flex-shrink-0.items-center',
                '.flex.items-center.justify-between .flex-shrink-0:first-child'
            ],
            // Rewrite button to insert after
            rewriteButton: [
                'button[aria-label="Rewrite"]',
                'button:has(svg use[xlink\\:href="#pplx-icon-repeat"])'
            ],
            // Response text content
            responseContent: [
                '.prose',
                '.markdown-content',
                '[class*="answer-content"]',
                '.whitespace-pre-wrap'
            ]
        },
        async injectSaveButtons() {
            // Find all response toolbars
            const toolbars = queryAllWithFallback(this.selectors.responseToolbarLeft);

            for (const toolbar of toolbars) {
                if (toolbar.querySelector('.brain-vault-save-btn')) continue;

                // Find the parent response container to get the text
                const responseContainer = toolbar.closest('[class*="answer"]') ||
                    toolbar.closest('.prose')?.parentElement ||
                    toolbar.parentElement?.parentElement;

                const textElement = responseContainer?.querySelector('.prose') ||
                    responseContainer?.querySelector('.whitespace-pre-wrap');

                const btn = createSaveButton(
                    () => textElement?.innerText || 'Perplexity Response',
                    this.name
                );

                // Match Perplexity's button style
                btn.style.cssText = `
                    display: inline-flex; align-items: center; justify-content: center;
                    width: 32px; height: 32px; border-radius: 9999px;
                    background-color: transparent; border: none; cursor: pointer;
                    opacity: 0.7; transition: all 0.3s ease;
                `;
                btn.onmouseover = () => {
                    btn.style.backgroundColor = 'rgba(128,128,128,0.1)';
                    btn.style.opacity = '1';
                };
                btn.onmouseout = () => {
                    btn.style.backgroundColor = 'transparent';
                    btn.style.opacity = '0.7';
                };

                // Insert after the Rewrite button (rightmost in left division)
                const rewriteBtn = toolbar.querySelector(this.selectors.rewriteButton[0]);
                if (rewriteBtn) {
                    rewriteBtn.after(btn);
                } else {
                    toolbar.appendChild(btn);
                }
            }
        },
        async injectUserPromptSaveButtons() {
            // Perplexity: anchor on the Edit Query / Copy Query buttons which reliably exist
            // The action group (.flex.shrink-0.items-center.gap-1) is opacity-0 by default and
            // reveals on hover via Tailwind group-hover — our button inherits that correctly.
            const editBtns = document.querySelectorAll('button[aria-label="Edit Query"], button[aria-label="Copy Query"]');
            const seenGroups = new WeakSet();
            for (const anchor of editBtns) {
                // Walk up to find the flex action group that holds Edit + Copy
                const actionGroup = anchor.closest('.flex.shrink-0.items-center') || anchor.parentElement;
                if (!actionGroup || seenGroups.has(actionGroup)) continue;
                if (actionGroup.querySelector('.brain-vault-save-btn')) continue;
                seenGroups.add(actionGroup);

                // Text: sibling of the action group inside the outer .flex.items-start wrapper
                const outerWrap = actionGroup.closest('.flex.items-start');
                const textEl = outerWrap?.querySelector('.whitespace-pre-line, span.min-w-0') || outerWrap;

                const btn = createSaveButton(() => textEl?.innerText || '', this.name);
                btn.onclick = async (e) => {
                    e.stopPropagation();
                    const text = textEl?.innerText || '';
                    const originalIcon = btn.querySelector('img')?.cloneNode(true);
                    const resp = await chrome.runtime.sendMessage({ action: 'saveMemory', data: { title: 'Perplexity Prompt', content: text, source: 'perplexity', interaction_type: 'prompt', tags: ['prompt', 'perplexity'] } });
                    if (resp?.success) {
                        btn.replaceChildren(createCheckmark());
                        showFloatingFeedback(btn, 'Prompt saved!', 'success');
                    } else {
                        btn.replaceChildren(createErrorIcon());
                        showFloatingFeedback(btn, resp?.error || 'Error', 'error');
                    }
                    setTimeout(() => { if (btn.isConnected) btn.replaceChildren(originalIcon || createLogoImage({ width: '16px', height: '16px' })); }, 2000);
                };
                btn.style.cssText = `
                    display: inline-flex; align-items: center; justify-content: center;
                    width: 32px; height: 32px; border-radius: 9999px;
                    background-color: transparent; border: none; cursor: pointer;
                    transition: background-color 0.3s ease;
                `;
                btn.onmouseover = () => { btn.style.backgroundColor = 'rgba(128,128,128,0.1)'; };
                btn.onmouseout = () => { btn.style.backgroundColor = 'transparent'; };
                actionGroup.prepend(btn);
            }
        },
        async injectContextButton() {
            // Find the right-side actions container (where model selector is)
            const actionContainer = queryWithFallback(this.selectors.inputActionsRight);
            if (!actionContainer || actionContainer.querySelector('.brain-vault-inject-btn')) return;

            const btn = createInjectButton(() => queryWithFallback(this.selectors.inputArea));

            // Match Perplexity's button style
            btn.style.cssText = `
                display: inline-flex; align-items: center; justify-content: center;
                width: 32px; height: 32px; border-radius: 9999px;
                background-color: transparent; border: none; cursor: pointer;
                opacity: 0.7; transition: all 0.3s ease; margin-right: 4px;
            `;
            btn.onmouseover = () => {
                btn.style.backgroundColor = 'rgba(128,128,128,0.1)';
                btn.style.opacity = '1';
            };
            btn.onmouseout = () => {
                btn.style.backgroundColor = 'transparent';
                btn.style.opacity = '0.7';
            };

            // Insert before the model selector button
            const modelBtn = actionContainer.querySelector(this.selectors.modelSelector[0]);
            if (modelBtn) {
                modelBtn.parentElement.insertBefore(btn, modelBtn.parentElement.firstChild);
            } else {
                actionContainer.prepend(btn);
            }
        }
    }
};

// ============================================================================
// ORCHESTRATOR
// ============================================================================

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'injectPrompt') {
        injectText(request.text);
        sendResponse({ success: true });
    }
    return true;
});

async function injectText(text) {
    const activeElement = document.activeElement;
    if (activeElement && (activeElement.tagName === 'TEXTAREA' || activeElement.getAttribute('contenteditable') === 'true')) {
        if (activeElement.tagName === 'TEXTAREA') activeElement.value += text;
        else activeElement.textContent += text;
        activeElement.dispatchEvent(new Event('input', { bubbles: true }));
    } else {
        try {
            await navigator.clipboard.writeText(text);
            alert('Memwyre: Prompt copied to clipboard (could not find input box).');
        } catch (err) {
            console.error('Memwyre: Clipboard write failed', err);
        }
    }
}

function getAdapter(hostname) {
    for (const key in ADAPTERS) {
        if (ADAPTERS[key].match(hostname)) return ADAPTERS[key];
    }
    return null;
}

const hostname = window.location.hostname;
const adapter = getAdapter(hostname);
if (!adapter) console.log('Memwyre: No adapter found for', hostname);

// Global spinner animation
const spinnerStyle = document.createElement('style');
spinnerStyle.textContent = `@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }`;
document.head.appendChild(spinnerStyle);

async function runInjections() {
    if (!adapter) return;
    try { await adapter.injectSaveButtons(); } catch (e) { console.warn('Memwyre: Save button injection failed', e); }
    try { await adapter.injectContextButton(); } catch (e) { console.warn('Memwyre: Context button injection failed', e); }
    try { if (adapter.injectUserPromptSaveButtons) await adapter.injectUserPromptSaveButtons(); } catch (e) { console.warn('Memwyre: User prompt save button injection failed', e); }
}

let injectionScheduled = false;
function scheduleInjection() {
    if (injectionScheduled) return;
    injectionScheduled = true;
    const scheduler = window.requestIdleCallback || ((cb) => setTimeout(cb, 50));
    scheduler(() => { injectionScheduled = false; runInjections(); }, { timeout: 500 });
}

const observer = new MutationObserver((mutations) => {
    if (mutations.some(m => m.addedNodes.length > 0 || m.removedNodes.length > 0)) {
        scheduleInjection();
    }
});

if (document.body) observer.observe(document.body, { childList: true, subtree: true });
setTimeout(() => runInjections(), 2000);
