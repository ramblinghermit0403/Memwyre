<template>
    <nav class="fixed w-full z-50 bg-white/95 dark:bg-[#191919]/95 backdrop-blur-md border-b border-black/5 dark:border-white/10">
      <div class="max-w-7xl mx-auto px-8 lg:px-12">
        <div class="flex justify-between items-center h-16">
          <router-link to="/" class="flex items-center group">
            <img src="/image.svg" alt="MemWyre" class="w-7 h-7 rounded-lg mr-2.5 group-hover:scale-105 transition-transform duration-300" />
            <span class="text-[15px] font-bold tracking-tight text-[#191919] dark:text-white">MemWyre</span>
          </router-link>
          
          <div class="hidden md:flex items-center gap-1">
            <a href="/#features" class="px-3 py-1.5 text-sm text-[#191919]/70 hover:text-[#191919] dark:text-white/60 dark:hover:text-white transition-colors rounded-md hover:bg-black/[0.04] dark:hover:bg-white/[0.06]">Features</a>
            <a href="/#workflow" class="px-3 py-1.5 text-sm text-[#191919]/70 hover:text-[#191919] dark:text-white/60 dark:hover:text-white transition-colors rounded-md hover:bg-black/[0.04] dark:hover:bg-white/[0.06]">Workflow</a>
            <a href="/#ecosystem" class="px-3 py-1.5 text-sm text-[#191919]/70 hover:text-[#191919] dark:text-white/60 dark:hover:text-white transition-colors rounded-md hover:bg-black/[0.04] dark:hover:bg-white/[0.06]">Ecosystem</a>
            <a href="/#use-cases" class="px-3 py-1.5 text-sm text-[#191919]/70 hover:text-[#191919] dark:text-white/60 dark:hover:text-white transition-colors rounded-md hover:bg-black/[0.04] dark:hover:bg-white/[0.06]">Use Cases</a>
            <a href="/#pricing" class="px-3 py-1.5 text-sm text-[#191919]/70 hover:text-[#191919] dark:text-white/60 dark:hover:text-white transition-colors rounded-md hover:bg-black/[0.04] dark:hover:bg-white/[0.06]">Pricing</a>
          </div>

          <div class="flex items-center gap-3">
            <router-link to="/login" class="text-sm text-[#191919]/70 hover:text-[#191919] dark:text-white/60 dark:hover:text-white transition-colors">
              Log in
            </router-link>
            <router-link to="/signup" class="px-4 py-2 bg-[#D97757] text-white text-sm font-semibold rounded-lg hover:bg-[#C4654A] transition-colors">
              Get MemWyre free
            </router-link>
          </div>
        </div>
      </div>
    </nav>
</template>
