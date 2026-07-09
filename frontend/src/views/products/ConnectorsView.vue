<template>
  <div class="min-h-screen bg-white text-gray-900 font-sans relative overflow-x-hidden selection:bg-[#D97757] selection:text-white pt-16">
    <!-- Global Vertical Grid Lines -->
    <div class="absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-300/80 pointer-events-none select-none z-30"></div>
    <div class="absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-300/80 pointer-events-none select-none z-30"></div>

    <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 relative z-10">
      
      <!-- 1. HERO SECTION -->
      <div class="pt-2 pb-10 sm:pb-12">
        <!-- Breadcrumb -->
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ PRODUCTS / CONNECTORS</div>
          <div>[1/3]</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-6 sm:mb-8"></div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div class="space-y-6">
            <h1 class="hero-serif text-4xl sm:text-6xl lg:text-[70px] tracking-[-0.02em] leading-[1.1] lg:leading-[78px] text-[rgb(1,1,16)] max-w-4xl">
              Your data, always<br class="hidden sm:block" />
              <span class="inline-block italic font-medium">in <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">sync.</span></span>
            </h1>
            <p class="text-base text-[#111827] leading-relaxed mt-6 sm:mt-8 max-w-2xl font-normal">
              Pull from Notion, Google Drive, Gmail, S3, and more. Configure once — your AI agent's context stays fresh automatically.
            </p>
            
            <!-- Buttons with technical grid brackets -->
            <div class="relative inline-flex p-3 mt-4 sm:mt-6 border border-dashed border-gray-300 rounded max-w-max z-20">
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

              <!-- Content (Buttons) -->
              <div class="flex flex-row items-center justify-start gap-3 sm:gap-4">
                <router-link to="/signup"
                  class="w-auto px-4 py-2 sm:px-6 sm:py-3 bg-[#050614] text-white font-bold rounded hover:bg-gray-800 transition-all duration-300 shadow-md text-xs sm:text-sm inline-flex items-center justify-center gap-2">
                  Start Connecting →
                </router-link>
                <a href="/docs/integrations/connectors" target="_blank"
                  class="w-auto px-4 py-2 sm:px-6 sm:py-3 bg-white text-[#050614] font-bold rounded border border-gray-250 hover:bg-gray-50 transition-all duration-300 text-xs sm:text-sm inline-flex items-center justify-center">
                  Read Documentation
                </a>
              </div>
            </div>
          </div>

          <!-- Interactive Scattered Connections Animation -->
          <div class="bg-white p-4 relative flex flex-col justify-center min-h-[300px] overflow-visible">
            <ScatteredMemoryHero class="-translate-y-[100px] -translate-x-[50px]" />
          </div>
        </div>
      </div>

      <!-- 2. THE PROBLEM / USE CASE -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none"></div>
      <div class="py-8 sm:py-10">
        <div class="max-w-3xl mb-6 sm:mb-8">
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">The Disconnect</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Your agent's knowledge is always stale.
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="(problem, idx) in [
            { title: 'Manual File Parsing', body: 'Extracting clean text from multi-format PDFs, docx, and markdowns manually is tedious and fails to scale.' },
            { title: 'Scattered Signals', body: 'Knowledge is trapped across static local documents, API documentation pages, and team chats with no unified ingest.' },
            { title: 'Stale Context', body: 'If information changes on a page or a document is modified, your AI agents have no way to deduplicate and update their memory.' }
          ]" :key="idx" class="p-6 border border-gray-200 rounded-lg bg-white shadow-sm hover:border-[#D97757]/40 transition-colors">
            <div class="text-xs tracking-wider font-mono font-bold text-gray-400 mb-4">0{{ idx + 1 }} . PROBLEM</div>
            <h3 class="text-lg font-bold text-gray-900 mb-2">{{ problem.title }}</h3>
            <p class="text-sm text-gray-500 leading-relaxed">{{ problem.body }}</p>
          </div>
        </div>
      </div>

      <!-- 3. TECHNICAL DETAILS / HOW IT WORKS -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none"></div>
      <div class="py-8 sm:py-10">
        <div class="max-w-3xl mb-6 sm:mb-8">
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">Deep Dive</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Set once. Always fresh.
          </h2>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div class="lg:col-span-5 space-y-8">
            <div v-for="(step, idx) in [
              { title: 'Ingest via API or Upload', body: 'Upload PDFs/docx files or call our url-ingestion endpoint directly to fetch content via httpx (HTTP/2 enabled).' },
              { title: 'Celery Background Queue', body: 'Background workers process the raw content, stripping navs, scripts, and null bytes to avoid database errors.' },
              { title: 'Realtime WebSocket Broadcasts', body: 'Once processed, our server broadcasts an inbox_update message to instantly refresh all active client interfaces.' }
            ]" :key="idx" class="flex gap-4">
              <div class="w-8 h-8 rounded-full border border-gray-300 text-sm font-bold font-mono flex items-center justify-center shrink-0 text-[#D97757] bg-white">
                {{ idx + 1 }}
              </div>
              <div>
                <h4 class="font-bold text-gray-900 mb-1">{{ step.title }}</h4>
                <p class="text-sm text-gray-500 leading-relaxed">{{ step.body }}</p>
              </div>
            </div>
          </div>

          <div class="lg:col-span-7 border border-gray-200 rounded-lg overflow-hidden bg-gray-50 p-6">
            <div class="flex items-center justify-between border-b border-gray-200 pb-3 mb-4 font-mono text-xs text-gray-400">
              <span>POST /api/v1/ingest/url</span>
              <span>JSON</span>
            </div>
            <pre class="text-xs sm:text-sm font-mono overflow-x-auto text-gray-700 leading-relaxed"><code>{
  <span class="text-[#D97757]">"url"</span>: <span class="text-[#2B7FFF]">"https://example.com/api-docs"</span>,
  <span class="text-[#D97757]">"tags"</span>: [
    <span class="text-[#2B7FFF]">"kubernetes"</span>,
    <span class="text-[#2B7FFF]">"deployment"</span>
  ],
  <span class="text-[#D97757]">"auto_approve"</span>: <span class="text-[#2B7FFF]">true</span>
}</code></pre>
          </div>
        </div>
      </div>

      <!-- 4. SUPPORTED PLUGINS & SERVICES -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none"></div>
      <div class="py-8 sm:py-10">
        <div class="max-w-3xl mb-6 sm:mb-8">
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">Integrations</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Connect everything your team uses.
          </h2>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div v-for="app in [
            { name: 'Notion', desc: 'Sync docs & databases', logo: notionLogo },
            { name: 'Google Drive', desc: 'Docs, Sheets, Slides', logo: driveLogo },
            { name: 'Gmail', desc: 'Email threads & context', iconClass: 'fa-solid fa-envelope' },
            { name: 'GitHub', desc: 'Issues, PRs, Markdown', iconClass: 'fa-brands fa-github' },
            { name: 'S3 / R2', desc: 'Raw binary buckets', iconClass: 'fa-solid fa-database' },
            { name: 'Slack', desc: 'Public channel discussions', iconClass: 'fa-brands fa-slack' },
            { name: 'Web Crawler', desc: 'HTML & Markdown scrape', iconClass: 'fa-solid fa-spider' }
          ]" :key="app.name" class="p-4 border border-gray-200 rounded bg-white hover:border-[#D97757]/30 transition-colors flex items-center gap-3">
            <img v-if="app.logo" :src="app.logo" class="w-6 h-6 shrink-0" :alt="app.name" />
            <div v-else-if="app.iconClass" class="w-6 h-6 shrink-0 flex items-center justify-center text-gray-500 text-lg">
              <i :class="app.iconClass"></i>
            </div>
            <div>
              <div class="font-bold text-gray-900 text-sm mb-0.5">{{ app.name }}</div>
              <div class="text-xs text-gray-400">{{ app.desc }}</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 4b. DETAILED TECHNICAL SPECIFICATIONS -->
      <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none"></div>
      <div class="py-8 sm:py-10">
        <div class="max-w-3xl mb-6 sm:mb-8">
          <span class="text-xs tracking-wider uppercase font-bold font-mono text-[#D97757]">Integration Details</span>
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mt-2">
            Technical specifications of our sync engine.
          </h2>
        </div>

        <div class="space-y-6 text-sm text-gray-600 leading-relaxed">
          <p>
            Memwyre’s data connectors are built to address the stale context problem by integrating directly into your team's existing workflow. The sync engine operates by monitoring third-party APIs (such as Notion, Google Drive, Slack, and GitHub) and ingesting new updates into your memory vault. For databases like Notion, the connector polls the workspace API and extracts text blocks, database relations, and properties, transforming them into clean, structured Markdown.
          </p>
          <p>
            When processing file attachments from Google Drive or local uploads (PDF, Docx, or raw text), the system extracts raw text and passes it to our parsing queue. This Celery-backed ingestion pipeline strips navigation elements, scripts, and null bytes, preventing database errors and eliminating useless token bloat before indexing.
          </p>
          <p>
            For engineering environments, the GitHub connector maps commits, pull request changes, and issues into relational entities. This allows your developer agents to understand the context behind a code change or issue resolution. Our API endpoint supports automated URL scraping where you can POST a web address with custom tags; the server scrapes the content, parses it to Markdown, and broadcasts a WebSocket notification to update all active MCP clients in under 300 milliseconds.
          </p>
          <p>
            To ensure secure connectivity, all third-party integrations utilize OAuth 2.0 authorization flows. The tokens are encrypted at rest using AES-256-GCM and are stored within an isolated vault environment. The connector orchestrator supports customizable sync schedules (ranging from real-time webhook updates to hourly or daily cron-style polling cycles) depending on your team's API limits and data rate constraints. This guarantees that your background workers do not exceed platform thresholds.
          </p>
          <p>
            Once data is successfully ingested and normalized into clean Markdown, it is parsed by our backend semantic engine to build detailed context profiles. These profiles map entity relationships, ensuring that when an AI assistant queries your memory vault, it receives a cohesive knowledge graph rather than disjointed chunks of text. You can monitor all active data syncs, execution logs, and pending document approvals directly in the Memwyre Web Dashboard interface. This administrative dashboard provides granular sync state oversight, active data bandwidth monitoring, and debug execution logs for every data connector.
          </p>
        </div>
      </div>

      <!-- 5. BOTTOM CTA -->
      <div class="border border-dashed border-gray-300 rounded-none p-12 text-center bg-white relative my-12 sm:my-16 overflow-hidden">
        <!-- corner brackets -->
        <div class="absolute top-2 left-2 w-3 h-3 border-t border-l border-gray-400"></div>
        <div class="absolute top-2 right-2 w-3 h-3 border-t border-r border-gray-400"></div>
        <div class="absolute bottom-2 left-2 w-3 h-3 border-b border-l border-gray-400"></div>
        <div class="absolute bottom-2 right-2 w-3 h-3 border-b border-r border-gray-400"></div>

        <h3 class="hero-serif text-2xl sm:text-3xl lg:text-4xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mb-4">
          Context infrastructure for AI agents.
        </h3>
        <p class="text-sm text-gray-500 max-w-md mx-auto mb-6">
          Stop importing. Start connecting. Set up your first data stream in minutes.
        </p>
        <router-link to="/signup" class="inline-block px-8 py-3 bg-[#050614] text-white text-sm font-bold rounded hover:bg-gray-800 transition-all duration-300 shadow-md">
          Connect Your Vault
        </router-link>
      </div>

    </div>
    <SiteFooter />
  </div>
</template>

<script setup>
import notionLogo from '@/assets/notion-svgrepo-com.svg';
import driveLogo from '@/assets/google-drive.svg';
import ScatteredMemoryHero from '@/components/landing/ScatteredMemoryHero.vue';
import SiteFooter from '@/components/SiteFooter.vue';
</script>
