<template>
  <div class="min-h-screen flex items-center justify-center bg-white dark:bg-surface px-6 py-24 sm:py-32 lg:px-8 font-sans transition-colors duration-300">
    <div class="text-center relative">
      <!-- Background blur effect -->
      <div class="absolute -top-24 -left-24 w-64 h-64 bg-primary/5 rounded-full blur-3xl animate-pulse"></div>
      <div class="absolute -bottom-24 -right-24 w-64 h-64 bg-accent/5 rounded-full blur-3xl animate-pulse delay-700"></div>

      <p class="text-6xl font-black text-primary drop-shadow-sm">404</p>
      <h1 class="mt-4 text-3xl font-extrabold tracking-tight text-gray-900 dark:text-text-primary sm:text-5xl">Page not found</h1>
      <p class="mt-6 text-lg leading-7 text-gray-500 dark:text-text-secondary max-w-md mx-auto">
        Sorry, we couldn’t find the page you’re looking for. It might have been moved or doesn't exist.
      </p>
      
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <router-link
          to="/"
          class="rounded-xl bg-black px-6 py-3 text-sm font-bold text-white shadow-sm hover:bg-gray-800 transition-all duration-300 hover:scale-105"
        >
          Go back home
        </router-link>
        <a href="mailto:shivharehimansh@gmail.com" class="text-sm font-bold text-gray-900 dark:text-text-primary hover:text-primary transition-colors">
          Contact support <span aria-hidden="true">&rarr;</span>
        </a>
      </div>

      <!-- Search-like illustration -->
      <div class="mt-16 flex justify-center">
        <div class="relative w-24 h-24 text-gray-200 dark:text-border">
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24" class="w-full h-full">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// No logic needed for static 404
</script>

<style scoped>
.bg-primary { background-color: var(--primary, #D97757); }
.text-primary { color: var(--primary, #D97757); }
.bg-accent { background-color: var(--accent, #D97757); }
</style>
