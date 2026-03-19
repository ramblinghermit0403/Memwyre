<template>
  <div class="h-screen flex flex-col transition-colors duration-300 font-sans overflow-hidden">
    <NavBar />

    <main class="flex-1 overflow-y-auto lg:overflow-hidden w-full pt-6 pb-10 lg:pb-6 no-scrollbar">
      <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 flex flex-col min-h-full lg:h-full lg:min-h-0">
        <div class="mb-6 shrink-0" id="tour-welcome">
          <h1 class="text-3xl font-bold text-gray-900 dark:text-white">Good {{ timeOfDay }}, {{ user?.name || 'User' }}</h1>
          <p class="mt-1 text-gray-500 dark:text-text-secondary">This is where your AI work lives.</p>
        </div>

        <div
          v-if="showOnboardingCard"
          class="mb-6 shrink-0 rounded-xl border border-[#E8CFC6] bg-[#FFF7F3] dark:bg-surface dark:border-border p-5"
        >
          <template v-if="!isVerified">
            <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
              <div>
                <h2 class="text-lg font-semibold text-gray-900 dark:text-white">Verify your email to finish setup</h2>
                <p class="mt-1 text-sm text-gray-600 dark:text-gray-300">
                  Your account is created, but email verification is required before full onboarding.
                </p>
              </div>
              <div class="flex flex-wrap gap-2">
                <button
                  @click="resendVerification"
                  :disabled="resendingVerification"
                  class="px-4 py-2 rounded-lg bg-[#D97757] text-white text-sm font-semibold hover:bg-[#C4654A] disabled:opacity-50"
                >
                  {{ resendingVerification ? 'Sending...' : 'Resend verification' }}
                </button>
                <button
                  @click="router.push('/settings')"
                  class="px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-600 text-sm font-semibold text-gray-700 dark:text-gray-200 hover:bg-white dark:hover:bg-gray-800"
                >
                  Go to settings
                </button>
                <button
                  @click="skipOnboarding"
                  class="px-4 py-2 rounded-lg text-sm font-semibold text-gray-600 dark:text-gray-300 hover:bg-white/70 dark:hover:bg-gray-800"
                >
                  Skip for now
                </button>
              </div>
            </div>
          </template>

          <template v-else>
            <div class="flex flex-col gap-4">
              <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-3">
                <div>
                  <h2 class="text-lg font-semibold text-gray-900 dark:text-white">Complete your onboarding</h2>
                  <p class="mt-1 text-sm text-gray-600 dark:text-gray-300">
                    Progress: {{ requiredProgress.completed }}/{{ requiredProgress.total }} required steps.
                  </p>
                </div>
                <div class="h-2 w-full lg:w-48 rounded-full bg-[#EEDAD3] dark:bg-gray-700 overflow-hidden">
                  <div class="h-full bg-[#D97757] transition-all" :style="{ width: requiredProgress.percent + '%' }"></div>
                </div>
              </div>

              <div class="grid gap-3">
                <div class="flex items-center justify-between rounded-lg border border-gray-200 dark:border-gray-700 bg-white dark:bg-surface-2 px-4 py-3">
                  <div class="text-sm text-gray-800 dark:text-gray-100">
                    <span class="font-semibold">Step 1:</span> Email verified
                  </div>
                  <span class="text-xs font-bold text-green-700 dark:text-green-400">Done</span>
                </div>

                <div class="flex items-center justify-between rounded-lg border border-gray-200 dark:border-gray-700 bg-white dark:bg-surface-2 px-4 py-3">
                  <div class="text-sm text-gray-800 dark:text-gray-100">
                    <span class="font-semibold">Step 2:</span> Start your first memory
                  </div>
                  <div class="flex items-center gap-2">
                    <span v-if="hasStartedFirstMemory" class="text-xs font-bold text-green-700 dark:text-green-400">Done</span>
                    <button
                      v-else
                      @click="startFirstMemory"
                      class="px-3 py-1.5 rounded-md bg-[#D97757] text-white text-xs font-semibold hover:bg-[#C4654A]"
                    >
                      Open editor
                    </button>
                  </div>
                </div>

                <div class="flex items-center justify-between rounded-lg border border-gray-200 dark:border-gray-700 bg-white dark:bg-surface-2 px-4 py-3">
                  <div class="text-sm text-gray-800 dark:text-gray-100">
                    <span class="font-semibold">Optional:</span> Take the demo tour
                  </div>
                  <div class="flex items-center gap-2">
                    <span v-if="hasCompletedTour" class="text-xs font-bold text-green-700 dark:text-green-400">Done</span>
                    <button
                      v-else
                      @click="startTour"
                      class="px-3 py-1.5 rounded-md border border-gray-300 dark:border-gray-600 text-xs font-semibold text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800"
                    >
                      Start tour
                    </button>
                  </div>
                </div>
              </div>

              <div class="flex flex-wrap gap-2 justify-end">
                <button
                  @click="skipOnboarding"
                  class="px-4 py-2 rounded-lg text-sm font-semibold text-gray-600 dark:text-gray-300 hover:bg-white/70 dark:hover:bg-gray-800"
                >
                  Skip for now
                </button>
                <button
                  @click="completeOnboarding"
                  class="px-4 py-2 rounded-lg bg-[#D97757] text-white text-sm font-semibold hover:bg-[#C4654A]"
                >
                  Complete onboarding
                </button>
              </div>
            </div>
          </template>
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
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue';
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
const hasStartedFirstMemory = ref(localStorage.getItem('onboarding_first_memory_started') === 'true');
const hasCompletedTour = ref(localStorage.getItem('tour_completed') === 'true');

const focusToday = computed(() => route.query.view === 'today');
const showOnboardingCard = computed(() => authStore.isAuthenticated && !authStore.hasCompletedOnboarding);
const requiredProgress = computed(() => {
  const total = 2;
  const completed = 1 + (hasStartedFirstMemory.value ? 1 : 0);
  return {
    total,
    completed,
    percent: Math.round((completed / total) * 100),
  };
});

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

const runTour = () => {
  setTimeout(() => {
    const driver = createTour();
    driver.drive();
    localStorage.setItem('tour_completed', 'true');
    hasCompletedTour.value = true;
    localStorage.removeItem('tour_requested');
  }, 250);
};

const startTour = () => {
  localStorage.removeItem('tour_completed');
  hasCompletedTour.value = false;
  localStorage.setItem('tour_requested', 'true');
  runTour();
};

const startFirstMemory = () => {
  localStorage.setItem('onboarding_first_memory_started', 'true');
  hasStartedFirstMemory.value = true;
  router.push('/editor/new?interaction_type=conversation&source_app=chatgpt');
};

const completeOnboarding = () => {
  authStore.completeOnboarding();
  localStorage.setItem('tour_completed', 'true');
  hasCompletedTour.value = true;
  toast.success('Onboarding completed.');
};

const skipOnboarding = () => {
  authStore.completeOnboarding();
  localStorage.setItem('tour_completed', 'true');
  hasCompletedTour.value = true;
  toast.info('Onboarding skipped for now.');
};

const resendVerification = async () => {
  if (resendingVerification.value) return;
  resendingVerification.value = true;
  try {
    await api.post('/auth/resend-verification');
    toast.success('Verification email sent. Please check your inbox.');
  } catch (err) {
    toast.error(err.response?.data?.detail || 'Failed to resend verification email.');
  } finally {
    resendingVerification.value = false;
  }
};

onMounted(() => {
  if (localStorage.getItem('tour_requested') === 'true') {
    runTour();
  }
});
</script>
