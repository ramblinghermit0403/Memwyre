<template>
  <div class="h-screen flex flex-col transition-colors duration-300 font-sans overflow-hidden">
    <NavBar />

    <main class="flex-1 overflow-y-auto lg:overflow-hidden w-full pt-6 pb-10 lg:pb-6 no-scrollbar">
      <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 flex flex-col min-h-full lg:h-full lg:min-h-0">
        <div class="mb-6 shrink-0" id="tour-welcome">
          <h1 class="text-3xl font-bold text-gray-900 dark:text-white">Good {{ timeOfDay }}, {{ user?.name || 'User' }}</h1>
          <p class="mt-1 text-gray-500 dark:text-text-secondary">This is where your AI work lives.</p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 flex-1 min-h-0">
          <div class="lg:col-span-8 min-h-0">
            <div id="tour-timeline" class="bg-white dark:bg-surface rounded-xl shadow-sm border border-gray-100 dark:border-border overflow-hidden h-[640px] lg:h-full min-h-0">
              <AIInteractionTimeline ref="timelineRef" :focus-today="focusToday" @open-item="openItem" />
            </div>
          </div>

          <div class="lg:col-span-4 min-h-0">
            <div class="bg-white dark:bg-surface rounded-xl shadow-sm border border-gray-100 dark:border-border overflow-hidden h-[640px] lg:h-full min-h-0">
              <DashboardInboxList />
            </div>
          </div>
        </div>
      </div>
    </main>

    <QuickActions @open-review="showDailyReview = true" />
    <DailyReviewModal v-if="showDailyReview" @close="showDailyReview = false" />

    <Teleport to="body">
      <transition enter-active-class="transition duration-300 ease-out" enter-from-class="opacity-0 scale-95" enter-to-class="opacity-100 scale-100" leave-active-class="transition duration-200 ease-in" leave-from-class="opacity-100 scale-100" leave-to-class="opacity-0 scale-95">
        <div v-if="showOnboardingModal" class="fixed inset-0 z-[1200] flex items-center justify-center p-4 sm:p-6">
          <!-- Backdrop -->
          <div class="absolute inset-0 bg-black/60 backdrop-blur-md transition-opacity"></div>

          <!-- Modal Content -->
          <div class="relative w-full max-w-4xl max-h-[90vh] bg-white dark:bg-surface rounded-[2rem] shadow-2xl overflow-hidden flex flex-col border border-gray-100 dark:border-border">
            
            <!-- Header -->
            <div class="px-8 sm:px-10 py-6 border-b border-gray-100 dark:border-border bg-gray-50/50 dark:bg-surface-2/30 flex items-center justify-between shrink-0">
              <div class="flex items-center gap-4">
                <img src="/image.svg" alt="Memwyre" class="w-10 h-10 rounded-xl shadow-sm" />
                <div>
                  <h2 class="text-xl font-bold text-gray-900 dark:text-white tracking-tight">Welcome to Memwyre</h2>
                  <p class="text-sm text-gray-500 dark:text-text-secondary font-medium">
                    {{ isVerified ? `Step ${onboardingStep} of 3` : 'Account Verification' }}
                  </p>
                </div>
              </div>
              
              <!-- Simple Stepper -->
              <div v-if="isVerified" class="hidden sm:flex items-center gap-2">
                <div v-for="step in 3" :key="step" class="flex items-center">
                  <div 
                    class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold transition-all duration-300"
                    :class="[
                      onboardingStep === step ? 'bg-primary text-white shadow-md' : 
                      step < onboardingStep ? 'bg-primary/20 text-primary dark:bg-primary/10' : 
                      'bg-gray-100 text-gray-400 dark:bg-gray-800 dark:text-gray-600'
                    ]"
                  >
                    {{ step < onboardingStep ? '✓' : step }}
                  </div>
                  <div v-if="step < 3" class="w-6 h-[2px] mx-1 rounded-full" :class="step < onboardingStep ? 'bg-primary/30' : 'bg-gray-100 dark:bg-gray-800'"></div>
                </div>
              </div>
            </div>

            <!-- Scrollable Body -->
            <div class="flex-1 overflow-y-auto px-6 sm:px-12 py-8 custom-scrollbar">
              
              <!-- Verification Step -->
              <template v-if="!isVerified">
                <div class="max-w-2xl mx-auto text-center py-8">
                  <div class="w-20 h-20 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-6">
                    <svg class="w-10 h-10 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                    </svg>
                  </div>
                  <h3 class="text-3xl font-bold text-gray-900 dark:text-white tracking-tight mb-4">Check your inbox</h3>
                  <p class="text-lg text-gray-600 dark:text-text-secondary mb-8 leading-relaxed">
                    We've sent a secure verification link to <strong class="text-gray-900 dark:text-white">{{ user?.email }}</strong>. 
                    Please verify your email to unlock your workspace and secure your vault.
                  </p>

                  <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                    <button
                      @click="checkVerificationStatus"
                      :disabled="checkingVerification"
                      class="w-full sm:w-auto px-8 py-3.5 rounded-xl bg-primary text-white font-semibold shadow-lg shadow-primary/30 hover:bg-primary-600 hover:shadow-primary/40 hover:-translate-y-0.5 transition-all disabled:opacity-50 disabled:hover:translate-y-0"
                    >
                      <span class="flex items-center justify-center gap-2">
                        <svg v-if="checkingVerification" class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                        {{ checkingVerification ? 'Checking...' : "I've verified my email" }}
                      </span>
                    </button>
                    <button
                      @click="resendVerification"
                      :disabled="resendingVerification"
                      class="w-full sm:w-auto px-6 py-3.5 rounded-xl border border-gray-200 dark:border-border text-gray-700 dark:text-text-primary font-semibold hover:bg-gray-50 dark:hover:bg-surface-2 transition-colors disabled:opacity-50"
                    >
                      {{ resendingVerification ? 'Sending...' : 'Resend link' }}
                    </button>
                  </div>

                  <p v-if="verificationPollActive" class="mt-8 text-sm text-gray-400 font-medium flex items-center justify-center gap-2">
                    <span class="relative flex h-2.5 w-2.5">
                      <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-primary opacity-75"></span>
                      <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-primary"></span>
                    </span>
                    Waiting for verification...
                  </p>
                </div>
              </template>

              <!-- Step 1: Work Type -->
              <template v-else-if="onboardingStep === 1">
                <div class="text-center max-w-2xl mx-auto mb-10">
                  <h3 class="text-3xl font-bold tracking-tight text-gray-900 dark:text-white">What's your primary AI workflow?</h3>
                  <p class="mt-3 text-lg text-gray-500 dark:text-text-secondary">
                    Select the type of context you capture most often. This helps us tailor your default editor view.
                  </p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 max-w-4xl mx-auto">
                  <button
                    v-for="option in aiWorkTypes"
                    :key="option.id"
                    @click="selectType(option.id)"
                    class="group relative p-6 rounded-2xl border-2 text-left transition-all duration-300 hover:shadow-xl hover:-translate-y-1 overflow-hidden"
                    :class="[
                      selectedType === option.id
                        ? 'border-primary bg-primary/5 shadow-lg shadow-primary/10 dark:bg-primary/10'
                        : 'border-gray-100 dark:border-gray-800 bg-white dark:bg-surface hover:border-primary/40'
                    ]"
                  >
                    <!-- Selection Indicator -->
                    <div class="absolute top-6 right-6">
                      <div class="w-6 h-6 rounded-full border-2 flex items-center justify-center transition-colors"
                        :class="selectedType === option.id ? 'border-primary bg-primary' : 'border-gray-300 dark:border-gray-600'">
                        <svg class="w-3.5 h-3.5 text-white opacity-0 transition-opacity" :class="{'opacity-100': selectedType === option.id}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                        </svg>
                      </div>
                    </div>

                    <div class="flex items-start gap-5">
                      <div class="w-14 h-14 shrink-0 rounded-2xl flex items-center justify-center transition-colors"
                        :class="selectedType === option.id ? 'bg-primary text-white shadow-inner' : 'bg-gray-50 dark:bg-gray-800 text-gray-500 dark:text-gray-400 group-hover:text-primary'">
                        <svg v-if="option.id === 'conversation'" class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M8 10h8M8 14h5M5 5h14a2 2 0 012 2v8a2 2 0 01-2 2H9l-4 4v-4H5a2 2 0 01-2-2V7a2 2 0 012-2z" />
                        </svg>
                        <svg v-else-if="option.id === 'prompt'" class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M6 18l8-8m0 0l2-2a2.828 2.828 0 114 4l-2 2m-4-4l4 4M5 20h4l9-9" />
                        </svg>
                        <svg v-else-if="option.id === 'webpage'" class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M3 6h18M8 3v3m8-3v3M5 6h14a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2z" />
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M7 11h4m-4 4h7" />
                        </svg>
                        <svg v-else class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M7 3h10a2 2 0 012 2v16l-7-4-7 4V5a2 2 0 012-2z" />
                        </svg>
                      </div>
                      <div class="pr-8">
                        <h4 class="text-xl font-bold text-gray-900 dark:text-white mb-1">{{ option.label }}</h4>
                        <p class="text-sm text-gray-500 dark:text-text-secondary leading-relaxed">{{ option.description }}</p>
                      </div>
                    </div>
                  </button>
                </div>
              </template>

              <!-- Step 2: Extension -->
              <template v-else-if="onboardingStep === 2">
                <div class="text-center max-w-2xl mx-auto mb-10">
                  <h3 class="text-3xl font-bold tracking-tight text-gray-900 dark:text-white">Install the Browser Extension</h3>
                  <p class="mt-3 text-lg text-gray-500 dark:text-text-secondary">
                    The extension is the core of the Memwyre experience, enabling one-click capture from ChatGPT, Claude, and any webpage.
                  </p>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-3xl mx-auto">
                  <button
                    v-for="choice in extensionOptions"
                    :key="choice.id"
                    @click="handleExtensionChoice(choice)"
                    class="group relative p-8 rounded-[2rem] border-2 border-gray-100 dark:border-gray-800 bg-white dark:bg-surface hover:border-primary/50 hover:shadow-2xl hover:shadow-primary/10 hover:-translate-y-1 transition-all duration-300 flex flex-col items-center justify-center text-center overflow-hidden"
                  >
                    <!-- Background Glow -->
                    <div class="absolute inset-0 bg-gradient-to-b from-transparent to-gray-50 dark:to-gray-800/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>

                    <div class="w-24 h-24 mb-6 relative z-10">
                      <div class="absolute inset-0 bg-gray-100 dark:bg-gray-800 rounded-3xl rotate-3 group-hover:rotate-6 transition-transform duration-300"></div>
                      <div class="absolute inset-0 bg-white dark:bg-surface border border-gray-200 dark:border-gray-700 rounded-3xl -rotate-3 group-hover:-rotate-6 transition-transform duration-300 flex items-center justify-center shadow-lg">
                        <img :src="choice.logo" :alt="choice.label" class="w-12 h-12 object-contain drop-shadow-sm" />
                      </div>
                    </div>
                    
                    <h4 class="text-2xl font-bold text-gray-900 dark:text-white mb-2 relative z-10">{{ choice.label }}</h4>
                    <p class="text-gray-500 dark:text-text-secondary relative z-10">{{ choice.description }}</p>
                  </button>
                </div>
              </template>

              <!-- Step 3: First Action -->
              <template v-else>
                <div class="text-center max-w-2xl mx-auto mb-8">
                  <h3 class="text-3xl font-bold tracking-tight text-gray-900 dark:text-white">Create your first {{ selectedTypeLabel.toLowerCase() }}</h3>
                  <p class="mt-3 text-lg text-gray-500 dark:text-text-secondary">
                    You're almost done. Click the button below to add your first piece of context to the vault.
                  </p>
                </div>

                <div class="max-w-2xl mx-auto">
                  <div class="bg-gray-50 dark:bg-surface-2 rounded-3xl p-8 border border-gray-100 dark:border-border relative overflow-hidden">
                    <!-- Status Ring -->
                    <div class="absolute top-0 right-0 p-8 hidden sm:block">
                      <div class="w-16 h-16 rounded-full flex items-center justify-center border-4 transition-colors duration-500"
                        :class="firstActionDone ? 'border-green-500 bg-green-50 text-green-600 dark:bg-green-900/30' : 'border-gray-200 dark:border-gray-700 text-gray-400 bg-white dark:bg-surface'">
                        <svg v-if="firstActionDone" class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                        </svg>
                        <svg v-else class="w-8 h-8 animate-pulse" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                        </svg>
                      </div>
                    </div>

                    <h4 class="text-xl font-bold text-gray-900 dark:text-white mb-2">Workflow Selected: {{ selectedTypeLabel }}</h4>
                    <p class="text-gray-600 dark:text-text-secondary max-w-md mb-8">{{ selectedTypeHint }}</p>

                    <div v-if="firstActionDone" class="bg-green-50 dark:bg-green-900/20 text-green-700 dark:text-green-400 px-5 py-4 rounded-xl border border-green-200 dark:border-green-800/50 flex items-center gap-3 font-medium">
                      <svg class="w-6 h-6 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                      First action successfully recorded! You're ready to proceed.
                    </div>
                    <div v-else>
                      <button @click="startFirstAction" class="inline-flex items-center gap-3 px-6 py-3.5 rounded-xl bg-gray-900 dark:bg-white text-white dark:text-gray-900 font-bold shadow-lg hover:scale-[1.02] transition-transform">
                        <span>Capture your first {{ selectedTypeLabel.toLowerCase() }}</span>
                        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                        </svg>
                      </button>
                    </div>

                    <div class="mt-8 pt-8 border-t border-gray-200 dark:border-border">
                      <p class="text-sm font-semibold text-gray-900 dark:text-white mb-2">Want to learn the ropes?</p>
                      <button
                        @click="startTour"
                        class="text-primary font-medium hover:text-primary-600 flex items-center gap-1 transition-colors"
                      >
                        <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" />
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        {{ hasCompletedTour ? 'Restart interactive tour' : 'Start interactive tour' }}
                      </button>
                    </div>
                  </div>
                </div>
              </template>
            </div>

            <!-- Footer / Actions -->
            <div class="px-8 sm:px-10 py-5 border-t border-gray-100 dark:border-border bg-gray-50/50 dark:bg-surface-2/30 flex items-center justify-between shrink-0">
              <button
                v-if="isVerified && onboardingStep > 1"
                @click="previousStep"
                class="px-6 py-2.5 rounded-xl text-gray-600 dark:text-text-secondary font-semibold hover:bg-gray-200 dark:hover:bg-surface-2 transition-colors"
              >
                Back
              </button>
              <div v-else></div>

              <button
                v-if="isVerified"
                @click="handlePrimaryAction"
                :disabled="!canRunPrimaryAction"
                class="flex items-center gap-2 px-8 py-3 rounded-xl bg-primary text-white font-bold shadow-lg shadow-primary/20 hover:bg-primary-600 hover:shadow-primary/40 hover:-translate-y-0.5 transition-all disabled:opacity-50 disabled:hover:translate-y-0 disabled:shadow-none"
              >
                {{ primaryActionLabel }}
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </transition>
    </Teleport>
  </div>
