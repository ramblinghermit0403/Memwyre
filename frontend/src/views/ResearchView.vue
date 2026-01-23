<template>
  <div class="min-h-screen bg-black text-white p-8 pt-24 font-sans selection:bg-purple-500/30">
    <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="text-center mb-20">
            <h2 class="text-sm font-bold uppercase tracking-widest text-green-400 mb-4">Benchmarks</h2>
            <h1 class="text-4xl lg:text-5xl font-extrabold tracking-tight mb-6 bg-gradient-to-r from-white to-gray-400 bg-clip-text text-transparent">
                Production-Ready Performance
            </h1>
            <p class="text-xl text-gray-400 max-w-3xl mx-auto leading-relaxed">
                A scalable memory-centric algorithm that dynamically extracts and retrieves key conversational facts—delivering 
                <span class="text-white font-bold">24% higher accuracy</span> than standard RAG, with 
                <span class="text-white font-bold">75% lower latency</span>.
            </p>
        </div>

        <!-- Metrics Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-24">
            <div class="p-8 rounded-2xl bg-gray-900/40 border border-gray-800 text-center">
                <div class="text-4xl font-bold text-green-400 mb-2">+24%</div>
                <div class="text-gray-400">Response Accuracy</div>
            </div>
            <div class="p-8 rounded-2xl bg-gray-900/40 border border-gray-800 text-center">
                <div class="text-4xl font-bold text-purple-400 mb-2">-75%</div>
                <div class="text-gray-400">P95 Retrieval Latency</div>
            </div>
            <div class="p-8 rounded-2xl bg-gray-900/40 border border-gray-800 text-center">
                <div class="text-4xl font-bold text-blue-400 mb-2">-90%</div>
                <div class="text-gray-400">Token Consumption</div>
            </div>
        </div>

        <!-- Charts Container -->
        <div class="space-y-24">
                <!-- Comparison -->
            <div class="space-y-8">
                <h3 class="text-2xl font-bold text-center">State-of-the-Art Accuracy</h3>
                <p class="text-gray-400 text-center max-w-2xl mx-auto">
                Comparing MemWyRE's graph-enhanced retrieval against standard OpenAI memory implementations on the LoCoMo benchmark.
                </p>
                <div class="max-w-3xl mx-auto h-64">
                    <ComparisonChart />
                </div>
            </div>

            <!-- Benchmark Detail -->
            <div class="space-y-8">
                <h3 class="text-2xl font-bold text-center">LoCoMo Benchmark Results</h3>
                <p class="text-gray-400 text-center max-w-4xl mx-auto">
                    MemWyRE balances accuracy and latency. While full-context models (like LangMem) achieve decent accuracy, their latency explodes. 
                    MemWyRE achieves top-tier accuracy (64.0%) while keeping P95 latency under 5 seconds.
                </p>
                <div class="max-w-5xl mx-auto h-96">
                        <BenchmarkChart />
                </div>
                
                <!-- Detailed Analysis -->
                <div class="max-w-4xl mx-auto mt-12 p-8 bg-gray-900/30 rounded-xl border border-gray-800">
                    <h3 class="text-xl font-bold mb-4 text-blue-400">Bot Performance Analysis</h3>
                    <p class="text-gray-300 leading-relaxed space-y-4 text-left">
                        <span class="block mb-4">
                            The latest <strong>LoCoMo benchmark</strong> run reveals a critical advantage in architectural efficiency. 
                            MemWyRE achieves a competitive <strong>64.00% accuracy score</strong>, statistically tying with high-overhead systems like Zep (66.0%) and outperforming standard RAG implementations (61.0%).
                        </span>
                        <span class="block">
                            However, the true differentiator lies in latency. While graph-based competitors struggle with tail latencies exceeding 25 seconds, 
                            MemWyRE delivers a <strong>P95 search latency of just 4.34 seconds</strong>. This represents a 
                            <strong>6x speedup vs Zep</strong> and an <strong>18x speedup vs LangMem</strong>, proving that deep semantic recall doesn't require sacrificing real-time user experience.
                        </span>
                    </p>
                </div>
            </div>

                <!-- Architecture Section -->
            <div class="mt-24">
                <h2 class="text-3xl font-bold text-center mb-12">Under The Hood</h2>
                <div class="relative p-1 bg-gradient-to-r from-gray-800 to-gray-900 rounded-2xl overflow-hidden border border-gray-800 max-w-5xl mx-auto">
                    <div class="bg-black/90 p-10 rounded-xl relative overflow-hidden">
                        <div class="flex flex-col md:flex-row items-center justify-center gap-12">
                            <div class="w-64 p-6 bg-blue-900/20 border border-blue-500/30 rounded-lg text-center">
                                <div class="text-sm text-blue-400 mb-2 font-mono">PHASE 1</div>
                                <h3 class="font-bold text-lg mb-2">Ingestion & Extraction</h3>
                                <p class="text-sm text-gray-400">LLM processes raw text to extract <span class="text-white">Facts</span> and <span class="text-white">Entities</span>.</p>
                            </div>
                            
                            <div class="hidden md:block text-gray-600">➜</div>

                            <div class="w-64 p-6 bg-purple-900/20 border border-purple-500/30 rounded-lg text-center">
                                <div class="text-sm text-purple-400 mb-2 font-mono">PHASE 2</div>
                                <h3 class="font-bold text-lg mb-2">Graph Resolution</h3>
                                <p class="text-sm text-gray-400">Deduplication and conflict resolution to update the <span class="text-white">Knowledge Graph</span>.</p>
                            </div>

                            <div class="hidden md:block text-gray-600">➜</div>

                            <div class="w-64 p-6 bg-green-900/20 border border-green-500/30 rounded-lg text-center">
                                <div class="text-sm text-green-400 mb-2 font-mono">PHASE 3</div>
                                <h3 class="font-bold text-lg mb-2">Unified Retrieval</h3>
                                <p class="text-sm text-gray-400">Parallel Vector + SQL search for <span class="text-white">Facts + Chunks</span>.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script setup>
import ComparisonChart from '../components/ComparisonChart.vue'
import BenchmarkChart from '../components/BenchmarkChart.vue'
</script>
