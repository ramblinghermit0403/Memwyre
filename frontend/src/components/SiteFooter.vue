<template>
    <footer class="border-t border-gray-100 dark:border-gray-900 py-12 bg-gray-50 dark:bg-black text-black dark:text-white">
      <div class="max-w-7xl mx-auto px-6 lg:px-8 flex flex-col md:flex-row justify-between items-center gap-6">
        <div class="flex items-center gap-2">
            <img src="/image.svg" alt="MemWyre" class="w-6 h-6 rounded-lg" />
            <span class="font-bold text-sm">MemWyre</span>
        </div>
        <p class="text-sm text-gray-400">© 2026 MemWyre. Crafted for clarity.</p>
        <div class="flex flex-wrap gap-4 md:gap-6 justify-center mt-4 md:mt-0">
             <a href="mailto:shivharehimansh@gmail.com" class="text-gray-400 hover:text-black dark:hover:text-white transition-colors">Support</a>
             <router-link to="/privacy-policy" class="text-gray-400 hover:text-black dark:hover:text-white transition-colors">Privacy Policy</router-link>
             <router-link to="/terms" class="text-gray-400 hover:text-black dark:hover:text-white transition-colors">Terms of Service</router-link>
             <a href="https://x.com/MemWyre" target="_blank" rel="noopener noreferrer" class="text-gray-400 hover:text-black dark:hover:text-white transition-colors">Twitter</a>

        </div>
      </div>
    </footer>
</template>
