<template>
  <div class="h-screen flex flex-col transition-colors duration-300 font-sans overflow-hidden bg-gray-50 dark:bg-[#121212]">
    <NavBar />
    
    <main class="flex-1 overflow-hidden w-full max-w-5xl mx-auto py-8 px-4 sm:px-6 lg:px-8 flex flex-col h-full">
      <div class="flex-none mb-6">
          <h1 class="text-3xl font-bold text-gray-900 dark:text-text-primary">Retrieval Pipeline Visualizer</h1>
          <p class="text-gray-500 dark:text-gray-400 mt-2">Debug and visualize the internal steps of the vector retrieval and reranking process.</p>
      </div>

      <div class="flex-none bg-white dark:bg-surface shadow rounded-lg p-6 border border-gray-200 dark:border-border mb-6">
        <form @submit.prevent="runSearch" class="flex gap-4 items-end">
          <div class="flex-1">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Search Query</label>
            <input 
              type="text" 
              v-model="searchQuery" 
              placeholder="Enter a test query..." 
              class="w-full bg-gray-50 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md py-2 px-3 text-gray-900 dark:text-white focus:ring-[#D97757] focus:border-[#D97757]"
              required
            >
          </div>
          <div class="w-24">
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Top K</label>
            <input 
              type="number" 
              v-model="topK" 
              min="1" 
              max="20"
              class="w-full bg-gray-50 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md py-2 px-3 text-gray-900 dark:text-white focus:ring-[#D97757] focus:border-[#D97757]"
            >
          </div>
          <button 
            type="submit" 
            :disabled="loading"
            class="px-6 py-2 bg-[#D97757] hover:bg-[#C4654A] text-white rounded-md font-medium transition-colors disabled:opacity-70 flex items-center justify-center min-w-[120px]"
          >
            <span v-if="loading" class="animate-spin h-5 w-5 border-2 border-white border-t-transparent rounded-full"></span>
            <span v-else>Run Pipeline</span>
          </button>
          <button 
            type="button" 
            v-if="debugData"
            @click="exportDebugData"
            class="px-4 py-2 bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 text-gray-800 dark:text-gray-200 rounded-md font-medium transition-colors flex items-center justify-center whitespace-nowrap gap-2"
            title="Download JSON for debugging"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
            Export
          </button>
        </form>
      </div>

      <!-- Scrollable Content Area -->
      <div class="flex-1 overflow-y-auto min-h-0 custom-scrollbar pr-2 pb-10 space-y-8" v-if="debugData">
          
          <!-- Step 1: Pinecone Fetch -->
          <div class="bg-white dark:bg-surface shadow rounded-lg p-6 border border-gray-200 dark:border-border">
            <h2 class="text-xl font-semibold text-gray-900 dark:text-white mb-4 flex items-center gap-2">
              <span class="bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200 py-1 px-3 rounded-full text-sm">Step 1</span>
              Raw Vector Store Fetch
            </h2>
            <div class="flex items-center gap-6 mb-4" v-if="debugData.unified_search">
                <div class="text-center">
                    <p class="text-2xl font-bold text-gray-900 dark:text-white">{{ debugData.unified_search.fetch_k }}</p>
                    <p class="text-xs text-gray-500">Requested Items (Top K * 10)</p>
                </div>
                <div class="text-gray-300 dark:text-gray-600">→</div>
                <div class="text-center">
                    <p class="text-2xl font-bold text-blue-600 dark:text-blue-400">{{ debugData.unified_search.facts_fetched + debugData.unified_search.memories_fetched }}</p>
                    <p class="text-xs text-gray-500">Total Chunks Fetched</p>
                </div>
            </div>

            <!-- Expandable Unified Table for Step 1 -->
            <div class="mt-6" v-if="debugData.unified_search?.raw_facts?.length || debugData.unified_search?.raw_memories?.length">
                <details class="group bg-gray-50 dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700">
                  <summary class="flex items-center justify-between cursor-pointer px-4 py-3 font-medium text-gray-900 dark:text-white">
                    <span>View Raw Data Items ({{ (debugData.unified_search.raw_facts?.length || 0) + (debugData.unified_search.raw_memories?.length || 0) }})</span>
                    <svg class="w-5 h-5 transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                  </summary>
                  <div class="px-4 pb-4 overflow-x-auto max-h-96 overflow-y-auto custom-scrollbar">
                    <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700 mt-2">
                      <thead class="bg-gray-50 dark:bg-gray-800">
                        <tr>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-24">Type</th>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-32">ID</th>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Content Snippet</th>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-32">Vector Score</th>
                        </tr>
                      </thead>
                      <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
                        <tr v-for="item in debugData.unified_search.raw_facts" :key="'f'+item.id" class="hover:bg-gray-50 dark:hover:bg-gray-800/50">
                          <td class="px-4 py-3 text-xs">
                              <span class="bg-indigo-100 text-indigo-800 dark:bg-indigo-900 dark:text-indigo-200 px-2 py-1 rounded-full uppercase font-bold">Fact</span>
                          </td>
                          <td class="px-4 py-3 text-sm text-gray-900 dark:text-gray-300 font-mono">{{ item.id }}</td>
                          <td class="px-4 py-3 text-sm text-gray-900 dark:text-gray-300"><div class="line-clamp-2 max-w-md" :title="item.text">{{ item.text }}</div></td>
                          <td class="px-4 py-3 text-sm font-bold text-indigo-600 dark:text-indigo-400">{{ Number(item.score).toFixed(4) }}</td>
                        </tr>
                        <tr v-for="item in debugData.unified_search.raw_memories" :key="'m'+item.id" class="hover:bg-gray-50 dark:hover:bg-gray-800/50">
                          <td class="px-4 py-3 text-xs">
                              <span class="bg-teal-100 text-teal-800 dark:bg-teal-900 dark:text-teal-200 px-2 py-1 rounded-full uppercase font-bold">Memory</span>
                          </td>
                          <td class="px-4 py-3 text-sm text-gray-900 dark:text-gray-300 font-mono">{{ item.id }}</td>
                          <td class="px-4 py-3 text-sm text-gray-900 dark:text-gray-300"><div class="line-clamp-2 max-w-md" :title="item.text">{{ item.text }}</div></td>
                          <td class="px-4 py-3 text-sm font-bold text-teal-600 dark:text-teal-400">{{ Number(item.score).toFixed(4) }}</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </details>
            </div>
          </div>

          <!-- Step 2: Fact Hydration -->
          <div class="bg-white dark:bg-surface shadow rounded-lg p-6 border border-gray-200 dark:border-border">
            <h2 class="text-xl font-semibold text-gray-900 dark:text-white mb-4 flex items-center gap-2">
              <span class="bg-indigo-100 text-indigo-800 dark:bg-indigo-900 dark:text-indigo-200 py-1 px-3 rounded-full text-sm">Step 2</span>
              Fact Store & Recency Ranking
            </h2>
            
            <div class="flex items-center gap-6 mb-4" v-if="debugData.state_search">
                <div class="text-center">
                    <p class="text-2xl font-bold text-gray-900 dark:text-white">{{ (debugData.state_search.selected?.length || 0) + (debugData.state_search.dropped?.length || 0) }}</p>
                    <p class="text-xs text-gray-500">Total Facts Evaluated</p>
                </div>
                <div class="text-gray-300 dark:text-gray-600">→</div>
                <div class="text-center">
                    <p class="text-2xl font-bold text-indigo-600 dark:text-indigo-400">{{ debugData.state_search.selected?.length || 0 }}</p>
                    <p class="text-xs text-gray-500">Passed Fact Gating</p>
                </div>
            </div>

            <!-- Expandable Unified Table for Step 2 -->
            <div class="mt-6" v-if="debugData.state_search">
                <details class="group bg-gray-50 dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700">
                  <summary class="flex items-center justify-between cursor-pointer px-4 py-3 font-medium text-gray-900 dark:text-white">
                    <span>View Raw Data Items ({{ (debugData.state_search?.selected?.length || 0) + (debugData.state_search?.dropped?.length || 0) }})</span>
                    <svg class="w-5 h-5 transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                  </summary>
                  <div class="px-4 pb-4 overflow-x-auto max-h-96 overflow-y-auto custom-scrollbar">
                    <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700 mt-2">
                      <thead class="bg-gray-50 dark:bg-gray-800">
                        <tr>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Fact ID</th>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Content</th>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Base Confidence</th>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Final SQL Score</th>
                        </tr>
                      </thead>
                      <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
                        <tr v-for="fact in debugData.state_search?.selected" :key="'s'+fact.fact_id" class="hover:bg-gray-50 dark:hover:bg-gray-800/50">
                          <td class="px-4 py-3 text-sm text-gray-900 dark:text-gray-300 font-mono">{{ fact.fact_id }}</td>
                          <td class="px-4 py-3 text-sm text-gray-900 dark:text-gray-300"><div class="line-clamp-2 max-w-md" :title="fact.text">{{ fact.text }}</div></td>
                          <td class="px-4 py-3 text-sm text-gray-500 dark:text-gray-400">{{ Number(fact.confidence).toFixed(2) }}</td>
                          <td class="px-4 py-3 text-sm font-bold text-indigo-600 dark:text-indigo-400">{{ Number(fact.score).toFixed(2) }}</td>
                        </tr>
                        <tr v-for="fact in debugData.state_search?.dropped" :key="'d'+fact.fact_id" class="bg-red-50/50 dark:bg-red-900/10 opacity-80">
                          <td class="px-4 py-3 text-sm text-gray-900 dark:text-gray-300 font-mono line-through decoration-red-400">{{ fact.fact_id }}</td>
                          <td class="px-4 py-3 text-sm text-gray-900 dark:text-gray-300"><div class="line-clamp-2 max-w-md" :title="fact.text">{{ fact.text }}</div></td>
                          <td colspan="2" class="px-4 py-3 text-xs font-bold text-red-600 dark:text-red-400">Dropped: {{ fact.reason }}</td>
                        </tr>
                        <tr v-if="!debugData.state_search?.selected?.length && !debugData.state_search?.dropped?.length">
                          <td colspan="4" class="px-4 py-4 text-center text-sm text-gray-500">No facts passed semantic hard-gating.</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </details>
            </div>
          </div>

          <!-- Step 3: Memory MMR -->
          <div class="bg-white dark:bg-surface shadow rounded-lg p-6 border border-gray-200 dark:border-border">
            <h2 class="text-xl font-semibold text-gray-900 dark:text-white mb-4 flex items-center gap-2">
              <span class="bg-teal-100 text-teal-800 dark:bg-teal-900 dark:text-teal-200 py-1 px-3 rounded-full text-sm">Step 3</span>
              Memory Store & MMR Filtering
            </h2>
            <div class="flex items-center gap-6 mb-4" v-if="debugData.semantic_search">
                <div class="text-center">
                    <p class="text-2xl font-bold text-gray-900 dark:text-white">{{ debugData.semantic_search.candidates_considered }}</p>
                    <p class="text-xs text-gray-500">Total Memories Evaluated</p>
                </div>
                <div class="text-gray-300 dark:text-gray-600">→</div>
                <div class="text-center">
                    <p class="text-2xl font-bold text-teal-600 dark:text-teal-400">{{ debugData.semantic_search.items_selected }}</p>
                    <p class="text-xs text-gray-500">Survived MMR Selection</p>
                </div>
            </div>
            <!-- Expandable Unified Table for Step 3 -->
            <div class="mt-6" v-if="debugData.semantic_search">
                <details class="group bg-gray-50 dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700">
                  <summary class="flex items-center justify-between cursor-pointer px-4 py-3 font-medium text-gray-900 dark:text-white">
                    <span>View Raw Data Items ({{ (debugData.semantic_search.raw_selected?.length || 0) + (debugData.semantic_search.raw_dropped?.length || 0) }})</span>
                    <svg class="w-5 h-5 transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                  </summary>
                  <div class="px-4 pb-4 overflow-x-auto max-h-96 overflow-y-auto custom-scrollbar">
                    <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700 mt-2">
                      <thead class="bg-gray-50 dark:bg-gray-800">
                        <tr>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-32">Memory ID</th>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Content Snippet</th>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-32">Vector Score</th>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-32">Status</th>
                        </tr>
                      </thead>
                      <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
                        <!-- Selected -->
                        <tr v-for="item in debugData.semantic_search.raw_selected" :key="'s'+item.id" class="hover:bg-gray-50 dark:hover:bg-gray-800/50">
                          <td class="px-4 py-3 text-sm text-gray-900 dark:text-gray-300 font-mono">{{ item.id }}</td>
                          <td class="px-4 py-3 text-sm text-gray-900 dark:text-gray-300"><div class="line-clamp-2 max-w-md" :title="item.text">{{ item.text }}</div></td>
                          <td class="px-4 py-3 text-sm font-bold text-teal-600 dark:text-teal-400">{{ Number(item.score).toFixed(4) }}</td>
                          <td class="px-4 py-3 text-sm font-bold text-teal-600 dark:text-teal-400">Selected</td>
                        </tr>
                        <!-- Dropped -->
                        <tr v-for="item in debugData.semantic_search.raw_dropped" :key="'d'+item.id" class="bg-red-50/50 dark:bg-red-900/10 opacity-80">
                          <td class="px-4 py-3 text-sm text-gray-900 dark:text-gray-300 font-mono line-through decoration-red-400">{{ item.id }}</td>
                          <td class="px-4 py-3 text-sm text-gray-900 dark:text-gray-300"><div class="line-clamp-2 max-w-md" :title="item.text">{{ item.text }}</div></td>
                          <td class="px-4 py-3 text-sm text-gray-500 dark:text-gray-400">{{ Number(item.score).toFixed(4) }}</td>
                          <td class="px-4 py-3 text-xs font-bold text-red-600 dark:text-red-400">Dropped: {{ item.reason }}</td>
                        </tr>
                        <tr v-if="!debugData.semantic_search?.raw_selected?.length && !debugData.semantic_search?.raw_dropped?.length">
                          <td colspan="4" class="px-4 py-4 text-center text-sm text-gray-500">No memories evaluated.</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </details>
            </div>
          </div>

          <!-- Step 4: Reranking -->
          <div class="bg-white dark:bg-surface shadow rounded-lg p-6 border border-gray-200 dark:border-border">
            <h2 class="text-xl font-semibold text-gray-900 dark:text-white mb-4 flex items-center gap-2">
              <span class="bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-200 py-1 px-3 rounded-full text-sm">Step 4</span>
              Cross-Encoder Reranking
            </h2>

            <div class="flex items-center gap-6 mb-4" v-if="debugData.reranking">
                <div class="text-center">
                    <p class="text-2xl font-bold text-gray-900 dark:text-white">{{ debugData.reranking.length }}</p>
                    <p class="text-xs text-gray-500">Total Items Reranked</p>
                </div>
                <div class="text-gray-300 dark:text-gray-600">→</div>
                <div class="text-center">
                    <p class="text-2xl font-bold text-orange-600 dark:text-orange-400">{{ debugData.reranking.filter(i => !i.is_dropped).length }}</p>
                    <p class="text-xs text-gray-500">Final Top K Selected</p>
                </div>
            </div>
            <!-- Expandable Unified Table for Step 4 -->
            <div class="mt-6" v-if="debugData.reranking">
                <details class="group bg-gray-50 dark:bg-gray-800 rounded-lg border border-gray-200 dark:border-gray-700">
                  <summary class="flex items-center justify-between cursor-pointer px-4 py-3 font-medium text-gray-900 dark:text-white">
                    <span>View Raw Data Items ({{ debugData.reranking?.length || 0 }})</span>
                    <svg class="w-5 h-5 transition-transform group-open:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                  </summary>
                  <div class="px-4 pb-4 overflow-x-auto max-h-96 overflow-y-auto custom-scrollbar">
                    <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700 mt-2">
                      <thead class="bg-gray-50 dark:bg-gray-800">
                        <tr>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-16">Rank</th>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-24">Type</th>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Content Snippet</th>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-32">Original Score</th>
                          <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider w-32">Rerank Score</th>
                        </tr>
                      </thead>
                      <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
                        <tr v-for="(item, index) in debugData.reranking" :key="index" :class="[item.is_dropped ? 'bg-red-50/50 dark:bg-red-900/10 opacity-70' : 'hover:bg-gray-50 dark:hover:bg-gray-800/50']">
                          <td class="px-4 py-3 text-sm font-bold text-gray-900 dark:text-white">
                              <span v-if="!item.is_dropped">#{{ index + 1 }}</span>
                              <span v-else class="text-red-500">Dropped</span>
                          </td>
                          <td class="px-4 py-3 text-xs">
                              <span :class="item.type === 'fact' ? 'bg-indigo-100 text-indigo-800 dark:bg-indigo-900 dark:text-indigo-200' : 'bg-teal-100 text-teal-800 dark:bg-teal-900 dark:text-teal-200'" class="px-2 py-1 rounded-full uppercase font-bold">
                                  {{ item.type }}
                              </span>
                          </td>
                          <td class="px-4 py-3 text-sm text-gray-900 dark:text-gray-300" :class="{'line-through decoration-red-400': item.is_dropped}">{{ item.text }}</td>
                          <td class="px-4 py-3 text-sm text-gray-500 dark:text-gray-400 line-through decoration-gray-400">{{ Number(item.original_score).toFixed(3) }}</td>
                          <td class="px-4 py-3 text-sm font-bold" :class="item.is_dropped ? 'text-red-500' : 'text-[#D97757]'">{{ Number(item.rerank_score).toFixed(3) }}</td>
                        </tr>
                        <tr v-if="!debugData.reranking?.length">
                          <td colspan="5" class="px-4 py-4 text-center text-sm text-gray-500">No items reached reranking stage.</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </details>
            </div>
          </div>
      </div>
      
      <div v-else-if="!loading && hasSearched" class="flex-1 flex items-center justify-center">
          <div class="text-center text-gray-500 dark:text-gray-400">
              <p>No debug data returned. Make sure the backend endpoint is working.</p>
          </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import NavBar from '../components/NavBar.vue';
