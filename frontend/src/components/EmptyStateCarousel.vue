<template>
  <div class="relative w-full h-full flex flex-col overflow-hidden" @mouseenter="pause" @mouseleave="resume">

    <!-- Slides -->
    <div class="relative flex-1 overflow-hidden">
      <div
        v-for="(slide, i) in slides"
        :key="slide.id"
        class="absolute inset-0 transition-opacity duration-500"
        :class="current === i ? 'opacity-100 pointer-events-auto' : 'opacity-0 pointer-events-none'"
      >
        <div class="h-full flex flex-col md:flex-row">

          <!-- Left: use-case text -->
          <div class="flex flex-col justify-center px-10 py-8 md:w-[42%] shrink-0 gap-5">
            <div class="flex items-center gap-2">
              <span class="text-[10px] font-bold uppercase tracking-widest text-[#D97757]">Use case</span>
              <span class="text-[10px] font-mono text-gray-400 dark:text-gray-500">{{ String(i + 1).padStart(2, '0') }} / {{ String(slides.length).padStart(2, '0') }}</span>
            </div>
            <div>
              <p class="text-xl font-bold text-gray-900 dark:text-white leading-snug">{{ slide.title }}</p>
              <p class="text-sm text-gray-500 dark:text-gray-400 mt-2 leading-relaxed">{{ slide.description }}</p>
            </div>
            <div class="flex flex-wrap gap-2">
              <span
                v-for="tag in slide.tags"
                :key="tag"
                class="text-[11px] px-2.5 py-1 rounded-full border border-gray-200 dark:border-border text-gray-500 dark:text-gray-400 bg-gray-50 dark:bg-surface-2 font-medium"
              >{{ tag }}</span>
            </div>
            <button
              @click="openQuickAdd"
              class="w-fit text-xs px-4 py-2 bg-[#D97757] text-white font-semibold rounded-lg hover:bg-[#C4654A] transition-colors shadow-sm"
            >
              Get started →
            </button>
          </div>

          <!-- Right: visual -->
          <div class="flex-1 relative overflow-hidden border-l border-gray-100 dark:border-border" :class="slide.bgClass">
            <!-- Ambient glow circles -->
            <div class="absolute inset-0 overflow-hidden pointer-events-none">
              <div class="absolute -top-20 -right-20 w-60 h-60 rounded-full opacity-[0.07]" :class="slide.glowColor + ' blur-3xl'" />
              <div class="absolute -bottom-10 -left-10 w-40 h-40 rounded-full opacity-[0.05]" :class="slide.glowColor + ' blur-2xl'" />
            </div>
            <!-- Cards scene -->
            <div class="absolute inset-0 flex items-center justify-center px-5 overflow-hidden">
              <div class="relative w-full max-w-[320px]">
                <component :is="slide.visual" />
              </div>
            </div>
            <!-- Bottom fade -->
            <div class="absolute inset-x-0 bottom-0 h-16 pointer-events-none z-10" :class="slide.fadeClass" />
          </div>
        </div>
      </div>
    </div>

    <!-- Dot nav -->
    <div class="flex items-center justify-center gap-2 py-3 border-t border-gray-100 dark:border-border shrink-0">
      <button
        v-for="(_, i) in slides"
        :key="i"
        @click="goTo(i)"
        class="h-1.5 rounded-full transition-all duration-300"
        :class="current === i ? 'w-5 bg-[#D97757]' : 'w-1.5 bg-gray-300 dark:bg-gray-600'"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, h } from 'vue';
import { useRouter } from 'vue-router';

import openaiSrc from '../assets/openai.svg';
import claudeSrc from '../assets/claude-color.svg';
import geminiSrc from '../assets/gemini-color.svg';
import perplexitySrc from '../assets/perplexity-color.svg';
import TimelineStaticMock from './slides/mocks/TimelineStaticMock.vue';

const router = useRouter();
const current = ref(0);
let timer = null;
const INTERVAL = 6000;

