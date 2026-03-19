// config.js

// Production-only config for store submission builds.
const ENV = 'prod';

const CONFIG = {
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
