<template>
  <div class="min-h-screen bg-white text-gray-900 font-sans relative overflow-x-hidden selection:bg-[#D97757] selection:text-white pt-16">
    <!-- Global Vertical Grid Lines -->
    <div class="hidden lg:block absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>
    <div class="hidden lg:block absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-200 pointer-events-none select-none z-30"></div>

    <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 relative z-10">
      
      <!-- Breadcrumb -->
      <div class="pt-6">
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div class="flex items-center gap-2">
            <router-link to="/research" class="flex items-center gap-2 text-gray-400 hover:text-gray-600 transition-colors">
              <img src="/logo.png" alt="Memwyre" class="h-4 w-auto dark:invert" />
              <span>/ RESEARCH / BENCHMARKS</span>
            </router-link>
          </div>
          <div>RELEASE: VERSION 2.0</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-200 pointer-events-none select-none mb-8"></div>
      </div>

      <!-- Hero Header -->
      <div class="space-y-6 max-w-4xl text-left">
        <h1 class="hero-serif text-4xl sm:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-900">
          LoCoMo Benchmark <br />
          <span class="italic font-medium text-gray-900">Evaluation of <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">AI Memory.</span></span>
        </h1>
        <p class="text-lg text-gray-500 leading-relaxed font-normal">
          LoCoMo-10 is a widely accepted standard for evaluating long-term memory performance in AI agents and conversational assistants. Below is the detailed analysis of Memwyre's retrieval capabilities on this benchmark.
        </p>
      </div>
 
      <!-- TL;DR -->
      <div class="relative p-6 bg-white border border-dashed border-gray-300 rounded shadow-sm text-left my-6">
        <!-- Corner Brackets -->
        <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
          <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
          <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
        </div>
        <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
          <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
          <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
        </div>
        <div class="space-y-2">
          <div class="text-[#D97757] font-mono text-xs uppercase font-bold tracking-wider">Quick Summary / TL;DR</div>
          <p class="text-sm text-gray-600 leading-relaxed font-normal">
            <strong>Answer:</strong> On the LoCoMo-10 long-term memory benchmark, Memwyre achieves a 73.5% overall accuracy (outperforming flat vector systems) while retrieving a mean token count of only 3,000 per request (versus 26,000 tokens of raw dialog). This is driven by dynamic context pruning, Ebbinghaus logarithmic decay, and two-stage cross-encoder vector re-ranking.
          </p>
        </div>
      </div>

      <!-- Metric Cards Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 my-10">
        <div class="relative p-6 bg-white border border-dashed border-gray-300 rounded shadow-sm text-left">
          <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
            <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
            <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="text-[#D97757] text-5xl font-extrabold font-mono tracking-tight">73.5%</div>
          <div class="mt-2">
            <div class="text-gray-900 font-bold text-base">Overall Accuracy</div>
            <div class="text-gray-500 text-xs tracking-wider uppercase font-semibold mt-0.5">Benchmark Score</div>
          </div>
        </div>

        <div class="relative p-6 bg-white border border-dashed border-gray-300 rounded shadow-sm text-left">
          <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
            <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
            <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="text-gray-900 text-5xl font-extrabold font-mono tracking-tight">3,000</div>
          <div class="mt-2">
            <div class="text-gray-900 font-bold text-base">Mean Tokens</div>
            <div class="text-gray-500 text-xs tracking-wider uppercase font-semibold mt-0.5">Average Context Size</div>
          </div>
        </div>

        <div class="relative p-6 bg-white border border-dashed border-gray-300 rounded shadow-sm text-left">
          <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
            <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
            <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="text-gray-900 text-5xl font-extrabold font-mono tracking-tight">26k</div>
          <div class="mt-2">
            <div class="text-gray-900 font-bold text-base">Tokens Per Dialog</div>
            <div class="text-gray-500 text-xs tracking-wider uppercase font-semibold mt-0.5">Up to 32 sessions</div>
          </div>
        </div>
      </div>

      <!-- Main Columns Layout -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 pb-24 text-left">
        
        <!-- Left Side: Report Sections Navigation -->
        <aside class="hidden lg:block lg:col-span-3 sticky top-24 self-start">
          <div class="border border-dashed border-gray-300 rounded p-6 bg-white shadow-sm relative">
            <!-- Corner Brackets -->
            <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
              <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
              <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
            </div>
            <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
              <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
              <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
            </div>

            <h4 class="text-xs uppercase tracking-wider font-mono font-bold text-gray-400 mb-4">Report Sections</h4>
            <nav class="space-y-3 font-sans text-sm">
              <a href="#introduction" class="block font-medium text-gray-600 hover:text-[#D97757] transition-colors">1. Introduction</a>
              <a href="#methodology" class="block font-medium text-gray-600 hover:text-[#D97757] transition-colors">2. Methodology</a>
              <a href="#questions" class="block font-medium text-gray-600 hover:text-[#D97757] transition-colors">3. Types of Questions</a>
              <a href="#performance" class="block font-medium text-gray-600 hover:text-[#D97757] transition-colors">4. Our Performance</a>
            </nav>
          </div>
        </aside>

        <!-- Right Side: The Report Content -->
        <div class="lg:col-span-9 space-y-12">
          
          <!-- 1. Introduction -->
          <section id="introduction" class="space-y-4 scroll-mt-20">
            <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 font-bold border-b border-gray-200 pb-2">
              1. Introduction
            </h2>
            <p class="text-gray-700 leading-relaxed">
              LoCoMo-10 stands for Long Conversational Memory – 10 conversations. It is one of the most widely used benchmarks for evaluating long-term memory systems for AI agents and conversational assistants. It was introduced by researchers at Snap Research in their LoCoMo paper.
            </p>
            <p class="text-gray-700 leading-relaxed">
              The "10" simply refers to the 10 long conversations contained in the original dataset file (<code class="bg-gray-100 px-1.5 py-0.5 rounded font-mono text-sm">locomo10.json</code>). Nearly all papers referring to "LoCoMo-10" are using these same ten conversations for evaluation.
            </p>
            <p class="text-gray-700 leading-relaxed">
              For memory systems like Memwyre, LoCoMo-10 is currently one of the best benchmarks because it closely resembles a real personal memory system: conversations happen over long periods, facts evolve over time, and users expect the AI to remember everything consistently.
            </p>
          </section>

          <!-- 2. Methodology -->
          <section id="methodology" class="space-y-4 scroll-mt-20">
            <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 font-bold border-b border-gray-200 pb-2">
              2. Methodology
            </h2>
            <p class="text-gray-700 leading-relaxed">
              The benchmark evaluates memory retrieval capabilities across a rich conversational dataset structure.
            </p>
            
            <h4 class="font-bold text-gray-950 text-base">Dataset Structure</h4>
            <p class="text-gray-700 leading-relaxed">
              LoCoMo-10 contains:
            </p>
            <ul class="list-disc pl-6 space-y-1.5 text-gray-700">
              <li>10 very long multi-session conversations.</li>
              <li>Conversations span weeks to months of simulated interactions.</li>
              <li>Around 16k–26k tokens per conversation.</li>
              <li>Up to 32 sessions per conversation.</li>
              <li>Exactly 1,540 questions.</li>
            </ul>
            <p class="text-gray-700 leading-relaxed">
              Each conversation is embedded with: personal facts, user preferences, events, temporal details, relationships between events, distractor information, and adversarial questions.
            </p>

            <h4 class="font-bold text-gray-950 text-base pt-2">Why LoCoMo is Difficult</h4>
            <p class="text-gray-700 leading-relaxed">
              Traditional retrieval architectures often fail on LoCoMo-10 because:
            </p>
            <ul class="list-disc pl-6 space-y-2 text-gray-700">
              <li>Relevant memories may be hundreds of turns apart in the dialogue context.</li>
              <li>Questions require reasoning and correlation across multiple disconnected chat sessions.</li>
              <li>Temporal relationships matter; values and events change chronologically.</li>
              <li>Adversarial questions actively target non-existent memories to punish hallucinations.</li>
              <li>Full-context feeding approaches become prohibitively expensive at this scale.</li>
            </ul>

            <h4 class="font-bold text-gray-950 text-base pt-2">Metrics Commonly Reported</h4>
            <p class="text-gray-700 leading-relaxed">
              Most memory systems report Accuracy, F1 Score, Hit@10, MRR (Mean Reciprocal Rank), and Category-wise scores (SH, MH, TR, OD, ADV). For retrieval systems like Memwyre, the crucial retrieval performance metrics are:
            </p>
            <ul class="list-disc pl-6 space-y-2 text-gray-700">
              <li><strong>Hit@10:</strong> Was the correct memory included in the top 10 retrieved context items?</li>
              <li><strong>MRR:</strong> How high did the correct target memory rank in the retrieval output?</li>
            </ul>
          </section>

          <!-- 3. Types of Questions -->
          <section id="questions" class="space-y-4 scroll-mt-20">
            <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 font-bold border-b border-gray-200 pb-2">
              3. Types of Questions
            </h2>
            <p class="text-gray-700 leading-relaxed">
              The benchmark evaluates five core memory abilities through specific types of questions:
            </p>

            <div class="overflow-x-auto border border-gray-200 rounded bg-white shadow-sm">
              <table class="w-full text-sm text-left text-gray-500">
                <thead class="text-xs uppercase bg-gray-50 text-gray-700 border-b border-gray-200">
                  <tr>
                    <th scope="col" class="px-6 py-3">Category</th>
                    <th scope="col" class="px-6 py-3">What it tests</th>
                    <th scope="col" class="px-6 py-3">Example</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-gray-200 text-gray-950">
                  <tr>
                    <td class="px-6 py-4 font-bold">Single-hop</td>
                    <td class="px-6 py-4 text-gray-600">Direct fact recall</td>
                    <td class="px-6 py-4 italic">"What is John's favorite sport?"</td>
                  </tr>
                  <tr>
                    <td class="px-6 py-4 font-bold">Multi-hop</td>
                    <td class="px-6 py-4 text-gray-600">Combining multiple memories</td>
                    <td class="px-6 py-4 italic">"Who introduced Sarah to the person she later worked with?"</td>
                  </tr>
                  <tr>
                    <td class="px-6 py-4 font-bold">Temporal</td>
                    <td class="px-6 py-4 text-gray-600">Understanding time and order</td>
                    <td class="px-6 py-4 italic">"When did they first discuss moving to Boston?"</td>
                  </tr>
                  <tr>
                    <td class="px-6 py-4 font-bold">Open-domain</td>
                    <td class="px-6 py-4 text-gray-600">General reasoning with context</td>
                    <td class="px-6 py-4 italic">"Why was Emily stressed during that period?"</td>
                  </tr>
                  <tr>
                    <td class="px-6 py-4 font-bold">Adversarial</td>
                    <td class="px-6 py-4 text-gray-600">Avoiding hallucinations</td>
                    <td class="px-6 py-4 italic">"What is Alex's dog named?" <span class="text-xs text-gray-500 font-normal">(when Alex never mentioned a dog)</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </section>

          <!-- 4. Our Performance -->
          <section id="performance" class="space-y-4 scroll-mt-20">
            <h2 class="hero-serif text-2xl sm:text-3xl tracking-tight text-gray-900 font-bold border-b border-gray-200 pb-2">
              4. Our Performance
            </h2>
            <p class="text-gray-700 leading-relaxed">
              The chart below illustrates Memwyre's performance on the four primary evaluation categories:
            </p>

            <div class="relative p-3 border border-dashed border-gray-300 rounded bg-gray-50/50 my-6">
              <!-- Corner Brackets (Crosshairs) -->
              <div class="absolute -top-2 -left-2 w-4 h-4 pointer-events-none">
                <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -top-2 -right-2 w-4 h-4 pointer-events-none">
                <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -bottom-2 -left-2 w-4 h-4 pointer-events-none">
                <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
              </div>
              <div class="absolute -bottom-2 -right-2 w-4 h-4 pointer-events-none">
                <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
                <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
              </div>

              <div class="p-4 sm:p-8 relative w-full bg-white border border-gray-250 rounded shadow-sm">
                <!-- Horizontal dashed gridlines -->
                <div class="absolute inset-x-8 sm:inset-x-12 top-4 bottom-20 flex flex-col justify-between pointer-events-none z-0">
                  <div class="w-full border-t border-dashed border-gray-200"></div>
                  <div class="w-full border-t border-dashed border-gray-200"></div>
                  <div class="w-full border-t border-dashed border-gray-200"></div>
                  <div class="w-full border-t border-dashed border-gray-200"></div>
                  <div class="w-full border-t border-dashed border-gray-200"></div>
                </div>

                <!-- Chart Area -->
                <div class="relative z-10 h-72 sm:h-96 flex items-end justify-between px-2 sm:px-6">
                  <!-- Category 1: Single-hop -->
                  <div class="flex flex-col items-center flex-1 h-full justify-end group">
                    <div class="flex items-end justify-center gap-1.5 sm:gap-4 h-[85%] w-full">
                      <!-- Old Bar -->
                      <div class="flex flex-col items-center justify-end h-full w-7 sm:w-12 relative">
                        <span class="text-gray-500 font-mono text-[10px] sm:text-xs mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">53.0</span>
                        <div 
                          class="w-full bg-zinc-300 border border-black rounded-t hover:bg-zinc-400 transition-all duration-1000 ease-out origin-bottom scale-y-0"
                          :class="{ 'scale-y-100': animateBars }"
                          style="height: 53.0%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.2) 8px, rgba(0, 0, 0, 0.2) 9px);"
                        ></div>
                      </div>
                      <!-- New Bar -->
                      <div class="flex flex-col items-center justify-end h-full w-7 sm:w-12 relative">
                        <span class="text-[#D97757] font-mono text-[10px] sm:text-xs font-bold mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">80.0</span>
                        <div 
                          class="w-full bg-[#D97757] border border-black rounded-t hover:bg-[#e68a6c] hover:shadow-[0_0_15px_rgba(217,119,87,0.15)] transition-all duration-1000 ease-out origin-bottom scale-y-0"
                          :class="{ 'scale-y-100': animateBars }"
                          style="height: 80.0%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.25) 8px, rgba(0, 0, 0, 0.25) 9px);"
                        ></div>
                      </div>
                    </div>
                  </div>

                  <!-- Category 2: Multi-hop -->
                  <div class="flex flex-col items-center flex-1 h-full justify-end group">
                    <div class="flex items-end justify-center gap-1.5 sm:gap-4 h-[85%] w-full">
                      <!-- Old Bar -->
                      <div class="flex flex-col items-center justify-end h-full w-7 sm:w-12 relative">
                        <span class="text-gray-500 font-mono text-[10px] sm:text-xs mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">24.0</span>
                        <div 
                          class="w-full bg-zinc-300 border border-black rounded-t hover:bg-zinc-400 transition-all duration-1000 ease-out origin-bottom scale-y-0"
                          :class="{ 'scale-y-100': animateBars }"
                          style="height: 24.0%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.2) 8px, rgba(0, 0, 0, 0.2) 9px);"
                        ></div>
                      </div>
                      <!-- New Bar -->
                      <div class="flex flex-col items-center justify-end h-full w-7 sm:w-12 relative">
                        <span class="text-[#D97757] font-mono text-[10px] sm:text-xs font-bold mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">45.0</span>
                        <div 
                          class="w-full bg-[#D97757] border border-black rounded-t hover:bg-[#e68a6c] hover:shadow-[0_0_15px_rgba(217,119,87,0.15)] transition-all duration-1000 ease-out origin-bottom scale-y-0"
                          :class="{ 'scale-y-100': animateBars }"
                          style="height: 45.0%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.25) 8px, rgba(0, 0, 0, 0.25) 9px);"
                        ></div>
                      </div>
                    </div>
                  </div>

                  <!-- Category 3: Open-domain -->
                  <div class="flex flex-col items-center flex-1 h-full justify-end group">
                    <div class="flex items-end justify-center gap-1.5 sm:gap-4 h-[85%] w-full">
                      <!-- Old Bar -->
                      <div class="flex flex-col items-center justify-end h-full w-7 sm:w-12 relative">
                        <span class="text-gray-500 font-mono text-[10px] sm:text-xs mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">50.0</span>
                        <div 
                          class="w-full bg-zinc-300 border border-black rounded-t hover:bg-zinc-400 transition-all duration-1000 ease-out origin-bottom scale-y-0"
                          :class="{ 'scale-y-100': animateBars }"
                          style="height: 50.0%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.2) 8px, rgba(0, 0, 0, 0.2) 9px);"
                        ></div>
                      </div>
                      <!-- New Bar -->
                      <div class="flex flex-col items-center justify-end h-full w-7 sm:w-12 relative">
                        <span class="text-[#D97757] font-mono text-[10px] sm:text-xs font-bold mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">76.0</span>
                        <div 
                          class="w-full bg-[#D97757] border border-black rounded-t hover:bg-[#e68a6c] hover:shadow-[0_0_15px_rgba(217,119,87,0.15)] transition-all duration-1000 ease-out origin-bottom scale-y-0"
                          :class="{ 'scale-y-100': animateBars }"
                          style="height: 76.0%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.25) 8px, rgba(0, 0, 0, 0.25) 9px);"
                        ></div>
                      </div>
                    </div>
                  </div>

                  <!-- Category 4: Temporal -->
                  <div class="flex flex-col items-center flex-1 h-full justify-end group">
                    <div class="flex items-end justify-center gap-1.5 sm:gap-4 h-[85%] w-full">
                      <!-- Old Bar -->
                      <div class="flex flex-col items-center justify-end h-full w-7 sm:w-12 relative">
                        <span class="text-gray-500 font-mono text-[10px] sm:text-xs mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">48.0</span>
                        <div 
                          class="w-full bg-zinc-300 border border-black rounded-t hover:bg-zinc-400 transition-all duration-1000 ease-out origin-bottom scale-y-0"
                          :class="{ 'scale-y-100': animateBars }"
                          style="height: 48.0%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.2) 8px, rgba(0, 0, 0, 0.2) 9px);"
                        ></div>
                      </div>
                      <!-- New Bar -->
                      <div class="flex flex-col items-center justify-end h-full w-7 sm:w-12 relative">
                        <span class="text-[#D97757] font-mono text-[10px] sm:text-xs font-bold mb-1 transition-all duration-500 delay-500 opacity-0" :class="{ 'opacity-100': animateBars }">74.0</span>
                        <div 
                          class="w-full bg-[#D97757] border border-black rounded-t hover:bg-[#e68a6c] hover:shadow-[0_0_15px_rgba(217,119,87,0.15)] transition-all duration-1000 ease-out origin-bottom scale-y-0"
                          :class="{ 'scale-y-100': animateBars }"
                          style="height: 74.0%; background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.25) 8px, rgba(0, 0, 0, 0.25) 9px);"
                        ></div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Bottom labels (X-axis) -->
                <div class="flex justify-between px-2 sm:px-6 border-t border-gray-200 pt-4 relative z-10 text-xs sm:text-sm font-medium text-gray-500">
                  <div class="flex-1 text-center">Single-hop</div>
                  <div class="flex-1 text-center">Multi-hop</div>
                  <div class="flex-1 text-center">Open-domain</div>
                  <div class="flex-1 text-center">Temporal</div>
                </div>

                <!-- Legend and Footer -->
                <div class="flex justify-between items-center mt-10 px-2 sm:px-6 relative z-10 text-xs tracking-wider uppercase font-bold">
                  <!-- Legend -->
                  <div class="flex items-center gap-6">
                    <div class="flex items-center gap-2">
                      <span class="w-3 h-3 bg-zinc-300 rounded-sm"></span>
                      <span class="text-gray-500">Old</span>
                    </div>
                    <div class="flex items-center gap-2">
                      <span class="w-3 h-3 bg-[#D97757] rounded-sm"></span>
                      <span class="text-gray-600">New</span>
                    </div>
                  </div>
                  <!-- Sublabel -->
                  <div class="text-gray-400 tracking-widest font-mono">LOCOMO</div>
                </div>

              </div>
            </div>

            <h4 class="font-bold text-gray-950 text-base mb-2">Why Memwyre Performs So Well</h4>
            <p class="text-gray-700 leading-relaxed">
              Memwyre's exceptional results on the LoCoMo-10 benchmark—such as achieving an 80% accuracy on Single-hop recall and a 74% score on Temporal alignment—are powered by a combination of targeted technological mechanisms:
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-6">
              <div class="p-5 border border-dashed border-gray-300 rounded bg-white relative">
                <!-- Corner Brackets -->
                <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
                  <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
                  <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
                </div>
                <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
                  <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
                  <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
                </div>
                <h5 class="font-bold text-gray-900 text-base mb-2 flex items-center gap-2 font-mono">
                  <span class="inline-block w-2 h-2 bg-[#D97757] rounded-full"></span>
                  Dynamic Pruning
                </h5>
                <p class="text-sm text-gray-600 leading-relaxed">
                  Instead of feeding raw conversational history into the LLM, Memwyre strips out pleasantries, filler phrases, and distractor information. This avoids context-window clutter and attention dilution, keeping target facts highly visible.
                </p>
              </div>

              <div class="p-5 border border-dashed border-gray-300 rounded bg-white relative">
                <!-- Corner Brackets -->
                <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
                  <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
                  <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
                </div>
                <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
                  <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
                  <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
                </div>
                <h5 class="font-bold text-gray-900 text-base mb-2 flex items-center gap-2 font-mono">
                  <span class="inline-block w-2 h-2 bg-[#D97757] rounded-full"></span>
                  Vector Re-ranking
                </h5>
                <p class="text-sm text-gray-600 leading-relaxed">
                  Memwyre uses a two-stage retrieval pipeline. It pulls a broad set of candidate memories (yielding a high Hit@10 rate), then re-ranks them using cross-encoders to ensure only the highest-scoring context matches are sent to the generation window.
                </p>
              </div>

              <div class="p-5 border border-dashed border-gray-300 rounded bg-white relative">
                <!-- Corner Brackets -->
                <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
                  <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
                  <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
                </div>
                <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
                  <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
                  <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
                </div>
                <h5 class="font-bold text-gray-900 text-base mb-2 flex items-center gap-2 font-mono">
                  <span class="inline-block w-2 h-2 bg-[#D97757] rounded-full"></span>
                  Ebbinghaus Decay Formula
                </h5>
                <p class="text-sm text-gray-600 leading-relaxed">
                  To handle changing user preferences across months of chat, older facts are naturally deprecated when newer contradictory preferences are written. This logarithmic decay mirrors human memory retention.
                </p>
              </div>

              <div class="p-5 border border-dashed border-gray-300 rounded bg-white relative">
                <!-- Corner Brackets -->
                <div class="absolute -top-1.5 -left-1.5 w-3 h-3 pointer-events-none">
                  <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
                  <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
                </div>
                <div class="absolute -bottom-1.5 -right-1.5 w-3 h-3 pointer-events-none">
                  <div class="absolute top-1.5 left-0 w-full h-px bg-gray-400"></div>
                  <div class="absolute left-1.5 top-0 h-full w-px bg-gray-400"></div>
                </div>
                <h5 class="font-bold text-gray-900 text-base mb-2 flex items-center gap-2 font-mono">
                  <span class="inline-block w-2 h-2 bg-[#D97757] rounded-full"></span>
                  Adversarial Immunity
                </h5>
                <p class="text-sm text-gray-600 leading-relaxed">
                  Memwyre's strict semantic containment blocks hallucinations. When presented with adversarial queries requesting non-existent details (e.g. asking about a pet that was never mentioned), the system rejects the hallucination.
                </p>
              </div>
            </div>

            <p class="text-gray-700 leading-relaxed mt-6">
              Our performance analysis indicates that retrieval recall remains extremely strong (especially on complex multi-hop correlations). The remaining delta is primarily a downstream bottleneck, which we are addressing through:
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-2">
              <div class="p-4 bg-gray-50 border border-gray-200 rounded">
                <h5 class="font-bold text-[#D97757] text-sm uppercase tracking-wider mb-2">Reranking Quality</h5>
                <p class="text-xs text-gray-600 leading-relaxed">Prioritizing the highest-scoring context items to match generation context bounds.</p>
              </div>
              <div class="p-4 bg-gray-50 border border-gray-200 rounded">
                <h5 class="font-bold text-[#D97757] text-sm uppercase tracking-wider mb-2">Evidence Selection</h5>
                <p class="text-xs text-gray-600 leading-relaxed">Extracting specific targets, filtering out ambient chat noise and distractors.</p>
              </div>
              <div class="p-4 bg-gray-50 border border-gray-200 rounded">
                <h5 class="font-bold text-[#D97757] text-sm uppercase tracking-wider mb-2">Answer Synthesis</h5>
                <p class="text-xs text-gray-600 leading-relaxed">Ensuring details from different sessions compile cleanly in the response.</p>
              </div>
            </div>

            <div class="p-6 bg-gray-50 border border-gray-200 rounded flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 mt-8">
              <div>
                <h4 class="font-bold text-gray-950">Interested in the raw benchmark datasets?</h4>
                <p class="text-xs text-gray-500 mt-0.5">Download our complete evaluation logs (JSON format).</p>
              </div>
              <a href="https://github.com/ramblinghermit0403/Memwyre/tree/main/.benchmarks" target="_blank" class="px-5 py-2 bg-black text-white text-xs font-bold rounded hover:bg-gray-800 transition-colors shrink-0">
                View GitHub Repository →
              </a>
            </div>
          </section>

        </div>

      </div>
    </div>
    <SiteFooter />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import SiteFooter from '@/components/SiteFooter.vue';

const animateBars = ref(false);

onMounted(() => {
  setTimeout(() => {
    animateBars.value = true;
  }, 100);
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

.hero-serif {
  font-family: 'Playfair Display', Georgia, serif;
}
</style>
