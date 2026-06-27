<template>
  <div class="py-16 sm:py-20 max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
      <div class="space-y-8">
        <h2 class="text-base font-bold uppercase tracking-widest text-text-muted mb-4">Why Memwyre</h2>
        <p
          class="hero-serif text-balance text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-extrabold tracking-tighter leading-[1.08]">
          Your AI work scatters.<br>
          <span class="text-primary">Memwyre compounds it.</span>
        </p>
        <p class="text-xl sm:text-2xl text-text-secondary leading-relaxed max-w-xl text-balance">
          Memwyre helps you capture everything you do with AI—research, code, decisions—and turns it into persistent,
          accessible knowledge tailored to your workflow.
        </p>
      </div>

      <!-- Visual Diagram -->
      <div
        class="relative min-h-[400px] md:min-h-[500px] w-full max-w-xl mx-auto flex items-center justify-center p-4 md:p-10 overflow-visible group">
        <!-- Ambient Glow -->
        <div
          class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 md:w-80 h-64 md:h-80 bg-primary/15 rounded-full blur-[100px] opacity-60 group-hover:opacity-100 transition-opacity duration-1000">
        </div>

        <!-- SVG Connection Lines + Traveling Dots -->
        <svg class="absolute inset-0 w-full h-full z-0 pointer-events-none" viewBox="0 0 500 500" fill="none">
          <line x1="250" y1="45" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6"
            opacity="0.2" />
          <line x1="340" y1="170" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6"
            opacity="0.2" />
          <line x1="460" y1="250" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6"
            opacity="0.2" />
          <line x1="340" y1="330" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6"
            opacity="0.2" />
          <line x1="250" y1="450" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6"
            opacity="0.2" />
          <line x1="160" y1="330" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6"
            opacity="0.2" />
          <line x1="40" y1="250" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6"
            opacity="0.2" />
          <line x1="160" y1="170" x2="250" y2="250" stroke="var(--primary)" stroke-width="1" stroke-dasharray="4 6"
            opacity="0.2" />

          <!-- Trailing dots -->
          <circle r="4" fill="var(--primary)" opacity="0.8">
            <animateMotion dur="3s" repeatCount="indefinite" begin="0s" path="M250,45 L250,250" />
            <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="0s" />
          </circle>
          <circle r="4" fill="var(--primary)" opacity="0.8">
            <animateMotion dur="3s" repeatCount="indefinite" begin="0.4s" path="M340,170 L250,250" />
            <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="0.4s" />
          </circle>
          <circle r="4" fill="var(--primary)" opacity="0.8">
            <animateMotion dur="3s" repeatCount="indefinite" begin="0.8s" path="M460,250 L250,250" />
            <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="0.8s" />
          </circle>
          <circle r="4" fill="var(--primary)" opacity="0.8">
            <animateMotion dur="3s" repeatCount="indefinite" begin="1.2s" path="M340,330 L250,250" />
            <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="1.2s" />
          </circle>
          <circle r="4" fill="var(--primary)" opacity="0.8">
            <animateMotion dur="3s" repeatCount="indefinite" begin="1.6s" path="M250,450 L250,250" />
            <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="1.6s" />
          </circle>
          <circle r="4" fill="var(--primary)" opacity="0.8">
            <animateMotion dur="3s" repeatCount="indefinite" begin="2.0s" path="M160,330 L250,250" />
            <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="2.0s" />
          </circle>
          <circle r="4" fill="var(--primary)" opacity="0.8">
            <animateMotion dur="3s" repeatCount="indefinite" begin="2.4s" path="M40,250 L250,250" />
            <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="2.4s" />
          </circle>
          <circle r="4" fill="var(--primary)" opacity="0.8">
            <animateMotion dur="3s" repeatCount="indefinite" begin="2.8s" path="M160,170 L250,250" />
            <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3s" repeatCount="indefinite" begin="2.8s" />
          </circle>
        </svg>

        <!-- Central Node: Memwyre -->
        <div
          class="relative z-10 flex flex-col items-center justify-center transform group-hover:scale-105 transition-all duration-500">
          <img src="/image.svg" alt="Memwyre" class="w-16 h-16 md:w-20 md:h-20 mb-3" />
          <span class="text-base md:text-lg font-bold tracking-tight text-text-primary">Memwyre</span>
        </div>

        <!-- Icons: 8 total distributed radially, alternating FAR/CLOSE -->

        <!-- 1. Top FAR -->
        <div
          class="absolute top-[3%] left-1/2 -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-1">
          <img src="@/assets/claude-color.svg" alt="Claude" class="w-10 h-10 md:w-14 md:h-14" />
          <div class="text-xs md:text-sm font-bold">Claude</div>
        </div>
        <!-- 2. Top Right CLOSE -->
        <div
          class="absolute top-[28%] left-[68%] -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-2"
          style="animation-delay: 0.3s;">
          <img src="@/assets/gemini-color.svg" alt="Gemini" class="w-10 h-10 md:w-14 md:h-14" />
          <div class="text-xs md:text-sm font-bold">Gemini</div>
        </div>
        <!-- 3. Right FAR -->
        <div
          class="absolute top-[44%] left-[92%] -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-3"
          style="animation-delay: 0.6s;">
          <img src="@/assets/chrome-logo-svgrepo-com.svg" alt="Chrome" class="w-10 h-10 md:w-14 md:h-14" />
          <div class="text-xs md:text-sm font-bold">Chrome</div>
        </div>
        <!-- 4. Bottom Right CLOSE -->
        <div
          class="absolute top-[60%] left-[68%] -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-1"
          style="animation-delay: 0.9s;">
          <img src="@/assets/perplexity-color.svg" alt="Perplexity" class="w-10 h-10 md:w-14 md:h-14" />
          <div class="text-xs md:text-sm font-bold">Perplexity</div>
        </div>
        <!-- 5. Bottom FAR -->
        <div
          class="absolute top-[84%] left-1/2 -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-2"
          style="animation-delay: 1.2s;">
          <img src="@/assets/openai.svg" alt="ChatGPT" class="w-10 h-10 md:w-14 md:h-14" />
          <div class="text-xs md:text-sm font-bold">ChatGPT</div>
        </div>
        <!-- 6. Bottom Left CLOSE -->
        <div
          class="absolute top-[60%] left-[32%] -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-3"
          style="animation-delay: 1.5s;">
          <img src="@/assets/notion-svgrepo-com.svg" alt="Notion" class="w-10 h-10 md:w-14 md:h-14" />
          <div class="text-xs md:text-sm font-bold">Notion</div>
        </div>
        <!-- 7. Left FAR -->
        <div
          class="absolute top-[44%] left-[8%] -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-1"
          style="animation-delay: 1.8s;">
          <img src="@/assets/openclaw-color.svg" alt="OpenClaw" class="w-10 h-10 md:w-14 md:h-14" />
          <div class="text-xs md:text-sm font-bold">OpenClaw</div>
        </div>
        <!-- 8. Top Left CLOSE -->
        <div
          class="absolute top-[28%] left-[32%] -translate-x-1/2 flex flex-col items-center gap-1 z-10 animate-float-2"
          style="animation-delay: 2.1s;">
          <img src="@/assets/Google-Antigravity-Icon-Full-Color.png" alt="Antigravity"
            class="w-10 h-10 md:w-14 md:h-14" />
          <div class="text-xs md:text-sm font-bold">Antigravity</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// Pure presentation component
</script>

<style scoped>
/* Floating icon animations */
@keyframes float {

  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-10px);
  }
}

.animate-float-1 {
  animation: float 4s ease-in-out infinite;
}

.animate-float-2 {
  animation: float 5s ease-in-out infinite reverse;
}

.animate-float-3 {
  animation: float 6s ease-in-out infinite;
}
.hero-serif {
  font-family: 'DM Serif Text', serif;
}
</style>
