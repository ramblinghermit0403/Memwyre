<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

let shouldRestoreDarkClass = false;

onMounted(() => {
  shouldRestoreDarkClass = document.documentElement.classList.contains('dark');
  document.documentElement.classList.remove('dark');
  document.documentElement.style.colorScheme = 'light';
});

onUnmounted(() => {
  document.documentElement.style.colorScheme = '';
  if (shouldRestoreDarkClass) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
});

const posts = ref([
  {
    slug: 'mcp-persistent-memory',
    category: 'MCP Server',
    title: 'How to Give Claude Desktop Persistent Memory using MCP',
    excerpt: 'Claude Desktop is powerful but stateless. Learn how to configure Memwyre as a local Model Context Protocol (MCP) server to store and query context across chat sessions.',
    readTime: '4 min read',
    date: 'Jun 15, 2026'
  },
  {
    slug: 'vscode-mcp-persistent-memory',
    category: 'MCP Server',
    title: 'How to Enable Persistent Codebase Memory in VS Code with MCP and Cline',
    excerpt: 'Give your VS Code AI agents (Cline, Roo-Code) a persistent memory layer. Step-by-step setup using the remote Memwyre MCP gateway.',
    readTime: '5 min read',
    date: 'Jun 02, 2026'
  },
  {
    slug: 'claude-code-memory-ingestion',
    category: 'CLI Plugins',
    title: 'Building Persistent Terminal Sessions: Claude Code Memory Ingestion',
    excerpt: "Anthropic's Claude Code CLI is incredibly fast. Integrate Memwyre hooks to automatically inject project memory on launch and ingest transcripts on exit.",
    readTime: '5 min read',
    date: 'May 18, 2026'
  },
  {
    slug: 'openclaw-autonomous-memory',
    category: 'CLI Plugins',
    title: 'Persistent Memory for Autonomous Agents: OpenClaw and Memwyre',
    excerpt: 'Autonomous agent workflows suffer from amnesia. Learn how to load the Memwyre OpenClaw plugin and enable the agent to query and update your vault.',
    readTime: '4 min read',
    date: 'May 04, 2026'
  },
  {
    slug: 'cursor-vs-claude-code-context',
    category: 'Comparisons',
    title: 'Cursor AI vs Claude Code: Managing Context and Memory in IDEs',
    excerpt: 'A technical breakdown comparing how Cursor AI and Claude Code manage workspace context, and how to extend both with Memwyre.',
    readTime: '6 min read',
    date: 'Apr 22, 2026'
  },
  {
    slug: 'state-of-ai-memory-2026',
    category: 'Architecture',
    title: 'State of AI Memory 2026: The Shift from Stateless to Stateful Agent Networks',
    excerpt: 'An inspection of context window explosion and why stateless attention buffers create substantial financial and latency overheads for enterprise codebase scale.',
    readTime: '5 min read',
    date: 'Apr 18, 2026'
  },
  {
    slug: 'rag-vs-memory-long-term-knowledge',
    category: 'Architecture',
    title: 'RAG vs. AI Memory: Choosing the Right Approach for Long-Term Knowledge',
    excerpt: 'Why basic Vector RAG fails for developer workflows due to chunk fragmentation, and why entity-profile routing provides better context.',
    readTime: '6 min read',
    date: 'Apr 09, 2026'
  }
]);
</script>

<template>
  <div class="relative min-h-screen bg-white dark:bg-[#0c0c0c] pt-28 pb-20 overflow-hidden font-sans">
    <!-- Grid Blueprint background line effects (consistent with landing page) -->
    <div class="absolute inset-0 pointer-events-none opacity-[0.03] dark:opacity-[0.05]">
      <div class="absolute inset-0 bg-[linear-gradient(to_right,#808080_1px,transparent_1px),linear-gradient(to_bottom,#808080_1px,transparent_1px)] bg-[size:40px_40px]"></div>
    </div>

    <!-- Global Vertical Grid Lines (matching landing page) -->
    <div class="absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-300/80 dark:bg-gray-800/60 pointer-events-none select-none z-30"></div>
    <div class="absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-300/80 dark:bg-gray-800/60 pointer-events-none select-none z-30"></div>

    <div class="relative max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">
      <!-- Breadcrumb & Header -->
      <div class="mb-16 text-left">
        <div class="text-xs tracking-wider uppercase font-bold font-mono text-gray-400 dark:text-gray-500 mb-6 px-1">
          / INSIGHTS & GUIDES
        </div>
        <h1 class="hero-serif text-4xl md:text-5xl lg:text-6xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] dark:text-white mb-6">
          Memwyre <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">Blog</span>
        </h1>
        <p class="text-base sm:text-lg text-[#4B5563] dark:text-gray-400 max-w-2xl font-normal leading-relaxed">
          Deep dives into Model Context Protocol (MCP), persistent context caching, vector memory, and agentic workflows.
        </p>
      </div>

      <!-- Grid of Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <article 
          v-for="post in posts" 
          :key="post.slug"
          class="group relative flex flex-col justify-between p-8 bg-white dark:bg-[#111] border border-gray-200 dark:border-gray-800/80 rounded-xl hover:border-[#D97757] dark:hover:border-[#D97757] transition-all duration-300 shadow-[0_4px_20px_rgba(0,0,0,0.02)] dark:shadow-none hover:shadow-[0_8px_30px_rgba(217,119,87,0.06)] hover:-translate-y-1"
        >
          <div>
            <!-- Cover Image (minimal, aspect-ratio 2:1) -->
            <div class="w-full aspect-[2/1] rounded-lg overflow-hidden mb-6 bg-gray-50 border border-gray-100 dark:bg-zinc-900/30 dark:border-zinc-800/80 flex items-center justify-center">
              <img 
                :src="`/blog-covers/${post.slug}.png`" 
                :alt="post.title" 
                class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform duration-300"
                @error="$event.target.src = 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80'"
              />
            </div>

            <div class="flex items-center justify-between mb-4">
              <span class="text-xs font-bold uppercase tracking-wider text-[#D97757]">
                {{ post.category }}
              </span>
              <span class="text-xs text-gray-400 dark:text-gray-500 font-light">
                {{ post.readTime }}
              </span>
            </div>
            
            <h2 class="text-xl font-semibold text-gray-900 dark:text-white mb-3 group-hover:text-[#D97757] transition-colors duration-200 leading-snug">
              <router-link :to="`/blog/${post.slug}`">
                {{ post.title }}
              </router-link>
            </h2>
            
            <p class="text-[14px] text-gray-500 dark:text-gray-400 font-light leading-relaxed mb-6">
              {{ post.excerpt }}
            </p>
          </div>

          <div class="flex items-center justify-between mt-auto pt-4 border-t border-gray-100 dark:border-gray-900">
            <span class="text-xs text-gray-400 dark:text-gray-500">
              {{ post.date }}
            </span>
            <router-link 
              :to="`/blog/${post.slug}`"
              class="inline-flex items-center gap-1 text-sm font-semibold text-[#D97757] hover:text-[#c05c3d] transition-colors duration-150"
            >
              Read Article
              <svg class="w-4 h-4 transform group-hover:translate-x-0.5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7" />
              </svg>
            </router-link>
          </div>
        </article>
      </div>
    </div>
  </div>
</template>
