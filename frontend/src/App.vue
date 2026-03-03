<script setup>
import { RouterView } from 'vue-router'
import { useThemeStore } from './stores/theme'
import { useAuthStore } from './stores/auth'
import OnboardingOverlay from './components/OnboardingOverlay.vue'

// Initialize theme store to ensure dark mode preference persists on reload
const themeStore = useThemeStore()
const authStore = useAuthStore()
</script>

<template>
  <div class="min-h-screen text-[#2D2B2A] dark:text-[#FAF6F0] relative">
    <RouterView />
    <OnboardingOverlay v-if="authStore.isAuthenticated && !authStore.hasCompletedOnboarding" />
  </div>
</template>

<style>
/* Global styles are imported in main.js via style.css */
</style>
