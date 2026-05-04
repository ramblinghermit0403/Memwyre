<template>
  <div class="terms-view force-light bg-white text-gray-900 min-h-screen font-sans selection:bg-primary selection:text-white transition-colors duration-300 overflow-x-hidden">
    <div class="py-24 px-4 sm:px-6 lg:px-8 max-w-6xl mx-auto flex flex-col md:flex-row gap-12 items-start">
    
      
      <!-- Sidebar Navigation -->
      <aside class="w-full md:w-64 shrink-0 sticky top-24 hidden md:block">
        <div class="mb-8">
          <router-link to="/" class="inline-flex items-center space-x-3 group">
            <img src="/image.svg" alt="Memwyre" class="w-10 h-10 rounded-xl group-hover:scale-105 transition-transform duration-300" />
            <span class="text-2xl font-bold tracking-tight text-gray-900 group-hover:text-primary transition-colors">
              Memwyre
            </span>
          </router-link>
        </div>
        
        <nav class="space-y-1 border-l-2 border-primary/10 pl-4">
          <a href="#acceptance" class="block py-2 text-sm font-medium text-gray-600 hover:text-primary transition-colors">Acceptance of Terms</a>
          <a href="#description" class="block py-2 text-sm font-medium text-gray-600 hover:text-primary transition-colors">Description of Service</a>
          <a href="#accounts" class="block py-2 text-sm font-medium text-gray-600 hover:text-primary transition-colors">User Accounts</a>
          <a href="#billing" class="block py-2 text-sm font-medium text-gray-600 hover:text-primary transition-colors">Subscriptions & Billing</a>
          <a href="#acceptable-use" class="block py-2 text-sm font-medium text-gray-600 hover:text-primary transition-colors">Acceptable Use Policy</a>
          <a href="#intellectual-property" class="block py-2 text-sm font-medium text-gray-600 hover:text-primary transition-colors">Intellectual Property</a>
          <a href="#limitation" class="block py-2 text-sm font-medium text-gray-600 hover:text-primary transition-colors">Limitation of Liability</a>
        </nav>
      </aside>

      <!-- Main Content -->
      <main class="flex-1 bg-gray-50/50 rounded-3xl shadow-xl border border-primary/10 p-8 sm:p-12 w-full">
        <!-- Mobile Header -->
        <div class="mb-8 md:hidden text-center">
          <router-link to="/" class="inline-flex items-center justify-center space-x-3 group mb-6">
            <img src="/image.svg" alt="Memwyre" class="w-10 h-10 rounded-xl" />
            <span class="text-2xl font-bold tracking-tight text-gray-900">Memwyre</span>
          </router-link>
        </div>

        <div class="mb-12 border-b border-primary/10 pb-8">
          <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight mb-4 text-gray-900">Terms of Service</h1>
          <p class="text-primary font-bold uppercase tracking-widest text-sm">Last Updated: March 3, 2026</p>
        </div>

        <div class="prose prose-lg max-w-none text-gray-600 prose-headings:text-gray-900 prose-a:text-primary hover:prose-a:text-primary-600 prose-strong:text-gray-900 prose-headings:scroll-mt-32">
          
          <h2 id="acceptance" class="text-2xl font-bold mb-6">Acceptance of Terms</h2>
          <p class="mb-6 leading-relaxed">
            By registering for an account, accessing the Memwyre web application, downloading the Chrome Extension, or utilizing the MCP Server (collectively, the "Service"), you agree to be bound by these Terms of Service. If you do not agree to these terms, please do not use the Service.
          </p>

          <h2 id="description" class="text-2xl font-bold mt-12 mb-6">Description of Service</h2>
          <p class="mb-6 leading-relaxed">
            Memwyre is an AI context aggregator and "second brain" platform. It allows users to save text snippets, links, and chat transcripts into a unified knowledge base, process those memories into searchable vectors, and interact with Large Language Models (LLMs) using that knowledge as context.
          </p>

          <h2 id="accounts" class="text-2xl font-bold mt-12 mb-6">User Accounts & Security</h2>
          <p class="mb-4 leading-relaxed">
            To use the Service, you must authenticate via supported providers (e.g., Google OAuth). You are responsible for:
          </p>
          <ul class="list-disc pl-6 space-y-3 mb-6 text-gray-600">
            <li>Maintaining the security of your authentication accounts.</li>
            <li>All activity that occurs within your Memwyre Workspace.</li>
            <li>Ensuring that the data you save to Memwyre using our extensions or MCP servers does not violate third-party terms or local laws.</li>
          </ul>

          <h2 id="billing" class="text-2xl font-bold mt-12 mb-6">Subscriptions, Limits, & Billing</h2>
          <div class="bg-surface-2 rounded-2xl p-8 mb-8 border border-primary/10 shadow-sm">
            <h3 class="text-xl font-bold mb-4 flex items-center text-gray-900">
              <svg class="w-6 h-6 mr-3 text-primary shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" /></svg>
              Billing Terms
            </h3>
            <ul class="list-disc pl-6 space-y-3 mb-6 text-gray-600">
              <li>Memwyre operates on a subscription model (e.g., the Pro Plan). Billing constitutes a recurring payment charged securely via our payment provider (Stripe).</li>
              <li>You may cancel your subscription at any time via the Billing dashboard. Access will continue until the end of the current paid billing cycle.</li>
              <li>Except where mandated by law, subscription fees are non-refundable.</li>
            </ul>

            <h3 class="text-xl font-bold mb-4 mt-8 flex items-center text-gray-900">
              <svg class="w-6 h-6 mr-3 text-primary shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
              Usage Limits (Fair Use)
            </h3>
            <ul class="list-disc pl-6 space-y-3 text-gray-600">
              <li>To ensure platform stability for all users, Pro Plans are subject to soft limits. This currently includes a standard daily budget of <strong>100,000 AI Model Tokens</strong> and over <strong>1,000,000 Token Storage capacity</strong> for your Brain Vault.</li>
              <li>Memwyre reserves the right to rate-limit or pause accounts that consistently exceed these budgets in a manner deemed abusive or disruptive to the service infrastructure.</li>
            </ul>
          </div>

          <h2 id="acceptable-use" class="text-2xl font-bold mt-12 mb-6">Acceptable Use Policy</h2>
          <p class="mb-4 leading-relaxed">
            You agree not to misuse the Memwyre service. Specifically, you will not:
          </p>
          <ul class="list-disc pl-6 space-y-3 mb-6 text-gray-600">
            <li>Reverse engineer, decompile, or attempt to extract the source code or inner workings of the Memwyre web application, API, or Extension.</li>
            <li>Use the API or MCP Servers for automated scraping, mass data harvesting, or any programmatic abuse outside of the intended integration use cases.</li>
            <li>Store illegal content, malware, or highly sensitive regulated data (such as HIPAA-protected health information) as Memwyre is not compliant for such specialized regulatory storage.</li>
          </ul>

          <h2 id="intellectual-property" class="text-2xl font-bold mt-12 mb-6">Intellectual Property</h2>
          <p class="mb-6 leading-relaxed">
            <strong>Your Data:</strong> You retain full ownership of all text, links, and documents you input into the Memwyre Service. Memwyre claims no ownership rights over your personal Brain Vault context.
          </p>
          <p class="mb-6 leading-relaxed">
            <strong>Memwyre IP:</strong> The Service, including its design, logos, UI/UX, database schemas, API logic, and the Memwyre MCP protocol integrations, are the exclusive intellectual property of Memwyre and its creators.
          </p>

          <h2 id="limitation" class="text-2xl font-bold mt-12 mb-6">Limitation of Liability</h2>
          <p class="mb-6 leading-relaxed italic border-l-4 border-primary/20 pl-4 py-2">
            The Service is provided "AS IS" and on an "AS AVAILABLE" basis. We make no warranties regarding the accuracy of AI-generated responses, the permanent availability of specific Third-Party LLM models, or the absolute prevention of data loss. In no event shall Memwyre be liable for indirect, incidental, special, consequential, or punitive damages arising from your use of the Service.
          </p>
        </div>
        
      </main>
    </div>

    <!-- Final CTA Section: Memory and Personality -->
    <div
      class="pt-20 pb-10 sm:pt-28 sm:pb-16 bg-white text-center px-6 relative overflow-hidden border-t border-black/5">
      <!-- Logo-masked numeric background (INVERTED for white bg) -->
      <LogoBgAnimation class="absolute inset-0 z-0 opacity-[0.08]" :invert="true" />

      <div class="max-w-7xl mx-auto relative z-10">
        <h2 class="font-display text-5xl sm:text-7xl lg:text-[7rem] font-medium tracking-tight mb-10 leading-[0.95]">
          <span
            class="bg-clip-text text-transparent bg-[repeating-linear-gradient(to_bottom,#111,#111_6px,white_6px,white_9px)]">
            The Second Brain
          </span><br />
          <span class="text-[#9575CD]">
            For Your AI.
          </span>
        </h2>
        <p class="text-gray-600 text-xl sm:text-2xl mb-14 max-w-3xl mx-auto font-medium leading-relaxed">
          A persistent knowledge vault that works everywhere you use AI.
        </p>
        <div class="flex flex-col sm:flex-row items-center justify-center gap-5">
          <router-link to="/signup"
            class="w-full sm:w-auto px-10 py-4 bg-black text-white font-bold rounded-xl hover:bg-gray-800 transition-all duration-300 shadow-xl hover:scale-105">
            Start Building Your Brain
          </router-link>
          <router-link to="/pricing"
            class="w-full sm:w-auto px-10 py-4 bg-white text-black font-bold rounded-xl border border-black/10 hover:bg-black/5 transition-all duration-300 hover:border-black/20">
            Pricing
          </router-link>
        </div>
      </div>

      <div
        class="max-w-7xl mx-auto px-8 lg:px-12 mt-12 relative z-10 border-t border-black/5 pt-10 flex flex-col md:flex-row justify-between items-start gap-8 text-left">
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
            <a href="https://github.com/ramblinghermit0403/memwyer-prod" target="_blank"
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

        <div class="grid grid-cols-2 sm:grid-cols-3 gap-12 sm:gap-24 w-full md:w-auto">
          <div class="flex flex-col gap-4">
            <h4 class="text-xs font-bold uppercase tracking-widest text-black/40">Product</h4>
            <a href="/#features"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Features</a>
            <a href="/pricing" class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Pricing</a>
            <a href="/#ecosystem"
              class="text-sm text-black hover:text-gray-500 transition-colors font-medium">Ecosystem</a>
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
import { onMounted } from 'vue';
import LogoBgAnimation from '@/components/landing/LogoBgAnimation.vue';

onMounted(() => {
  window.scrollTo(0, 0);
});
</script>

<style scoped>
html {
  scroll-behavior: smooth;
}
aside {
  height: calc(100vh - 120px);
}
</style>


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
