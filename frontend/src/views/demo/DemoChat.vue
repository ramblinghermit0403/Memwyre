<template>
  <div class="demo-shell dark">
    <!-- ChatDemo uses IntersectionObserver — wrap with enough size to trigger it -->
    <div class="demo-inner">
      <ChatDemo />
    </div>
  </div>
</template>

<script setup>
import ChatDemo from '@/components/landing/ChatDemo.vue'
</script>

<style scoped>
.demo-shell {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background: #000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.demo-inner {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Override ChatDemo's own max-width + rounded border when fullscreen */
.demo-inner :deep(.relative.w-full.max-w-4xl) {
  max-width: 100%;
  width: 100%;
  height: 100%;
  border-radius: 0;
  border: none;
  aspect-ratio: unset;
}
</style>
