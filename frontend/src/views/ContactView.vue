<template>
  <div class="relative min-h-screen bg-white dark:bg-[#0c0c0c] pt-28 pb-20 overflow-x-hidden font-sans text-gray-900 dark:text-gray-100 transition-colors duration-300">
    <!-- Grid Blueprint background line effects (consistent with branding) -->
    <div class="absolute inset-0 pointer-events-none opacity-[0.03] dark:opacity-[0.05]">
      <div class="absolute inset-0 bg-[linear-gradient(to_right,#808080_1px,transparent_1px),linear-gradient(to_bottom,#808080_1px,transparent_1px)] bg-[size:40px_40px]"></div>
    </div>

    <!-- Global Vertical Grid Lines -->
    <div class="hidden lg:block absolute top-0 bottom-0 left-6 sm:left-8 lg:left-[calc(50%-640px)] w-px bg-gray-300/80 dark:bg-gray-800/60 pointer-events-none select-none z-30"></div>
    <div class="hidden lg:block absolute top-0 bottom-0 right-6 sm:right-8 lg:right-[calc(50%-640px)] w-px bg-gray-300/80 dark:bg-gray-800/60 pointer-events-none select-none z-30"></div>

    <div class="relative max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 z-10">
      <!-- Breadcrumb & Header -->
      <div class="mb-16 text-left">
        <div class="text-xs tracking-wider uppercase font-bold font-mono text-gray-400 dark:text-gray-500 mb-6 px-1">
          / CONNECT WITH US
        </div>
        <h1 class="hero-serif text-4xl md:text-5xl lg:text-6xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] dark:text-white mb-6">
          Get in Touch <br />
          <span class="italic font-medium">We'd love to hear <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">from you.</span></span>
        </h1>
        <p class="text-base sm:text-lg text-[#4B5563] dark:text-gray-400 max-w-2xl font-normal leading-relaxed">
          Have questions about pricing, setup, or custom enterprise deployments? Fill out the form or reach out directly to our developer team.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 sm:gap-16 items-start">
        <!-- Left Side: Contact details -->
        <div class="lg:col-span-5 space-y-10 text-left">
          
          <!-- Email Widget -->
          <div class="border border-dashed border-gray-300 dark:border-zinc-800 p-6 bg-gray-50/50 dark:bg-[#111] rounded-none">
            <h3 class="text-xs font-bold uppercase tracking-widest text-[#D97757] mb-3">Direct Contact</h3>
            <p class="text-sm text-gray-500 dark:text-gray-400 mb-4">
              Write to us anytime. We aim to reply to all developer inquiries within 12 hours.
            </p>
            <div class="flex items-center justify-between gap-3 p-3 bg-white dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded-none font-mono text-sm">
              <span class="text-gray-800 dark:text-gray-200 select-all truncate">himansh@memwyre.tech</span>
              <button 
                @click="copyEmail" 
                class="text-[#D97757] hover:text-[#C4654A] font-semibold text-xs tracking-wider uppercase shrink-0 transition-colors cursor-pointer select-none"
              >
                {{ emailCopied ? 'Copied' : 'Copy' }}
              </button>
            </div>
            <div class="mt-4">
              <a href="mailto:himansh@memwyre.tech" class="text-xs font-bold text-[#D97757] hover:underline inline-flex items-center gap-1">
                Open in mail client
                <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
              </a>
            </div>
          </div>

          <!-- Other Channels -->
          <div class="space-y-6">
            <div>
              <h4 class="text-xs font-bold uppercase tracking-widest text-gray-400 dark:text-gray-500 mb-2">Developer Channels</h4>
              <ul class="space-y-3">
                <li class="flex items-center gap-2">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                  <a href="https://github.com/ramblinghermit0403/Memwyre" target="_blank" class="text-sm font-medium hover:text-[#D97757] underline transition-colors">GitHub Repository</a>
                </li>
                <li class="flex items-center gap-2">
                  <span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span>
                  <a href="https://twitter.com/Memwyre" target="_blank" class="text-sm font-medium hover:text-[#D97757] underline transition-colors">Follow us on X (Twitter)</a>
                </li>
              </ul>
            </div>

            <div>
              <h4 class="text-xs font-bold uppercase tracking-widest text-gray-400 dark:text-gray-500 mb-2">Security & Terms</h4>
              <p class="text-xs text-gray-500 leading-relaxed max-w-sm">
                Before sending context-sensitive inquiries, feel free to read our <router-link to="/privacy-policy" class="underline hover:text-[#D97757]">Privacy Policy</router-link> and details on data retention.
              </p>
            </div>
          </div>
        </div>

        <!-- Right Side: Contact Form / Success Message -->
        <div class="lg:col-span-7">
          <transition name="fade-slide" mode="out-in">
            <!-- Form State -->
            <div v-if="!submitted" class="border border-gray-200 dark:border-zinc-800 p-8 sm:p-10 bg-white dark:bg-[#111] rounded-none shadow-sm text-left">
              <h2 class="text-xl font-bold mb-6 text-gray-900 dark:text-white">Send a Message</h2>
              <form @submit.prevent="handleSubmit" class="space-y-6">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                  <div>
                    <label for="name" class="block text-xs font-bold uppercase tracking-wider text-gray-500 dark:text-gray-400 mb-2">Your Name</label>
                    <input 
                      type="text" 
                      id="name" 
                      v-model="form.name" 
                      required 
                      class="w-full px-4 py-3 bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded-none text-sm focus:outline-none focus:border-[#D97757] dark:focus:border-[#D97757] transition-colors"
                      placeholder="Jane Doe"
                    />
                  </div>
                  <div>
                    <label for="email" class="block text-xs font-bold uppercase tracking-wider text-gray-500 dark:text-gray-400 mb-2">Email Address</label>
                    <input 
                      type="email" 
                      id="email" 
                      v-model="form.email" 
                      required 
                      class="w-full px-4 py-3 bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded-none text-sm focus:outline-none focus:border-[#D97757] dark:focus:border-[#D97757] transition-colors"
                      placeholder="jane@company.com"
                    />
                  </div>
                </div>

                <div>
                  <label for="subject" class="block text-xs font-bold uppercase tracking-wider text-gray-500 dark:text-gray-400 mb-2">Subject</label>
                  <input 
                    type="text" 
                    id="subject" 
                    v-model="form.subject" 
                    required 
                    class="w-full px-4 py-3 bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded-none text-sm focus:outline-none focus:border-[#D97757] dark:focus:border-[#D97757] transition-colors"
                    placeholder="MCP server configuration query"
                  />
                </div>

                <div>
                  <label for="message" class="block text-xs font-bold uppercase tracking-wider text-gray-500 dark:text-gray-400 mb-2">Message</label>
                  <textarea 
                    id="message" 
                    v-model="form.message" 
                    required 
                    rows="5"
                    class="w-full px-4 py-3 bg-gray-50 dark:bg-zinc-900 border border-gray-200 dark:border-zinc-800 rounded-none text-sm focus:outline-none focus:border-[#D97757] dark:focus:border-[#D97757] transition-colors resize-none"
                    placeholder="Write details of your query here..."
                  ></textarea>
                </div>

                <div>
                  <button 
                    type="submit" 
                    :disabled="sending"
                    class="w-full py-3.5 bg-[#D97757] hover:bg-[#c05c3d] disabled:bg-gray-400 disabled:cursor-not-allowed text-white font-semibold rounded-none transition-colors text-sm uppercase tracking-wider shadow-sm flex items-center justify-center gap-2"
                  >
                    <span>{{ sending ? 'Sending Message...' : 'Submit Message' }}</span>
                    <svg v-if="!sending" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                    </svg>
                  </button>
                </div>
              </form>
            </div>

            <!-- Success State Card -->
            <div v-else class="border border-green-200 dark:border-green-950 p-8 sm:p-12 bg-green-50/20 dark:bg-green-950/10 rounded-none text-center">
              <div class="w-12 h-12 bg-green-100 dark:bg-green-900/50 text-green-600 dark:text-green-400 rounded-full flex items-center justify-center mx-auto mb-6">
                <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <h2 class="text-2xl font-bold mb-3 text-gray-900 dark:text-white">Message Sent!</h2>
              <p class="text-sm text-gray-600 dark:text-gray-400 max-w-md mx-auto mb-8">
                Thank you for contacting us, {{ form.name }}. We have received your query about "{{ form.subject }}" and will get back to you shortly at {{ form.email }}.
              </p>
              <button 
                @click="resetForm" 
                class="px-6 py-2.5 border border-[#D97757] text-[#D97757] hover:bg-[#D97757] hover:text-white transition-colors text-sm font-semibold rounded-none"
              >
                Send another message
              </button>
            </div>
          </transition>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const emailCopied = ref(false);
const submitted = ref(false);
const sending = ref(false);

const form = ref({
  name: '',
  email: '',
  subject: '',
  message: ''
});

const copyEmail = async () => {
  try {
    await navigator.clipboard.writeText('himansh@memwyre.tech');
    emailCopied.value = true;
    setTimeout(() => {
      emailCopied.value = false;
    }, 2000);
  } catch (err) {
    console.error('Failed to copy email:', err);
  }
};

const handleSubmit = () => {
  sending.value = true;
  // Simulate API submit latency
  setTimeout(() => {
    sending.value = false;
    submitted.value = true;
  }, 1000);
};

const resetForm = () => {
  form.value = {
    name: '',
    email: '',
    subject: '',
    message: ''
  };
  submitted.value = false;
};
</script>

<style scoped>
.hero-serif {
  font-family: 'DM Serif Text', serif;
}

.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.3s ease;
}
.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(10px);
}
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
