<template>
  <div class="h-screen flex flex-col transition-colors duration-300 font-sans overflow-hidden">
    <NavBar />

    <main class="flex-1 overflow-y-auto w-full max-w-4xl mx-auto py-10 px-4 sm:px-6 lg:px-8">
      <!-- Header -->
      <div class="mb-10">
        <h1 class="text-3xl font-bold text-gray-900 dark:text-text-primary">Billing</h1>
        <p class="mt-2 text-sm text-gray-500 dark:text-text-secondary">Manage your MemWyre Pro subscription.</p>
      </div>

      <!-- Success/Cancel Banner -->
      <div v-if="queryStatus === 'success'" class="mb-6 p-4 bg-green-50 dark:bg-green-900/20 border border-green-200 dark:border-green-800 rounded-lg animate-fade-in">
        <div class="flex items-center gap-3">
          <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
          <div>
            <p class="font-medium text-green-800 dark:text-green-200">Payment successful!</p>
            <p class="text-sm text-green-700 dark:text-green-300">Your Pro subscription is being activated. It may take a moment to reflect.</p>
          </div>
        </div>
      </div>

      <div v-if="queryStatus === 'cancelled'" class="mb-6 p-4 bg-yellow-50 dark:bg-yellow-900/20 border border-yellow-200 dark:border-yellow-800 rounded-lg animate-fade-in">
        <div class="flex items-center gap-3">
          <svg class="w-5 h-5 text-yellow-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4.5c-.77-.833-2.694-.833-3.464 0L3.34 16.5c-.77.833.192 2.5 1.732 2.5z" /></svg>
          <p class="font-medium text-yellow-800 dark:text-yellow-200">Checkout was cancelled. No charges were made.</p>
        </div>
      </div>

      <!-- Loading -->
      <div v-if="billing.loading" class="flex items-center justify-center py-20">
        <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-[#D97757]"></div>
      </div>

      <div v-else>
        <!-- Current Plan Card -->
        <div class="bg-white dark:bg-surface shadow rounded-xl border border-gray-100 dark:border-border p-8 mb-8 animate-fade-in">
          <div class="flex items-center justify-between mb-6">
            <div>
              <h2 class="text-lg font-semibold text-gray-900 dark:text-text-primary">Current Plan</h2>
              <div class="flex items-center gap-3 mt-2">
                <span
                  :class="billing.isPro ? 'bg-[#D97757] text-white' : 'bg-gray-200 text-gray-700 dark:bg-gray-700 dark:text-gray-300'"
                  class="px-3 py-1 rounded-full text-sm font-bold uppercase tracking-wider"
                >
                  {{ billing.plan || 'Free' }}
                </span>
                <span
                  :class="{
                    'text-green-600 dark:text-green-400': billing.status === 'active' || billing.isDevMode,
                    'text-yellow-600 dark:text-yellow-400': billing.status === 'on_hold',
                    'text-red-600 dark:text-red-400': billing.status === 'failed' || billing.status === 'cancelled',
                    'text-gray-500 dark:text-gray-400': billing.status === 'inactive'
                  }"
                  class="text-sm font-medium"
                >
                  {{ billing.statusLabel }}
                </span>
              </div>
            </div>

            <!-- Dev mode badge -->
            <div v-if="billing.isDevMode" class="px-3 py-1.5 bg-purple-100 dark:bg-purple-900/30 text-purple-700 dark:text-purple-300 rounded-lg text-xs font-bold uppercase tracking-wider">
              ðŸ›  Dev Mode Active
            </div>
          </div>

          <!-- Period info -->
          <div v-if="billing.currentPeriodEnd && billing.isPro" class="text-sm text-gray-500 dark:text-text-secondary">
            Current period ends: <span class="font-medium text-gray-700 dark:text-gray-300">{{ formatDate(billing.currentPeriodEnd) }}</span>
          </div>
        </div>

        <!-- Upgrade CTA (shown when on free plan) -->
        <div v-if="!billing.isPro" class="relative overflow-hidden bg-white dark:bg-surface shadow rounded-xl border border-gray-100 dark:border-border p-8 mb-8 animate-fade-in">
          <!-- Gradient accent -->
          <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-[#D97757] via-[#E8956E] to-[#D97757]"></div>

          <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-6">
            <div>
              <h2 class="text-2xl font-bold text-gray-900 dark:text-text-primary">Upgrade to Pro</h2>
              <p class="mt-2 text-gray-500 dark:text-text-secondary max-w-md">Unlock unlimited memories, document uploads, AI chat, and more.</p>

              <ul class="mt-4 space-y-2">
                <li v-for="feature in proFeatures" :key="feature" class="flex items-center gap-2 text-sm text-gray-700 dark:text-gray-300">
                  <svg class="w-4 h-4 text-[#D97757] flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                  {{ feature }}
                </li>
              </ul>
            </div>

            <div class="flex flex-col items-center gap-3">
              <div class="text-center">
                <span class="text-4xl font-bold text-gray-900 dark:text-text-primary">$12</span>
                <span class="text-gray-500 dark:text-text-secondary">/month</span>
              </div>
              <button
                @click="handleUpgrade"
                :disabled="checkingOut"
                class="w-full md:w-auto inline-flex items-center justify-center px-8 py-3 border border-transparent text-sm font-bold rounded-lg text-white bg-[#D97757] hover:bg-[#C4654A] transition-all shadow-sm disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <svg v-if="checkingOut" class="animate-spin -ml-1 mr-2 h-4 w-4" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" /><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z" /></svg>
                {{ checkingOut ? 'Redirecting...' : 'Upgrade Now' }}
              </button>
            </div>
          </div>
        </div>

        <!-- Manage Subscription (shown when on Pro) -->
        <div v-if="billing.isPro && !billing.isDevMode" class="bg-white dark:bg-surface shadow rounded-xl border border-gray-100 dark:border-border p-8 animate-fade-in">
          <h3 class="text-lg font-semibold text-gray-900 dark:text-text-primary mb-4">Manage Subscription</h3>

          <div class="flex items-center justify-between p-4 bg-gray-50 dark:bg-surface-2 rounded-lg">
            <div>
              <p class="font-medium text-gray-900 dark:text-text-primary">Cancel Subscription</p>
              <p class="text-sm text-gray-500 dark:text-text-secondary mt-1">Your access will continue until the end of the current billing period.</p>
            </div>
            <button
              @click="handleCancel"
              :disabled="cancelling"
              class="inline-flex items-center px-4 py-2 border border-red-300 dark:border-red-800 text-sm font-medium rounded-lg text-red-600 dark:text-red-400 bg-white dark:bg-transparent hover:bg-red-50 dark:hover:bg-red-900/20 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {{ cancelling ? 'Cancelling...' : 'Cancel Plan' }}
            </button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import { useBillingStore } from '../stores/billing';
import { useToast } from 'vue-toastification';
import NavBar from '../components/NavBar.vue';

const route = useRoute();
const billing = useBillingStore();
const toast = useToast();

const checkingOut = ref(false);
const cancelling = ref(false);

const queryStatus = computed(() => route.query.status);

const proFeatures = [
  '1M+ token storage',
  '100K daily AI token budget',
  'PDF & web page ingestion (YouTube coming soon)',
  'MCP Server for IDE integration',
  'Browser Extension (Chrome & Edge)',
  'OpenClaw agent plugin access',
  'Priority support',
];

const formatDate = (isoString) => {
  if (!isoString) return '';
  return new Date(isoString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
};

const handleUpgrade = async () => {
  checkingOut.value = true;
  try {
    await billing.startCheckout();
  } catch (err) {
    toast.error('Failed to start checkout. Please try again.');
    checkingOut.value = false;
  }
};

const handleCancel = async () => {
  if (!confirm('Are you sure you want to cancel your Pro subscription?')) return;
  cancelling.value = true;
  try {
    await billing.cancelSubscription();
    toast.success('Subscription cancelled. Access continues until period end.');
  } catch (err) {
    toast.error('Failed to cancel subscription.');
  } finally {
    cancelling.value = false;
  }
};

onMounted(() => {
  billing.fetchStatus();
});
</script>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.3s ease-in-out;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(5px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
