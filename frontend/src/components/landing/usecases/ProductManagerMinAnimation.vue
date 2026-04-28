<template>
  <div class="w-full h-full max-w-[220px] mx-auto relative group perspective-1000">
    <!-- Background Connection Network -->
    <svg class="absolute inset-0 w-full h-full opacity-20 group-hover:opacity-40 transition-opacity duration-700" viewBox="0 0 200 200">
      <circle cx="40" cy="40" r="2" fill="currentColor" class="text-primary/40" />
      <circle cx="160" cy="30" r="2" fill="currentColor" class="text-primary/40" />
      <circle cx="150" cy="160" r="2" fill="currentColor" class="text-primary/40" />
      <circle cx="50" cy="150" r="2" fill="currentColor" class="text-primary/40" />
      <line x1="40" y1="40" x2="160" y2="30" stroke="currentColor" stroke-width="0.5" class="text-primary/20 dash-animate" />
      <line x1="160" y1="30" x2="150" y2="160" stroke="currentColor" stroke-width="0.5" class="text-primary/20 dash-animate-delayed" />
      <line x1="150" y1="160" x2="50" y2="150" stroke="currentColor" stroke-width="0.5" class="text-primary/20 dash-animate" />
      <line x1="50" y1="150" x2="40" y2="40" stroke="currentColor" stroke-width="0.5" class="text-primary/20 dash-animate-delayed" />
    </svg>

    <!-- Floating Strategic Cards -->
    <div class="relative z-10 flex flex-col items-center justify-center h-full min-h-[200px]">
      <!-- Roadmap Card -->
      <div class="w-40 h-24 bg-white/80 backdrop-blur-md rounded-xl border border-black/5 shadow-lg transform -rotate-3 -translate-y-4 group-hover:-translate-y-6 group-hover:rotate-0 transition-all duration-700 p-3">
        <div class="flex items-center gap-2 mb-2">
          <div class="w-2 h-2 rounded-full bg-primary"></div>
          <div class="w-16 h-1.5 bg-gray-100 rounded-full"></div>
        </div>
        <div class="space-y-1.5">
          <div class="h-1 bg-gray-50 rounded-full w-full"></div>
          <div class="h-1 bg-gray-50 rounded-full w-[80%]"></div>
          <div class="flex gap-1 mt-2">
            <div class="h-3 w-6 bg-primary/10 rounded-sm"></div>
            <div class="h-3 w-10 bg-gray-50 rounded-sm"></div>
          </div>
        </div>
      </div>

      <!-- PRD Card -->
      <div class="absolute w-36 h-20 bg-white/90 backdrop-blur-sm rounded-lg border border-black/5 shadow-xl transform rotate-6 translate-x-4 translate-y-6 group-hover:translate-x-8 group-hover:translate-y-8 transition-all duration-700 p-3">
        <div class="flex items-center gap-2 mb-2">
          <div class="w-2 h-2 rounded-sm bg-[#9575CD]"></div>
          <div class="w-12 h-1.5 bg-gray-100 rounded-full"></div>
        </div>
        <div class="space-y-1.5">
          <div class="h-1 bg-[#9575CD]/10 rounded-full w-[90%]"></div>
          <div class="h-1 bg-gray-50 rounded-full w-[70%]"></div>
        </div>
      </div>

      <!-- User Research Node -->
      <div class="absolute top-1/2 left-0 w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center transform -translate-x-6 -translate-y-10 group-hover:-translate-x-10 transition-all duration-700">
        <div class="w-4 h-4 bg-primary rounded-full animate-ping opacity-20"></div>
        <div class="absolute inset-0 flex items-center justify-center text-primary text-xs">💡</div>
      </div>
    </div>
  </div>
</template>

<script setup>
// Pure template animation
</script>

<style scoped>
.perspective-1000 {
  perspective: 1000px;
}

.dash-animate {
  stroke-dasharray: 5;
  animation: dash 10s linear infinite;
}

.dash-animate-delayed {
  stroke-dasharray: 5;
  animation: dash 15s linear infinite reverse;
}

@keyframes dash {
  to {
    stroke-dashoffset: 100;
  }
}
</style>