</template>

<script setup>
import { computed, onMounted, onUnmounted, ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';
import NavBar from '../components/NavBar.vue';
import QuickActions from '../components/QuickActions.vue';
import DashboardInboxList from '../components/DashboardInboxList.vue';
import DailyReviewModal from '../components/DailyReviewModal.vue';
import AIInteractionTimeline from '../components/AIInteractionTimeline.vue';
import { createTour } from '../tour';
import { useInboxStore } from '../stores/inbox';
import { useAuthStore } from '../stores/auth';
import api from '../services/api';
import chromeLogo from '../assets/chrome-logo-svgrepo-com.svg';
import edgeLogo from '../assets/microsoft-edge-logo.svg';
import {
  migrateOnboardingLegacyState,
  readScopedBoolean,
  readScopedString,
  writeScopedBoolean,
  writeScopedString,
} from '../utils/onboardingState';

const route = useRoute();
const router = useRouter();
const toast = useToast();
const inboxStore = useInboxStore();
const authStore = useAuthStore();

const user = computed(() => authStore.user);
const isVerified = computed(() => !!user.value?.is_verified);
const showDailyReview = ref(false);
const timelineRef = ref(null);
const resendingVerification = ref(false);
const checkingVerification = ref(false);
const verificationPollActive = ref(false);
const verificationCountdown = ref(8);
let _verificationPollTimer = null;
let _verificationCountdownTimer = null;

const onboardingStep = ref(1);
const selectedType = ref('');
const firstActionDone = ref(false);
const firstActionStartedAt = ref('');
const hasCompletedTour = ref(false);
const extensionChoice = ref('');

const aiWorkTypes = [
  { id: 'conversation', label: 'Conversation', description: 'Save an AI chat exchange.' },
  { id: 'prompt', label: 'Prompt', description: 'Store a reusable prompt template.' },
  { id: 'webpage', label: 'Webpage', description: 'Ingest a web page as memory context.' },
  { id: 'memory', label: 'Memory', description: 'Create a standalone memory note.' },
];

const extensionOptions = [
  {
    id: 'chrome',
    label: 'I use Chrome',
    description: 'Install from the Chrome Web Store.',
    logo: chromeLogo,
    url: 'https://chromewebstore.google.com/detail/memwyre/biplnkodgfdgejgblohhjeckiclfpekn',
  },
  {
    id: 'edge',
    label: 'I use Edge',
    description: 'Install from Microsoft Edge Add-ons.',
    logo: edgeLogo,
    url: 'https://microsoftedge.microsoft.com/addons/detail/memwyre/ihibkjgaiafhhbjmchmkphlkomodkmpd',
  },
];

const focusToday = computed(() => route.query.view === 'today');
const showOnboardingModal = computed(() => authStore.isAuthenticated && !authStore.hasCompletedOnboarding);

const selectedTypeLabel = computed(
  () => aiWorkTypes.find((item) => item.id === selectedType.value)?.label || 'AI work',
);

const selectedTypeHint = computed(() => {
  if (selectedType.value === 'webpage') return 'This opens the existing webpage ingestion flow.';
  if (selectedType.value === 'prompt') return 'The editor will open with prompt type selected.';
  if (selectedType.value === 'conversation') return 'The editor will open with conversation type selected.';
  return 'The editor will open with memory type selected.';
});

const progressPercent = computed(() => {
  const step = Math.max(1, Math.min(3, onboardingStep.value || 1));
  return Math.round((step / 3) * 100);
});

const maxUnlockedStep = computed(() => {
  if (!selectedType.value) return 1;
  if (!extensionChoice.value) return 2;
  return 3;
});

const canRunPrimaryAction = computed(() => {
  if (onboardingStep.value === 1) return !!selectedType.value;
  if (onboardingStep.value === 2) return !!extensionChoice.value;
  return !!selectedType.value && !!extensionChoice.value;
});

const primaryActionLabel = computed(() => {
  if (onboardingStep.value === 1) return 'Continue';
  if (onboardingStep.value === 2) return 'Continue';
  if (!firstActionDone.value) return 'Start first action';
  return 'Finish onboarding';
});

const onboardingStorageReady = computed(() => !!user.value?.id && typeof localStorage !== 'undefined');

const onboardingNow = () => new Date().toISOString().replace('Z', '');

const persistOnboardingStep = () => {
  if (!onboardingStorageReady.value) return;
  writeScopedString(localStorage, user.value.id, 'step', onboardingStep.value);
};

const setStep = (step) => {
  const target = Math.max(1, Math.min(3, Number(step) || 1));
  if (target > maxUnlockedStep.value) return;
  onboardingStep.value = target;
  persistOnboardingStep();
};

const previousStep = () => {
  setStep(onboardingStep.value - 1);
};

const selectType = (typeId) => {
  selectedType.value = typeId;
  if (!onboardingStorageReady.value) return;
  writeScopedString(localStorage, user.value.id, 'selected_type', typeId);
};

const setExtensionChoice = (choice) => {
  extensionChoice.value = choice;
  if (!onboardingStorageReady.value) return;
  writeScopedString(localStorage, user.value.id, 'extension_choice', choice);
};

const handleExtensionChoice = (choice) => {
  if (!choice) return;
  setExtensionChoice(choice.id);
  if (choice.url) {
    window.open(choice.url, '_blank', 'noopener,noreferrer');
  }
};

const hydrateOnboardingState = () => {
  if (!onboardingStorageReady.value) return;

  migrateOnboardingLegacyState(localStorage, user.value.id);

  const storedType = readScopedString(localStorage, user.value.id, 'selected_type', '');
  selectedType.value = aiWorkTypes.some((item) => item.id === storedType) ? storedType : '';
  firstActionDone.value = readScopedBoolean(localStorage, user.value.id, 'first_action_done', false);
  firstActionStartedAt.value = readScopedString(localStorage, user.value.id, 'first_action_started_at', '');
  hasCompletedTour.value = readScopedBoolean(localStorage, user.value.id, 'tour_completed', false);
  extensionChoice.value = readScopedString(localStorage, user.value.id, 'extension_choice', '');

  const rawStep = Number.parseInt(readScopedString(localStorage, user.value.id, 'step', '1'), 10);
  onboardingStep.value = Number.isFinite(rawStep) ? rawStep : 1;

  if (!selectedType.value) onboardingStep.value = 1;
  else if (!extensionChoice.value) onboardingStep.value = Math.max(2, onboardingStep.value);
  else onboardingStep.value = 3;

  persistOnboardingStep();
};

const runTour = () => {
  setTimeout(() => {
    const driver = createTour();
    driver.drive();
    if (onboardingStorageReady.value) {
      writeScopedBoolean(localStorage, user.value.id, 'tour_completed', true);
      writeScopedBoolean(localStorage, user.value.id, 'tour_requested', false);
    }
    hasCompletedTour.value = true;
  }, 250);
};

const startTour = async () => {
  if (onboardingStorageReady.value) {
    writeScopedBoolean(localStorage, user.value.id, 'tour_completed', false);
    writeScopedBoolean(localStorage, user.value.id, 'tour_requested', true);
  }
  hasCompletedTour.value = false;
  // Close the modal first so the tour can highlight elements underneath
  await authStore.completeOnboarding();
  runTour();
};

const refreshFirstActionCompletion = async () => {
  if (!showOnboardingModal.value || !isVerified.value || !selectedType.value) return;
  if (firstActionDone.value) return;

  try {
    const params = {
      view: 'timeline',
      limit: 1,
      interaction_type: selectedType.value,
    };
    if (firstActionStartedAt.value) params.date_from = firstActionStartedAt.value;

    const response = await api.get('/memory/', { params });
    const hasCreatedItem = (response.data || []).some((item) => String(item.id || '').startsWith('mem_'));
    if (!hasCreatedItem) return;

    firstActionDone.value = true;
    if (onboardingStorageReady.value) {
      writeScopedBoolean(localStorage, user.value.id, 'first_action_done', true);
    }
    toast.success('First action completed.');
  } catch (error) {
    console.error('Failed to verify onboarding first action completion', error);
  }
};

const startFirstAction = () => {
  if (!selectedType.value || !onboardingStorageReady.value) return;

  firstActionStartedAt.value = onboardingNow();
  writeScopedString(localStorage, user.value.id, 'first_action_started_at', firstActionStartedAt.value);
  writeScopedString(localStorage, user.value.id, 'selected_type', selectedType.value);

  if (selectedType.value === 'webpage') {
    router.push({
      path: '/dashboard',
      query: {
        ...route.query,
        quick_add: 'webpage',
      },
    });
    return;
  }

  router.push(`/editor/new?interaction_type=${selectedType.value}&source_app=web-app`);
};

const completeOnboarding = async (message, requireReady = true) => {
  if (requireReady && (!selectedType.value || !extensionChoice.value || !firstActionDone.value)) return;
  await authStore.completeOnboarding();
  if (onboardingStorageReady.value) {
    writeScopedBoolean(localStorage, user.value.id, 'tour_requested', false);
  }
  if (message) toast.success(message);
};

const skipOnboarding = async () => {
  await completeOnboarding('Onboarding skipped for now.', false);
};

const handlePrimaryAction = async () => {
  if (onboardingStep.value === 1 && selectedType.value) {
    onboardingStep.value = 2;
    persistOnboardingStep();
    return;
  }

  if (onboardingStep.value === 2 && extensionChoice.value) {
    onboardingStep.value = 3;
    persistOnboardingStep();
    return;
  }

  if (onboardingStep.value === 3) {
    if (!firstActionDone.value) {
      startFirstAction();
      return;
    }
    completeOnboarding('Onboarding completed.');
  }
};

const timeOfDay = computed(() => {
  const hour = new Date().getHours();
  if (hour < 12) return 'Morning';
  if (hour < 18) return 'Afternoon';
  return 'Evening';
});

const openItem = (item) => {
  if (!item?.id) return;
  router.push(`/editor/${item.id}`);
};

inboxStore.fetchInbox();
inboxStore.connectWebSocket();

const resendVerification = async () => {
  if (resendingVerification.value) return;
  resendingVerification.value = true;
  try {
    await api.post('/auth/resend-verification');
    toast.success('Verification email sent. Please check your inbox.');
    startVerificationPolling();
  } catch (err) {
    toast.error(err.response?.data?.detail || 'Failed to resend verification email.');
  } finally {
    resendingVerification.value = false;
  }
};

const checkVerificationStatus = async () => {
  if (checkingVerification.value) return;
  checkingVerification.value = true;
  try {
    await authStore.fetchUser();
    if (isVerified.value) {
      stopVerificationPolling();
      toast.success('Email verified! Continuing onboarding.');
    } else {
      toast.info('Email not yet verified. Please check your inbox.');
    }
  } catch (err) {
    toast.error('Failed to check verification status.');
  } finally {
    checkingVerification.value = false;
  }
};

const startVerificationPolling = () => {
  if (verificationPollActive.value) return;
  verificationPollActive.value = true;
  verificationCountdown.value = 8;

  _verificationCountdownTimer = setInterval(() => {
    verificationCountdown.value -= 1;
    if (verificationCountdown.value <= 0) {
      verificationCountdown.value = 8;
    }
  }, 1000);

  _verificationPollTimer = setInterval(async () => {
    if (isVerified.value) {
      stopVerificationPolling();
      return;
    }
    try {
      await authStore.fetchUser();
      if (isVerified.value) {
        stopVerificationPolling();
        toast.success('Email verified! Continuing onboarding.');
      }
    } catch (e) { /* silent */ }
  }, 8000);
};

const stopVerificationPolling = () => {
  verificationPollActive.value = false;
  clearInterval(_verificationPollTimer);
  clearInterval(_verificationCountdownTimer);
  _verificationPollTimer = null;
  _verificationCountdownTimer = null;
};

watch(
  () => user.value?.id,
  () => {
    hydrateOnboardingState();
    refreshFirstActionCompletion();
  },
);

watch(
  () => route.fullPath,
  () => {
    refreshFirstActionCompletion();
  },
);

onMounted(() => {
  hydrateOnboardingState();
  if (onboardingStorageReady.value && readScopedBoolean(localStorage, user.value.id, 'tour_requested', false)) {
    runTour();
  }
  refreshFirstActionCompletion();
  // Start polling for email verification if modal is shown and not yet verified
  if (showOnboardingModal.value && !isVerified.value) {
    startVerificationPolling();
  }
});

// Stop polling when component unmounts
onUnmounted(() => {
  stopVerificationPolling();
});

// Watch: if verification is detected via any means, stop polling
watch(isVerified, (verified) => {
  if (verified) stopVerificationPolling();
});
</script>

