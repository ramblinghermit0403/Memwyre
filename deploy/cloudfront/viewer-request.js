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

    // --- 2. Docs Redirect ---
    if (uri === "/docs" || uri.indexOf("/docs/") === 0) {
        var newPath = uri.substring(5);
        if (newPath === "") newPath = "/";
        return {
            statusCode: 301,
            statusDescription: "Moved Permanently",
            headers: {
                "location": { "value": "https://docs.memwyre.tech" + newPath }
            }
        };
    }

    // --- 3. Trailing Slash Normalization ---
    // Strip trailing slash for all pages
    if (uri.length > 1 && uri.charAt(uri.length - 1) === '/') {
        return {
            statusCode: 301,
            statusDescription: "Moved Permanently",
            headers: {
                "location": { "value": "https://" + host + uri.slice(0, -1) }
            }
        };
    }

    // --- 4. Markdown Content Negotiation ---
    // If requesting homepage and Accept includes text/markdown, serve index.md
    if (uri === '/' || uri === '/index.html') {
        var accept = headers['accept'] ? headers['accept'].value : '';
        if (accept.indexOf('text/markdown') >= 0) {
            request.uri = '/index.md';
            return request;
        }
    }

    // --- 5. Directory Index Rewrite ---
    // If the URI does not contain a file extension, append index.html or .html so S3 serves the file
    var lastSegment = request.uri.substring(request.uri.lastIndexOf('/') + 1);
    var hasExtension = lastSegment.indexOf('.') !== -1;

    if (!hasExtension) {
        if (request.uri.charAt(request.uri.length - 1) === '/') {
            request.uri += 'index.html';
        } else {
            request.uri += '/index.html';
        }
    }

    return request;
}
