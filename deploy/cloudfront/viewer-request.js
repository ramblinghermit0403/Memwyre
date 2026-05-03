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

    // --- 2. Trailing Slash Normalization ---
    // Special case for /docs (static site needs trailing slash)
    if (uri.startsWith('/docs')) {
        if (!uri.endsWith('/')) {
            return {
                statusCode: 301,
                statusDescription: "Moved Permanently",
                headers: {
                    "location": { "value": "https://" + host + uri + '/' }
                }
            };
        }
    } else {
        // For other URIs, strip trailing slash (SPA routes)
        if (uri.length > 1 && uri.endsWith('/')) {
            return {
                statusCode: 301,
                statusDescription: "Moved Permanently",
                headers: {
                    "location": { "value": "https://" + host + uri.slice(0, -1) }
                }
            };
        }
    }

    // --- 3. Markdown Content Negotiation ---
    // If requesting homepage and Accept includes text/markdown, serve index.md
    if (uri === '/' || uri === '/index.html') {
        var accept = headers['accept'] ? headers['accept'].value : '';
        if (accept.indexOf('text/markdown') >= 0) {
            request.uri = '/index.md';
            return request;
        }
    }

    // --- 4. Directory Index Rewrite ---
    // If URI ends with '/', append index.html for S3 serving
    if (request.uri.endsWith('/')) {
        request.uri += 'index.html';
    }

    return request;
}
