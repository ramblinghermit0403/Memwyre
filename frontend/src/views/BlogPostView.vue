<script setup>
import { ref, onMounted, onUnmounted, watch, nextTick, onServerPrefetch } from 'vue';

let shouldRestoreDarkClass = false;
import { useRoute, useRouter } from 'vue-router';
import SiteFooter from '@/components/SiteFooter.vue';
import { Marked } from 'marked';
import mermaid from 'mermaid';

const route = useRoute();
const router = useRouter();

const marked = new Marked({
  renderer: {
    code(code, infostring) {
      let text = '';
      let lang = '';
      if (typeof code === 'object' && code !== null) {
        text = code.text;
        lang = code.lang;
      } else {
        text = code;
        lang = infostring;
      }
      
      if (lang === 'mermaid') {
        // Safely pass the raw mermaid text by base64 encoding it
        let b64 = '';
        if (typeof window !== 'undefined' && window.btoa) {
          b64 = window.btoa(unescape(encodeURIComponent(text)));
        }
        return `<div class="mermaid-container flex justify-center w-full my-8" data-mermaid="${b64}"></div>`;
      }
      return `<pre><code class="language-${lang || ''}">${text}</code></pre>`;
    }
  }
});

const rawContent = ref('');
const parsedHtml = ref('');
const isLoading = ref(true);
const error = ref(null);

// Get meta info for other articles sidebar
const recentPosts = [
  {
    slug: 'mcp-persistent-memory',
    title: 'How to Give Claude Desktop Persistent Memory using MCP',
    category: 'MCP Server',
    author: 'Himansh Shivhare',
    fullDate: 'June 15, 2026'
  },
  {
    slug: 'vscode-mcp-persistent-memory',
    title: 'How to Enable Persistent Codebase Memory in VS Code with MCP and Cline',
    category: 'MCP Server',
    author: 'Himansh Shivhare',
    fullDate: 'June 2, 2026'
  },
  {
    slug: 'claude-code-memory-ingestion',
    title: 'Building Persistent Terminal Sessions: Claude Code Memory Ingestion with Memwyre',
    category: 'CLI Plugins',
    author: 'Himansh Shivhare',
    fullDate: 'May 18, 2026'
  },
  {
    slug: 'openclaw-autonomous-memory',
    title: 'Persistent Memory for Autonomous Agents: OpenClaw and Memwyre Integration',
    category: 'CLI Plugins',
    author: 'Himansh Shivhare',
    fullDate: 'May 4, 2026'
  },
  {
    slug: 'cursor-vs-claude-code-context',
    title: 'Cursor AI vs Claude Code: Managing Context and Memory in IDEs',
    category: 'Comparisons',
    author: 'Himansh Shivhare',
    fullDate: 'April 22, 2026'
  },
  {
    slug: 'state-of-ai-memory-2026',
    title: 'State of AI Memory 2026: The Shift from Stateless to Stateful Agent Networks',
    category: 'Architecture',
    author: 'Himansh Shivhare',
    fullDate: 'April 18, 2026'
  },
  {
    slug: 'rag-vs-memory-long-term-knowledge',
    title: 'RAG vs. AI Memory: Choosing the Right Approach for Long-Term Knowledge',
    category: 'Architecture',
    author: 'Himansh Shivhare',
    fullDate: 'April 9, 2026'
  }
];

const markdownFiles = import.meta.glob('../assets/blog/*.md', { query: '?raw', import: 'default' });

const renderMermaid = async () => {
  if (typeof window === 'undefined') return;
  const containers = document.querySelectorAll('.mermaid-container');
  for (let i = 0; i < containers.length; i++) {
    const el = containers[i];
    const b64 = el.getAttribute('data-mermaid');
    if (el.querySelector('svg')) continue; // Already rendered
    if (b64) {
      try {
        const text = decodeURIComponent(escape(window.atob(b64)));
        const id = `mermaid-svg-${Date.now()}-${i}`;
        const { svg } = await mermaid.render(id, text);
        el.innerHTML = svg;
      } catch (mermaidError) {
        console.error('Mermaid render error:', mermaidError);
        el.innerHTML = '<span class="text-red-500 text-sm">Failed to render diagram. Check console.</span>';
      }
    }
  }
};

