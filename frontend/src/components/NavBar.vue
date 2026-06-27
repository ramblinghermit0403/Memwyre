<template>
  <nav class="bg-white/80 dark:bg-surface/80 backdrop-blur-md border-b border-gray-200 dark:border-border sticky top-0 z-50 transition-colors duration-300">
    <div class="w-full px-6">
      <div class="flex justify-between h-16">
        <div class="flex items-center">
          <router-link to="/" class="flex-shrink-0 flex items-center group">
            <div class="flex items-center select-none" id="nav-logo">
              <img src="/logo.png" alt="Memwyre" class="h-[35px] w-auto dark:invert transition-transform duration-300 group-hover:scale-[1.02]" />
            </div>
          </router-link>

          <!-- Workspace Switcher (Only show if authenticated) -->
          <div v-if="authStore.isAuthenticated" class="relative flex items-center ml-4" v-click-outside="closeWorkspaceMenu">
            <div class="h-6 w-px bg-gray-200 dark:bg-divider mr-4"></div>
            
            <button 
              @click="toggleWorkspaceMenu" 
              class="flex items-center gap-2 px-3 py-1.5 rounded-lg border border-gray-200 dark:border-border bg-white dark:bg-surface hover:bg-gray-50 dark:hover:bg-surface-2 transition-colors text-sm font-semibold text-gray-700 dark:text-text-primary select-none cursor-pointer group"
            >
              <!-- Folder/Workspace Icon -->
              <svg class="w-4 h-4 text-gray-400 dark:text-gray-500 group-hover:text-gray-600 dark:group-hover:text-gray-300 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" />
              </svg>
              <span class="max-w-[120px] truncate">{{ currentProjectName }}</span>
              <svg 
                class="w-3.5 h-3.5 text-gray-400 group-hover:text-gray-600 dark:group-hover:text-gray-300 transition-transform duration-200" 
                :class="{ 'rotate-180': isWorkspaceMenuOpen }"
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7" />
              </svg>
            </button>

            <!-- Dropdown Menu -->
            <transition
              enter-active-class="transition ease-out duration-100"
              enter-from-class="transform opacity-0 scale-95"
              enter-to-class="transform opacity-100 scale-100"
              leave-active-class="transition ease-in duration-75"
              leave-from-class="transform opacity-100 scale-100"
              leave-to-class="transform opacity-0 scale-95"
            >
              <div v-if="isWorkspaceMenuOpen" class="absolute left-0 mt-2 top-10 w-64 bg-white dark:bg-elevated rounded-lg shadow-xl py-1.5 ring-1 ring-black ring-opacity-5 z-[60] border border-gray-100 dark:border-border">
                <div class="px-3.5 py-1.5 border-b border-gray-100 dark:border-border">
                  <p class="text-[11px] font-bold text-gray-400 dark:text-text-muted uppercase tracking-wider">Switch Workspace</p>
                </div>
                
                <div class="max-h-48 overflow-y-auto py-1">
                  <button 
                    v-for="proj in projectStore.projects" 
                    :key="proj.id"
                    @click="selectWorkspace(proj.id)"
                    class="flex w-full items-center justify-between px-3.5 py-2 text-sm text-gray-700 dark:text-text-secondary hover:bg-gray-50 dark:hover:bg-surface-2 transition-colors text-left"
                    :class="{ 'font-semibold text-primary dark:text-[#D97757] bg-primary/5 dark:bg-[#D97757]/10': proj.id === projectStore.currentProjectId }"
                  >
                    <span class="truncate pr-2">{{ proj.name }}</span>
                    <svg v-if="proj.id === projectStore.currentProjectId" class="w-4 h-4 text-primary dark:text-[#D97757]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
                    </svg>
                  </button>
                </div>

                <div class="border-t border-gray-100 dark:border-border px-3.5 py-2 space-y-2">
                  <div class="flex gap-2">
                    <input 
                      v-model="newWorkspaceName" 
                      @keyup.enter="handleCreateWorkspace"
                      class="flex-1 min-w-0 text-xs border border-gray-200 dark:border-border rounded px-2 py-1 bg-white dark:bg-surface text-gray-900 dark:text-white focus:outline-none focus:border-[#D97757] transition-colors"
                      placeholder="New workspace..."
                    />
                    <button 
                      @click="handleCreateWorkspace"
                      class="shrink-0 text-xs px-2.5 py-1 rounded bg-[#D97757] hover:bg-[#C4654A] text-white font-bold transition-colors"
                    >
                      Add
                    </button>
                  </div>
                  <router-link 
                    to="/projects" 
                    class="block text-center text-[11px] font-semibold text-gray-400 hover:text-gray-600 dark:text-text-muted dark:hover:text-text-secondary transition-colors"
                  >
                    Manage Workspaces
                  </router-link>
                </div>
              </div>
            </transition>
          </div>
        </div>

        <div class="flex items-center gap-3">
          <button id="tour-quick-actions" @click="isQuickCreateOpen = true" class="flex items-center gap-2 bg-[#D97757] text-white hover:bg-[#C4654A] px-4 py-2 rounded-full text-sm font-bold transition-all shadow-sm">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
            Quick Add
          </button>

          <router-link to="/dashboard" class="flex items-center gap-2 text-gray-500 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white px-3 py-2 rounded-md text-sm font-medium transition-colors">
            Dashboard
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
import { computed, ref, watch, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useInboxStore } from '../stores/inbox';
import { useAuthStore } from '../stores/auth';
import { useProjectStore } from '../stores/project';
import { useToast } from 'vue-toastification';
import QuickCreateModal from './QuickCreateModal.vue';

const projectStore = useProjectStore();
const toast = useToast();

const isWorkspaceMenuOpen = ref(false);
const newWorkspaceName = ref('');

const currentProjectName = computed(() => {
  const current = projectStore.projects.find(p => p.id === projectStore.currentProjectId);
  return current ? current.name : 'default';
});

const toggleWorkspaceMenu = () => {
  isWorkspaceMenuOpen.value = !isWorkspaceMenuOpen.value;
};

const closeWorkspaceMenu = () => {
  isWorkspaceMenuOpen.value = false;
};

const selectWorkspace = (id) => {
  projectStore.setCurrentProjectId(id);
  isWorkspaceMenuOpen.value = false;
  toast.success('Workspace switched');
};

const handleCreateWorkspace = async () => {
  const name = newWorkspaceName.value.trim();
  if (!name) return;
  try {
    await projectStore.createNewProject(name);
    newWorkspaceName.value = '';
    isWorkspaceMenuOpen.value = false;
    toast.success(`Workspace "${name}" created`);
  } catch (error) {
    toast.error('Failed to create workspace');
  }
};

onMounted(() => {
  if (authStore.isAuthenticated && projectStore.projects.length === 0) {
    projectStore.fetchProjects();
  }
});

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
