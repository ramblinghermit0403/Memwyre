// CloudFront Function: agent-readiness
// Purpose: Adds Link headers and handles Markdown content negotiation
// Type: Viewer Request (must be attached to the CloudFront distribution)
//
// SETUP:
// 1. Go to CloudFront → Functions → Create function
// 2. Paste this code
// 3. Publish
// 4. Associate with your distribution's Viewer Request event

function handler(event) {
    var request = event.request;
    var headers = request.headers;
    var uri = request.uri;

    // --- Markdown Content Negotiation ---
    // If requesting the homepage and the Accept header includes text/markdown,
    // rewrite to serve index.md instead of index.html
    if (uri === '/' || uri === '/index.html') {
        var accept = headers['accept'] ? headers['accept'].value : '';
        if (accept.includes('text/markdown')) {
            request.uri = '/index.md';
            return request;
        }
    }

    return request;
}
