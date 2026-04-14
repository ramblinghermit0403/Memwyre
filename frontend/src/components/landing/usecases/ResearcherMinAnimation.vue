<template>
  <div class="aspect-square w-full max-w-[160px] mx-auto relative bg-white/50 rounded-xl overflow-hidden border border-black/5 p-4 flex flex-col gap-4 group">
    <!-- Sources -->
    <div class="flex justify-between gap-2">
      <div v-for="i in 3" :key="i" 
           class="h-8 w-1/3 rounded-md bg-gray-100 flex flex-col gap-1 p-1 items-center justify-center overflow-hidden">
        <div v-for="j in 2" :key="j" class="h-0.5 w-full bg-gray-200 rounded-full"></div>
        <div class="h-0.5 w-[80%] bg-primary/30 rounded-full animate-pulse" :style="{ animationDelay: i * 0.5 + 's' }"></div>
      </div>
    </div>
    
    <!-- Synthesis Animation -->
    <div class="flex-1 relative flex items-center justify-center">
      <div class="absolute inset-0 flex items-center justify-center">
        <div class="w-1.5 h-1.5 bg-primary rounded-full opacity-0 group-hover:animate-merge-1"></div>
        <div class="w-1.5 h-1.5 bg-primary rounded-full opacity-0 group-hover:animate-merge-2"></div>
        <div class="w-1.5 h-1.5 bg-primary rounded-full opacity-0 group-hover:animate-merge-3"></div>
      </div>
      
      <!-- Result -->
      <div class="w-full h-10 bg-gray-50 border border-black/5 rounded-lg p-2 flex flex-col gap-1.5 transition-all duration-700 opacity-40 group-hover:opacity-100 group-hover:bg-primary/5 group-hover:border-primary/20">
        <div v-for="i in 3" :key="i" class="h-1 bg-gray-200 rounded-full" :style="{ width: [90, 70, 40][i-1] + '%' }"></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@keyframes merge-1 {
  0% { transform: translate(-30px, -40px); opacity: 0; }
  20% { opacity: 1; }
  80% { transform: translate(0, 0); opacity: 0; }
}
@keyframes merge-2 {
  0% { transform: translate(0, -40px); opacity: 0; }
  20% { opacity: 1; }
  80% { transform: translate(0, 0); opacity: 0; }
}
@keyframes merge-3 {
  0% { transform: translate(30px, -40px); opacity: 0; }
  20% { opacity: 1; }
  80% { transform: translate(0, 0); opacity: 0; }
}

.group:hover .animate-merge-1 { animation: merge-1 2s ease-in-out infinite; }
.group:hover .animate-merge-2 { animation: merge-2 2s ease-in-out infinite; animation-delay: 0.3s; }
.group:hover .animate-merge-3 { animation: merge-3 2s ease-in-out infinite; animation-delay: 0.6s; }
</style>
