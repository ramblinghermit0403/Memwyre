<template>
  <footer class="border-t border-black/5 bg-white py-12">
    <div class="max-w-7xl mx-auto px-8 lg:px-12 flex flex-col md:flex-row justify-between items-center gap-6">
      <div class="flex items-center gap-2">
        <img src="/image.svg" alt="Memwyre" class="w-5 h-5 rounded" />
        <span class="font-semibold text-sm text-black">Memwyre</span>
      </div>
      <p class="text-sm text-black/40">© 2026 Memwyre. Crafted for clarity.</p>
      <div class="flex flex-wrap gap-5 justify-center">
        <a href="mailto:shivharehimansh@gmail.com"
          class="text-sm text-black/40 hover:text-black transition-colors">Support</a>
        <router-link to="/privacy-policy" class="text-sm text-black/40 hover:text-black transition-colors">Privacy
          Policy</router-link>
        <router-link to="/terms" class="text-sm text-black/40 hover:text-black transition-colors">Terms of
          Service</router-link>
        <a href="https://x.com/MemWyre" target="_blank" rel="noopener noreferrer"
          class="text-sm text-black/40 hover:text-black transition-colors">Twitter</a>
      </div>
    </div>
  </footer>
</template>
