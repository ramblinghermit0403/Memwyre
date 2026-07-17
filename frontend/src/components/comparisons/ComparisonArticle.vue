<template>
  <div class="min-h-screen bg-white text-gray-900 font-sans relative overflow-x-hidden selection:bg-[#D97757] selection:text-white pt-16">
    <div class="absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>
    <div class="absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>

    <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 relative z-10">
      <div class="pt-6">
        <div class="flex flex-col gap-2 sm:flex-row sm:justify-between sm:items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ COMPARISONS / {{ article.breadcrumb }}</div>
          <div>LAST RESEARCHED: {{ article.researchedAt }}</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-200 pointer-events-none select-none mb-8"></div>
      </div>

      <header class="space-y-6 max-w-4xl text-left">
        <p class="text-xs uppercase tracking-wider font-mono font-bold text-[#D97757]">{{ article.category }}</p>
        <h1 class="hero-serif text-4xl sm:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-900">
          {{ article.title }} <br />
          <span class="italic font-medium text-gray-900">
            {{ article.subtitleStart }}
            <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">{{ article.subtitleHighlight }}</span>
          </span>
        </h1>
        <p class="text-lg text-gray-500 leading-relaxed font-normal">
          {{ article.description }}
        </p>
      </header>

      <section class="grid grid-cols-1 lg:grid-cols-3 gap-6 my-10 text-left">
        <div class="lg:col-span-2 border border-dashed border-gray-300 rounded p-6 bg-[#FDFCFB] relative">
          <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
            <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
            <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
          </div>

          <h2 class="hero-serif text-xl sm:text-2xl text-gray-900 mb-4">Short Verdict</h2>
          <p class="text-sm text-gray-600 leading-relaxed mb-5">{{ article.verdict }}</p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div v-for="item in article.bestFor" :key="item.title" class="border border-gray-200 bg-white rounded p-4">
              <div class="text-[11px] uppercase tracking-wider font-mono font-bold text-gray-400 mb-2">{{ item.label }}</div>
              <h3 class="text-sm font-bold text-gray-900 mb-2">{{ item.title }}</h3>
              <p class="text-xs text-gray-500 leading-relaxed">{{ item.body }}</p>
            </div>
          </div>
        </div>

        <aside class="border border-gray-200 rounded p-6 bg-white">
          <h2 class="hero-serif text-xl text-gray-900 mb-4">Research Basis</h2>
          <ul class="space-y-3 text-sm text-gray-600">
            <li v-for="basis in article.researchBasis" :key="basis" class="flex gap-2">
              <span class="text-[#D97757] font-bold">/</span>
              <span>{{ basis }}</span>
            </li>
          </ul>
        </aside>
      </section>

      <section class="my-10 text-left">
        <h2 class="hero-serif text-xl sm:text-2xl text-gray-900 mb-6">Quick Comparison</h2>
        <div class="overflow-x-auto border border-gray-200 rounded bg-white">
          <table class="w-full text-sm text-left text-gray-600">
            <thead class="text-xs uppercase bg-gray-100 text-gray-700 border-b border-gray-200 font-mono">
              <tr>
                <th scope="col" class="px-6 py-4">Question</th>
                <th scope="col" class="px-6 py-4 bg-[#D97757]/5 text-gray-950 font-bold">Memwyre</th>
                <th scope="col" class="px-6 py-4">{{ article.competitor }}</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 text-gray-700">
              <tr v-for="row in article.quickComparison" :key="row.question">
                <td class="px-6 py-4 font-bold text-gray-900 align-top">{{ row.question }}</td>
                <td class="px-6 py-4 bg-[#D97757]/5 text-gray-950 align-top">{{ row.memwyre }}</td>
                <td class="px-6 py-4 align-top">{{ row.competitor }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <section class="grid grid-cols-1 md:grid-cols-2 gap-12 py-10 text-left">
        <article v-for="column in article.productFit" :key="column.title" class="space-y-4">
          <h2 class="hero-serif text-2xl text-gray-900">{{ column.title }}</h2>
          <p v-for="paragraph in column.body" :key="paragraph" class="text-gray-600 leading-relaxed text-sm">
            {{ paragraph }}
          </p>
        </article>
      </section>

      <section class="grid grid-cols-1 lg:grid-cols-2 gap-6 my-10 text-left">
        <div class="border border-gray-200 rounded p-6 bg-white">
          <h2 class="hero-serif text-xl sm:text-2xl text-gray-900 mb-5">Architecture And Workflow</h2>
          <div class="space-y-5">
            <div v-for="item in article.architecture" :key="item.title">
              <h3 class="text-sm font-bold text-gray-900 mb-1">{{ item.title }}</h3>
              <p class="text-sm text-gray-600 leading-relaxed">{{ item.body }}</p>
            </div>
          </div>
        </div>

        <div class="border border-gray-200 rounded p-6 bg-white">
          <h2 class="hero-serif text-xl sm:text-2xl text-gray-900 mb-5">Use Case Fit</h2>
          <div class="space-y-4">
            <div v-for="item in article.useCases" :key="item.useCase" class="grid grid-cols-1 sm:grid-cols-[150px_1fr] gap-1 sm:gap-4 border-b border-gray-100 pb-4 last:border-b-0 last:pb-0">
              <div class="text-xs uppercase tracking-wider font-mono font-bold text-gray-400">{{ item.useCase }}</div>
              <div class="text-sm text-gray-600 leading-relaxed">{{ item.fit }}</div>
            </div>
          </div>
        </div>
      </section>

      <section class="grid grid-cols-1 md:grid-cols-2 gap-6 my-10 text-left">
        <div v-for="column in article.limitations" :key="column.title" class="border border-gray-200 rounded p-6 bg-white">
          <h2 class="hero-serif text-xl sm:text-2xl text-gray-900 mb-4">{{ column.title }}</h2>
          <ul class="space-y-3 text-sm text-gray-600 leading-relaxed">
            <li v-for="item in column.items" :key="item" class="flex gap-2">
              <span class="text-[#D97757] font-bold">/</span>
              <span>{{ item }}</span>
            </li>
          </ul>
        </div>
      </section>

      <section class="border border-gray-200 rounded p-6 bg-[#FDFCFB] my-10 text-left">
        <h2 class="hero-serif text-xl sm:text-2xl text-gray-900 mb-5">Final Recommendation</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div v-for="item in article.recommendations" :key="item.title">
            <h3 class="text-sm font-bold text-gray-900 mb-2">{{ item.title }}</h3>
            <p class="text-sm text-gray-600 leading-relaxed">{{ item.body }}</p>
          </div>
        </div>
      </section>

      <section class="my-10 text-left">
        <h2 class="hero-serif text-xl sm:text-2xl text-gray-900 mb-4">Sources Reviewed</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
          <a
            v-for="source in article.sources"
            :key="source.url"
            :href="source.url"
            target="_blank"
            rel="noopener noreferrer"
            class="border border-gray-200 rounded p-4 text-sm text-gray-600 hover:text-[#D97757] hover:border-[#D97757]/50 transition-colors"
          >
            <span class="font-bold text-gray-900">{{ source.label }}</span>
            <span class="block text-xs text-gray-400 mt-1">{{ source.url }}</span>
          </a>
        </div>
      </section>

      <div class="p-8 bg-[#050614] text-white rounded text-center my-12 relative overflow-hidden">
        <h2 class="hero-serif text-2xl sm:text-3xl mb-3">Build A Shared Memory Layer</h2>
        <p class="text-gray-400 text-sm max-w-xl mx-auto mb-6">
          Connect your browser, IDE, MCP clients, and developer agents to one persistent memory vault.
        </p>
        <div class="flex flex-col sm:flex-row justify-center gap-4">
          <router-link to="/signup/" class="px-6 py-2.5 bg-[#D97757] hover:bg-[#e68a6c] text-white text-sm font-semibold rounded transition-colors shadow-sm">
            Start Free
          </router-link>
          <router-link to="/mcp" class="px-6 py-2.5 bg-white/10 hover:bg-white/20 text-white text-sm font-semibold rounded transition-colors">
            Explore MCP Setup
          </router-link>
        </div>
      </div>
    </div>

    <SiteFooter />
  </div>
</template>

<script setup>
import SiteFooter from '@/components/SiteFooter.vue';

defineProps({
  article: {
    type: Object,
    required: true,
  },
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

.hero-serif {
  font-family: 'Playfair Display', Georgia, serif;
}
</style>
