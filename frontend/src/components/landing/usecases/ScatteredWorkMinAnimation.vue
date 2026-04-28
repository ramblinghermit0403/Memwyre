<template>
  <div class="relative w-full h-full min-h-[350px] flex items-center justify-center p-4 overflow-visible group scale-75 sm:scale-90 lg:scale-100">
    <!-- Unified Large Triple-Icon Row (No Labels) -->
    <div class="relative z-10 flex items-center justify-center gap-8">
      <!-- Gemini -->
      <div class="w-32 h-32 rounded-3xl bg-white flex items-center justify-center p-4 shadow-2xl">
        <img src="@/assets/gemini-color.svg" alt="Gemini" class="w-full h-full object-contain" />
      </div>

      <!-- ChatGPT -->
      <div class="w-32 h-32 rounded-3xl bg-white flex items-center justify-center p-4 shadow-2xl">
        <img src="@/assets/openai.svg" alt="ChatGPT" class="w-full h-full object-contain" />
      </div>

      <!-- Claude -->
      <div class="w-32 h-32 rounded-3xl bg-white flex items-center justify-center p-4 shadow-2xl">
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
