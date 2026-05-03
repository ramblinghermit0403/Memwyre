<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const isHidden = ref(false);
const isAtTop = ref(true);
let lastScrollY = 0;
let ticking = false;

const handleScroll = () => {
  if (ticking) return;
  ticking = true;

  requestAnimationFrame(() => {
    const currentScrollY = window.scrollY;

    // Hide/show based on scroll direction
    if (currentScrollY > lastScrollY && currentScrollY > 80) {
      isHidden.value = true;
    } else {
      isHidden.value = false;
    }

    isAtTop.value = currentScrollY < 10;

    lastScrollY = currentScrollY;
    ticking = false;
  });
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});

// Reset scroll state on route change
watch(() => route.path, () => {
  lastScrollY = 0;
  isHidden.value = false;
  isAtTop.value = true;
});
</script>

<template>
  <header :class="[
    'fixed top-0 left-0 right-0 z-50 transition-transform duration-300 ease-in-out bg-white border-b border-black/5 shadow-sm',
    isHidden ? '-translate-y-full' : 'translate-y-0'
  ]">
    <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">
      <div class="flex justify-between items-center h-16">
        <router-link to="/" class="flex items-center group">
          <img src="/image.svg" alt="Memwyre"
            class="w-7 h-7 rounded-sm mr-2.5 group-hover:scale-105 transition-transform duration-300" />
          <span class="text-2xl font-medium tracking-tight text-black transition-colors duration-300"
            style="font-family: 'Inter', system-ui, sans-serif;">Memwyre</span>
        </router-link>

        <div class="hidden md:flex items-center gap-1">
          <a v-for="link in [
            { name: 'Features', href: '/#features' },
            { name: 'Ecosystem', href: '/#ecosystem' },
            { name: 'Use Cases', href: '/#use-cases' },
            { name: 'Integrations', href: '/docs/' },
            { name: 'Pricing', href: '/pricing' }
          ]" :key="link.name" :href="link.href"
            class="px-3 py-1.5 text-sm font-medium transition-all duration-200 rounded-md text-black/60 hover:text-black hover:bg-black/5">
            {{ link.name }}
          </a>
        </div>

        <div class="flex items-center gap-3">
          <router-link to="/login"
            class="text-sm font-medium transition-colors duration-200 text-black/60 hover:text-black">
            Log in
          </router-link>
          <router-link to="/signup"
            class="px-4 py-2 bg-black text-white text-sm font-semibold rounded-lg hover:bg-gray-800 transition-colors shadow-sm">
            Start Free
          </router-link>
        </div>
      </div>
    </div>
  </header>
</template>
