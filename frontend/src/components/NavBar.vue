<template>
  <nav class="bg-white/80 dark:bg-surface/80 backdrop-blur-md border-b border-gray-200 dark:border-border sticky top-0 z-50 transition-colors duration-300">
    <div class="w-full px-10 sm:px-16 lg:px-28">
      <div class="flex justify-between h-16">
        <div class="flex items-center">
          <router-link to="/" class="flex-shrink-0 flex items-center group">
            <div class="flex items-center select-none" id="nav-logo">
              <img src="/image.svg" alt="Memwyre" class="w-7 h-7 rounded-sm mr-2.5 group-hover:scale-105 transition-transform duration-300" />
              <h1 class="text-2xl font-medium tracking-tight text-black dark:text-white transition-colors duration-300" style="font-family: 'Inter', system-ui, sans-serif;">Memwyre</h1>
            </div>
          </router-link>
        </div>

        <div class="flex items-center gap-3">
          <button id="tour-quick-actions" @click="isQuickCreateOpen = true" class="flex items-center gap-2 bg-[#D97757] text-white hover:bg-[#C4654A] px-4 py-2 rounded-full text-sm font-bold transition-all shadow-sm">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
            Quick Add
          </button>

          <router-link to="/dashboard" class="flex items-center gap-2 text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white px-3 py-2 rounded-md text-sm font-medium transition-colors">
            AI Interactions
          </router-link>

          <router-link to="/projects" class="flex items-center gap-2 text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white px-3 py-2 rounded-md text-sm font-medium transition-colors">
            Projects
          </router-link>

          <router-link id="tour-inbox" to="/inbox" class="relative flex items-center gap-2 text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white px-3 py-2 rounded-md text-sm font-medium transition-colors">
            Inbox
            <span v-if="inboxCount > 0" class="absolute -top-1.5 -right-1.5 flex h-4 min-w-[16px] items-center justify-center rounded-full bg-red-500 px-1 text-[10px] font-bold text-white ring-2 ring-white dark:ring-gray-800">{{ inboxCount > 99 ? '99+' : inboxCount }}</span>
          </router-link>

          <router-link id="tour-ask" to="/chat" class="flex items-center gap-2 text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white px-3 py-2 rounded-md text-sm font-medium transition-colors">
            Ask
          </router-link>

          <router-link to="/integrations" class="flex items-center gap-2 text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white px-3 py-2 rounded-md text-sm font-medium transition-colors">
            Integrations
          </router-link>

          <div class="h-6 w-px bg-gray-200 dark:bg-divider mx-2"></div>

          <div class="relative ml-1" v-click-outside="closeProfile">
            <button @click="toggleProfile" class="focus:outline-none transition-transform active:scale-95 block">
              <img class="h-8 w-8 rounded-full border border-gray-200 dark:border-border transition-all" :src="userAvatar" alt="User Avatar">
            </button>

            <transition
              enter-active-class="transition ease-out duration-100"
              enter-from-class="transform opacity-0 scale-95"
              enter-to-class="transform opacity-100 scale-100"
              leave-active-class="transition ease-in duration-75"
              leave-from-class="transform opacity-100 scale-100"
              leave-to-class="transform opacity-0 scale-95"
            >
              <div v-if="isProfileOpen" class="absolute right-0 mt-2 w-48 bg-white dark:bg-elevated rounded-lg shadow-xl py-1 ring-1 ring-black ring-opacity-5 z-50 border border-gray-100 dark:border-border">
                <div class="px-4 py-3 border-b border-gray-100 dark:border-divider">
                  <p class="text-sm text-gray-500 dark:text-text-secondary">Signed in as</p>
                  <p class="text-sm font-medium text-gray-900 dark:text-text-primary truncate">{{ authStore.user?.email || 'Guest' }}</p>
                </div>
                <router-link to="/billing" class="flex items-center px-4 py-2 text-sm text-gray-700 dark:text-text-secondary hover:bg-gray-50 dark:hover:bg-surface-2 transition-colors">Billing</router-link>
                <router-link to="/settings" class="flex items-center px-4 py-2 text-sm text-gray-700 dark:text-text-secondary hover:bg-gray-50 dark:hover:bg-surface-2 transition-colors">Settings</router-link>
                <button @click="logout" class="flex w-full items-center px-4 py-2 text-sm text-red-600 dark:text-danger hover:bg-red-50 dark:hover:bg-red-900/20 transition-colors">Logout</button>
              </div>
            </transition>
          </div>
        </div>
      </div>
    </div>
  </nav>
  <QuickCreateModal :is-open="isQuickCreateOpen" :initial-tab="quickAddTab" @close="isQuickCreateOpen = false" />
</template>

<script setup>
import { computed, ref, watch } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useInboxStore } from '../stores/inbox';
import { useAuthStore } from '../stores/auth';
import QuickCreateModal from './QuickCreateModal.vue';

const router = useRouter();
const route = useRoute();
const inboxStore = useInboxStore();
const authStore = useAuthStore();
const inboxCount = computed(() => inboxStore.count);
const isProfileOpen = ref(false);
const isQuickCreateOpen = ref(false);
const quickAddTab = computed(() => {
  const candidate = String(route.query.quick_add || '').toLowerCase();
  if (['create', 'documents', 'webpage'].includes(candidate)) return candidate;
  return 'documents';
});

const pastelColors = ['FFB3BA', 'FFDFBA', 'FFFFBA', 'BAFFC9', 'BAE1FF', 'E6B3FF', 'FFB3E6', 'B3FFE6', 'E6FFB3', 'FFE6B3'];

const getPastelColor = (str) => {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = str.charCodeAt(i) + ((hash << 5) - hash);
  }
  return pastelColors[Math.abs(hash) % pastelColors.length];
};

const userAvatar = computed(() => {
  const email = authStore.user?.email || 'User';
  const bg = getPastelColor(email);
  return `https://ui-avatars.com/api/?name=${encodeURIComponent(email)}&background=${bg}&color=333333`;
});

const toggleProfile = () => {
  isProfileOpen.value = !isProfileOpen.value;
};

const closeProfile = () => {
  if (isProfileOpen.value) isProfileOpen.value = false;
};

watch(() => route.path, () => {
  closeProfile();
});

watch(
  () => route.query.quick_add,
  (value) => {
    const candidate = String(value || '').toLowerCase();
    if (!['create', 'documents', 'webpage'].includes(candidate)) return;
    isQuickCreateOpen.value = true;
    const query = { ...route.query };
    delete query.quick_add;
    router.replace({ query });
  },
  { immediate: true },
);

const logout = () => {
  authStore.logout();
  router.push('/login');
};

const vClickOutside = {
  mounted(el, binding) {
    el.clickOutsideEvent = function(event) {
      if (!(el === event.target || el.contains(event.target))) {
        binding.value(event, el);
      }
    };
    document.body.addEventListener('click', el.clickOutsideEvent);
  },
  unmounted(el) {
    document.body.removeEventListener('click', el.clickOutsideEvent);
  }
};
</script>
