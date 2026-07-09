<template>
  <div class="min-h-screen bg-white dark:bg-black text-black dark:text-white transition-colors duration-300 font-sans overflow-x-hidden selection:bg-black selection:text-white dark:selection:bg-white dark:selection:text-black">
    <SiteNavBar />
    
    <!-- Content Router View -->
    <main id="main-content">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import { onMounted, onUnmounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import SiteNavBar from '../components/SiteNavBar.vue';

const route = useRoute();

let shouldRestoreDarkClass = false;

onMounted(() => {
  if (typeof document !== 'undefined') {
    shouldRestoreDarkClass = document.documentElement.classList.contains('dark');
    document.documentElement.classList.remove('dark');
    document.documentElement.style.colorScheme = 'light';
  }
});

watch(() => route.path, () => {
  if (typeof document !== 'undefined') {
    document.documentElement.classList.remove('dark');
    document.documentElement.style.colorScheme = 'light';
  }
}, { immediate: true });

onUnmounted(() => {
  if (typeof document !== 'undefined') {
    document.documentElement.style.colorScheme = '';
    if (shouldRestoreDarkClass) {
      document.documentElement.classList.add('dark');
    }
  }
});
</script>
