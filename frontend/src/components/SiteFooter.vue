<template>
  <footer class="w-full bg-white relative overflow-hidden mt-12 sm:mt-16">
    <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 border-t border-black/5 pt-10 pb-12 flex flex-col md:flex-row justify-between items-start gap-8 text-left">
      <div class="flex flex-col items-start gap-8">
        <!-- Socials -->
        <div class="flex items-center gap-5">
          <a href="https://twitter.com/Memwyre" target="_blank"
            aria-label="Follow Memwyre on X (Twitter)"
            class="text-black hover:text-gray-500 transition-all duration-300 transform hover:scale-110">
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path
                d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
            </svg>
          </a>
          <a href="https://github.com/ramblinghermit0403/Memwyre" target="_blank"
            aria-label="Visit Memwyre on GitHub"
            class="text-black hover:text-gray-500 transition-all duration-300 transform hover:scale-110">
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path
                d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
            </svg>
          </a>
        </div>

        <div class="flex items-center gap-2">
          <img src="/logo.png" alt="Memwyre" class="h-[35px] w-auto dark:invert" />
        </div>
        <p class="text-sm text-gray-500 max-w-xs leading-relaxed">
          Building the unified memory layer for the next generation of AI agents and professionals.
        </p>
        <p class="text-xs text-black/30 font-medium">© 2026 Memwyre. Crafted for clarity.</p>
      </div>

      <div class="grid grid-cols-2 md:grid-cols-5 gap-12 sm:gap-16 w-full md:w-auto text-left">
        <div class="flex flex-col gap-4">
          <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Core Product</h4>
          <router-link to="/#features"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">Features</router-link>
          <router-link to="/pricing/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">Pricing</router-link>
          <router-link to="/use-cases/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">Use Cases</router-link>
          <router-link to="/extension/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">Extension</router-link>
        </div>
        <div class="flex flex-col gap-4">
          <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Integrations</h4>
          <router-link to="/mcp/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">MCP Server</router-link>
          <router-link to="/plugins/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">IDE Plugins</router-link>
          <router-link to="/chatgpt-memory/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">ChatGPT</router-link>
          <router-link to="/claude-memory/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">Claude</router-link>
          <router-link to="/cursor-memory/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">Cursor AI</router-link>
          <router-link to="/mcp-memory/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">Universal MCP</router-link>
        </div>
        <div class="flex flex-col gap-4">
          <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Research</h4>
          <router-link to="/research/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">Research Hub</router-link>
          <router-link to="/ai-memory-benchmark-locomo/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">LoCoMo Report</router-link>
          <router-link to="/research/what-is-ai-memory/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">What is Memory?</router-link>
          <router-link to="/blog/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">Blog</router-link>
        </div>
        <div class="flex flex-col gap-4">
          <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Comparisons</h4>
          <router-link to="/memwyre-vs-mem0/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">vs Mem0</router-link>
          <router-link to="/memwyre-vs-supermemory/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">vs Supermemory</router-link>
          <router-link to="/memwyre-vs-zep/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">vs Zep</router-link>
        </div>
        <div class="flex flex-col gap-4">
          <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Support &amp; Legal</h4>
           <a href="https://docs.memwyre.tech" target="_blank"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">Documentation</a>
          <router-link to="/contact/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">Contact Us</router-link>
          <router-link to="/privacy-policy/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">Privacy Policy</router-link>
          <router-link to="/terms/"
            class="text-sm text-black hover:text-[#D97757] transition-colors font-medium">Terms of Service</router-link>
        </div>
      </div>
    </div>
  </footer>
</template>
