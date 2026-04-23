// CloudFront Function: agent-readiness-response
// Purpose: Adds Link headers to homepage responses
// Type: Viewer Response (must be attached to the CloudFront distribution)
//
// SETUP:
// 1. Go to CloudFront → Functions → Create function
// 2. Paste this code
// 3. Publish
// 4. Associate with your distribution's Viewer Response event

function handler(event) {
    var response = event.response;
    var request = event.request;
    var headers = response.headers;

    // --- Link Header ---
    // Add Link header pointing to the API catalog and MCP server card
    // on homepage responses only
    if (request.uri === '/' || request.uri === '/index.html' || request.uri === '/index.md') {
        headers['link'] = {
            value: '</.well-known/api-catalog>; rel="api-catalog", </.well-known/mcp.json>; rel="mcp-server-card"'
        };
    }

    // --- Content-Type for Markdown ---
    // Ensure .md files are served with text/markdown content type
    if (request.uri.endsWith('.md')) {
        headers['content-type'] = { value: 'text/markdown; charset=utf-8' };
    }

    return response;
}
