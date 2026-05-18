<template>
  <div class="portfolio-container antialiased selection:bg-[#D97757] selection:text-white bg-white text-[#191919]">
    <nav class="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-black/5 px-6 py-4 flex items-center justify-between">
      <div class="font-bold text-xl tracking-tight text-gray-900">Himansh Shivhare</div>
      <div class="hidden md:flex gap-8">
        <a href="#projects" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Projects</a>
        <a href="#services" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Services</a>
        <a href="#contact" class="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">Contact</a>
      </div>
      <a href="mailto:you@email.com" class="text-sm font-bold bg-black text-white px-5 py-2.5 rounded-xl hover:bg-gray-800 transition-all shadow-md hover:scale-105">Hire me</a>
    </nav>

    <!-- Hero -->
    <div class="relative z-10 pt-24 sm:pt-32 pb-20 sm:pb-28 overflow-hidden flex items-center bg-white">
      <LogoBgAnimation class="absolute inset-0 z-0 opacity-[0.08]" :invert="true" />
      <div class="relative z-10 max-w-5xl mx-auto px-6 text-center flex flex-col items-center">
        <div class="inline-flex items-center gap-2 text-sm font-bold bg-[#D97757]/10 text-[#D97757] px-4 py-1.5 rounded-full mb-8">
          <span class="w-2 h-2 rounded-full bg-[#D97757] animate-pulse"></span>
          Available for freelance work
        </div>
        <h1 class="text-5xl sm:text-7xl font-extrabold tracking-tight leading-[1.05] text-gray-900 mb-6">
          I build <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#D97757] via-[#FF9A7B] to-[#D97757] animate-gradient-x italic font-normal">AI integrations</span> <br class="hidden sm:block" /> that actually ship.
        </h1>
        <p class="text-lg sm:text-xl text-gray-500 leading-relaxed max-w-2xl font-medium mb-10">
          WhatsApp automation, AI memory systems, and agent tooling for startups and founders who need reliable infrastructure — not demos.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 w-full sm:w-auto">
          <a href="mailto:you@email.com" class="px-8 py-4 bg-black text-white font-bold rounded-xl hover:bg-gray-800 transition-all shadow-xl hover:scale-105 text-base w-full sm:w-auto text-center">
            Let's work together →
          </a>
          <a href="#projects" class="px-8 py-4 bg-white text-black font-bold rounded-xl border border-black/10 hover:bg-black/5 transition-all hover:border-black/20 text-base w-full sm:w-auto text-center">
            See my work
          </a>
        </div>
      </div>
    </div>

    <!-- Skills bar -->
    <div class="border-y border-black/5 bg-[#f7f6f3] py-6 px-6">
      <div class="max-w-5xl mx-auto flex flex-wrap justify-center gap-3">
        <span class="px-4 py-2 bg-white border border-black/5 rounded-full text-sm font-medium text-gray-700 shadow-sm">WhatsApp API</span>
        <span class="px-4 py-2 bg-white border border-black/5 rounded-full text-sm font-medium text-gray-700 shadow-sm">MCP / AI Agents</span>
        <span class="px-4 py-2 bg-white border border-black/5 rounded-full text-sm font-medium text-gray-700 shadow-sm">LLM Integration</span>
        <span class="px-4 py-2 bg-white border border-black/5 rounded-full text-sm font-medium text-gray-700 shadow-sm">Chrome Extensions</span>
        <span class="px-4 py-2 bg-white border border-black/5 rounded-full text-sm font-medium text-gray-700 shadow-sm">Node.js</span>
        <span class="px-4 py-2 bg-white border border-black/5 rounded-full text-sm font-medium text-gray-700 shadow-sm">React</span>
        <span class="px-4 py-2 bg-white border border-black/5 rounded-full text-sm font-medium text-gray-700 shadow-sm">REST APIs</span>
        <span class="px-4 py-2 bg-white border border-black/5 rounded-full text-sm font-medium text-gray-700 shadow-sm">Webhook Systems</span>
      </div>
    </div>

    <!-- Projects -->
    <section id="projects" class="py-24 max-w-5xl mx-auto px-6">
      <div class="mb-12">
        <h2 class="text-sm font-bold uppercase tracking-widest text-gray-400 mb-4">Work</h2>
        <p class="font-display text-3xl sm:text-4xl font-extrabold tracking-tight text-gray-900">Things I've built</p>
      </div>
      
      <div class="space-y-8">
        <div v-for="project in projects" :key="project.id" 
          class="bg-white border border-black/5 rounded-2xl p-8 sm:p-10 shadow-lg hover:shadow-xl transition-all duration-300 grid grid-cols-1 sm:grid-cols-[auto_1fr] gap-6 items-start group">
          <div class="shrink-0 group-hover:scale-110 transition-transform">
            <img v-if="project.icon && project.icon.startsWith('/')" :src="project.icon" :alt="project.title" class="w-14 h-14 object-contain" />
            <span v-else class="text-3xl">{{ project.icon || '🚀' }}</span>
          </div>
          <div>
            <h3 class="text-xl font-bold text-gray-900 mb-3 tracking-tight">{{ project.title }}</h3>
            <p class="text-gray-600 leading-relaxed mb-6 font-medium">
              {{ project.description }}
            </p>
            <div class="flex flex-wrap gap-2 mb-6">
              <span v-for="tag in project.tags" :key="tag" class="px-3 py-1 bg-[#f7f6f3] text-gray-700 text-xs font-bold rounded-full">
                {{ tag }}
              </span>
            </div>
            <router-link :to="`/portfolio/${project.id}`" class="inline-flex items-center text-[#D97757] font-bold hover:text-[#C4654A] transition-colors">
              View project <span class="ml-2 group-hover:translate-x-1 transition-transform">→</span>
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- Services -->
    <section id="services" class="py-24 bg-[#f7f6f3] border-t border-black/5">
      <div class="max-w-5xl mx-auto px-6">
        <div class="mb-12">
          <h2 class="text-sm font-bold uppercase tracking-widest text-gray-400 mb-4">Services</h2>
          <p class="font-display text-3xl sm:text-4xl font-extrabold tracking-tight text-gray-900">What I can build for you</p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="bg-white border border-black/5 rounded-2xl p-8 hover:shadow-lg transition-all duration-300">
            <div class="text-3xl mb-4">💬</div>
            <h3 class="text-lg font-bold text-gray-900 mb-2 tracking-tight">WhatsApp automation</h3>
            <p class="text-gray-600 leading-relaxed font-medium">Outreach campaigns, chatbots, and notification systems on the WhatsApp Business API. I've already built one — I can build yours.</p>
          </div>
          <div class="bg-white border border-black/5 rounded-2xl p-8 hover:shadow-lg transition-all duration-300">
            <div class="text-3xl mb-4">🤖</div>
            <h3 class="text-lg font-bold text-gray-900 mb-2 tracking-tight">AI agent integration</h3>
            <p class="text-gray-600 leading-relaxed font-medium">Connect your product to LLMs, build agentic workflows, wire up MCP servers, and ship AI features that work in production.</p>
          </div>
          <div class="bg-white border border-black/5 rounded-2xl p-8 hover:shadow-lg transition-all duration-300">
            <div class="text-3xl mb-4">🔌</div>
            <h3 class="text-lg font-bold text-gray-900 mb-2 tracking-tight">API & backend systems</h3>
            <p class="text-gray-600 leading-relaxed font-medium">Custom APIs, webhooks, and integrations between your tools. Clean, documented, and built to scale.</p>
          </div>
          <div class="bg-white border border-black/5 rounded-2xl p-8 hover:shadow-lg transition-all duration-300">
            <div class="text-3xl mb-4">🚀</div>
            <h3 class="text-lg font-bold text-gray-900 mb-2 tracking-tight">MVP development</h3>
            <p class="text-gray-600 leading-relaxed font-medium">Got an idea? I'll help you scope and ship a working product fast — no bloat, no over-engineering.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <div id="contact" class="py-24 px-6 max-w-5xl mx-auto">
      <div class="bg-[#111111] rounded-3xl p-10 sm:p-16 text-center relative overflow-hidden group">
        <div class="absolute inset-0 opacity-20 pointer-events-none group-hover:opacity-40 transition-opacity duration-700 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-white/20 via-[#111111]/0 to-transparent"></div>
        <div class="relative z-10">
          <h2 class="text-3xl sm:text-5xl font-extrabold text-white mb-6 tracking-tight">Let's build something together</h2>
          <p class="text-gray-400 text-lg sm:text-xl font-medium mb-10 max-w-2xl mx-auto">
            I'm currently available for freelance projects. If you need AI integration work done right, let's talk.
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <a href="mailto:you@email.com" class="px-8 py-4 bg-white text-black font-bold rounded-xl hover:bg-gray-200 transition-all shadow-xl hover:scale-105 text-base">
              Email me
            </a>
            <a href="https://twitter.com/yourhandle" class="px-8 py-4 bg-transparent text-white font-bold rounded-xl border border-white/20 hover:bg-white/10 transition-all text-base">
              Follow on X / Twitter
            </a>
          </div>
        </div>
      </div>
    </div>

    <div class="w-full bg-white border-t border-black/5">
      <footer class="max-w-7xl mx-auto px-8 lg:px-12 relative z-10 pt-16 pb-16 flex flex-col md:flex-row justify-between items-start gap-8 text-left">
        <div class="flex flex-col items-start gap-8">
          <!-- Socials -->
          <div class="flex items-center gap-5">
            <a href="https://twitter.com/yourhandle" target="_blank"
              class="text-black hover:text-gray-500 transition-all duration-300 transform hover:scale-110">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path
                  d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
              </svg>
            </a>
            <a href="https://github.com/yourhandle" target="_blank"
              class="text-black hover:text-gray-500 transition-all duration-300 transform hover:scale-110">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path
                  d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
              </svg>
            </a>
          </div>

          <div class="flex items-center gap-2">
            <span class="font-medium text-2xl text-black tracking-tight"
              style="font-family: 'Inter', system-ui, sans-serif;">Himansh Shivhare</span>
          </div>
          <p class="text-sm text-gray-500 max-w-xs leading-relaxed">
            Building AI integrations and scalable backend systems for startups and professionals.
          </p>
          <p class="text-xs text-black/30 font-medium">© 2026 Himansh Shivhare. Crafted with care.</p>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 gap-12 sm:gap-24 w-full md:w-auto">
          <div class="flex flex-col gap-4">
            <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Portfolio</h4>
            <a href="#projects" class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Projects</a>
            <a href="#services" class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Services</a>
          </div>
          <div class="flex flex-col gap-4">
            <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Connect</h4>
            <a href="mailto:you@email.com"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Email Me</a>
            <a href="https://twitter.com/yourhandle" target="_blank"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Twitter</a>
          </div>
          <div class="flex flex-col gap-4">
            <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Links</h4>
            <a href="https://github.com/yourhandle" target="_blank"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">GitHub</a>
          </div>
        </div>
      </footer>
    </div>
  </div>
</template>

<script setup>
import LogoBgAnimation from '@/components/landing/LogoBgAnimation.vue';
import { projects } from '@/data/projects';
</script>

<style scoped>
.font-display {
  font-family: 'Inter', system-ui, sans-serif;
}

.animate-gradient-x {
  background-size: 200% 200%;
  animation: gradient-x 3s ease infinite;
}

@keyframes gradient-x {
  0%, 100% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
}

.portfolio-container {
  font-family: 'Inter', system-ui, sans-serif;
}
</style>
