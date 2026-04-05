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
      <div v-if="showOnboardingModal" class="fixed inset-0 z-[1200]">
        <div class="absolute inset-0 bg-black/45 backdrop-blur-sm"></div>

        <div class="relative h-screen w-screen flex items-center justify-center">
          <div class="w-[1120px] h-[760px] rounded-[30px] bg-white dark:bg-surface shadow-2xl">
            <div class="relative h-full overflow-hidden rounded-[30px] bg-white dark:bg-surface flex flex-col">
              <div class="relative px-6 sm:px-10 pt-8 pb-6 border-b border-gray-100 dark:border-gray-800">
                <div class="flex items-start justify-between gap-4">
                  <div class="flex items-center">
                    <div>
                      <p class="text-xl sm:text-2xl font-bold text-gray-900 dark:text-white">MemWyre Onboarding</p>
                      <p class="text-xs sm:text-sm text-gray-500 dark:text-gray-300">
                        {{ isVerified ? `Step ${onboardingStep} of 3` : 'Verify account before setup' }}
                      </p>
                    </div>
                  </div>
                </div>

                <div v-if="isVerified" class="mt-5">
                  <div class="h-2 rounded-full bg-gray-200 dark:bg-gray-700 overflow-hidden">
                    <div class="h-full bg-[#D97757] transition-all duration-300" :style="{ width: progressPercent + '%' }"></div>
                  </div>
                  <div class="mt-3 grid grid-cols-3 gap-2">
                    <button
                      v-for="step in 3"
                      :key="step"
                      @click="setStep(step)"
                      :disabled="step > maxUnlockedStep"
                      :class="[
                        'rounded-lg border px-3 py-2 text-left text-xs sm:text-sm transition-colors',
                        onboardingStep === step
                          ? 'border-gray-400 dark:border-gray-500 bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white'
                          : 'border-gray-200 dark:border-gray-700 bg-white dark:bg-surface text-gray-500 dark:text-gray-400',
                        step > maxUnlockedStep ? 'opacity-40 cursor-not-allowed' : ''
                      ]"
                    >
                      <div class="font-semibold">Step {{ step }}</div>
                      <div class="text-[11px] sm:text-xs mt-0.5">
                        {{ step === 1 ? 'AI work type' : step === 2 ? 'Browser extension' : 'First memory and tour' }}
                      </div>
                    </button>
                  </div>
                </div>
              </div>

              <div class="relative px-6 sm:px-10 py-6 sm:py-8 flex-1 overflow-y-auto">
                <template v-if="!isVerified">
                  <div class="rounded-2xl border border-[#EBC4B6] bg-[#FFF5F1] dark:bg-gray-800/70 p-6 sm:p-8">
                    <h3 class="text-2xl font-bold text-gray-900 dark:text-white">Verify your email first</h3>
                    <p class="mt-2 text-sm text-gray-600 dark:text-gray-300 max-w-2xl">
                      Email verification is required before we can finish onboarding and unlock the full workflow.
                      A verification link was sent to <strong>{{ user?.email }}</strong>.
                    </p>

                    <div class="mt-6 flex flex-wrap gap-3">
                      <button
                        @click="resendVerification"
                        :disabled="resendingVerification"
                        class="px-4 py-2.5 rounded-lg bg-[#D97757] text-white text-sm font-semibold hover:bg-[#C4654A] disabled:opacity-50"
                      >
                        {{ resendingVerification ? 'Sending...' : 'Resend verification email' }}
                      </button>
                      <button
                        @click="checkVerificationStatus"
                        :disabled="checkingVerification"
                        class="px-4 py-2.5 rounded-lg border border-[#D97757] text-[#D97757] text-sm font-semibold hover:bg-[#FFF5F1] disabled:opacity-50"
                      >
                        {{ checkingVerification ? 'Checking...' : "I've verified — Check status" }}
                      </button>
                    </div>

                    <p v-if="verificationPollActive" class="mt-3 text-xs text-gray-400 dark:text-gray-500">
                      Auto-checking every 8 seconds... {{ verificationCountdown }}s
                    </p>
                  </div>
                </template>

                <template v-else-if="onboardingStep === 1">
                  <div class="mb-5">
                    <h3 class="text-3xl font-bold tracking-tight text-gray-900 dark:text-white">Where do you do AI work first?</h3>
                    <p class="mt-2 text-sm sm:text-base text-gray-500 dark:text-gray-300">
                      Select one option. You can change this later.
                    </p>
                  </div>

                  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <button
                      v-for="option in aiWorkTypes"
                      :key="option.id"
                      @click="selectType(option.id)"
                      :class="[
                        'group rounded-2xl border p-4 sm:p-5 text-left transition-all',
                        selectedType === option.id
                          ? 'border-[#D97757] bg-[#FFF3EE] dark:bg-gray-800 shadow-[0_8px_20px_rgba(217,119,87,0.15)]'
                          : 'border-gray-200 dark:border-gray-700 bg-white dark:bg-surface hover:border-[#D97757]/50'
                      ]"
                    >
                      <div class="flex items-start justify-between gap-3">
                        <div class="flex items-start gap-3">
                          <div class="h-11 w-11 rounded-xl bg-[#FFF3EE] dark:bg-gray-700/80 flex items-center justify-center">
                            <svg v-if="option.id === 'conversation'" class="h-6 w-6 text-[#D97757] dark:text-[#F3D4C8]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M8 10h8M8 14h5M5 5h14a2 2 0 012 2v8a2 2 0 01-2 2H9l-4 4v-4H5a2 2 0 01-2-2V7a2 2 0 012-2z" />
                            </svg>
                            <svg v-else-if="option.id === 'prompt'" class="h-6 w-6 text-[#D97757] dark:text-[#F3D4C8]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M6 18l8-8m0 0l2-2a2.828 2.828 0 114 4l-2 2m-4-4l4 4M5 20h4l9-9" />
                            </svg>
                            <svg v-else-if="option.id === 'webpage'" class="h-6 w-6 text-[#D97757] dark:text-[#F3D4C8]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M3 6h18M8 3v3m8-3v3M5 6h14a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2z" />
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M7 11h4m-4 4h7" />
                            </svg>
                            <svg v-else class="h-6 w-6 text-[#D97757] dark:text-[#F3D4C8]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M7 3h10a2 2 0 012 2v16l-7-4-7 4V5a2 2 0 012-2z" />
                            </svg>
                          </div>
                          <div>
                            <p class="text-lg font-semibold text-gray-900 dark:text-white">{{ option.label }}</p>
                            <p class="text-sm text-gray-500 dark:text-gray-300 mt-1">{{ option.description }}</p>
                          </div>
                        </div>
                        <div
                          :class="[
                            'mt-1 h-6 w-6 rounded-full border flex items-center justify-center',
                            selectedType === option.id
                              ? 'border-[#D97757] bg-[#D97757] text-white'
                              : 'border-gray-300 dark:border-gray-600 text-transparent'
                          ]"
                        >
                          <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                          </svg>
                        </div>
                      </div>
                    </button>
                  </div>
                </template>

                <template v-else-if="onboardingStep === 2">
                  <div class="h-full flex flex-col">
                    <div class="mb-5">
                      <h3 class="text-3xl font-bold tracking-tight text-gray-900 dark:text-white">Install extension in Chrome or Edge</h3>
                      <p class="mt-2 text-sm sm:text-base text-gray-500 dark:text-gray-300">
                        This gives one-click capture from AI chats and webpages.
                      </p>
                    </div>

                    <div class="grid grid-cols-2 gap-4 flex-1">
                      <button
                        v-for="choice in extensionOptions"
                        :key="choice.id"
                        @click="handleExtensionChoice(choice)"
                        class="rounded-2xl border border-gray-200 dark:border-gray-700 bg-white dark:bg-surface hover:border-gray-400 dark:hover:border-gray-500 hover:shadow-md p-6 sm:p-8 text-left transition-all h-full flex flex-col items-center justify-center gap-4 group"
                      >
                        <div class="h-16 w-16 rounded-2xl bg-gray-100 dark:bg-gray-800 flex items-center justify-center group-hover:bg-gray-200 dark:group-hover:bg-gray-700 transition-colors">
                          <img
                            :src="choice.logo"
                            :alt="choice.label"
                            class="h-8 w-8 object-contain"
                          />
                        </div>
                        <div class="text-center">
                          <p class="text-xl font-bold text-gray-900 dark:text-white">{{ choice.label }}</p>
                          <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">{{ choice.description }}</p>
                        </div>
                      </button>
                    </div>
                  </div>
                </template>

                <template v-else>
                  <div class="mb-5">
                    <h3 class="text-3xl font-bold tracking-tight text-gray-900 dark:text-white">Create your first {{ selectedTypeLabel.toLowerCase() }}</h3>
                    <p class="mt-2 text-sm sm:text-base text-gray-500 dark:text-gray-300">
                      Start now, then finish onboarding.
                    </p>
                  </div>

                  <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
                    <div class="rounded-2xl border border-gray-200 dark:border-gray-700 bg-white dark:bg-surface p-5">
                      <p class="text-sm font-semibold text-gray-800 dark:text-gray-100">Selected work type</p>
                      <p class="mt-1 text-2xl font-bold text-gray-900 dark:text-white">{{ selectedTypeLabel }}</p>
                      <p class="mt-2 text-sm text-gray-500 dark:text-gray-300">{{ selectedTypeHint }}</p>
                    </div>

                    <div class="rounded-2xl border border-gray-200 dark:border-gray-700 bg-white dark:bg-surface p-5">
                      <p class="text-sm font-semibold text-gray-800 dark:text-gray-100">Status</p>
                      <p v-if="firstActionDone" class="mt-2 text-green-700 dark:text-green-400 font-semibold">
                        First action completed. You can finish onboarding.
                      </p>
                      <p v-else class="mt-2 text-gray-500 dark:text-gray-300">
                        First action not completed yet. Click the primary button to start.
                      </p>

                      <button
                        @click="startTour"
                        class="mt-4 px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-600 text-sm font-semibold text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-800"
                      >
                        {{ hasCompletedTour ? 'Run tour again' : 'Start optional tour' }}
                      </button>
                    </div>
                  </div>
                </template>
              </div>

              <div class="relative px-6 sm:px-10 py-4 border-t border-gray-100 dark:border-gray-800 flex items-center justify-between">
                <button
                  v-if="isVerified && onboardingStep > 1"
                  @click="previousStep"
                  class="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-gray-300 dark:border-gray-600 text-sm font-semibold text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-800"
                >
                  <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7" />
                  </svg>
                  Back
                </button>
                <div v-else></div>

                <button
                  v-if="isVerified"
                  @click="handlePrimaryAction"
                  :disabled="!canRunPrimaryAction"
                  class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-[#D97757] text-white text-sm sm:text-base font-semibold hover:bg-[#C4654A] disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {{ primaryActionLabel }}
                  <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
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

const startTour = () => {
  if (onboardingStorageReady.value) {
    writeScopedBoolean(localStorage, user.value.id, 'tour_completed', false);
    writeScopedBoolean(localStorage, user.value.id, 'tour_requested', true);
  }
  hasCompletedTour.value = false;
  // Close the modal first so the tour can highlight elements underneath
  authStore.completeOnboarding();
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

const completeOnboarding = (message, requireReady = true) => {
  if (requireReady && (!selectedType.value || !extensionChoice.value || !firstActionDone.value)) return;
  authStore.completeOnboarding();
  if (onboardingStorageReady.value) {
    writeScopedBoolean(localStorage, user.value.id, 'tour_requested', false);
  }
  if (message) toast.success(message);
};

const skipOnboarding = () => {
  completeOnboarding('Onboarding skipped for now.', false);
};

const handlePrimaryAction = () => {
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

