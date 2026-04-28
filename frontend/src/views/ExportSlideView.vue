<template>
  <div class="fixed inset-0 bg-black flex items-center justify-center overflow-hidden">
    <!-- Forced 1920x1080 Container -->
    <div class="w-[1920px] h-[1080px] bg-[#1f1f23] shadow-2xl relative overflow-hidden">
      <component :is="activeSlide" v-if="activeSlide" />
      <div v-else class="w-full h-full flex items-center justify-center text-4xl text-white font-bold">
        Slide {{ slideId }} Not Found
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

import SlideOmnipresent from '@/components/slides/SlideOmnipresent.vue'
import SlideChat from '@/components/slides/SlideChat.vue'
import SlideTimeline from '@/components/slides/SlideTimeline.vue'
import SlideInbox from '@/components/slides/SlideInbox.vue'
import SlideCrossPost from '@/components/slides/SlideCrossPost.vue'

const route = useRoute()
const slideId = computed(() => route.params.id)

const slides = {
  '1': SlideOmnipresent,
  '2': SlideChat,
  '3': SlideTimeline,
  '4': SlideInbox,
  '5': SlideCrossPost
}

const activeSlide = computed(() => slides[slideId.value])
</script>

<style>
/* Remove all scrollbars for export */
body {
  overflow: hidden !important;
  margin: 0 !important;
  padding: 0 !important;
}
::-webkit-scrollbar {
  display: none !important;
}
</style>
