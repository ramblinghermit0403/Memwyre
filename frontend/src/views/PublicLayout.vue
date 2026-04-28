<template>
  <div class="min-h-screen bg-white dark:bg-black text-black dark:text-white transition-colors duration-300 font-sans selection:bg-black selection:text-white dark:selection:bg-white dark:selection:text-black">
    <SiteNavBar />
    
    <!-- Content Router View -->
    <router-view />
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import SiteNavBar from '../components/SiteNavBar.vue';

const route = useRoute();
</script>
