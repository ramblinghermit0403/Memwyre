<script setup>
import { ref, onMounted, onUnmounted, watch, nextTick, computed, onServerPrefetch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import SiteFooter from '@/components/SiteFooter.vue';
import { Marked } from 'marked';
import mermaid from 'mermaid';

const route = useRoute();
const router = useRouter();

// Slugify heading helper
const slugify = (text) => {
  return text.toLowerCase()
    .replace(/[^\w\s-]/g, '')
    .replace(/\s+/g, '-');
};

const marked = new Marked({
  renderer: {
    heading(text, level, raw) {
      let depth = level;
      let rawText = '';
      if (typeof text === 'object' && text !== null) {
        rawText = text.text;
        depth = text.depth;
      } else {
        rawText = text;
      }
      const slug = slugify(rawText);
      return `<h${depth} id="${slug}">${rawText}</h${depth}>`;
    },
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
const toc = ref([]);
const activeSection = ref('');

const parseToc = (md) => {
  if (!md) return;
  const headings = [];
  const lines = md.split(/\r?\n/);
  let sectionIndex = 1;
  for (const line of lines) {
    const match = line.match(/^(#{2,3})\s+(.+)$/);
    if (match) {
      const level = match[1].length;
      const text = match[2].trim();
      const slug = slugify(text);
      headings.push({ level, text, slug, index: sectionIndex++ });
    }
  }
  toc.value = headings;
};

watch(rawContent, (newContent) => {
  parseToc(newContent);
}, { immediate: true });

// Get meta info for other articles sidebar
const recentPosts = [
  {
    slug: 'mcp-persistent-memory',
    title: 'How to Give Claude Desktop Persistent Memory using MCP',
    category: 'MCP Server',
    author: 'Himansh Shivhare',
    fullDate: 'June 15, 2026',
    readTime: '4 MIN'
  },
  {
    slug: 'vscode-mcp-persistent-memory',
    title: 'How to Enable Persistent Codebase Memory in VS Code with MCP and Cline',
    category: 'MCP Server',
    author: 'Himansh Shivhare',
    fullDate: 'June 2, 2026',
    readTime: '5 MIN'
  },
  {
    slug: 'claude-code-memory-ingestion',
    title: 'Building Persistent Terminal Sessions: Claude Code Memory Ingestion',
    category: 'CLI Plugins',
    author: 'Himansh Shivhare',
    fullDate: 'May 18, 2026',
    readTime: '5 MIN'
  },
  {
    slug: 'openclaw-autonomous-memory',
    title: 'Persistent Memory for Autonomous Agents: OpenClaw and Memwyre',
    category: 'CLI Plugins',
    author: 'Himansh Shivhare',
    fullDate: 'May 4, 2026',
    readTime: '4 MIN'
  },
  {
    slug: 'cursor-vs-claude-code-context',
    title: 'Cursor AI vs Claude Code: Managing Context and Memory in IDEs',
    category: 'Comparisons',
    author: 'Himansh Shivhare',
    fullDate: 'April 22, 2026',
    readTime: '6 MIN'
  },
  {
    slug: 'state-of-ai-memory-2026',
    title: 'State of AI Memory 2026: The Shift from Stateless to Stateful Agent Networks',
    category: 'Architecture',
    author: 'Himansh Shivhare',
    fullDate: 'April 18, 2026',
    readTime: '5 MIN'
  },
  {
    slug: 'rag-vs-memory-long-term-knowledge',
    title: 'RAG vs. AI Memory: Choosing the Right Approach for Long-Term Knowledge',
    category: 'Architecture',
    author: 'Himansh Shivhare',
    fullDate: 'April 9, 2026',
    readTime: '6 MIN'
  },
  {
    slug: 'what-is-ai-memory',
    title: 'What is AI Memory? The Architecture of Long-Term Context',
    category: 'Research',
    author: 'Memwyre Research Lab',
    fullDate: 'June 24, 2026',
    readTime: '15 MIN'
  },
  {
    slug: 'ai-memory-benchmark-locomo',
    title: 'LoCoMo Benchmark: Evaluation of AI Memory',
    category: 'Research',
    author: 'Memwyre Research Lab',
    fullDate: 'June 24, 2026',
    readTime: '12 MIN'
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

// Scrollspy Observer
let observer = null;
const setupScrollObserver = () => {
  if (typeof window === 'undefined') return;
  if (observer) observer.disconnect();

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

  nextTick(() => {
    const headings = document.querySelectorAll('.markdown-content h2, .markdown-content h3');
    headings.forEach((h) => {
      observer.observe(h);
    });
  });
};

watch(parsedHtml, () => {
  setTimeout(() => {
    setupScrollObserver();
  }, 200);
});

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

  setTimeout(() => {
    renderMermaid();
    setupScrollObserver();
  }, 200);
});

onUnmounted(() => {
  if (observer) observer.disconnect();
});

watch(() => route.params.slug, (newSlug) => {
  if (newSlug) {
    loadPost(newSlug);
  }
});

// Meta helpers
const pageUrl = computed(() => typeof window !== 'undefined' ? window.location.href : '');
const pageTitle = computed(() => {
  const currentPost = recentPosts.find(p => p.slug === route.params.slug);
  return currentPost ? currentPost.title : 'Memwyre Guide';
});

const copyLink = () => {
  if (typeof window !== 'undefined') {
    navigator.clipboard.writeText(window.location.href);
    alert('Article link copied to clipboard!');
  }
};
</script>

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
          :to="recentPosts.find(p => p.slug === route.params.slug)?.category === 'Research' ? '/research' : '/blog'" 
          class="inline-flex items-center gap-2 text-xs uppercase tracking-wider font-semibold text-gray-500 dark:text-gray-400 hover:text-[#D97757] dark:hover:text-[#D97757] transition-colors"
        >
          <span class="inline-flex items-center justify-center w-5 h-5 rounded-full border border-gray-300 dark:border-zinc-800 text-[10px]">&larr;</span>
          {{ recentPosts.find(p => p.slug === route.params.slug)?.category === 'Research' ? 'All research' : 'All articles' }}
        </router-link>
      </div>

      <!-- Loading State -->
      <div v-if="isLoading" class="flex flex-col items-center justify-center py-32">
        <div class="w-10 h-10 border-4 border-gray-300 dark:border-gray-800 border-t-[#D97757] rounded-full animate-spin"></div>
        <p class="mt-4 text-sm text-gray-400 dark:text-gray-500">Loading article...</p>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="bg-red-500/5 border border-red-500/20 text-red-500 rounded p-8 text-center my-10">
        <h2 class="text-lg font-semibold mb-2">Error</h2>
        <p class="text-sm font-light mb-6">{{ error }}</p>
        <router-link to="/blog" class="px-4 py-2 bg-black dark:bg-white text-white dark:text-black rounded text-sm font-semibold hover:bg-gray-800 dark:hover:bg-gray-150 transition-colors">
          Return to Blog Home
        </router-link>
      </div>

      <!-- Article Flow -->
      <div v-else>
        <!-- Header Section -->
        <div class="space-y-4 mb-8 text-left">
          <div class="text-xs font-bold uppercase tracking-wider text-[#D97757] font-mono">
            {{ recentPosts.find(p => p.slug === route.params.slug)?.category || 'Engineering' }} 
            <span class="text-gray-300 dark:text-gray-700 mx-2">/</span> 
            {{ recentPosts.find(p => p.slug === route.params.slug)?.fullDate || 'June 24, 2026' }}
          </div>
          
          <h1 v-if="route.params.slug === 'what-is-ai-memory'" class="hero-serif text-4xl sm:text-5xl lg:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-950 dark:text-white">
            What is AI Memory? <br />
            <span class="italic font-medium text-gray-900 dark:text-gray-100">The Architecture of <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">Long-Term Context.</span></span>
          </h1>
          <h1 v-else-if="route.params.slug === 'ai-memory-benchmark-locomo'" class="hero-serif text-4xl sm:text-5xl lg:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-950 dark:text-white">
            LoCoMo Benchmark <br />
            <span class="italic font-medium text-gray-900 dark:text-gray-100">Evaluation of <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">AI Memory.</span></span>
          </h1>
          <h1 v-else class="hero-serif text-4xl sm:text-5xl lg:text-6xl tracking-[-0.02em] leading-[1.1] text-gray-950 dark:text-white">
            {{ recentPosts.find(p => p.slug === route.params.slug)?.title || 'Memwyre Guide' }}
          </h1>

          <div class="text-[10px] tracking-wider uppercase font-bold font-mono text-gray-400 dark:text-gray-500 pt-2">
            {{ recentPosts.find(p => p.slug === route.params.slug)?.readTime || '5 MIN' }} READ
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
                  alt="Himansh Shivhare" 
                  class="w-10 h-10 rounded-full object-cover border border-gray-200 dark:border-zinc-800"
                  @error="$event.target.src = 'https://ui-avatars.com/api/?name=Himansh+Shivhare&background=f3f4f6&color=333'"
                />
                <span class="text-sm font-semibold text-gray-900 dark:text-white">
                  {{ recentPosts.find(p => p.slug === route.params.slug)?.author || 'Himansh Shivhare' }}
                </span>
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
                :src="`/blog-covers/${route.params.slug}.png`" 
                :alt="recentPosts.find(p => p.slug === route.params.slug)?.title || 'Blog Cover'" 
                class="w-full h-full object-cover"
                @error="$event.target.src = 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1200&q=80'"
              />
            </div>

            <!-- Parsed Markdown HTML -->
            <div class="markdown-content mb-16 animate-fade-in" v-html="parsedHtml"></div>

            <!-- Read Next section -->
            <div class="pt-10 border-t border-gray-100 dark:border-gray-900">
              <h3 class="text-xs font-bold uppercase tracking-wider text-gray-400 dark:text-gray-500 mb-6 pb-2 border-b border-gray-100 dark:border-gray-900 font-mono">
                Read Next
              </h3>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div 
                  v-for="post in recentPosts.filter(p => p.slug !== route.params.slug).slice(0, 3)" 
                  :key="post.slug"
                  class="group flex flex-col justify-between p-4 rounded-lg border border-gray-150 dark:border-zinc-800 hover:border-[#D97757] dark:hover:border-[#D97757] transition-all duration-200 bg-gray-50/35 dark:bg-[#151515]/25"
                >
                  <h4 class="text-xs font-semibold text-gray-900 dark:text-white group-hover:text-[#D97757] transition-colors leading-snug mb-3">
                    <router-link :to="post.category === 'Research' ? `/research/${post.slug}` : `/blog/${post.slug}`">
                      {{ post.title }}
                    </router-link>
                  </h4>
                  <router-link 
                    :to="post.category === 'Research' ? `/research/${post.slug}` : `/blog/${post.slug}`"
                    class="inline-flex items-center gap-1 text-[11px] font-bold text-[#D97757] hover:text-[#c05c3d] transition-colors duration-150 font-mono"
                  >
                    Read &rarr;
                  </router-link>
                </div>
              </div>
            </div>
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
  font-family: 'Playfair Display', Georgia, serif;
  color: #111827;
  line-height: 1.25;
  margin-top: 36px;
  margin-bottom: 16px;
  scroll-margin-top: 100px;
}

.dark .markdown-content h1,
.dark .markdown-content h2,
.dark .markdown-content h3,
.dark .markdown-content h4 {
  color: #f3f4f6;
}

.markdown-content h1 {
  font-size: 32px;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.markdown-content h2 {
  font-size: 26px;
  font-weight: 500;
  letter-spacing: -0.015em;
  border-bottom: 1px solid rgba(0,0,0,0.06);
  padding-bottom: 8px;
}

.dark .markdown-content h2 {
  border-bottom-color: rgba(255,255,255,0.06);
}

.markdown-content h3 {
  font-size: 20px;
  font-weight: 600;
  letter-spacing: -0.01em;
}

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
