<template>
    <footer class="border-t border-black/5 dark:border-white/10 py-10 bg-white dark:bg-[#191919]">
      <div class="max-w-7xl mx-auto px-8 lg:px-12 flex flex-col md:flex-row justify-between items-center gap-6">
        <div class="flex items-center gap-2">
            <img src="/image.svg" alt="MemWyre" class="w-5 h-5 rounded" />
            <span class="font-semibold text-sm text-[#191919] dark:text-white">MemWyre</span>
        </div>
        <p class="text-sm text-[#191919]/40 dark:text-white/40">© 2026 MemWyre. Crafted for clarity.</p>
        <div class="flex flex-wrap gap-5 justify-center">
             <a href="mailto:shivharehimansh@gmail.com" class="text-sm text-[#191919]/40 hover:text-[#191919] dark:text-white/40 dark:hover:text-white transition-colors">Support</a>
             <router-link to="/privacy-policy" class="text-sm text-[#191919]/40 hover:text-[#191919] dark:text-white/40 dark:hover:text-white transition-colors">Privacy Policy</router-link>
             <router-link to="/terms" class="text-sm text-[#191919]/40 hover:text-[#191919] dark:text-white/40 dark:hover:text-white transition-colors">Terms of Service</router-link>
             <a href="https://x.com/MemWyre" target="_blank" rel="noopener noreferrer" class="text-sm text-[#191919]/40 hover:text-[#191919] dark:text-white/40 dark:hover:text-white transition-colors">Twitter</a>
        </div>
      </div>
    </footer>
</template>
