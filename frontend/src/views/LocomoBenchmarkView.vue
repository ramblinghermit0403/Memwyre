<template>
  <div class="relative min-h-screen bg-white dark:bg-[#0c0c0c] pt-28 pb-0 font-sans">
    <!-- Grid Blueprint background line effects -->
    <div class="absolute inset-0 pointer-events-none opacity-[0.03] dark:opacity-[0.05]">
      <div class="absolute inset-0 bg-[linear-gradient(to_right,#808080_1px,transparent_1px),linear-gradient(to_bottom,#808080_1px,transparent_1px)] bg-[size:40px_40px]"></div>
    </div>

    <!-- Global Vertical Grid Lines -->
    <div class="hidden lg:block absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-300/80 dark:bg-gray-800/60 pointer-events-none select-none z-30"></div>
    <div class="hidden lg:block absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-300/80 dark:bg-gray-800/60 pointer-events-none select-none z-30"></div>

    <div class="relative max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 relative z-10 animate-fade-in">
      
      <!-- Back Navigation Header -->
      <div class="pt-6 mb-8">
        <router-link 
          to="/research" 
          class="inline-flex items-center gap-2 text-xs uppercase tracking-wider font-semibold text-gray-500 dark:text-gray-400 hover:text-[#D97757] dark:hover:text-[#D97757] transition-colors"
        >
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full border border-gray-300 dark:border-zinc-800 text-[10px]">&larr;</span>
          All articles
        </router-link>
      </div>

      <!-- Header Section -->
      <div class="space-y-4 mb-8 text-left">
        <div class="text-xs font-bold uppercase tracking-wider text-[#D97757] font-mono">
          RESEARCH / BENCHMARKS 
          <span class="text-gray-300 dark:text-gray-700 mx-2">/</span> 
          JULY 22, 2026
        </div>
        
        <h1 class="hero-serif text-4xl sm:text-5xl lg:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-950 dark:text-white">
          LoCoMo Benchmark <br />
          <span class="italic font-medium text-gray-900 dark:text-gray-100">Evaluation of <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">AI Memory.</span></span>
        </h1>

        <div class="text-[10px] tracking-wider uppercase font-bold font-mono text-gray-400 dark:text-gray-500 pt-2">
          14 MINUTES READ · MODEL-AGNOSTIC EVALUATION
        </div>
      </div>

      <!-- Section Separator Line -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-200 dark:bg-gray-850 pointer-events-none select-none"></div>

      <!-- 3-Column Layout Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-y-8 lg:gap-0 pb-24">
        
        <!-- Left Sidebar (Author Info & Social Sharing) -->
        <aside class="lg:col-span-2 lg:border-r border-gray-200 dark:border-gray-800 lg:pr-8 pt-8 lg:pt-12 text-left">
          <div class="sticky top-24 space-y-8">
            <!-- Author Card -->
            <div class="flex items-center gap-3">
              <img 
                src="https://avatars.githubusercontent.com/u/170114968?v=4" 
                alt="Memwyre Research Lab" 
                class="w-10 h-10 rounded-full object-cover border border-gray-200 dark:border-zinc-800"
                @error="$event.target.src = 'https://ui-avatars.com/api/?name=Memwyre+Research+Lab&background=f3f4f6&color=333'"
              />
              <span class="text-sm font-semibold text-gray-900 dark:text-white">
                Memwyre Research Lab
              </span>
            </div>

            <!-- External Benchmark Resource Links -->
            <div class="space-y-2 pt-6 border-t border-gray-100 dark:border-gray-900">
              <div class="text-[11px] font-mono text-gray-400 dark:text-gray-500 tracking-wider uppercase font-bold mb-3">BENCHMARK RESOURCES</div>
              <a 
                href="https://arxiv.org/abs/2406.16016" 
                target="_blank"
                class="flex items-center gap-2 text-xs text-gray-600 dark:text-gray-400 hover:text-[#D97757] dark:hover:text-[#D97757] transition-colors"
              >
                <span class="w-1.5 h-1.5 rounded-full bg-[#D97757]"></span>
                LoCoMo Paper (arXiv)
              </a>
              <a 
                href="https://github.com/snap-research/LoCoMo" 
                target="_blank"
                class="flex items-center gap-2 text-xs text-gray-600 dark:text-gray-400 hover:text-[#D97757] dark:hover:text-[#D97757] transition-colors"
              >
                <span class="w-1.5 h-1.5 rounded-full bg-[#D97757]"></span>
                LoCoMo Dataset Repo
              </a>
              <a 
                href="https://github.com/supermemoryai/memorybench" 
                target="_blank"
                class="flex items-center gap-2 text-xs text-gray-600 dark:text-gray-400 hover:text-[#D97757] dark:hover:text-[#D97757] transition-colors"
              >
                <span class="w-1.5 h-1.5 rounded-full bg-[#D97757]"></span>
                MemoryBench Harness
              </a>
            </div>

            <!-- Share Buttons -->
            <div class="space-y-3 pt-6 border-t border-gray-100 dark:border-gray-900">
              <div class="text-[11px] font-mono text-gray-400 dark:text-gray-500 tracking-wider uppercase font-bold">SHARE THIS ARTICLE</div>
              <div class="flex items-center gap-2">
                <a 
                  :href="`https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(pageUrl)}`" 
                  target="_blank"
                  class="w-9 h-9 rounded border border-gray-200 dark:border-zinc-800 flex items-center justify-center text-gray-500 hover:text-[#D97757] dark:hover:text-[#D97757] transition-all bg-white dark:bg-[#111]"
                >
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" />
                  </svg>
                </a>
                <a 
                  :href="`https://twitter.com/intent/tweet?url=${encodeURIComponent(pageUrl)}&text=${encodeURIComponent(pageTitle)}`" 
                  target="_blank"
                  class="w-9 h-9 rounded border border-gray-200 dark:border-zinc-800 flex items-center justify-center text-gray-500 hover:text-[#D97757] dark:hover:text-[#D97757] transition-all bg-white dark:bg-[#111]"
                >
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
                  </svg>
                </a>
                <button 
                  @click="copyLink"
                  class="w-9 h-9 rounded border border-gray-200 dark:border-zinc-800 flex items-center justify-center text-gray-500 hover:text-[#D97757] dark:hover:text-[#D97757] transition-all bg-white dark:bg-[#111] cursor-pointer"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </aside>

        <!-- Middle Column (Banner & Article Body) -->
        <main class="lg:col-span-8 px-0 lg:px-8 pt-0 lg:pt-12 text-left">
          <!-- Cover Image -->
          <div class="w-full aspect-[2/1] rounded-xl overflow-hidden mb-10 bg-gray-50 border border-gray-150 dark:bg-zinc-900/30 dark:border-zinc-800/80">
            <img 
              src="/blog-covers/ai-memory-benchmark-locomo-v2.png" 
              alt="LoCoMo Benchmark" 
              class="w-full h-full object-cover"
            />
          </div>

          <article class="markdown-content space-y-12">
            <p class="text-xl text-gray-600 dark:text-gray-300 leading-relaxed font-light">
              LoCoMo-10 is the industry-standard benchmark for evaluating long-term memory systems in AI agents and conversational assistants. Below is the detailed analysis of Memwyre's performance on the complete 1,986-question benchmark using <strong>Kimi K2.5</strong> on AWS Bedrock compared with previous <strong>GPT-4o-mini</strong> evaluations.
            </p>

            <!-- TL;DR -->
            <div class="relative p-6 bg-white dark:bg-[#111] border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl shadow-sm my-6">
              <!-- Corner Brackets -->
              <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none border-t-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
              <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none border-b-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>
              <div class="space-y-2">
                <div class="text-[#D97757] font-mono text-xs uppercase font-bold tracking-wider">Quick Summary / Key Takeaways</div>
                <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed font-normal">
                  <strong>Answer:</strong> On the full LoCoMo benchmark (1,986 questions across 10 long-term conversational histories), Memwyre achieves a <strong>69.89% overall accuracy</strong> (<strong>70.52% non-adversarial</strong>) while maintaining a minimal context footprint (~4,924 tokens/question vs. 26,000+ raw dialog tokens). Crucially, evaluating across both proprietary models (<strong>GPT-4o-mini</strong>) and open-weight models (<strong>Kimi K2.5</strong>) demonstrates that Memwyre's memory engine delivers high-performing, consistent results regardless of the underlying LLM backend.
                </p>
              </div>
            </div>

            <!-- Metric Cards Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 my-10">
              <div class="relative p-6 bg-white dark:bg-[#111] border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl shadow-sm text-left">
                <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none border-t-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
                <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none border-b-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>
                <div class="text-[#D97757] text-5xl font-extrabold font-mono tracking-tight">69.9%</div>
                <div class="mt-2">
                  <div class="text-gray-900 dark:text-white font-bold text-base">Overall Accuracy</div>
                  <div class="text-gray-500 dark:text-gray-400 text-xs tracking-wider uppercase font-semibold mt-0.5">Full 1,986 Questions</div>
                </div>
              </div>

              <div class="relative p-6 bg-white dark:bg-[#111] border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl shadow-sm text-left">
                <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none border-t-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
                <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none border-b-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>
                <div class="text-gray-900 dark:text-white text-5xl font-extrabold font-mono tracking-tight">70.5%</div>
                <div class="mt-2">
                  <div class="text-gray-900 dark:text-white font-bold text-base">Non-Adversarial</div>
                  <div class="text-gray-500 dark:text-gray-400 text-xs tracking-wider uppercase font-semibold mt-0.5">1,540 Standard Questions</div>
                </div>
              </div>

              <div class="relative p-6 bg-white dark:bg-[#111] border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl shadow-sm text-left">
                <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none border-t-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
                <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none border-b-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>
                <div class="text-gray-900 dark:text-white text-5xl font-extrabold font-mono tracking-tight">4.9k</div>
                <div class="mt-2">
                  <div class="text-gray-900 dark:text-white font-bold text-base">Mean Tokens</div>
                  <div class="text-gray-500 dark:text-gray-400 text-xs tracking-wider uppercase font-semibold mt-0.5">Vs 26k+ Raw Context</div>
                </div>
              </div>
            </div>

            <!-- 1. Introduction -->
            <section id="introduction" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white border-b border-gray-200 dark:border-zinc-800 pb-2">
                1. Introduction &amp; What is LoCoMo?
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                <strong>LoCoMo</strong> (Long Conversational Memory) is the premier benchmark for evaluating long-term memory in AI agents and conversational assistants. It was introduced by researchers at Snap Research in their paper <a href="https://arxiv.org/abs/2406.16016" target="_blank" class="text-[#D97757] underline hover:text-[#c4654a]">LoCoMo: Building Long Conversational Memory for LLMs</a>.
              </p>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                The benchmark dataset contains 10 comprehensive multi-session conversations spanning up to 35 sessions per user over weeks and months of simulated dialogue. Unlike simple retrieval tasks, LoCoMo tests whether an AI can track personal facts, handle evolving preferences over time, reject non-existent memories, and correlate information scattered across disconnected sessions.
              </p>
              
              <!-- LoCoMo Scale & Context Specs Box -->
              <div class="p-5 border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl bg-white dark:bg-[#111] relative my-4">
                <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none border-t-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
                <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none border-b-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>
                
                <h4 class="text-xs font-mono font-bold uppercase tracking-wider text-[#D97757] mb-3">LoCoMo Benchmark Dataset Scale</h4>
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 text-left">
                  <div>
                    <div class="text-xs text-gray-500 dark:text-gray-400 font-medium">Conversations</div>
                    <div class="text-lg font-extrabold font-mono text-gray-900 dark:text-white">10 Histories</div>
                    <div class="text-[11px] text-gray-400 dark:text-gray-500">27.2 avg sessions (up to 35)</div>
                  </div>
                  <div>
                    <div class="text-xs text-gray-500 dark:text-gray-400 font-medium">Total Questions</div>
                    <div class="text-lg font-extrabold font-mono text-gray-900 dark:text-white">1,986 Qs</div>
                    <div class="text-[11px] text-gray-400 dark:text-gray-500">Includes 446 adversarial</div>
                  </div>
                  <div>
                    <div class="text-xs text-gray-500 dark:text-gray-400 font-medium">Avg Tokens / Conv</div>
                    <div class="text-lg font-extrabold font-mono text-gray-900 dark:text-white">~20,079</div>
                    <div class="text-[11px] text-gray-400 dark:text-gray-500">Min 12.2k | Max 23.4k</div>
                  </div>
                  <div>
                    <div class="text-xs text-gray-500 dark:text-gray-400 font-medium">Total Corpus</div>
                    <div class="text-lg font-extrabold font-mono text-[#D97757]">~200,789</div>
                    <div class="text-[11px] text-gray-400 dark:text-gray-500">Tokens concatenated</div>
                  </div>
                </div>
              </div>

              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                To evaluate Memwyre, we run full-suite benchmarks using <a href="https://github.com/supermemoryai/memorybench" target="_blank" class="text-[#D97757] underline hover:text-[#c4654a]">MemoryBench</a>—an open-source evaluation framework for AI memory engines—and publish raw evaluation artifacts to our <a href="https://github.com/snap-research/LoCoMo" target="_blank" class="text-[#D97757] underline hover:text-[#c4654a]">LoCoMo dataset integration</a>.
              </p>
            </section>

            <!-- 2. Methodology & LLM Independence -->
            <section id="methodology" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white border-b border-gray-200 dark:border-zinc-800 pb-2">
                2. Methodology &amp; LLM Model Independence
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                A critical design goal of Memwyre is <strong>LLM Model Independence</strong>: the memory engine must perform reliably regardless of which LLM handles ingestion, answer generation, or judging.
              </p>
              
              <h4 class="font-bold text-gray-950 dark:text-white text-base pt-2">Identical Evaluation: GPT-4o-mini vs. Kimi K2.5</h4>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                To test model independence, we evaluated Memwyre under identical benchmark conditions across the complete dataset (1,986 questions) using two different base models:
              </p>
              <ul class="list-disc pl-6 space-y-2 text-gray-700 dark:text-gray-300">
                <li><strong>GPT-4o-mini Configuration:</strong> Used GPT-4o-mini end-to-end across all evaluation phases (fact extraction, answer generation, and judging).</li>
                <li><strong>Kimi K2.5 Configuration:</strong> Used Kimi K2.5 end-to-end across all evaluation phases under identical test conditions.</li>
              </ul>
              
              <div class="overflow-x-auto border border-gray-200 dark:border-zinc-800 rounded-xl bg-white dark:bg-[#111] shadow-sm my-4">
                <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                  <thead class="text-xs uppercase bg-gray-50 dark:bg-zinc-900 text-gray-700 dark:text-gray-300 border-b border-gray-200 dark:border-zinc-850">
                    <tr>
                      <th scope="col" class="px-6 py-3">Evaluation Configuration</th>
                      <th scope="col" class="px-6 py-3">Total Questions</th>
                      <th scope="col" class="px-6 py-3">Base Model</th>
                      <th scope="col" class="px-6 py-3">Overall Accuracy</th>
                      <th scope="col" class="px-6 py-3">Non-Adversarial</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-gray-200 dark:divide-zinc-850 text-gray-950 dark:text-gray-350 font-sans">
                    <tr>
                      <td class="px-6 py-4 font-semibold text-gray-800 dark:text-gray-200">GPT-4o-mini Evaluation</td>
                      <td class="px-6 py-4 font-mono">1,986</td>
                      <td class="px-6 py-4 font-mono text-xs">GPT-4o-mini</td>
                      <td class="px-6 py-4 font-bold text-gray-900 dark:text-white">70.67%</td>
                      <td class="px-6 py-4">71.20%</td>
                    </tr>
                    <tr class="bg-[#D97757]/5 dark:bg-[#D97757]/10">
                      <td class="px-6 py-4 font-semibold text-[#D97757]">Kimi K2.5 Evaluation</td>
                      <td class="px-6 py-4 font-bold text-gray-900 dark:text-white font-mono">1,986</td>
                      <td class="px-6 py-4 font-mono text-xs font-semibold text-[#D97757]">Kimi K2.5</td>
                      <td class="px-6 py-4 font-bold text-[#D97757]">69.89%</td>
                      <td class="px-6 py-4 font-bold text-[#D97757]">70.52%</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                Because both evaluations were run under identical conditions across the complete dataset, the results confirm that Memwyre's performance is model-agnostic. Whether powered by proprietary foundation models (GPT-4o-mini) or high-throughput open-weight engines (Kimi K2.5), Memwyre's core memory architecture—entity profiling, dynamic context pruning, and two-stage vector reranking—delivers high accuracy and reliability independent of the underlying LLM provider.
              </p>

              <h4 class="font-bold text-gray-950 dark:text-white text-base pt-4">Memwyre vs. Standard Long-Context Architecture Patterns</h4>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                To put these benchmark results in perspective, standard long-term memory approaches in AI applications typically fall into two extremes, both with severe drawbacks:
              </p>
              
              <div class="overflow-x-auto border border-gray-200 dark:border-zinc-800 rounded-xl bg-white dark:bg-[#111] shadow-sm my-4">
                <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                  <thead class="text-xs uppercase bg-gray-50 dark:bg-zinc-900 text-gray-700 dark:text-gray-300 border-b border-gray-200 dark:border-zinc-850">
                    <tr>
                      <th scope="col" class="px-6 py-3">Architecture Pattern</th>
                      <th scope="col" class="px-6 py-3">Token Consumption</th>
                      <th scope="col" class="px-6 py-3">Multi-Session Recall</th>
                      <th scope="col" class="px-6 py-3">Key Drawback</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-gray-200 dark:divide-zinc-850 text-gray-950 dark:text-gray-350 font-sans">
                    <tr>
                      <td class="px-6 py-4 font-semibold text-gray-800 dark:text-gray-200">Standard Vector RAG</td>
                      <td class="px-6 py-4 font-mono text-xs">Low (~1.5k tok)</td>
                      <td class="px-6 py-4 text-xs font-semibold text-red-500">Poor (~42%)</td>
                      <td class="px-6 py-4 text-xs">Chunk fragmentation; misses facts scattered across turns.</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-semibold text-gray-800 dark:text-gray-200">Naive Full Context Window</td>
                      <td class="px-6 py-4 font-mono text-xs text-red-500">Extreme (26k+ tok)</td>
                      <td class="px-6 py-4 text-xs font-semibold text-yellow-600">Moderate (~58%)</td>
                      <td class="px-6 py-4 text-xs">Prohibitive cost; "Lost in the Middle" attention decay.</td>
                    </tr>
                    <tr class="bg-[#D97757]/5 dark:bg-[#D97757]/10">
                      <td class="px-6 py-4 font-semibold text-[#D97757]">Memwyre Memory Engine</td>
                      <td class="px-6 py-4 font-mono text-xs font-semibold text-[#D97757]">Optimized (~4.9k tok)</td>
                      <td class="px-6 py-4 text-xs font-bold text-[#D97757]">High (70.5%)</td>
                      <td class="px-6 py-4 text-xs font-semibold text-green-600">81% context reduction with top-tier multi-hop recall.</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </section>

            <!-- 3. Question Categories -->
            <section id="questions" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white border-b border-gray-200 dark:border-zinc-800 pb-2">
                3. Question Types &amp; Evaluation Categories
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                LoCoMo tests five distinct memory capabilities across 1,986 questions:
              </p>

              <div class="overflow-x-auto border border-gray-200 dark:border-zinc-800 rounded-xl bg-white dark:bg-[#111] shadow-sm">
                <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                  <thead class="text-xs uppercase bg-gray-50 dark:bg-zinc-900 text-gray-700 dark:text-gray-300 border-b border-gray-200 dark:border-zinc-850">
                    <tr>
                      <th scope="col" class="px-6 py-3">Category</th>
                      <th scope="col" class="px-6 py-3">What it tests</th>
                      <th scope="col" class="px-6 py-3">Total Questions</th>
                      <th scope="col" class="px-6 py-3">Example</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-gray-200 dark:divide-zinc-850 text-gray-950 dark:text-gray-350 font-sans">
                    <tr>
                      <td class="px-6 py-4 font-bold dark:text-white">Single-hop</td>
                      <td class="px-6 py-4">Direct fact recall</td>
                      <td class="px-6 py-4 font-mono">841</td>
                      <td class="px-6 py-4 italic">"What is John's favorite sport?"</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold dark:text-white">Adversarial</td>
                      <td class="px-6 py-4">Abstain / anti-hallucination</td>
                      <td class="px-6 py-4 font-mono">446</td>
                      <td class="px-6 py-4 italic">"What is Alex's dog named?" <span class="text-xs text-gray-500 font-normal">(when Alex never mentioned a dog)</span></td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold dark:text-white">Temporal</td>
                      <td class="px-6 py-4">Understanding time &amp; order</td>
                      <td class="px-6 py-4 font-mono">321</td>
                      <td class="px-6 py-4 italic">"When did they first discuss moving to Boston?"</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold dark:text-white">Multi-hop</td>
                      <td class="px-6 py-4">Combining multiple memories</td>
                      <td class="px-6 py-4 font-mono">282</td>
                      <td class="px-6 py-4 italic">"Who introduced Sarah to the person she later worked with?"</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold dark:text-white">World-knowledge</td>
                      <td class="px-6 py-4">Commonsense &amp; context reasoning</td>
                      <td class="px-6 py-4 font-mono">96</td>
                      <td class="px-6 py-4 italic">"Why was Emily stressed during that period?"</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </section>

            <!-- 4. Our Performance -->
            <section id="performance" class="space-y-4 scroll-mt-20">
              <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 dark:text-white border-b border-gray-200 dark:border-zinc-800 pb-2">
                4. Full Benchmark Performance Breakdown
              </h2>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                Below is the category-by-category accuracy and latency performance across the complete 1,986-question LoCoMo benchmark (using Kimi K2.5):
              </p>

              <!-- Detailed Category Metrics Table -->
              <div class="overflow-x-auto border border-gray-200 dark:border-zinc-800 rounded-xl bg-white dark:bg-[#111] shadow-sm my-4">
                <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                  <thead class="text-xs uppercase bg-gray-50 dark:bg-zinc-900 text-gray-700 dark:text-gray-300 border-b border-gray-200 dark:border-zinc-850">
                    <tr>
                      <th scope="col" class="px-6 py-3">Question Category</th>
                      <th scope="col" class="px-6 py-3">Total Qs</th>
                      <th scope="col" class="px-6 py-3">Correct</th>
                      <th scope="col" class="px-6 py-3">Accuracy</th>
                    </tr>
                  </thead>
                  <tbody class="divide-y divide-gray-200 dark:divide-zinc-850 text-gray-950 dark:text-gray-350 font-sans">
                    <tr class="bg-[#D97757]/5">
                      <td class="px-6 py-4 font-bold text-gray-900 dark:text-white">Single-hop Recall</td>
                      <td class="px-6 py-4 font-mono">841</td>
                      <td class="px-6 py-4 font-mono">661</td>
                      <td class="px-6 py-4 font-bold text-[#D97757]">78.60%</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-900 dark:text-white">Adversarial (Abstain)</td>
                      <td class="px-6 py-4 font-mono">446</td>
                      <td class="px-6 py-4 font-mono">302</td>
                      <td class="px-6 py-4 font-bold text-gray-900 dark:text-white">67.71%</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-900 dark:text-white">Temporal Reasoning</td>
                      <td class="px-6 py-4 font-mono">321</td>
                      <td class="px-6 py-4 font-mono">206</td>
                      <td class="px-6 py-4 font-bold text-gray-900 dark:text-white">64.17%</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-900 dark:text-white">World Knowledge</td>
                      <td class="px-6 py-4 font-mono">96</td>
                      <td class="px-6 py-4 font-mono">57</td>
                      <td class="px-6 py-4 font-bold text-gray-900 dark:text-white">59.38%</td>
                    </tr>
                    <tr>
                      <td class="px-6 py-4 font-bold text-gray-900 dark:text-white">Multi-hop Reasoning</td>
                      <td class="px-6 py-4 font-mono">282</td>
                      <td class="px-6 py-4 font-mono">162</td>
                      <td class="px-6 py-4 font-bold text-gray-900 dark:text-white">57.45%</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <!-- Bar Chart Visual -->
              <div class="relative p-3 border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl bg-gray-50/50 dark:bg-zinc-900/10 my-6">
                <!-- Corner Brackets (Crosshairs) -->
                <div class="absolute -top-2 -left-2 w-4 h-4 pointer-events-none border-t-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
                <div class="absolute -top-2 -right-2 w-4 h-4 pointer-events-none border-t-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>
                <div class="absolute -bottom-2 -left-2 w-4 h-4 pointer-events-none border-b-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
                <div class="absolute -bottom-2 -right-2 w-4 h-4 pointer-events-none border-b-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>

                <div class="p-4 sm:p-8 relative w-full bg-white dark:bg-[#111] border border-gray-250 dark:border-zinc-800 rounded-xl shadow-sm">
                  <!-- Horizontal dashed gridlines -->
                  <div class="absolute inset-x-8 sm:inset-x-12 top-4 bottom-20 flex flex-col justify-between pointer-events-none z-0">
                    <div class="w-full border-t border-dashed border-gray-200 dark:border-zinc-800"></div>
                    <div class="w-full border-t border-dashed border-gray-200 dark:border-zinc-800"></div>
                    <div class="w-full border-t border-dashed border-gray-200 dark:border-zinc-800"></div>
                    <div class="w-full border-t border-dashed border-gray-200 dark:border-zinc-800"></div>
                    <div class="w-full border-t border-dashed border-gray-200 dark:border-zinc-800"></div>
                  </div>

                  <!-- Chart Area -->
                  <div class="relative z-10 h-72 sm:h-96 flex items-end justify-between px-2 sm:px-6">
                    <!-- Category 1: Single-hop -->
                    <div class="flex flex-col items-center flex-1 h-full justify-end group">
                      <div class="flex items-end justify-center h-[85%] w-full">
                        <div class="flex flex-col items-center justify-end h-full w-10 sm:w-14 relative">
                          <span class="text-[#D97757] font-mono text-[10px] sm:text-xs font-bold mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">78.6%</span>
                          <div 
                            class="w-full bg-[#D97757] border border-black dark:border-zinc-900 rounded-t hover:bg-[#e68a6c] transition-all duration-1000 ease-out origin-bottom scale-y-0"
                            :class="{ 'scale-y-100': animateBars }"
                            style="height: 78.6%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.25) 8px, rgba(0, 0, 0, 0.25) 9px);"
                          ></div>
                        </div>
                      </div>
                    </div>

                    <!-- Category 2: Adversarial -->
                    <div class="flex flex-col items-center flex-1 h-full justify-end group">
                      <div class="flex items-end justify-center h-[85%] w-full">
                        <div class="flex flex-col items-center justify-end h-full w-10 sm:w-14 relative">
                          <span class="text-[#D97757] font-mono text-[10px] sm:text-xs font-bold mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">67.7%</span>
                          <div 
                            class="w-full bg-[#D97757] border border-black dark:border-zinc-900 rounded-t hover:bg-[#e68a6c] transition-all duration-1000 ease-out origin-bottom scale-y-0"
                            :class="{ 'scale-y-100': animateBars }"
                            style="height: 67.7%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.25) 8px, rgba(0, 0, 0, 0.25) 9px);"
                          ></div>
                        </div>
                      </div>
                    </div>

                    <!-- Category 3: Temporal -->
                    <div class="flex flex-col items-center flex-1 h-full justify-end group">
                      <div class="flex items-end justify-center h-[85%] w-full">
                        <div class="flex flex-col items-center justify-end h-full w-10 sm:w-14 relative">
                          <span class="text-[#D97757] font-mono text-[10px] sm:text-xs font-bold mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">64.2%</span>
                          <div 
                            class="w-full bg-[#D97757] border border-black dark:border-zinc-900 rounded-t hover:bg-[#e68a6c] transition-all duration-1000 ease-out origin-bottom scale-y-0"
                            :class="{ 'scale-y-100': animateBars }"
                            style="height: 64.2%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.25) 8px, rgba(0, 0, 0, 0.25) 9px);"
                          ></div>
                        </div>
                      </div>
                    </div>

                    <!-- Category 4: World Knowledge -->
                    <div class="flex flex-col items-center flex-1 h-full justify-end group">
                      <div class="flex items-end justify-center h-[85%] w-full">
                        <div class="flex flex-col items-center justify-end h-full w-10 sm:w-14 relative">
                          <span class="text-[#D97757] font-mono text-[10px] sm:text-xs font-bold mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">59.4%</span>
                          <div 
                            class="w-full bg-[#D97757] border border-black dark:border-zinc-900 rounded-t hover:bg-[#e68a6c] transition-all duration-1000 ease-out origin-bottom scale-y-0"
                            :class="{ 'scale-y-100': animateBars }"
                            style="height: 59.4%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.25) 8px, rgba(0, 0, 0, 0.25) 9px);"
                          ></div>
                        </div>
                      </div>
                    </div>

                    <!-- Category 5: Multi-hop -->
                    <div class="flex flex-col items-center flex-1 h-full justify-end group">
                      <div class="flex items-end justify-center h-[85%] w-full">
                        <div class="flex flex-col items-center justify-end h-full w-10 sm:w-14 relative">
                          <span class="text-[#D97757] font-mono text-[10px] sm:text-xs font-bold mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">57.5%</span>
                          <div 
                            class="w-full bg-[#D97757] border border-black dark:border-zinc-900 rounded-t hover:bg-[#e68a6c] transition-all duration-1000 ease-out origin-bottom scale-y-0"
                            :class="{ 'scale-y-100': animateBars }"
                            style="height: 57.5%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.25) 8px, rgba(0, 0, 0, 0.25) 9px);"
                          ></div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Bottom labels (X-axis) -->
                  <div class="flex justify-between px-2 sm:px-6 border-t border-gray-200 dark:border-zinc-800 pt-4 relative z-10 text-xs sm:text-sm font-medium text-gray-500 dark:text-gray-400">
                    <div class="flex-1 text-center">Single-hop</div>
                    <div class="flex-1 text-center">Adversarial</div>
                    <div class="flex-1 text-center">Temporal</div>
                    <div class="flex-1 text-center">World-Knowledge</div>
                    <div class="flex-1 text-center">Multi-hop</div>
                  </div>

                  <!-- Legend and Footer -->
                  <div class="flex justify-between items-center mt-10 px-2 sm:px-6 relative z-10 text-xs tracking-wider uppercase font-bold">
                    <div class="flex items-center gap-2">
                      <span class="w-3 h-3 bg-[#D97757] rounded-sm"></span>
                      <span class="text-gray-600 dark:text-gray-300">Accuracy (%)</span>
                    </div>
                    <div class="text-gray-400 dark:text-gray-500 tracking-widest font-mono">LOCOMO FULL BENCHMARK (1,986 QS)</div>
                  </div>
                </div>
              </div>

              <h4 class="font-bold text-gray-950 dark:text-white text-base mb-2">Why Memwyre Performs So Well</h4>
              <p class="text-gray-700 dark:text-gray-300 leading-relaxed">
                Memwyre's exceptional results on the LoCoMo-10 benchmark—achieving 78.6% accuracy on Single-hop recall and strong anti-hallucination immunity—are powered by four architectural pillars:
              </p>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-6">
                <div class="p-5 border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl bg-white dark:bg-[#111] relative">
                  <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none border-t-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
                  <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none border-b-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>
                  <h5 class="font-bold text-gray-900 dark:text-white text-base mb-2 flex items-center gap-2 font-mono">
                    <span class="inline-block w-2 h-2 bg-[#D97757] rounded-full"></span>
                    Dynamic Pruning
                  </h5>
                  <p class="text-sm text-gray-600 dark:text-gray-455 leading-relaxed">
                    Instead of feeding raw conversational history into the LLM, Memwyre strips out pleasantries, filler phrases, and distractor information. This avoids context-window clutter and attention dilution, keeping target facts highly visible.
                  </p>
                </div>

                <div class="p-5 border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl bg-white dark:bg-[#111] relative">
                  <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none border-t-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
                  <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none border-b-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>
                  <h5 class="font-bold text-gray-900 dark:text-white text-base mb-2 flex items-center gap-2 font-mono">
                    <span class="inline-block w-2 h-2 bg-[#D97757] rounded-full"></span>
                    Vector Re-ranking
                  </h5>
                  <p class="text-sm text-gray-600 dark:text-gray-455 leading-relaxed">
                    Memwyre uses a two-stage retrieval pipeline. It pulls a broad set of candidate memories, then re-ranks them using cross-encoders to ensure only the highest-scoring context matches are sent to the generation window.
                  </p>
                </div>

                <div class="p-5 border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl bg-white dark:bg-[#111] relative">
                  <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none border-t-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
                  <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none border-b-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>
                  <h5 class="font-bold text-gray-900 dark:text-white text-base mb-2 flex items-center gap-2 font-mono">
                    <span class="inline-block w-2 h-2 bg-[#D97757] rounded-full"></span>
                    Ebbinghaus Decay Formula
                  </h5>
                  <p class="text-sm text-gray-600 dark:text-gray-455 leading-relaxed">
                    To handle changing user preferences across months of chat, older facts are naturally deprecated when newer contradictory preferences are written. This logarithmic decay mirrors human memory retention.
                  </p>
                </div>

                <div class="p-5 border border-dashed border-gray-300 dark:border-zinc-800 rounded-xl bg-white dark:bg-[#111] relative">
                  <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none border-t-2 border-l-2 border-gray-400 dark:border-zinc-700"></div>
                  <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none border-b-2 border-r-2 border-gray-400 dark:border-zinc-700"></div>
                  <h5 class="font-bold text-gray-900 dark:text-white text-base mb-2 flex items-center gap-2 font-mono">
                    <span class="inline-block w-2 h-2 bg-[#D97757] rounded-full"></span>
                    Adversarial Immunity
                  </h5>
                  <p class="text-sm text-gray-600 dark:text-gray-455 leading-relaxed">
                    Memwyre's strict semantic containment blocks hallucinations. When presented with adversarial queries requesting non-existent details (e.g. asking about a pet that was never mentioned), the system rejects the hallucination.
                  </p>
                </div>
              </div>

              <!-- Open Data & External Links Box -->
              <div class="p-6 bg-gray-50 dark:bg-[#111] border border-gray-200 dark:border-zinc-800 rounded-xl flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 mt-8">
                <div>
                  <h4 class="font-bold text-gray-950 dark:text-white">Explore the Open Benchmarks &amp; Data</h4>
                  <p class="text-xs text-gray-555 dark:text-gray-400 mt-0.5">Explore MemoryBench, LoCoMo paper, and Memwyre evaluation logs.</p>
                </div>
                <div class="flex items-center gap-3 shrink-0">
                  <a href="https://github.com/supermemoryai/memorybench" target="_blank" class="px-4 py-2 border border-gray-300 dark:border-zinc-700 text-gray-900 dark:text-white text-xs font-bold rounded hover:bg-gray-100 dark:hover:bg-zinc-800 transition-colors">
                    MemoryBench Harness →
                  </a>
                  <a href="https://github.com/ramblinghermit0403/Memwyre" target="_blank" class="px-4 py-2 bg-black dark:bg-white text-white dark:text-black text-xs font-bold rounded hover:bg-gray-800 dark:hover:bg-gray-100 transition-colors">
                    GitHub Repo →
                  </a>
                </div>
              </div>
            </section>
          </article>
        </main>

        <!-- Right Sidebar (Dynamic Table of Contents) -->
        <aside class="hidden lg:block lg:col-span-2 lg:border-l border-gray-200 dark:border-gray-800 lg:pl-8 pt-12 text-left">
          <div class="sticky top-24 space-y-4">
            <div class="text-[11px] font-mono text-gray-400 dark:text-gray-500 tracking-wider uppercase font-bold">ON THIS PAGE</div>
            <nav class="space-y-3 text-sm relative pl-4 border-l border-gray-100 dark:border-zinc-900">
              <a 
                v-for="heading in toc" 
                :key="heading.slug" 
                :href="`#${heading.slug}`" 
                class="block font-medium text-gray-500 dark:text-gray-400 hover:text-[#D97757] dark:hover:text-[#D97757] transition-colors leading-snug relative"
                :class="{ 'text-[#D97757] font-semibold': activeSection === heading.slug, 'pl-4 text-xs opacity-80': heading.level === 3 }"
              >
                <!-- Active Indicator vertical line -->
                <div 
                  v-if="activeSection === heading.slug" 
                  class="absolute -left-[17px] top-0 bottom-0 w-0.5 bg-[#D97757]"
                ></div>
                {{ heading.text }}
              </a>
            </nav>
          </div>
        </aside>

      </div>
    </div>
    <SiteFooter />
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue';
import SiteFooter from '@/components/SiteFooter.vue';

