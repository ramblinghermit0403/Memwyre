<template>
  <div class="min-h-screen bg-white dark:bg-black text-black dark:text-white transition-colors duration-300 font-sans selection:bg-black selection:text-white dark:selection:bg-white dark:selection:text-black">
    <SiteNavBar />
    
    <!-- Content Router View -->
    <router-view />

    <SiteFooter />
  </div>
</template>

<script setup>
import SiteNavBar from '../components/SiteNavBar.vue';
import SiteFooter from '../components/SiteFooter.vue';
</script>
