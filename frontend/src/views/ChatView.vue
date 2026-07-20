<script setup>
import { computed, ref, onMounted, onUnmounted, nextTick, watch } from 'vue';
import { useRouter } from 'vue-router';
import { useChatStore } from '../stores/chat';
import { useAuthStore } from '../stores/auth';
import { useProjectStore } from '../stores/project';
import NavBar from '../components/NavBar.vue';
import ConfirmationModal from '../components/ConfirmationModal.vue';
import AgentProgressRail from '../components/chat/AgentProgressRail.vue';
import AssistantMessageCard from '../components/chat/AssistantMessageCard.vue';
import { useToast } from 'vue-toastification';

const chatStore = useChatStore();
const authStore = useAuthStore();
const projectStore = useProjectStore();
const router = useRouter();
const toast = useToast();

const inputContent = ref('');
const messagesContainer = ref(null);

const showHistory = ref(window.innerWidth >= 768);
const showControls = ref(true);
const showDeleteModal = ref(false);

const expandedThinkingTurns = ref(new Set());
const activeTurnId = computed(() => chatStore.activeTurnId);
const activeThinkingSteps = computed(() => chatStore.getTurnSteps(activeTurnId.value));
const waitingForFirstStep = computed(() => chatStore.thinking && activeThinkingSteps.value.length === 0);

onMounted(async () => {
  await chatStore.fetchSessions();
  chatStore.connectWebSocket();
  if (chatStore.sessions.length > 0 && !chatStore.currentSession) {
    await chatStore.selectSession(chatStore.sessions[0].id);
  }
});

onUnmounted(() => {
  chatStore.disconnectWebSocket();
});

watch(() => chatStore.messages.length, () => nextTick(scrollToBottom));
watch(() => activeThinkingSteps.value.map((s) => `${s.step}:${s.status}:${s.timestamp}`).join('|'), () => nextTick(scrollToBottom));
watch(() => chatStore.thinking, () => nextTick(scrollToBottom));

watch(() => projectStore.currentProjectId, async () => {
  await chatStore.fetchSessions();
  if (chatStore.sessions.length > 0) {
    await chatStore.selectSession(chatStore.sessions[0].id);
  } else {
    chatStore.currentSession = null;
    chatStore.messages = [];
    chatStore.currentContext = [];
  }
});

function toggleThinkingTurn(turnId) {
  if (!turnId) return;
  const next = new Set(expandedThinkingTurns.value);
  if (next.has(turnId)) next.delete(turnId);
  else next.add(turnId);
  expandedThinkingTurns.value = next;
}

function isThinkingExpanded(turnId) {
  return turnId ? expandedThinkingTurns.value.has(turnId) : false;
}

function scrollToBottom() {
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight;
  }
}

function formatDate(dateStr) {
  if (!dateStr) return '';
  const date = new Date(dateStr);
  return new Intl.DateTimeFormat('en-US', {
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  }).format(date);
}

async function createNewChat() {
  await chatStore.createSession();
}

async function selectSession(id) {
  await chatStore.selectSession(id);
}

async function handleSend() {
  const content = inputContent.value.trim();
  if (!content || chatStore.thinking) return;

  if (!chatStore.currentSession) {
    await chatStore.createSession();
  }

  inputContent.value = '';
  await chatStore.sendMessage(content, 0.8, 8000);
}

function handleClearHistory() {
  showDeleteModal.value = true;
}

async function confirmClearHistory() {
  await chatStore.clearHistory();
  inputContent.value = '';
  showDeleteModal.value = false;
}

async function copyToClipboard(text) {
  try {
    await navigator.clipboard.writeText(text || '');
    toast.success('Copied to clipboard');
  } catch (err) {
    toast.error('Failed to copy');
  }
}

async function handleFeedback(messageId, type) {
  await chatStore.sendFeedback(messageId, type);
  toast.success('Feedback submitted');
}

function handleOpenSource(source) {
  if (source?.id) {
    router.push({ name: 'editor', params: { id: source.id } });
  }
}
</script>

