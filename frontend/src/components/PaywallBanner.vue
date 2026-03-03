<template>
  <div v-if="visible" class="mx-auto max-w-2xl my-8 animate-fade-in">
    <div class="relative overflow-hidden bg-white dark:bg-surface rounded-xl border border-gray-200 dark:border-border shadow-sm p-6">
      <!-- Accent bar -->
      <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-[#D97757] via-[#E8956E] to-[#D97757]"></div>

      <div class="flex flex-col sm:flex-row sm:items-center gap-4">
        <div class="flex-shrink-0 p-3 bg-[#D97757]/10 dark:bg-[#D97757]/20 rounded-lg">
          <svg class="w-6 h-6 text-[#D97757]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
          </svg>
        </div>
        <div class="flex-1">
          <h3 class="text-base font-semibold text-gray-900 dark:text-text-primary">Pro Feature</h3>
          <p class="mt-1 text-sm text-gray-500 dark:text-text-secondary">
            {{ message || 'This feature requires an active Pro subscription.' }}
          </p>
        </div>
        <router-link
          to="/billing"
          class="inline-flex items-center justify-center px-5 py-2.5 text-sm font-bold rounded-lg text-white bg-[#D97757] hover:bg-[#C4654A] transition-all shadow-sm whitespace-nowrap"
        >
          Upgrade to Pro
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  visible: {
    type: Boolean,
    default: true,
  },
  message: {
    type: String,
    default: '',
  },
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
