<template>
  <div class="demo-shell dark">
    <InboxDemo />
  </div>
</template>

<script setup>
import InboxDemo from '@/components/landing/InboxDemo.vue'
</script>

<style scoped>
.demo-shell {
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background: #111111;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Make InboxDemo fill the whole screen */
.demo-shell :deep(.dark.w-full.h-full) {
  width: 100vw;
  height: 100vh;
  border-radius: 0;
  border: none;
}
</style>
