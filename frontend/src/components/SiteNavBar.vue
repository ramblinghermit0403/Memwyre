<template>
    <nav class="fixed w-full z-50 bg-white/90 dark:bg-black/90 backdrop-blur-sm border-b border-gray-100 dark:border-gray-800">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="flex justify-between items-center h-20">
          <router-link to="/" class="flex items-center group">
            <img src="/image.svg" alt="MemWyre" class="w-8 h-8 rounded-lg mr-3 group-hover:scale-105 transition-transform duration-300" />
            <span class="text-xl font-bold tracking-tight text-black dark:text-white">MemWyre</span>
          </router-link>
          
          <div class="hidden md:flex items-center space-x-8 text-sm font-medium">
            <!-- Use explicit routes for anchors if we are not on home -->
            <!-- For simplicity, assuming Hash mode or simply linking to /#id -->
            <a href="/#features" class="text-gray-500 hover:text-black dark:hover:text-white transition-colors">Features</a>
            <a href="/#workflow" class="text-gray-500 hover:text-black dark:hover:text-white transition-colors">Workflow</a>
            <a href="/#ecosystem" class="text-gray-500 hover:text-black dark:hover:text-white transition-colors">Ecosystem</a>
            <router-link to="/use-cases" class="text-gray-500 hover:text-black dark:hover:text-white transition-colors">Use Cases</router-link>
            <router-link to="/research" class="text-gray-500 hover:text-black dark:hover:text-white transition-colors">Research</router-link>
            <a href="/#faq" class="text-gray-500 hover:text-black dark:hover:text-white transition-colors">FAQ</a>
          </div>

          <div class="flex items-center gap-4">
            <router-link to="/login" class="text-sm font-medium text-gray-500 hover:text-black dark:hover:text-white transition-colors">
              Log in
            </router-link>
            <router-link to="/register" class="px-5 py-2.5 bg-black dark:bg-white text-white dark:text-black text-sm font-bold rounded-full hover:opacity-90 transition-opacity">
              Get Started
            </router-link>
          </div>
        </div>
      </div>
    </nav>
</template>
