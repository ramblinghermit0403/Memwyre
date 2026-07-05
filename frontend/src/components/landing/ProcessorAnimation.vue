<template>
  <div class="processor-animation-container">
    <div class="svg-wrapper" v-html="processorSvg"></div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
// Import the SVG raw content so we can inject it and target its internal IDs with CSS
import rawSvg from '@/assets/motion/processor_orange.svg?raw';

// Force HMR compile trigger: orange_processor_v4

// Remove explicit width and height from the root SVG to make it responsive
const processorSvg = computed(() => {
  return rawSvg
    .replace(/width="[\d.]+"/, 'width="100%"')
    .replace(/height="[\d.]+"/, 'height="100%"');
});
</script>

<style scoped>
.processor-animation-container {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: visible; /* Changed from hidden to allow scaling out */
}

.svg-wrapper {
  position: absolute;
  width: 220%;
  max-width: 220%;
  height: auto;
  transform: translate(4%, calc(5% + 100px));
  opacity: 1; /* Fully visible / unfaded on mobile view */
  transition: all 0.5s ease-in-out;
}

@media (min-width: 768px) {
  .svg-wrapper {
    width: 180%;
    max-width: 180%;
    transform: translate(calc(5% - 150px), 5%);
    opacity: 1;
  }
}

@media (min-width: 1024px) {
  .svg-wrapper {
    width: 180%;
    max-width: 180%;
    transform: translate(calc(5% - 300px), 5%);
    opacity: 1; /* Fully visible on large screens */
  }
}

@media (max-width: 640px) and (max-height: 720px) {
  .svg-wrapper {
    width: 160%;
    max-width: 160%;
    transform: translate(4%, calc(5% + 180px));
    opacity: 0.5; /* Slightly faded to avoid blocking readability on short screen */
  }
}
</style>

<!-- 
  Non-scoped styles for SVG animations.
  Vue scoped styles mangle @keyframes names, breaking animation references 
  on v-html injected SVG content. Using a separate non-scoped block avoids this.
-->
<style>
/* Ensure the injected SVG scales correctly */
.processor-animation-container svg {
  width: 100%;
  height: auto;
  display: block;
}

/* 
  Conveyor Belt Animation for the infinite tiles group.
*/
#conveyor-belt {
  animation: conveyorBelt 15s linear infinite;
}

/* 
  Memories Belt Animation - the pill-shaped labels flowing OUT of the processor.
  Same infinite loop technique: #memories-belt moves, static wrapper clips.
*/
#memories-belt {
  animation: memoriesBelt 15s linear infinite;
}

@keyframes conveyorBelt {
  0% {
    transform: translate(0, 0);
  }
  100% {
    transform: translate(1710px, -987.75px);
  }
}

@keyframes memoriesBelt {
  0% {
    transform: translate(0, 0);
  }
  100% {
    transform: translate(2370px, -1372px);
  }
}
</style>
