<template>
  <div class="demo-shell dark">
    <OmnipresentDemo />
  </div>
</template>

<script setup>
import OmnipresentDemo from '@/components/landing/OmnipresentDemo.vue'
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
</style>