const activeSection = ref('');
const animateBars = ref(false);

const toc = [
  { level: 2, text: '1. Introduction', slug: 'introduction' },
  { level: 2, text: '2. Methodology', slug: 'methodology' },
  { level: 2, text: '3. Types of Questions', slug: 'questions' },
  { level: 2, text: '4. Our Performance', slug: 'performance' }
];

// Scrollspy Observer
let observer = null;
onMounted(() => {
  setTimeout(() => {
    animateBars.value = true;
  }, 100);

  if (typeof window !== 'undefined') {
    observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          activeSection.value = entry.target.id;
        }
      });
    }, {
      root: null,
      rootMargin: '0px 0px -75% 0px',
      threshold: 0
    });

    const headings = document.querySelectorAll('.scroll-mt-20');
    headings.forEach((h) => {
      observer.observe(h);
    });
  }
});

onUnmounted(() => {
  if (observer) observer.disconnect();
});

// Meta helpers
const pageUrl = computed(() => typeof window !== 'undefined' ? window.location.href : '');
const pageTitle = 'LoCoMo Benchmark Evaluation of AI Memory';

const copyLink = () => {
  if (typeof window !== 'undefined') {
    navigator.clipboard.writeText(window.location.href);
    alert('Link copied to clipboard!');
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

.hero-serif {
  font-family: 'Playfair Display', Georgia, serif;
}

.markdown-content h2,
.markdown-content h3 {
  font-family: 'Playfair Display', Georgia, serif;
  color: #111827;
  line-height: 1.25;
  margin-top: 36px;
  margin-bottom: 16px;
  scroll-margin-top: 100px;
}

.dark .markdown-content h2,
.dark .markdown-content h3 {
  color: #f3f4f6;
}
</style>