<template>
  <div class="h-screen flex flex-col bg-[#F9F9FB] dark:bg-[#121214] text-[#2D2B2A] dark:text-[#FAF6F0] font-sans transition-colors duration-300">
    <NavBar />

    <div class="flex-1 flex overflow-hidden relative">
      <!-- Left Sidebar: Lobe UI Session History -->
      <transition enter-active-class="transition-transform duration-300 ease-in-out" enter-from-class="-translate-x-full" enter-to-class="translate-x-0" leave-active-class="transition-transform duration-300 ease-in-out" leave-from-class="translate-x-0" leave-to-class="-translate-x-full">
        <aside v-if="showHistory" class="w-72 bg-white/80 dark:bg-surface/80 backdrop-blur-md border-r border-gray-200/80 dark:border-border flex flex-col shrink-0 absolute md:static z-20 h-full shadow-xl md:shadow-none">
          <div class="p-4 border-b border-gray-100 dark:border-border/60 flex justify-between items-center">
            <div class="flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-[#D97757]"></span>
              <h3 class="font-semibold text-sm tracking-tight text-gray-800 dark:text-gray-200">Conversations</h3>
            </div>
            <button @click="showHistory = false" class="md:hidden text-gray-400 hover:text-gray-600">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
            </button>
          </div>

          <div class="p-3">
            <button @click="createNewChat" class="w-full py-2.5 px-4 bg-gradient-to-r from-[#D97757] to-[#e5896c] hover:from-[#c86646] hover:to-[#D97757] text-white font-medium rounded-xl transition-all flex items-center justify-center gap-2 shadow-sm text-sm active:scale-[0.99]">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
              New Conversation
            </button>
          </div>

          <div class="flex-1 overflow-y-auto px-2 pb-4 space-y-1">
            <button
              v-for="session in chatStore.sessions"
              :key="session.id"
              @click="selectSession(session.id)"
              class="w-full text-left px-3.5 py-3 rounded-xl hover:bg-gray-100/70 dark:hover:bg-surface-2/60 transition-all group relative border border-transparent"
              :class="{ 'bg-gray-100/90 border-gray-200/80 dark:bg-surface-2 dark:border-gray-700/60 shadow-xs': chatStore.currentSession?.id === session.id }"
            >
              <p class="text-xs font-semibold text-gray-800 dark:text-gray-200 truncate pr-2">{{ session.title || 'Untitled Chat' }}</p>
              <p class="text-[10px] font-mono text-gray-400 dark:text-gray-500 mt-1">{{ formatDate(session.updated_at) }}</p>
            </button>
          </div>

          <div class="p-3 border-t border-gray-100 dark:border-border/60">
            <button @click="handleClearHistory" class="w-full py-2 text-xs font-mono text-gray-400 hover:text-red-500 transition-colors">Clear All History</button>
          </div>
        </aside>
      </transition>

      <!-- Center Main: Lobe UI Agent Stream & Floating Composer -->
      <main class="flex-1 flex flex-col min-w-0 bg-[#F9F9FB] dark:bg-[#121214] relative">
        <div
          v-if="chatStore.messages.length === 0"
          class="absolute inset-0 z-0 pointer-events-none opacity-40 dark:opacity-20"
          style="background-image: radial-gradient(#9ca3af 1px, transparent 1px); background-size: 32px 32px;"
        ></div>

        <!-- Controls Toggles -->
        <div class="absolute top-3 left-3 z-50 flex items-center gap-2">
          <button @click="showHistory = !showHistory" class="p-2 bg-white/80 dark:bg-surface/80 backdrop-blur-md rounded-xl shadow-xs border border-gray-200/80 dark:border-border text-gray-600 hover:text-gray-900 transition-colors"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" /></svg></button>
          <div v-if="chatStore.currentSession" class="hidden sm:flex items-center space-x-2 px-3 py-1 bg-white/70 dark:bg-surface/70 rounded-full border border-gray-200/60 dark:border-gray-800 text-xs font-medium text-gray-600 dark:text-gray-300">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
            <span class="truncate max-w-xs font-mono">{{ chatStore.currentSession?.title || 'Active Session' }}</span>
          </div>
        </div>

        <div class="absolute top-3 right-3 z-10 lg:hidden">
          <button @click="showControls = !showControls" class="p-2 bg-white/80 dark:bg-surface/80 rounded-xl shadow-xs border border-gray-200/80 dark:border-border text-gray-600"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" /></svg></button>
        </div>

        <!-- Chat Stream Container -->
        <div v-if="chatStore.messages.length > 0" class="flex-1 overflow-y-auto p-4 md:p-8 scroll-smooth z-10 pt-16" ref="messagesContainer">
          <div class="space-y-6 max-w-3xl mx-auto">
            <template v-for="msg in chatStore.messages" :key="msg.id">
              <!-- User Message Card -->
              <div v-if="msg.role === 'user'" class="flex justify-end my-3">
                <div class="max-w-[85%] min-w-0 flex flex-col items-end">
                  <div class="bg-gradient-to-r from-[#D97757] to-[#e5896c] text-white px-5 py-3.5 rounded-2xl rounded-tr-xs shadow-xs text-sm md:text-base leading-relaxed">
                    <p class="whitespace-pre-wrap">{{ msg.content }}</p>
                  </div>
                  <div class="text-right mt-1 text-[10px] font-mono text-gray-400 tracking-wide mr-1 flex items-center space-x-1">
                    <span>{{ formatDate(msg.created_at).split(',')[1] || 'Now' }}</span>
                  </div>
                </div>
              </div>

              <!-- Assistant Message Card -->
              <AssistantMessageCard
                v-else-if="msg.role === 'assistant'"
                :message="msg"
                @copy="copyToClipboard(msg.content)"
                @feedback="(type) => handleFeedback(msg.id, type)"
                @open-source="handleOpenSource"
              />
            </template>
          </div>

          <!-- Live Agent Progress Rail -->
          <AgentProgressRail
            v-if="chatStore.thinking"
            class="max-w-3xl mx-auto mt-2"
            :steps="activeThinkingSteps"
            :turn-id="activeTurnId || ''"
            :waiting-for-first-step="waitingForFirstStep"
            :expanded="isThinkingExpanded(activeTurnId)"
            @toggle="toggleThinkingTurn(activeTurnId)"
          />
        </div>

        <!-- Floating Lobe UI Input Composer -->
        <div class="px-4 pt-2 pb-6 z-10" v-if="chatStore.messages.length > 0 && chatStore.currentSession">
          <div class="max-w-3xl mx-auto">
            <div class="bg-white/90 dark:bg-surface/90 backdrop-blur-lg rounded-2xl transition-all shadow-lg border border-gray-200/80 dark:border-gray-700/80 p-2.5">
              <textarea
                v-model="inputContent"
                @keydown.enter.prevent="handleSend"
                placeholder="Ask your Memwyre assistant..."
                rows="1"
                class="w-full bg-transparent border-0 focus:border-0 focus:ring-0 outline-none focus:outline-none rounded-xl px-3 py-2 text-sm md:text-base text-gray-900 dark:text-white resize-none max-h-36 placeholder-gray-400 font-sans"
              ></textarea>

              <div class="px-2 pt-2 border-t border-gray-100 dark:border-gray-800/80 flex justify-between items-center text-xs text-gray-500">
                <!-- Model Switcher Pill -->
                <div class="relative group inline-flex items-center px-2.5 py-1 rounded-lg bg-gray-100/80 dark:bg-gray-800/80 border border-gray-200/60 dark:border-gray-700">
                  <select
                    v-model="chatStore.selectedModel"
                    class="appearance-none bg-transparent border-none text-xs text-gray-800 dark:text-gray-200 font-medium font-sans cursor-pointer focus:ring-0 pr-5 hover:text-black dark:hover:text-white transition-colors"
                    title="Select AI Model"
                  >
                    <option v-for="model in chatStore.availableModels" :key="model.id" :value="model.id" class="text-gray-900 bg-white dark:bg-surface dark:text-gray-100">{{ model.name }}</option>
                  </select>
                  <svg class="w-3 h-3 absolute right-2 top-1/2 -translate-y-1/2 pointer-events-none text-gray-400 group-hover:text-gray-600 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                </div>

                <div class="flex items-center space-x-3">
                  <span class="hidden sm:inline-block text-[11px] font-mono text-gray-400">Enter to send</span>
                  <button
                    @click="handleSend"
                    :disabled="!inputContent.trim() || chatStore.thinking"
                    class="p-2 bg-[#D97757] text-white rounded-xl hover:bg-[#C4654A] disabled:opacity-50 transition-all active:scale-95 shadow-xs flex items-center justify-center w-8 h-8"
                  >
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" /></svg>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Empty State Hero Composer -->
        <div v-else class="flex-1 flex flex-col items-center justify-center p-4 z-10">
          <div class="max-w-2xl w-full">
            <div class="mb-6 text-center">
              <span class="px-3 py-1 rounded-full text-xs font-medium bg-[#D97757]/10 text-[#D97757] border border-[#D97757]/20 inline-block mb-3">Memwyre Agent</span>
              <h1 class="text-3xl font-bold text-gray-900 dark:text-white tracking-tight">
                Hello, <span class="text-[#D97757]">{{ authStore.user?.name || authStore.user?.email?.split('@')[0] || 'Traveler' }}</span>
              </h1>
              <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">What would you like to explore or search across your memories?</p>
            </div>

            <div class="bg-white/90 dark:bg-surface/90 backdrop-blur-xl rounded-2xl shadow-xl border border-gray-200/80 dark:border-gray-700/80 p-3">
              <textarea
                v-model="inputContent"
                @keydown.enter.prevent="handleSend"
                placeholder="Ask your Memwyre assistant..."
                rows="2"
                class="w-full bg-transparent border-0 focus:border-0 focus:ring-0 outline-none focus:outline-none rounded-xl px-4 py-3 text-base text-gray-900 dark:text-white resize-none min-h-[90px] placeholder-gray-400 font-sans"
              ></textarea>

              <div class="px-3 pt-2 border-t border-gray-100 dark:border-gray-800 flex justify-between items-center text-xs text-gray-500">
                <div class="relative group inline-flex items-center px-3 py-1.5 rounded-lg bg-gray-100/80 dark:bg-gray-800/80 border border-gray-200/60 dark:border-gray-700">
                  <select
                    v-model="chatStore.selectedModel"
                    class="appearance-none bg-transparent border-none text-xs text-gray-800 dark:text-gray-200 font-medium font-sans cursor-pointer focus:ring-0 pr-5 hover:text-black dark:hover:text-white transition-colors"
                    title="Select AI Model"
                  >
                    <option v-for="model in chatStore.availableModels" :key="model.id" :value="model.id" class="text-gray-900 bg-white dark:bg-surface dark:text-gray-100">{{ model.name }}</option>
                  </select>
                  <svg class="w-3 h-3 absolute right-2 top-1/2 -translate-y-1/2 pointer-events-none text-gray-400 group-hover:text-gray-600 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                </div>

                <button
                  @click="handleSend"
                  :disabled="!inputContent.trim() || chatStore.thinking"
                  class="px-4 py-2 bg-[#D97757] text-white font-medium rounded-xl hover:bg-[#C4654A] disabled:opacity-50 transition-all active:scale-95 shadow-md flex items-center justify-center space-x-2 text-xs"
                >
                  <span>Start Chat</span>
                  <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" /></svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </main>

      <!-- Right Panel: Lobe UI Context Rail -->
      <transition enter-active-class="transition-transform duration-300 ease-in-out" enter-from-class="translate-x-full" enter-to-class="translate-x-0" leave-active-class="transition-transform duration-300 ease-in-out" leave-from-class="translate-x-0" leave-to-class="translate-x-full">
        <aside v-if="showControls" class="w-80 bg-white/80 dark:bg-surface/80 backdrop-blur-md border-l border-gray-200/80 dark:border-border hidden lg:flex flex-col shrink-0">
          <div class="p-4 border-b border-gray-100 dark:border-border/60 flex justify-between items-center">
            <h3 class="font-semibold text-xs uppercase tracking-wider text-gray-500 dark:text-gray-400 font-mono">Retrieved Context</h3>
          </div>

          <div class="p-4 space-y-6 overflow-y-auto">
            <div>
              <div v-if="chatStore.currentContext.length > 0" class="space-y-2">
                <div v-for="(source, index) in chatStore.currentContext" :key="index" class="p-3 bg-gray-50/80 dark:bg-surface-2/60 rounded-xl border border-gray-200/60 dark:border-border flex justify-between items-center gap-2">
                  <div class="overflow-hidden">
                    <p class="text-xs text-black dark:text-white font-medium mb-0.5 truncate" :title="source.title || source">{{ source.title || source }}</p>
                    <span class="text-[10px] text-gray-400 font-mono">Memory / Context Source</span>
                  </div>
                  <button
                    v-if="source.id"
                    @click="router.push({ name: 'editor', params: { id: source.id } })"
                    class="shrink-0 text-xs px-2.5 py-1 rounded-lg border border-gray-200 dark:border-border bg-white dark:bg-surface text-gray-600 dark:text-text-secondary hover:text-[#D97757] transition-colors font-medium cursor-pointer"
                  >
                    Open
                  </button>
                </div>
              </div>

              <div v-else class="p-4 bg-gray-50/60 dark:bg-surface-2/40 rounded-xl border border-gray-200/60 dark:border-border/60 text-center">
                <p class="text-xs text-gray-400 font-mono italic">No active document context.</p>
                <p class="text-[11px] text-gray-400 mt-1">Retrieved sources will automatically appear here as the agent responds.</p>
              </div>
            </div>
          </div>
        </aside>
      </transition>
    </div>

    <ConfirmationModal
      :is-open="showDeleteModal"
      title="Clear History"
      message="Are you sure you want to delete all chat history? This cannot be undone."
      confirm-text="Clear History"
      @confirm="confirmClearHistory"
      @cancel="showDeleteModal = false"
    />
  </div>
</template>

<style scoped>
.overflow-y-auto::-webkit-scrollbar {
  width: 5px;
}
.overflow-y-auto::-webkit-scrollbar-track {
  background: transparent;
}
.overflow-y-auto::-webkit-scrollbar-thumb {
  background-color: rgba(156, 163, 175, 0.3);
  border-radius: 20px;
}
</style>