const loadPost = async (slug) => {
  isLoading.value = true;
  error.value = null;
  
  const filePath = `../assets/blog/${slug}.md`;
  
  if (markdownFiles[filePath]) {
    try {
      const rawMd = await markdownFiles[filePath]();
      rawContent.value = rawMd;
      
      // Strip title heading (# Title) from raw markdown to display it in a custom header section instead
      const lines = rawMd.split(/\r?\n/);
      if (lines[0] && lines[0].startsWith('# ')) {
        lines.shift();
      }
      const cleanedMd = lines.join('\n');
      parsedHtml.value = marked.parse(cleanedMd);
    } catch (err) {
      console.error(err);
      error.value = 'Failed to load the article.';
    } finally {
      isLoading.value = false;
      
      // Render Mermaid diagrams after DOM updates are completely flushed on client
      if (typeof window !== 'undefined') {
        setTimeout(async () => {
          await renderMermaid();
        }, 50);
      }
    }
  } else {
    error.value = 'Article not found.';
    isLoading.value = false;
  }
};

// Initial state load check: handle server vs client hydration
const isServer = typeof window === 'undefined';
let preRenderedContent = '';

if (!isServer && window.__BLOG_POST_DATA__ && window.__BLOG_POST_DATA__.slug === route.params.slug) {
  preRenderedContent = window.__BLOG_POST_DATA__.content;
}

if (preRenderedContent) {
  rawContent.value = preRenderedContent;
  const lines = preRenderedContent.split(/\r?\n/);
  if (lines[0] && lines[0].startsWith('# ')) {
    lines.shift();
  }
  const cleanedMd = lines.join('\n');
  parsedHtml.value = marked.parse(cleanedMd);
  isLoading.value = false;
} else {
  // If no pre-rendered content (or if we are on the server), start loading the post
  const loadPromise = loadPost(route.params.slug);
  
  if (isServer) {
    onServerPrefetch(async () => {
      try {
        await loadPromise;
      } catch (err) {
        console.error('Prefetch error:', err);
      }
    });
  }
}

onMounted(() => {
  shouldRestoreDarkClass = document.documentElement.classList.contains('dark');
  document.documentElement.classList.remove('dark');
  document.documentElement.style.colorScheme = 'light';

  try {
    mermaid.initialize({
      startOnLoad: false,
      theme: 'neutral',
      securityLevel: 'loose',
      flowchart: {
        useMaxWidth: true,
        htmlLabels: true
      }
    });
  } catch (initError) {
    console.error('Mermaid initialization failed:', initError);
  }

  // Trigger mermaid render for pre-rendered content after page mounts
  setTimeout(() => {
    renderMermaid();
  }, 100);
});

onUnmounted(() => {
  document.documentElement.style.colorScheme = '';
  if (shouldRestoreDarkClass) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
});

