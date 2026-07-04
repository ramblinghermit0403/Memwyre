<template>
  <div class="relative w-full h-full min-h-[160px] flex items-center justify-center p-2 overflow-visible group">
    <!-- Unified Large Triple-Icon Row (No Labels) -->
    <div class="relative z-10 flex items-center justify-center gap-6">
      <!-- Gemini -->
      <div class="w-24 h-24 rounded-2xl bg-white flex items-center justify-center p-4.5 shadow-lg animate-float-1">
        <img src="@/assets/gemini-color.svg" alt="Gemini" class="w-full h-full object-contain" />
      </div>

      <!-- ChatGPT -->
      <div class="w-24 h-24 rounded-2xl bg-white flex items-center justify-center p-4.5 shadow-lg animate-float-2">
        <img src="@/assets/openai.svg" alt="ChatGPT" class="w-full h-full object-contain" />
      </div>

      <!-- Claude -->
      <div class="w-24 h-24 rounded-2xl bg-white flex items-center justify-center p-4.5 shadow-lg animate-float-3">
        <img src="@/assets/claude-color.svg" alt="Claude" class="w-full h-full object-contain" />
      </div>
    </div>
  </div>
</template>

<style scoped>
@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}
.animate-float-1 { animation: float 4s ease-in-out infinite; }
.animate-float-2 { animation: float 5s ease-in-out infinite reverse; }
.animate-float-3 { animation: float 6s ease-in-out infinite; }
</style>
