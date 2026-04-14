<template>
  <div class="aspect-square w-full max-w-[160px] mx-auto relative bg-white/50 rounded-xl overflow-hidden border border-black/5 p-4 flex items-center justify-center group perspective-1000">
    <!-- Card container -->
    <div class="relative w-20 h-28 transition-transform duration-700 preserve-3d group-hover:rotate-y-180">
      <!-- Front -->
      <div class="absolute inset-0 bg-white border border-black/5 rounded-lg shadow-sm backface-hidden p-3 flex flex-col gap-2">
        <div class="w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center mx-auto">
          <span class="text-xs text-primary font-bold">?</span>
        </div>
        <div class="space-y-1">
          <div class="h-1 w-full bg-gray-100 rounded-full"></div>
          <div class="h-1 w-3/4 bg-gray-100 rounded-full"></div>
        </div>
      </div>
      
      <!-- Back -->
      <div class="absolute inset-0 bg-primary/5 border border-primary/20 rounded-lg shadow-sm backface-hidden rotate-y-180 p-3 flex flex-col items-center justify-center gap-2">
        <div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-white scale-0 transition-transform duration-300 delay-300 group-hover:scale-100">
          <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
          </svg>
        </div>
        <div class="text-[10px] font-bold text-primary uppercase tracking-tighter">Recall Cache</div>
      </div>
    </div>
    
    <!-- Floating particles -->
    <div class="absolute top-4 right-4 w-2 h-2 bg-primary/30 rounded-full animate-bounce"></div>
    <div class="absolute bottom-4 left-4 w-1.5 h-1.5 bg-gray-300 rounded-full animate-bounce [animation-delay:0.5s]"></div>
  </div>
</template>

<style scoped>
.perspective-1000 {
  perspective: 1000px;
}
.preserve-3d {
  transform-style: preserve-3d;
}
.backface-hidden {
  backface-visibility: hidden;
}
.rotate-y-180 {
  transform: rotateY(180deg);
}
</style>
