import api from './api';

const billingService = {
    /**
     * Get current subscription status
     */
    getStatus() {
        return api.get('/billing/status');
    },

    /**
     * Create checkout session → returns { checkout_url, session_id }
     */
    createCheckout() {
        return api.post('/billing/checkout');
    },

    /**
     * Cancel subscription at end of billing period
     */
    cancelSubscription() {
        return api.post('/billing/cancel');
    }
};

export default billingService;
