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
            <div class="bg-white dark:bg-surface rounded-xl shadow-sm border border-gray-100 dark:border-border overflow-hidden h-[640px] lg:h-full min-h-0">
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
import { computed, onMounted, ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import NavBar from '../components/NavBar.vue';
import QuickActions from '../components/QuickActions.vue';
import DashboardInboxList from '../components/DashboardInboxList.vue';
import DailyReviewModal from '../components/DailyReviewModal.vue';
import AIInteractionTimeline from '../components/AIInteractionTimeline.vue';
import { createTour } from '../tour';
import { useInboxStore } from '../stores/inbox';
import { useAuthStore } from '../stores/auth';

const route = useRoute();
const router = useRouter();
const inboxStore = useInboxStore();
const authStore = useAuthStore();
const user = computed(() => authStore.user);
const showDailyReview = ref(false);
const timelineRef = ref(null);

const focusToday = computed(() => route.query.view === 'today');

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

const checkAndTriggerTour = () => {
  if (authStore.hasCompletedOnboarding) {
    const tourCompleted = localStorage.getItem('tour_completed');
    if (!tourCompleted) {
      setTimeout(() => {
        const driver = createTour();
        driver.drive();
        localStorage.setItem('tour_completed', 'true');
      }, 300);
    }
  }
};

onMounted(() => {
  checkAndTriggerTour();
});

watch(() => authStore.hasCompletedOnboarding, (newVal) => {
  if (newVal) checkAndTriggerTour();
});
</script>
