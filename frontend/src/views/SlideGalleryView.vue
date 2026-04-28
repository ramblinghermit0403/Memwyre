<template>
  <div class="min-h-screen bg-[#0d0f14] text-white p-8 overflow-y-auto">
    <div class="max-w-[1400px] mx-auto space-y-24">
      
      <header class="mb-12">
        <h1 class="text-4xl font-bold tracking-tight mb-2">Memwyre Cinematic Slides</h1>
        <p class="text-gray-400">16:9 Presentation Assets (1920x1080 design-time resolution)</p>
      </header>

      <!-- Slide 1: Omnipresent -->
      <section class="space-y-6">
        <h2 class="text-2xl font-semibold px-4 flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-[#1a1a1e] border border-white/10 flex items-center justify-center text-sm">1</span>
          Omnipresent Overlay
        </h2>
        <div class="relative w-full aspect-video bg-[#1a1a1e] rounded-[1.5rem] overflow-hidden border border-white/5 shadow-2xl scale-wrapper">
          <div class="slide-content">
            <SlideOmnipresent />
          </div>
        </div>
      </section>

      <!-- Slide 2: Chat -->
      <section class="space-y-6">
        <h2 class="text-2xl font-semibold px-4 flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-[#1a1a1e] border border-white/10 flex items-center justify-center text-sm">2</span>
          Contextual Chat
        </h2>
        <div class="relative w-full aspect-video bg-[#1a1a1e] rounded-[1.5rem] overflow-hidden border border-white/5 shadow-2xl scale-wrapper">
          <div class="slide-content">
            <SlideChat />
          </div>
        </div>
      </section>

      <!-- Slide 3: Timeline -->
      <section class="space-y-6">
        <h2 class="text-2xl font-semibold px-4 flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-[#1a1a1e] border border-white/10 flex items-center justify-center text-sm">3</span>
          Timeline Extraction
        </h2>
        <div class="relative w-full aspect-video bg-[#1a1a1e] rounded-[1.5rem] overflow-hidden border border-white/5 shadow-2xl scale-wrapper">
          <div class="slide-content">
            <SlideTimeline />
          </div>
        </div>
      </section>

      <!-- Slide 4: Inbox -->
      <section class="space-y-6">
        <h2 class="text-2xl font-semibold px-4 flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-[#1a1a1e] border border-white/10 flex items-center justify-center text-sm">4</span>
          Memory Inbox
        </h2>
        <div class="relative w-full aspect-video bg-[#1a1a1e] rounded-[1.5rem] overflow-hidden border border-white/5 shadow-2xl scale-wrapper">
          <div class="slide-content">
            <SlideInbox />
          </div>
        </div>
      </section>

      <!-- Slide 5: Cross-Post -->
      <section class="space-y-6">
        <h2 class="text-2xl font-semibold px-4 flex items-center gap-3">
          <span class="w-8 h-8 rounded-full bg-[#1a1a1e] border border-white/10 flex items-center justify-center text-sm">5</span>
          Instant Handoff
        </h2>
        <div class="relative w-full aspect-video bg-[#1a1a1e] rounded-[1.5rem] overflow-hidden border border-white/5 shadow-2xl scale-wrapper">
          <div class="slide-content">
            <SlideCrossPost />
          </div>
        </div>
      </section>

    </div>
  </div>
</template>

<script setup>
import SlideOmnipresent from '@/components/slides/SlideOmnipresent.vue'
import SlideChat from '@/components/slides/SlideChat.vue'
import SlideTimeline from '@/components/slides/SlideTimeline.vue'
import SlideInbox from '@/components/slides/SlideInbox.vue'
import SlideCrossPost from '@/components/slides/SlideCrossPost.vue'
</script>

<style scoped>
.scale-wrapper {
  /* Use inline-size for more reliable container queries in responsive layouts */
  container-type: inline-size;
  width: 100%;
}

.slide-content {
  position: absolute;
  top: 0;
  left: 0;
  width: 1920px;
  height: 1080px;
  transform: scale(calc(100cqw / 1920));
  transform-origin: top left;
  background: #1a1a1e;
}
</style>
