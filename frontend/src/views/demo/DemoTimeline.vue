<template>
  <div class="demo-shell dark">
    <TimelineDemo />
  </div>
</template>

<script setup>
import TimelineDemo from '@/components/landing/TimelineDemo.vue'
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
</style>
