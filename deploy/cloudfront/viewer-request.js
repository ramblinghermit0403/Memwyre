// CloudFront Function: agent-readiness + www redirect
// Type: Viewer Request
//
// Combines:
// 1. www.memwyre.tech → memwyre.tech redirect (existing)
// 2. Markdown content negotiation for AI agents (new)

function handler(event) {
    var request = event.request;
    var headers = request.headers;
    var uri = request.uri;

    // --- 1. WWW Redirect (existing logic) ---
    var host = headers.host ? headers.host.value : "";

    if (host === "www.memwyre.tech") {
        return {
            statusCode: 301,
            statusDescription: "Moved Permanently",
            headers: {
                "location": { "value": "https://memwyre.tech" + uri }
            }
        };
    }

    // --- 2. Markdown Content Negotiation ---
    // If requesting homepage and Accept includes text/markdown, serve index.md
    if (uri === '/' || uri === '/index.html') {
        var accept = headers['accept'] ? headers['accept'].value : '';
        if (accept.indexOf('text/markdown') >= 0) {
            request.uri = '/index.md';
            return request;
        }
    }

    return request;
}
