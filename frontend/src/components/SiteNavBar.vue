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

const isProductsOpen = ref(false);
const products = [
  // { name: 'Connectors', to: '/connectors' },
  { name: 'Chrome Extension', to: '/extension' },
  { name: 'MCP', to: '/mcp' },
  { name: 'Plugins', to: '/plugins' },
  // { name: 'RAG', to: '/rag' },
  // { name: 'Memory Graph', to: '/memory-graph' },
  { name: 'Personal App', to: '/personal' }
];

const toggleProducts = () => {
  isProductsOpen.value = !isProductsOpen.value;
};

const closeProducts = () => {
  isProductsOpen.value = false;
};

const vClickOutside = {
  mounted(el, binding) {
    el.clickOutsideEvent = function(event) {
      if (!(el === event.target || el.contains(event.target))) {
        binding.value(event, el);
      }
    };
    document.body.addEventListener('click', el.clickOutsideEvent);
  },
  unmounted(el) {
    document.body.removeEventListener('click', el.clickOutsideEvent);
  }
};

// Reset scroll state on route change
watch(() => route.path, () => {
  lastScrollY = 0;
  isHidden.value = false;
  isAtTop.value = true;
  isProductsOpen.value = false;
});
</script>

<template>
  <header :class="[
    'fixed top-0 left-0 right-0 z-50 transition-transform duration-300 ease-in-out bg-white border-b border-black/5 shadow-sm',
    isHidden ? '-translate-y-full' : 'translate-y-0'
  ]">
    <div class="w-full px-6">
      <div class="flex justify-between items-center h-16">
        <router-link to="/" class="flex items-center group">
          <img src="/logo.png" alt="Memwyre"
            class="h-[35px] w-auto dark:invert transition-transform duration-300 group-hover:scale-[1.02]" />
        </router-link>

        <div class="hidden md:flex items-center gap-1">
          <!-- Products Dropdown -->
          <div 
            class="relative" 
            @mouseenter="isProductsOpen = true" 
            @mouseleave="isProductsOpen = false"
            v-click-outside="closeProducts"
          >
            <button 
              @click="toggleProducts" 
              class="flex items-center gap-1 px-3 py-1.5 text-sm font-normal transition-all duration-200 rounded-md text-black hover:bg-black/5 focus:outline-none"
            >
              Products
              <svg 
                class="w-4 h-4 transition-transform duration-200" 
                :class="{ 'rotate-180': isProductsOpen }" 
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>
            
            <transition
              enter-active-class="transition ease-out duration-150"
              enter-from-class="transform opacity-0 scale-95"
              enter-to-class="transform opacity-100 scale-100"
              leave-active-class="transition ease-in duration-100"
              leave-from-class="transform opacity-100 scale-100"
              leave-to-class="transform opacity-0 scale-95"
            >
              <div 
                v-if="isProductsOpen" 
                class="absolute left-0 mt-1.5 w-56 bg-white border border-gray-200 shadow-lg py-2 z-50 rounded-none"
              >
                <router-link 
                  v-for="product in products" 
                  :key="product.name" 
                  :to="product.to" 
                  class="block px-6 py-2.5 text-[15px] font-normal text-black hover:bg-black/5 transition-colors duration-150"
                  @click="isProductsOpen = false"
                >
                  {{ product.name }}
                </router-link>
              </div>
            </transition>
          </div>

          <template v-for="link in [
            { name: 'Features', to: '/#features' },
            { name: 'Ecosystem', to: '/#ecosystem' },
            { name: 'Pricing', to: '/#pricing' }
          ]" :key="link.name">
            <router-link :to="link.to"
              class="px-3 py-1.5 text-sm font-normal transition-all duration-200 rounded-md text-black hover:bg-black/5">
              {{ link.name }}
            </router-link>
          </template>
          <router-link to="/research"
            class="px-3 py-1.5 text-sm font-normal transition-all duration-200 rounded-md text-black hover:bg-black/5">
            Research
          </router-link>
          <router-link to="/blog"
            class="px-3 py-1.5 text-sm font-normal transition-all duration-200 rounded-md text-black hover:bg-black/5">
            Blog
          </router-link>
          <!-- Docs is a separate VitePress static site — needs a hard navigation, not router-link -->
          <a href="/docs/"
            class="px-3 py-1.5 text-sm font-normal transition-all duration-200 rounded-md text-black hover:bg-black/5">
            Docs
          </a>
        </div>

        <div class="flex items-center gap-3">
          <router-link to="/login"
            class="text-sm font-normal transition-colors duration-200 text-black/60 hover:text-black">
            Log in
          </router-link>
          <router-link to="/signup"
            class="px-4 py-2 bg-black text-white text-sm font-semibold rounded hover:bg-gray-800 transition-colors shadow-sm">
            Start Free
          </router-link>
        </div>
      </div>
    </div>
  </header>
</template>
