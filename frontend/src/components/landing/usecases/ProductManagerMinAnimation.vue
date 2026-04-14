<template>
  <div class="aspect-square w-full max-w-[160px] mx-auto relative bg-white/50 rounded-xl overflow-hidden border border-black/5 p-4 flex flex-col items-center justify-center group">
    <!-- Chaotic signals -->
    <div class="absolute inset-0 p-4 transition-opacity duration-500 group-hover:opacity-0">
      <div v-for="i in 6" :key="i"
           class="absolute w-4 h-1 bg-gray-200 rounded-full animate-float-slow"
           :style="{ 
             top: 20 + Math.random() * 60 + '%', 
             left: 20 + Math.random() * 60 + '%',
             transform: 'rotate(' + (Math.random() * 360) + 'deg)',
             animationDelay: i * 0.4 + 's'
           }">
      </div>
    </div>
    
    <!-- Structured outcome -->
    <div class="w-full flex flex-col gap-2 p-3 bg-white border border-black/5 rounded-lg shadow-sm translate-y-8 opacity-0 group-hover:translate-y-0 group-hover:opacity-100 transition-all duration-700 ease-out">
      <div class="flex items-center gap-2 mb-1">
        <div class="w-2 h-2 bg-primary rounded-full"></div>
        <div class="w-12 h-1 bg-gray-300 rounded-full"></div>
      </div>
      <div v-for="i in 3" :key="i" class="h-1 bg-gray-100 rounded-full" :style="{ width: [100, 85, 60][i-1] + '%' }"></div>
    </div>
    
    <!-- Pulse ring -->
    <div class="absolute w-12 h-12 border-2 border-primary/20 rounded-full scale-0 group-hover:animate-pulse-expand"></div>
  </div>
</template>

<style scoped>
@keyframes float-slow {
  0%, 100% { transform: translateY(0) rotate(var(--rot)); }
  50% { transform: translateY(-10px) rotate(var(--rot)); }
}

@keyframes pulse-expand {
  0% { transform: scale(0); opacity: 1; }
  100% { transform: scale(3); opacity: 0; }
}

.animate-pulse-expand {
  animation: pulse-expand 1.5s ease-out infinite;
}
</style>
