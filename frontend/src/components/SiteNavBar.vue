
<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const isScrolled = ref(false);

const handleScroll = () => {
  isScrolled.value = window.scrollY > 300;
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>

<template>
  <div class="fixed top-6 left-0 right-0 z-50 flex justify-center px-4 pointer-events-none">
    <nav :class="[
      'w-full max-w-6xl pointer-events-auto backdrop-blur-xl border rounded-full shadow-2xl transition-all duration-300',
      isScrolled ? 'bg-white/90 border-black/5' : 'bg-black/20 border-white/10'
    ]">
      <div class="px-6 sm:px-8">
        <div class="flex justify-between items-center h-14 sm:h-16">
          <router-link to="/" class="flex items-center group">
            <img src="/image.svg" alt="Memwyre"
              class="w-7 h-7 rounded-sm mr-2 group-hover:scale-105 transition-transform duration-300" />
            <span :class="[
              'text-2xl tracking-tight drop-shadow-sm transition-colors duration-300',
              isScrolled ? 'text-black' : 'text-white'
            ]" style="font-family: 'Inter', system-ui, sans-serif;">Memwyre</span>
          </router-link>

          <div class="hidden md:flex items-center gap-1">
            <a v-for="link in [
              { name: 'Features', href: '/#features' },
              { name: 'Workflow', href: '/#workflow' },
              { name: 'Ecosystem', href: '/#ecosystem' },
              { name: 'Use Cases', href: '/#use-cases' },
              { name: 'Pricing', href: '/#pricing' }
            ]" :key="link.name" :href="link.href" :class="[
              'px-3 py-1.5 text-sm transition-all duration-300 rounded-md',
              isScrolled
                ? 'text-black/70 hover:text-black hover:bg-black/5'
                : 'text-white/70 hover:text-white hover:bg-white/10'
            ]">
              {{ link.name }}
            </a>
          </div>

          <div class="flex items-center gap-3">
            <router-link to="/login" :class="[
              'text-sm transition-colors duration-300',
              isScrolled ? 'text-black/70 hover:text-black' : 'text-white/70 hover:text-white'
            ]">
              Log in
            </router-link>
            <router-link to="/signup"
              class="px-4 py-2 bg-[#D97757] text-white text-sm font-semibold rounded-lg hover:bg-[#C4654A] transition-colors shadow-lg">
              Signup
            </router-link>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>
