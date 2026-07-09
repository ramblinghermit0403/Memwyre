<template>
  <div class="force-light relative min-h-[100svh] bg-white text-text-primary transition-colors duration-300 font-sans overflow-x-hidden selection:bg-primary selection:text-white *:selection:bg-primary *:selection:text-white">
    <div class="pt-16 pb-24 sm:pt-24 sm:pb-32">
      <div id="pricing" class="max-w-5xl mx-auto px-6 sm:px-8 lg:px-12">
        <div class="text-center mb-16">
          <h2 class="text-sm font-bold uppercase tracking-widest text-text-muted mb-4">Pricing</h2>
          <h1 class="hero-serif text-4xl sm:text-5xl tracking-tight text-gray-900 leading-[1.1]">
            AI that works where <span class="italic font-medium">your team <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">works.</span></span>
          </h1>
          <p class="mt-4 text-lg text-text-secondary max-w-2xl mx-auto">
            Simple, transparent pricing for individuals and teams.
          </p>

          <!-- Command Installer Codeblock in Hero -->
          <div class="relative bg-zinc-50 border border-dashed border-zinc-200 rounded-none p-3.5 font-mono text-[11px] sm:text-xs text-zinc-600 flex items-center justify-between gap-3 max-w-sm mt-4 mx-auto select-none">
            <div class="flex items-center gap-1.5 overflow-x-auto whitespace-nowrap scrollbar-none select-all py-0.5">
              <span class="text-[#D97757] select-none font-bold">$</span>
              <span>npx -y install-memwyre</span>
            </div>
            <button 
              @click="copyCommand('npx -y install-memwyre')" 
              class="text-[#D97757] hover:text-[#C4654A] font-semibold text-[10px] sm:text-xs tracking-wider uppercase shrink-0 transition-colors cursor-pointer select-none"
            >
              {{ copiedText === 'npx -y install-memwyre' ? 'Copied' : 'Copy' }}
            </button>
          </div>
        </div>

        <div class="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-6 items-stretch">
          <!-- Free Plan -->
          <div class="rounded-3xl bg-white border border-black/5 p-8 sm:p-10 relative transition-all duration-500 hover:-translate-y-1 hover:shadow-lg">
            <div class="flex items-center gap-3 mb-4">
              <div class="text-xl font-bold text-gray-900">Free</div>
            </div>
            <div class="flex items-end gap-2 mb-3">
              <div class="text-4xl font-extrabold tracking-tight text-gray-900">$0</div>
              <div class="text-sm text-gray-500 mb-1">forever</div>
            </div>
            <p class="text-text-secondary mb-6">A great way to get started with building your persistent AI memory layer.</p>

            <router-link to="/signup"
              class="inline-flex w-full items-center justify-center rounded bg-gray-50 text-gray-900 border border-gray-200 px-4 py-3.5 text-sm font-bold hover:bg-gray-100 transition-all duration-300 hover:scale-[1.02]">
              Get Started for Free
            </router-link>

            <ul class="mt-8 space-y-3 text-sm text-text-secondary">
              <li class="flex items-start gap-3">
                <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Up to 50 memories
              </li>
              <li class="flex items-start gap-3">
                <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Up to 10 document uploads
              </li>
              <li class="flex items-start gap-3">
                <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Standard AI token budget
              </li>
              <li class="flex items-start gap-3">
                <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                IDE Integration (MCP)
              </li>
              <li class="flex items-start gap-3">
                <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Community Support
              </li>
            </ul>
          </div>

          <!-- Pro (Recommended) -->
          <div class="rounded-3xl bg-white border border-black/5 p-8 sm:p-10 relative shadow-[0_8px_30px_rgb(0,0,0,0.06)] transition-all duration-500 hover:-translate-y-2 hover:shadow-[0_20px_40px_rgb(0,0,0,0.12)]">
            <div class="flex items-center gap-3 mb-4">
              <div class="text-xl font-bold text-gray-900">Pro</div>
              <span class="text-xs font-bold px-3 py-1 rounded-full bg-gradient-to-r from-[#D97757] to-[#FF9A7B] text-white shadow-sm">
                Recommended
              </span>
            </div>
            <div class="flex items-end gap-2 mb-3">
              <div class="text-4xl font-extrabold tracking-tight text-gray-900">$12</div>
              <div class="text-sm text-gray-500 mb-1">/month</div>
            </div>
            <p class="text-text-secondary mb-6">Everything in Free, plus unlimited storage and priority features.
            </p>

            <router-link to="/signup"
              class="inline-flex w-full items-center justify-center rounded bg-gray-900 text-white px-4 py-3.5 text-sm font-bold shadow-[0_4px_14px_0_rgb(0,0,0,0.2)] hover:bg-gray-800 transition-all duration-300 hover:scale-[1.02]">
              Get Started with Pro Memory
            </router-link>

            <div class="mt-6 flex flex-wrap items-center gap-2">
              <span class="text-xs font-semibold uppercase tracking-widest text-text-muted mr-2">Integrations</span>
              <img src="@/assets/vscode.svg" alt="VS Code" class="w-5 h-5" title="VS Code" />
              <img src="@/assets/google-drive.svg" alt="Google Drive" class="w-5 h-5" title="Google Drive" />
              <img src="@/assets/notion-svgrepo-com.svg" alt="Notion" class="w-5 h-5" title="Notion" />
              <img src="@/assets/claude-color.svg" alt="Claude Desktop" class="w-5 h-5" title="Claude Desktop" />
              <img src="@/assets/claudecode-color.svg" alt="Claude Code" class="w-5 h-5" title="Claude Code" />
              <img src="@/assets/openclaw-color.svg" alt="OpenClaw" class="w-5 h-5" title="OpenClaw" />
            </div>

            <ul class="mt-4 space-y-3 text-sm text-text-secondary">
              <li class="flex items-start gap-3">
                <svg class="w-5 h-5 text-[#D97757] shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24"
                  stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Unlimited memories &amp; documents
              </li>
              <li class="flex items-start gap-3">
                <svg class="w-5 h-5 text-[#D97757] shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24"
                  stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Google Drive &amp; Notion sync
              </li>
              <li class="flex items-start gap-3">
                <svg class="w-5 h-5 text-[#D97757] shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24"
                  stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Claude Code, OpenCode &amp; OpenClaw plugins
              </li>
              <li class="flex items-start gap-3">
                <svg class="w-5 h-5 text-[#D97757] shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24"
                  stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Browser Extension &amp; MCP IDE Server
              </li>
              <li class="flex items-start gap-3">
                <svg class="w-5 h-5 text-[#D97757] shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24"
                  stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Extended daily AI chat quota &amp; support
              </li>
            </ul>
          </div>

          <!-- Enterprise -->
          <div class="rounded-3xl bg-white border border-black/5 p-8 sm:p-10 relative transition-all duration-500 hover:-translate-y-1 hover:shadow-lg">
            <div class="flex items-center gap-3 mb-4">
              <div class="text-xl font-bold text-gray-900">Enterprise</div>
            </div>
            <div class="flex items-end gap-2 mb-3">
              <div class="text-4xl font-extrabold tracking-tight text-gray-900">Custom</div>
            </div>
            <p class="text-text-secondary mb-6">Tailored deployments for teams that need dedicated infrastructure, SSO, and volume pricing.</p>

            <a href="mailto:shivharehimansh@gmail.com?subject=Memwyre%20Enterprise%20Inquiry"
              class="inline-flex w-full items-center justify-center rounded bg-gray-50 text-gray-900 border border-gray-200 px-4 py-3.5 text-sm font-bold hover:bg-gray-100 transition-all duration-300 hover:scale-[1.02]">
              Contact Sales
            </a>

            <ul class="mt-8 space-y-3 text-sm text-text-secondary">
              <li class="flex items-start gap-3">
                <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Everything in Pro
              </li>
              <li class="flex items-start gap-3">
                <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Dedicated infrastructure
              </li>
              <li class="flex items-start gap-3">
                <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                SSO &amp; team management
              </li>
              <li class="flex items-start gap-3">
                <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Volume pricing
              </li>
              <li class="flex items-start gap-3">
                <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Custom integrations &amp; SLA
              </li>
              <li class="flex items-start gap-3">
                <svg class="w-5 h-5 text-gray-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Dedicated support
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- Final CTA Section: Memory and Personality -->
    <div
      class="pt-20 pb-10 sm:pt-28 sm:pb-16 bg-white text-center px-6 relative overflow-hidden border-t border-black/5">
      <!-- Logo-masked numeric background (INVERTED for white bg) -->
      <LogoBgAnimation class="absolute inset-0 z-0 opacity-[0.08]" :invert="true" />

      <div class="max-w-5xl mx-auto relative z-10">
        <h2 class="font-display text-5xl sm:text-7xl lg:text-[7rem] font-medium tracking-tight mb-10 leading-[0.95]">
          <span
            class="bg-clip-text text-transparent bg-[repeating-linear-gradient(to_bottom,#111,#111_6px,white_6px,white_9px)]">
            The Second Brain
          </span><br />
          <span class="text-black">
            For Your AI.
          </span>
        </h2>

        <div class="flex flex-col sm:flex-row items-center justify-center gap-5">
          <router-link to="/signup"
            class="w-full sm:w-auto px-10 py-4 bg-black text-white font-bold rounded hover:bg-gray-800 transition-all duration-300 shadow-xl hover:scale-105">
            Get Started
          </router-link>
          <router-link to="/pricing"
            class="w-full sm:w-auto px-10 py-4 bg-white text-black font-bold rounded border border-black/10 hover:bg-black/5 transition-all duration-300 hover:border-black/20">
            Compare Plans
          </router-link>
        </div>
      </div>

      <div
        class="max-w-5xl mx-auto px-8 lg:px-12 mt-12 relative z-10 border-t border-black/5 pt-10 flex flex-col md:flex-row justify-between items-start gap-8 text-left">
        <div class="flex flex-col items-start gap-8">
          <!-- Socials -->
          <div class="flex items-center gap-5">
            <a v-if="false" href="https://linkedin.com/company/memwyre" target="_blank"
              class="text-black hover:text-gray-500 transition-all duration-300 transform hover:scale-110">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path
                  d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" />
              </svg>
            </a>
            <a href="https://twitter.com/Memwyre" target="_blank"
              class="text-black hover:text-gray-500 transition-all duration-300 transform hover:scale-110">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path
                  d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
              </svg>
            </a>
            <a href="https://github.com/ramblinghermit0403/Memwyre" target="_blank"
              class="text-black hover:text-gray-500 transition-all duration-300 transform hover:scale-110">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path
                  d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
              </svg>
            </a>
          </div>

          <div class="flex items-center gap-2">
            <img src="/image.svg" alt="Memwyre" class="w-6 h-6 rounded" />
            <span class="font-medium text-2xl text-black tracking-tight"
              style="font-family: 'Inter', system-ui, sans-serif;">Memwyre</span>
          </div>
          <p class="text-sm text-gray-500 max-w-xs leading-relaxed">
            Building the unified memory layer for the next generation of AI agents and professionals.
          </p>
          <p class="text-xs text-black/30 font-medium">© 2026 Memwyre. Crafted for clarity.</p>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-12 sm:gap-16 w-full md:w-auto">
          <div class="flex flex-col gap-4">
            <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Product</h4>
            <router-link to="/#features"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Features</router-link>
            <router-link to="/pricing" class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Pricing</router-link>
            <router-link to="/#ecosystem"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Ecosystem</router-link>
          </div>
          <div class="flex flex-col gap-4">
            <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Products</h4>
            <router-link to="/extension"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Chrome Extension</router-link>
            <router-link to="/mcp"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">MCP</router-link>
            <router-link to="/plugins"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Plugins</router-link>
          </div>
          <div class="flex flex-col gap-4">
            <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Support</h4>
            <a href="mailto:shivharehimansh@gmail.com"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Contact Us</a>
            <a href="https://x.com/Memwyre" target="_blank"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Twitter</a>
          </div>
          <div class="flex flex-col gap-4">
            <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Legal</h4>
            <router-link to="/privacy-policy"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Privacy</router-link>
            <router-link to="/terms"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Terms</router-link>
          </div>
        </div>
      </div>
    </div>


  </div>
