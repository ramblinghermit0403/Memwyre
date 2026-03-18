// config.js

// Change this to 'prod' before publishing to the Chrome Web Store
const ENV = 'prod'; // Options: 'dev', 'prod'

const CONFIG = {
    dev: {
        API_BASE_URL: 'http://localhost:8000/api/v1',
        WEB_APP_URL: 'http://localhost:5173'
    },
    prod: {
        API_BASE_URL: 'https://server.memwyre.tech/api/v1',
        WEB_APP_URL: 'https://memwyre.tech'
    }
};

// Export for Background Service Worker (uses importScripts)
if (typeof self !== 'undefined' && self.importScripts) {
    self.ENV = ENV;
    self.CONFIG = CONFIG;
}

// Export for Content Scripts / DOM Scripts (window attached)
if (typeof window !== 'undefined') {
    window.ENV = ENV;
    window.CONFIG = CONFIG;
}