import api from '../services/api';
import { useToast } from 'vue-toastification';

const toast = useToast();
const searchQuery = ref('');
const topK = ref(5);
const loading = ref(false);
const hasSearched = ref(false);
const debugData = ref(null);
const finalResults = ref(null);

const runSearch = async () => {
    if (!searchQuery.value) return;
    
    loading.value = true;
    hasSearched.value = true;
    debugData.value = null;
    finalResults.value = null;
    
    try {
        const response = await api.post('/retrieval/debug/search', {
            query: searchQuery.value,
            top_k: topK.value,
            view: 'auto'
        });
        
        debugData.value = response.data.debug_pipeline;
        finalResults.value = response.data.results;
        toast.success("Pipeline executed successfully!");
        
    } catch (err) {
        console.error(err);
        toast.error(err.response?.data?.detail || "Failed to execute debug search.");
    } finally {
        loading.value = false;
    }
};

const exportDebugData = () => {
    if (!debugData.value) return;
    
    const dataStr = JSON.stringify(debugData.value, null, 2);
    const blob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    
    const a = document.createElement('a');
    a.href = url;
    a.download = `retrieval_debug_${new Date().getTime()}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    toast.info("Debug data exported!");
};
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 8px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: rgba(156, 163, 175, 0.5);
  border-radius: 20px;
}
.dark .custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: rgba(75, 85, 99, 0.5);
}
</style>