// ── Visual: AI Agent with memory ─────────────────────────────────────────────
const AgentVisual = {
  render() {
    const memories = ['OAuth2 Architecture Notes', 'API Rate Limiting Research', 'Competitor Analysis Q2'];
    return h('div', { class: 'space-y-3' }, [
      // Agent header card
      h('div', { class: 'bg-white dark:bg-surface rounded-xl border border-gray-200 dark:border-border shadow-md overflow-hidden' }, [
        h('div', { class: 'px-4 py-3 flex items-center gap-3 bg-gradient-to-r from-[#D97757]/5 to-transparent border-b border-gray-100 dark:border-border' }, [
          h('div', { class: 'w-9 h-9 rounded-full bg-gradient-to-br from-[#D97757] to-[#E89B7B] flex items-center justify-center shadow-sm' }, [
            h('svg', { class: 'w-4 h-4 text-white', fill: 'none', viewBox: '0 0 24 24', stroke: 'currentColor', 'stroke-width': '2' }, [
              h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', d: 'M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z' })
            ]),
          ]),
          h('div', {}, [
            h('p', { class: 'text-sm font-bold text-gray-900 dark:text-white' }, 'Research Agent'),
            h('p', { class: 'text-[10px] text-gray-400' }, '3 memories connected'),
          ]),
          h('span', { class: 'ml-auto text-[10px] px-2.5 py-1 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200/60 dark:bg-emerald-950/30 dark:text-emerald-300 dark:border-emerald-900/40 font-bold' }, '● Active'),
        ]),
        // Memory links
        h('div', { class: 'px-4 py-3 space-y-2' },
          memories.map((m, idx) =>
            h('div', {
              class: 'flex items-center gap-2.5 px-3 py-2 rounded-lg bg-gray-50 dark:bg-surface-2 border border-gray-100 dark:border-border',
              style: `animation: fadeSlideIn 0.4s ease ${idx * 0.1}s both`,
            }, [
              h('div', { class: 'w-5 h-5 rounded flex items-center justify-center bg-[#D97757]/10 shrink-0' }, [
                h('svg', { class: 'w-3 h-3 text-[#D97757]', fill: 'none', viewBox: '0 0 24 24', stroke: 'currentColor', 'stroke-width': '2' }, [
                  h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', d: 'M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101' })
                ]),
              ]),
              h('span', { class: 'text-xs text-gray-700 dark:text-gray-300 font-medium' }, m),
            ])
          )
        ),
      ]),
      // Chat bubble
      h('div', { class: 'relative bg-white dark:bg-surface rounded-xl border border-gray-200 dark:border-border shadow-md px-4 py-3' }, [
        h('div', { class: 'absolute -top-1.5 left-6 w-3 h-3 bg-white dark:bg-surface border-l border-t border-gray-200 dark:border-border rotate-45' }),
        h('div', { class: 'flex items-start gap-2.5' }, [
          h('img', { src: openaiSrc, class: 'w-5 h-5 mt-0.5 shrink-0' }),
          h('p', { class: 'text-xs text-gray-600 dark:text-gray-300 leading-relaxed' }, [
            h('span', { class: 'font-semibold text-gray-900 dark:text-white' }, 'Based on your OAuth2 notes: '),
            'Use refresh token rotation with PKCE and 15-min access token TTL.',
          ]),
        ]),
      ]),
    ]);
  }
};

