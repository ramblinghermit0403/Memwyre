<script setup>
import { RouterView } from 'vue-router'
import { onMounted } from 'vue'
import { useThemeStore } from './stores/theme'
import { useAuthStore } from './stores/auth'

// Initialize theme store to ensure dark mode preference persists on reload
const isClient = typeof window !== 'undefined'
if (isClient) {
  useThemeStore()
}

const authStore = isClient ? useAuthStore() : null

onMounted(async () => {
  if (!authStore || !authStore.isAuthenticated) return
  try {
    await authStore.fetchUser()
  } catch (e) {
    // Keep app usable even if profile sync fails.
  }
})
</script>

<template>
  <div class="min-h-screen text-[#2D2B2A] dark:text-[#FAF6F0] relative">
    <RouterView />
  </div>
</template>

<style>
/* Global styles are imported in main.js via style.css */
</style>