// Reload post when route parameter slug changes (client-side routing only)
watch(() => route.params.slug, (newSlug) => {
  if (newSlug) {
    loadPost(newSlug);
    if (typeof window !== 'undefined') {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }
});
</script>

<template>
  <div class="relative min-h-screen bg-[#fafafa] dark:bg-[#0c0c0c] pt-16 pb-0 overflow-hidden font-sans">
    <!-- Centered A4-style page column with vertical lines on the sides -->
    <div class="relative max-w-4xl mx-auto border-l border-r border-gray-200 dark:border-gray-800/60 bg-white dark:bg-[#111] min-h-[calc(100vh-4rem)] pt-12 pb-20 px-6 sm:px-16 shadow-none">
      
      <!-- Loading State -->
      <div v-if="isLoading" class="flex flex-col items-center justify-center py-32">
        <div class="w-10 h-10 border-4 border-gray-300 dark:border-gray-800 border-t-[#D97757] rounded-full animate-spin"></div>
        <p class="mt-4 text-sm text-gray-400 dark:text-gray-500">Loading article...</p>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="bg-red-500/5 border border-red-500/20 text-red-500 rounded p-8 text-center my-10 animate-fade-in">
        <h2 class="text-lg font-semibold mb-2">Error</h2>
        <p class="text-sm font-light mb-6">{{ error }}</p>
        <router-link to="/blog" class="px-4 py-2 bg-black dark:bg-white text-white dark:text-black rounded text-sm font-semibold hover:bg-gray-800 dark:hover:bg-gray-150 transition-colors">
          Return to Blog Home
        </router-link>
      </div>

      <!-- Main Content Flow -->
      <div v-else>
        <!-- Breadcrumb / Category Navigation (e.g. Blog / Engineering Guide) -->
        <div class="flex items-center gap-1.5 text-[14px] text-gray-500 dark:text-gray-400 mb-6 font-normal">
          <router-link to="/blog" class="hover:text-black dark:hover:text-white transition-colors duration-150">Blog</router-link>
          <span class="text-gray-300 dark:text-gray-700">/</span>
          <span>{{ recentPosts.find(p => p.slug === route.params.slug)?.category || 'Engineering' }}</span>
        </div>

        <!-- Header Metadata -->
        <div class="mb-8 pb-6 border-b border-gray-100 dark:border-gray-900">
          <h1 class="text-3xl sm:text-4xl lg:text-[42px] font-bold tracking-tight text-gray-900 dark:text-white leading-[1.2] mb-6">
            {{ recentPosts.find(p => p.slug === route.params.slug)?.title || 'Memwyre Guide' }}
          </h1>
          <div class="flex items-center gap-2 text-[14px] text-gray-500 dark:text-gray-400">
            <img 
              src="https://avatars.githubusercontent.com/u/170114968?v=4" 
              alt="Himansh Shivhare" 
              class="w-6 h-6 rounded-full object-cover"
              @error="$event.target.src = 'https://ui-avatars.com/api/?name=Himansh+Shivhare&background=f3f4f6&color=333'"
            />
            <span class="font-normal text-gray-900 dark:text-gray-100">
              {{ recentPosts.find(p => p.slug === route.params.slug)?.author || 'Himansh Shivhare' }}
            </span>
            <span class="text-gray-300 dark:text-gray-700">•</span>
            <span>{{ recentPosts.find(p => p.slug === route.params.slug)?.fullDate || 'June 24, 2026' }}</span>
          </div>
        </div>

        <!-- Cover Image -->
        <div class="w-full aspect-[2/1] rounded-xl overflow-hidden mb-10 bg-gray-50 border border-gray-150 dark:bg-zinc-900/30 dark:border-zinc-800/80">
          <img 
            :src="`/blog-covers/${route.params.slug}.png`" 
            :alt="recentPosts.find(p => p.slug === route.params.slug)?.title || 'Blog Cover'" 
            class="w-full h-full object-cover"
            @error="$event.target.src = 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1200&q=80'"
          />
        </div>

        <!-- Parsed Markdown HTML Container -->
        <div class="markdown-content mb-16" v-html="parsedHtml"></div>

        <!-- Read Next / Other Articles (at the end of the article) -->
        <div class="pt-10 border-t border-gray-100 dark:border-gray-900">
          <h3 class="text-xs font-bold uppercase tracking-wider text-gray-400 dark:text-gray-500 mb-6 pb-2 border-b border-gray-100 dark:border-gray-900">
            Read Next
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div 
              v-for="post in recentPosts.filter(p => p.slug !== route.params.slug).slice(0, 2)" 
              :key="post.slug"
              class="group flex flex-col justify-between p-5 rounded-lg border border-gray-100 dark:border-gray-950 hover:border-[#D97757] dark:hover:border-[#D97757] transition-all duration-200 bg-gray-50/35 dark:bg-[#151515]/25"
            >
              <h4 class="text-base font-semibold text-gray-900 dark:text-white group-hover:text-[#D97757] transition-colors leading-snug mb-3">
                <router-link :to="`/blog/${post.slug}`">
                  {{ post.title }}
                </router-link>
              </h4>
              <router-link 
                :to="`/blog/${post.slug}`"
                class="inline-flex items-center gap-1 text-xs font-bold text-[#D97757] hover:text-[#c05c3d] transition-colors duration-150"
              >
                Read Article →
              </router-link>
            </div>
          </div>
        </div>
      </div>

    </div>
    <SiteFooter />
  </div>
</template>

<style>
/* CSS Styles for Parsed Markdown Content */
.markdown-content {
  font-family: inherit;
  color: var(--vp-c-text-1, #374151);
}

/* Mermaid Diagram Styling */
.markdown-content .mermaid-container {
  background: transparent;
  border: none;
  display: flex;
  justify-content: center;
  margin: 36px 0;
  width: 100%;
}

.markdown-content .mermaid-container svg {
  max-width: 100%;
  height: auto;
}

/* Force dark text for mermaid node labels in both dark/light mode for readability */
.markdown-content .mermaid-container text,
.markdown-content .mermaid-container text *,
.markdown-content .mermaid-container .node text,
.markdown-content .mermaid-container .node span,
.markdown-content .mermaid-container .node .label,
.markdown-content .mermaid-container .node .label *,
.markdown-content .mermaid-container .edgeLabel text,
.markdown-content .mermaid-container .edgeLabel span {
  color: #111827 !important;
  fill: #111827 !important;
}

.markdown-content .mermaid-container .node .label {
  font-family: inherit !important;
  font-size: 13px !important;
  line-height: 1.4 !important;
}

.markdown-content .mermaid-container .node .label b {
  font-size: 14px !important;
  font-weight: 700 !important;
  display: block;
  margin: 2px 0;
}

.markdown-content .mermaid-container .node .label font {
  font-size: 11px !important;
  color: #4b5563 !important;
  display: block;
  font-weight: 400 !important;
  line-height: 1.3 !important;
  margin-top: 2px;
}

.dark .markdown-content {
  color: #d1d5db;
}

.markdown-content h1,
.markdown-content h2,
.markdown-content h3,
.markdown-content h4 {
  font-weight: 600;
  color: #111827;
  line-height: 1.35;
  margin-top: 32px;
  margin-bottom: 16px;
}

.dark .markdown-content h1,
.dark .markdown-content h2,
.dark .markdown-content h3,
.dark .markdown-content h4 {
  color: #f3f4f6;
}

.markdown-content h1 { font-size: 26px; }
.markdown-content h2 { font-size: 22px; border-bottom: 1px solid rgba(0,0,0,0.06); padding-bottom: 8px; }
.dark .markdown-content h2 { border-bottom-color: rgba(255,255,255,0.06); }
.markdown-content h3 { font-size: 18px; }

.markdown-content p {
  font-size: 15px;
  line-height: 1.7;
  font-weight: 300;
  margin-top: 0;
  margin-bottom: 20px;
}

.markdown-content a {
  color: #D97757;
  font-weight: 500;
  text-decoration: underline;
  text-underline-offset: 4px;
}

.markdown-content a:hover {
  color: #c05c3d;
}

.markdown-content ul,
.markdown-content ol {
  margin-top: 0;
  margin-bottom: 20px;
  padding-left: 24px;
}

.markdown-content li {
  font-size: 15px;
  line-height: 1.7;
  font-weight: 300;
  margin-bottom: 8px;
}

.markdown-content pre {
  background: #f4f4f5;
  border: 1px solid #e4e4e7;
  border-radius: 8px;
  padding: 16px;
  overflow-x: auto;
  margin-top: 20px;
  margin-bottom: 24px;
}

.dark .markdown-content pre {
  background: #18181b;
  border-color: #27272a;
}

.markdown-content code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 13px;
  background: #f4f4f5;
  color: #0f0f10;
  padding: 3px 6px;
  border-radius: 4px;
  border: 1px solid #e4e4e7;
}

.dark .markdown-content code {
  background: #18181b;
  color: #f3f4f6;
  border-color: #27272a;
}

.markdown-content pre code {
  padding: 0;
  background: transparent;
  color: inherit;
  border: none;
  font-size: 13px;
}

.markdown-content blockquote {
  border-left: 4px solid #D97757;
  padding-left: 20px;
  font-style: italic;
  color: #4b5563;
  margin: 24px 0;
}

.dark .markdown-content blockquote {
  color: #9ca3af;
}

.markdown-content table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  margin-bottom: 24px;
  font-size: 14px;
}

.markdown-content th,
.markdown-content td {
  padding: 10px 14px;
  border: 1px solid #e4e4e7;
  text-align: left;
}

.dark .markdown-content th,
.dark .markdown-content td {
  border-color: #27272a;
}

.markdown-content th {
  background: #f4f4f5;
  font-weight: 600;
}

.dark .markdown-content th {
  background: #18181b;
}

.markdown-content hr {
  border: 0;
  border-top: 1px solid #e4e4e7;
  margin: 32px 0;
}

.dark .markdown-content hr {
  border-top-color: #27272a;
}
</style>