// ── Visual: Company knowledge base ───────────────────────────────────────────
const CompanyKBVisual = {
  render() {
    const docs = [
      { emoji: '📄', title: 'Engineering RFC — Auth v2',    dept: 'Engineering', color: 'bg-blue-50 text-blue-700 border-blue-200/60 dark:bg-blue-950/30 dark:text-blue-300 dark:border-blue-900/40' },
      { emoji: '📊', title: 'Q2 Sales Playbook',            dept: 'Sales',       color: 'bg-emerald-50 text-emerald-700 border-emerald-200/60 dark:bg-emerald-950/30 dark:text-emerald-300 dark:border-emerald-900/40' },
      { emoji: '🎨', title: 'Brand Guidelines 2025',        dept: 'Design',      color: 'bg-purple-50 text-purple-700 border-purple-200/60 dark:bg-purple-950/30 dark:text-purple-300 dark:border-purple-900/40' },
      { emoji: '🔒', title: 'Security & Onboarding Policy', dept: 'HR',          color: 'bg-amber-50 text-amber-700 border-amber-200/60 dark:bg-amber-950/30 dark:text-amber-300 dark:border-amber-900/40' },
    ];
    return h('div', { class: 'bg-white dark:bg-surface rounded-xl border border-gray-200 dark:border-border shadow-md overflow-hidden' }, [
      h('div', { class: 'px-4 py-3 border-b border-gray-100 dark:border-border flex items-center justify-between bg-gradient-to-r from-blue-500/5 to-transparent' }, [
        h('div', { class: 'flex items-center gap-2' }, [
          h('div', { class: 'w-7 h-7 rounded-lg bg-blue-50 dark:bg-blue-950/30 flex items-center justify-center' }, [
            h('span', { class: 'text-sm' }, '🏢'),
          ]),
          h('div', {}, [
            h('span', { class: 'text-sm font-bold text-gray-900 dark:text-white' }, 'Acme Corp'),
            h('p', { class: 'text-[10px] text-gray-400' }, 'Shared knowledge base'),
          ]),
        ]),
        h('span', { class: 'text-[10px] text-gray-400 font-mono bg-gray-100 dark:bg-surface-2 px-2 py-0.5 rounded' }, '42 docs'),
      ]),
      h('div', {},
        docs.map(({ emoji, title, dept, color }, idx) =>
          h('div', {
            class: `flex items-center gap-3 px-4 py-3 border-b border-gray-50 dark:border-border last:border-0 hover:bg-gray-50/50 dark:hover:bg-surface-2/50 transition-colors`,
            style: `animation: fadeSlideIn 0.4s ease ${idx * 0.08}s both`,
          }, [
            h('span', { class: 'text-base w-6 text-center' }, emoji),
            h('div', { class: 'flex-1 min-w-0' }, [
              h('p', { class: 'text-xs font-semibold text-gray-900 dark:text-white truncate' }, title),
            ]),
            h('span', { class: `text-[10px] font-bold px-2 py-0.5 rounded-full border shrink-0 ${color}` }, dept),
          ])
        )
      ),
    ]);
  }
};

// ── Visual: Personal second brain ────────────────────────────────────────────
const TimelineSlideVisual = {
  render() {
    return h('div', { class: 'relative w-full flex items-start justify-center overflow-hidden h-[330px] pt-2' }, [
      h('div', { class: 'transform scale-[0.45] origin-top' }, [
        h(TimelineStaticMock)
      ])
    ]);
  }
};

// ── Visual: Dev context manager ──────────────────────────────────────────────
const DevContextVisual = {
  render() {
    const contexts = [
      { label: 'Auth System Guidelines',     tag: 'Architecture', color: 'bg-blue-50 text-blue-700 border-blue-200/60 dark:bg-blue-950/30 dark:text-blue-300 dark:border-blue-900/40' },
      { label: 'API Rate Limiting — specs',  tag: 'Backend',      color: 'bg-purple-50 text-purple-700 border-purple-200/60 dark:bg-purple-950/30 dark:text-purple-300 dark:border-purple-900/40' },
      { label: 'Error handling conventions', tag: 'Standards',    color: 'bg-amber-50 text-amber-700 border-amber-200/60 dark:bg-amber-950/30 dark:text-amber-300 dark:border-amber-900/40' },
    ];
    return h('div', { class: 'space-y-3' }, [
      // Input bar
      h('div', { class: 'bg-white dark:bg-surface rounded-xl border border-gray-200 dark:border-border shadow-md overflow-hidden' }, [
        h('div', { class: 'px-4 py-3 flex items-center gap-3 border-b border-gray-100 dark:border-border bg-gradient-to-r from-emerald-500/5 to-transparent' }, [
          h('img', { src: openaiSrc, class: 'w-5 h-5 shrink-0' }),
          h('span', { class: 'text-xs font-bold text-gray-900 dark:text-white' }, 'ChatGPT'),
          h('span', { class: 'ml-auto text-[10px] px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200/60 dark:bg-emerald-950/30 dark:text-emerald-300 dark:border-emerald-900/40 font-bold' }, '3 injected'),
        ]),
        h('div', { class: 'px-4 py-3' }, [
          h('div', { class: 'flex items-center gap-2' }, [
            h('span', { class: 'text-xs text-gray-500 dark:text-gray-400' }, 'Fix the token refresh race condition...'),
            h('div', { class: 'w-0.5 h-4 bg-gray-400 rounded-sm animate-pulse' }),
          ]),
        ]),
      ]),
      // Context badges — stacked
      h('div', { class: 'space-y-2' },
        contexts.map(({ label, tag, color }, idx) =>
          h('div', {
            class: 'flex items-center gap-3 px-4 py-2.5 bg-white dark:bg-surface rounded-xl border border-gray-200 dark:border-border shadow-sm',
            style: `animation: fadeSlideIn 0.4s ease ${idx * 0.1}s both`,
          }, [
            h('div', { class: 'w-5 h-5 rounded flex items-center justify-center bg-[#D97757]/10 shrink-0' }, [
              h('svg', { class: 'w-3 h-3 text-[#D97757]', fill: 'none', viewBox: '0 0 24 24', stroke: 'currentColor', 'stroke-width': '2' }, [
                h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', d: 'M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101' })
              ]),
            ]),
            h('span', { class: 'text-xs text-gray-700 dark:text-gray-300 font-medium flex-1 truncate' }, label),
            h('span', { class: `text-[10px] font-bold px-2 py-0.5 rounded-full border shrink-0 ${color}` }, tag),
          ])
        )
      ),
    ]);
  }
};

