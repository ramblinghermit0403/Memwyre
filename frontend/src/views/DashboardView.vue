<template>
  <div class="h-screen flex flex-col bg-gray-50 dark:bg-app transition-colors duration-300 font-sans overflow-hidden">
    <NavBar />

    <main class="flex-1 overflow-y-auto w-full max-w-7xl mx-auto pt-8 pb-12 sm:px-6 lg:px-8">
      <div class="px-4 sm:px-0 flex flex-col min-h-full">
          <div class="mb-8">
            <h2 class="text-3xl font-bold text-gray-900 dark:text-text-primary">Dashboard</h2>
            <p class="mt-1 text-gray-500 dark:text-text-secondary">Welcome back to your Brain Vault. Here's a quick overview of your knowledge base and actions.</p>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 flex-1">
              <!-- Left Column: Unified Document List (span 2 cols) -->
              <div class="lg:col-span-2 flex flex-col">
                  <div class="bg-white dark:bg-surface rounded-xl shadow-sm border border-gray-100 dark:border-border overflow-hidden flex-1 flex flex-col min-h-[500px]">
                      <UnifiedDocumentList class="flex-1" />
                  </div>
              </div>

              <!-- Right Column: Actions & Widgets -->
              <div class="flex flex-col gap-6 h-full">
                  <!-- Ask Brain Vault -->
                   <div class="bg-white dark:bg-surface rounded-xl shadow-sm border border-gray-100 dark:border-border p-6 flex-1 flex flex-col">
                       <h3 class="text-lg font-semibold text-gray-900 dark:text-text-primary mb-2 flex items-center gap-2">
                           <svg class="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3M3.343 15.657l-.707-.707m16.5 0l-.707.707M6 12a6 6 0 1110.41-4.58L16.2 7.2" /></svg>
                           Ask Your Brain Vault
                       </h3>
                       <p class="text-sm text-gray-500 dark:text-text-secondary mb-4">Instantly retrieve information from your knowledge base.</p>
                      <RetrievalTest :embedded="true" class="flex-1" />
                  </div>

                  <!-- File Upload -->
                  <div class="bg-white dark:bg-surface rounded-xl shadow-sm border border-gray-100 dark:border-border p-6 flex-1 flex flex-col">
                      <h3 class="text-lg font-semibold text-gray-900 dark:text-text-primary mb-2 flex items-center gap-2">
                           <svg class="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" /></svg>
                           File Upload
                      </h3>
                      <p class="text-sm text-gray-500 dark:text-text-secondary mb-4">Drag and drop or select files to add to your vault.</p>
                      <FileUpload class="flex-1" />
                  </div>
              </div>
          </div>
      </div>
    </main>
    <QuickActions />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import NavBar from '../components/NavBar.vue';
import UnifiedDocumentList from '../components/UnifiedDocumentList.vue';
import QuickActions from '../components/QuickActions.vue';
import FileUpload from '../components/FileUpload.vue';
import RetrievalTest from '../components/RetrievalTest.vue';
import { createTour } from '../tour';
import { useInboxStore } from '../stores/inbox';

const inboxStore = useInboxStore();
inboxStore.fetchInbox();
inboxStore.connectWebSocket();

onMounted(() => {
    const tourCompleted = localStorage.getItem('tour_completed');
    if (!tourCompleted) {
        const driver = createTour();
        driver.drive();
        localStorage.setItem('tour_completed', 'true');
    }
});
</script>