</template>

<script setup>
import { ref } from 'vue';
import LogoBgAnimation from '@/components/landing/LogoBgAnimation.vue';

const copiedText = ref('');
const copyCommand = (cmd) => {
  navigator.clipboard.writeText(cmd);
  copiedText.value = cmd;
  setTimeout(() => {
    copiedText.value = '';
  }, 2000);
};
</script>

<style scoped>
.force-light,
.force-light * {
  --bg-app: #FAF6F0;
  --bg-surface: #FFFFFF;
  --bg-surface-2: #F7F6F3;
  --bg-elevated: #FFFFFF;
  --primary: #D97757;
  --primary-600: #C4654A;
  --accent: #D97757;
  --accent-600: #C4654A;
  --success: #059669;
  --warning: #D97706;
  --danger: #DC2626;
  --info: #D97757;
  --text-primary: #191919;
  --text-secondary: #37352F99;
  --text-muted: #37352F66;
  --border: rgba(25, 25, 25, 0.06);
  --divider-strong: rgba(25, 25, 25, 0.09);
  --backdrop: rgba(0, 0, 0, 0.4);
  --input-bg: #FFFFFF;
  --input-border: rgba(25, 25, 25, 0.08);
  --placeholder: #37352F66;
  color-scheme: light;
}
</style>