// ── Slides config ─────────────────────────────────────────────────────────────
const slides = [
  {
    id: 'agent',
    title: 'Build AI agents with memory',
    description: 'Give your AI agents persistent context. They remember what you\'ve built, decided, and learned — so every session picks up where you left off.',
    tags: ['#agents', '#memory', '#ChatGPT', '#Claude'],
    visual: AgentVisual,
    bgClass: 'bg-gradient-to-br from-gray-50 via-orange-50/30 to-gray-50 dark:from-surface-2 dark:via-surface-2 dark:to-surface-2',
    glowColor: 'bg-[#D97757]',
    fadeClass: 'bg-gradient-to-t from-gray-50 dark:from-surface-2 to-transparent',
  },
  {
    id: 'company-kb',
    title: 'Company knowledge base',
    description: 'Centralize RFCs, playbooks, and policies. Every teammate\'s AI tool pulls from the same source of truth — no more copy-pasting context.',
    tags: ['#teams', '#knowledge', '#onboarding', '#docs'],
    visual: CompanyKBVisual,
    bgClass: 'bg-gradient-to-br from-gray-50 via-blue-50/30 to-gray-50 dark:from-surface-2 dark:via-surface-2 dark:to-surface-2',
    glowColor: 'bg-blue-500',
    fadeClass: 'bg-gradient-to-t from-gray-50 dark:from-surface-2 to-transparent',
  },
  {
    id: 'second-brain',
    title: 'Your personal second brain',
    description: 'Every insight, book note, and conversation saved automatically. Ask any AI tool questions across your entire knowledge history.',
    tags: ['#personal', '#notes', '#research', '#PKM'],
    visual: TimelineSlideVisual,
    bgClass: 'bg-gradient-to-br from-gray-50 via-violet-50/30 to-gray-50 dark:from-surface-2 dark:via-surface-2 dark:to-surface-2',
    glowColor: 'bg-violet-500',
    fadeClass: 'bg-gradient-to-t from-gray-50 dark:from-surface-2 to-transparent',
  },
  {
    id: 'dev-context',
    title: 'Never lose dev context again',
    description: 'Save architecture decisions, API specs, and coding standards. Inject them into any AI coding tool with one click — no re-explaining.',
    tags: ['#developers', '#architecture', '#Cursor', '#Copilot'],
    visual: DevContextVisual,
    bgClass: 'bg-gradient-to-br from-gray-50 via-emerald-50/30 to-gray-50 dark:from-surface-2 dark:via-surface-2 dark:to-surface-2',
    glowColor: 'bg-emerald-500',
    fadeClass: 'bg-gradient-to-t from-gray-50 dark:from-surface-2 to-transparent',
  },
];

// ── Carousel logic ────────────────────────────────────────────────────────────
const advance = () => { current.value = (current.value + 1) % slides.length; };
const goTo = (i) => { current.value = i; restart(); };
const pause = () => clearInterval(timer);
const resume = () => { clearInterval(timer); timer = setInterval(advance, INTERVAL); };
const restart = () => { clearInterval(timer); timer = setInterval(advance, INTERVAL); };
const openQuickAdd = () => router.push({ query: { quick_add: 'documents' } });

onMounted(() => { timer = setInterval(advance, INTERVAL); });
onUnmounted(() => clearInterval(timer));
</script>

<style scoped>
@keyframes fadeSlideIn {
  from { opacity: 0; transform: translateY(6px); }
  to   { opacity: 1; transform: translateY(0); }
}
</style>
