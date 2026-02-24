import { defineStore } from 'pinia';
import billingService from '../services/billing';

export const useBillingStore = defineStore('billing', {
    state: () => ({
        plan: null,         // 'free' | 'pro'
        status: null,       // 'active' | 'inactive' | 'cancelled' | 'on_hold' | 'failed' | 'dev_mode_active'
        isActive: false,
        currentPeriodEnd: null,
        loading: false,
        error: null,
    }),

    getters: {
        isPro: (state) => state.isActive,
        isFree: (state) => !state.isActive,
        isDevMode: (state) => state.status === 'dev_mode_active',
        statusLabel: (state) => {
            const labels = {
                active: 'Active',
                inactive: 'No Plan',
                cancelled: 'Cancelled',
                on_hold: 'On Hold',
                failed: 'Payment Failed',
                dev_mode_active: 'Dev Mode',
            };
            return labels[state.status] || 'Unknown';
        },
    },

    actions: {
        async fetchStatus() {
            this.loading = true;
            this.error = null;
            try {
                const res = await billingService.getStatus();
                this.plan = res.data.plan;
                this.status = res.data.status;
                this.isActive = res.data.is_active;
                this.currentPeriodEnd = res.data.current_period_end;
            } catch (err) {
                console.error('Failed to fetch billing status:', err);
                this.error = 'Failed to load subscription status';
            } finally {
                this.loading = false;
            }
        },

        async startCheckout() {
            try {
                const res = await billingService.createCheckout();
                if (res.data.checkout_url) {
                    window.location.href = res.data.checkout_url;
                }
                return res.data;
            } catch (err) {
                console.error('Checkout failed:', err);
                throw err;
            }
        },

        async cancelSubscription() {
            try {
                const res = await billingService.cancelSubscription();
                await this.fetchStatus(); // Refresh status
                return res.data;
            } catch (err) {
                console.error('Cancel failed:', err);
                throw err;
            }
        },
    },
});
