import api from './api';

export default {
    /**
     * List all active API keys for the current user.
     */
    async listKeys() {
        return api.get('/user/api-keys');
    },

    /**
     * Create a new API key.
     * @param {string} name - The friendly name for the key.
     */
    async createKey(name) {
        return api.post('/user/api-keys', { name });
    },

    /**
     * Revoke (delete) an API key.
     * @param {number} id - The ID of the key to revoke.
     */
    async revokeKey(id) {
        return api.delete(`/user/api-keys/${id}`);
    }
};
