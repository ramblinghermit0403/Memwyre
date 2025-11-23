chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'getContent') {
        let content = '';
        if (request.type === 'selection') {
            content = window.getSelection().toString();
        } else if (request.type === 'page') {
            content = document.body.innerText;
        }

        sendResponse({
            content: content,
            title: document.title
        });
    }
});
