<template>
  <div class="relative min-h-screen bg-white dark:bg-black text-black dark:text-white transition-colors duration-300 font-sans selection:bg-black selection:text-white dark:selection:bg-white dark:selection:text-black overflow-x-hidden">

    
    <!-- Hero Video Background -->
    <!-- Hero Video Background -->
    <div class="absolute top-0 right-[-5%] w-full lg:w-[60%] h-[800px] z-0 pointer-events-none overflow-hidden">
        <video 
            src="/hero.mp4" 
            autoplay 
            muted 
            playsinline
            class="w-full h-full object-cover opacity-100 dark:opacity-100"
        ></video>
        <!-- Gradients for seamless blend -->
        <div class="absolute inset-0 bg-gradient-to-l from-transparent via-transparent to-white dark:to-black"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-white dark:to-black"></div>
    </div>

    <!-- Hero Section -->
    <div class="relative z-10 pt-32 pb-12 lg:pt-40 lg:pb-24 px-6 lg:px-8 max-w-7xl mx-auto">
      <div class="flex flex-col items-start text-left">
        <!-- Hero Content -->
        <div class="max-w-4xl">
            <h1 class="text-6xl lg:text-8xl font-extrabold tracking-tighter leading-[0.9] text-black dark:text-white mb-8">
            Your Second Brain,<br>
            <span class="bg-black text-white dark:bg-white dark:text-black px-1 lg:px-4 leading-normal">Supercharged.</span>
            </h1>
            <p class="text-xl lg:text-2xl text-gray-500 dark:text-gray-400 leading-relaxed mb-12 max-w-2xl">
            Capture thoughts, ingest documents, and chat with your personal knowledge base. Secure, private, and minimal.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-start">
            <router-link to="/register" class="px-8 py-4 bg-black dark:bg-white text-white dark:text-black text-lg font-bold rounded-full hover:translate-y-[-2px] transition-transform duration-300 flex items-center justify-center gap-2">
                Start Building
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" /></svg>
            </router-link>
            <a href="#features" class="px-8 py-4 border border-gray-200 dark:border-gray-800 text-black dark:text-white text-lg font-bold rounded-full hover:bg-gray-50 dark:hover:bg-gray-900 transition-colors flex items-center justify-center">
                How it works
            </a>
            </div>
        </div>
      </div>
    </div>

    <!-- Features Grid -->
    <div id="features" class="py-16 px-6 lg:px-8 max-w-7xl mx-auto">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-x-8 gap-y-16">
        <div class="group">
          <div class="w-12 h-12 flex items-center justify-center border border-gray-200 dark:border-gray-800 rounded-xl mb-6 group-hover:bg-black group-hover:text-white dark:group-hover:bg-white dark:group-hover:text-black transition-colors duration-300">
             <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" /></svg>
          </div>
          <h3 class="text-2xl font-bold mb-3">Memory Map</h3>
          <p class="text-gray-500 dark:text-gray-400 leading-relaxed">
            Visualize connections between your thoughts. Our intelligent tagging system links related concepts automatically, revealing hidden patterns.
          </p>
        </div>

        <div class="group">
          <div class="w-12 h-12 flex items-center justify-center border border-gray-200 dark:border-gray-800 rounded-xl mb-6 group-hover:bg-black group-hover:text-white dark:group-hover:bg-white dark:group-hover:text-black transition-colors duration-300">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" /></svg>
          </div>
          <h3 class="text-2xl font-bold mb-3">Contextual Chat</h3>
          <p class="text-gray-500 dark:text-gray-400 leading-relaxed">
            Don't just search—converse. Ask questions and get answers grounded in your own notes, documents, and code snippets.
          </p>
        </div>

        <div class="group">
          <div class="w-12 h-12 flex items-center justify-center border border-gray-200 dark:border-gray-800 rounded-xl mb-6 group-hover:bg-black group-hover:text-white dark:group-hover:bg-white dark:group-hover:text-black transition-colors duration-300">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" /></svg>
          </div>
          <h3 class="text-2xl font-bold mb-3">Unified Ingestion</h3>
          <p class="text-gray-500 dark:text-gray-400 leading-relaxed">
            Bring everything together. Import PDFs, scrape web pages, add YouTube videos, and sync your notes into one central vault.
          </p>
        </div>
      </div>
    </div>

    <!-- Workflow Section -->
     <div id="workflow" class="py-16 border-y-0 border-transparent">
      <div class="max-w-7xl mx-auto px-6 lg:px-8">
        <div class="mb-20">
          <h2 class="text-sm font-bold uppercase tracking-widest text-gray-400 mb-4">Workflow</h2>
          <p class="text-4xl lg:text-5xl font-extrabold tracking-tight">Structured for flow.</p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="space-y-12">
                <div class="flex gap-6">
                    <span class="text-4xl font-light text-gray-200 dark:text-gray-700">01</span>
                    <div>
                        <h3 class="text-2xl font-bold mb-2">Ingest</h3>
                        <p class="text-gray-500 dark:text-gray-400">Drag & drop PDFs, paste URLs, or sync from your browser. We handle the parsing.</p>
                    </div>
                </div>
                 <div class="flex gap-6">
                    <span class="text-4xl font-light text-gray-200 dark:text-gray-700">02</span>
                    <div>
                        <h3 class="text-2xl font-bold mb-2">Connect</h3>
                        <p class="text-gray-500 dark:text-gray-400">AI automatically tags and links your content, creating a navigable graph of knowledge.</p>
                    </div>
                </div>
                 <div class="flex gap-6">
                    <span class="text-4xl font-light text-gray-200 dark:text-gray-700">03</span>
                    <div>
                        <h3 class="text-2xl font-bold mb-2">Retrieve</h3>
                        <p class="text-gray-500 dark:text-gray-400">Ask questions naturally. Get synthesized answers with direct citations to your sources.</p>
                    </div>
                </div>
            </div>
            
            <div class="relative group">
                <div class="absolute -inset-1 bg-gradient-to-r from-gray-200 to-gray-100 dark:from-gray-800 dark:to-gray-900 rounded-2xl blur opacity-25 group-hover:opacity-50 transition duration-1000"></div>
                <div class="relative bg-white dark:bg-black border border-gray-100 dark:border-gray-800 rounded-2xl p-8 shadow-2xl">
                    <div class="font-mono text-sm space-y-4">
                        <div class="flex items-center gap-2 border-b border-gray-100 dark:border-gray-800 pb-4 mb-4">
                            <span class="w-3 h-3 rounded-full bg-black dark:bg-white"></span>
                            <span class="text-gray-400">Ask MemWyre</span>
                        </div>
                        <p class="text-gray-800 dark:text-gray-200 min-h-[50px]">
                            {{ typedText }}<span class="cursor">&nbsp;</span>
                        </p>
                        <transition name="fade">
                            <div v-if="typedText.length >= 20" class="transition-opacity duration-1000 ease-in-out">
                                <br>
                                <span class="text-gray-400">Searching 3 documents...</span><br>
                                <span class="text-blue-500">Found matches in "Auth Specs v2" and "API Docs".</span><br><br>
                                Based on "Auth Specs v2", you should use the OAuth2 provider pattern. Here is the implementation snippet...
                            </div>
                        </transition>
                    </div>
                </div>
            </div>
        </div>
      </div>
     </div>

    <!-- Ecosystem -->
    <div id="ecosystem" class="py-16 px-6 lg:px-8 max-w-7xl mx-auto">
        <div class="max-w-3xl mb-20">
             <h2 class="text-sm font-bold uppercase tracking-widest text-gray-400 mb-4">Ecosystem</h2>
             <p class="text-4xl lg:text-5xl font-extrabold tracking-tight mb-6">Built to extend.</p>
             <p class="text-xl text-gray-500 dark:text-gray-400">MemWyre isn't a silo. It powers your entire workflow through standard protocols.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
             <div class="p-10 border border-gray-200 dark:border-gray-800 rounded-3xl hover:border-black dark:hover:border-white transition-colors duration-300">
                 <div class="w-12 h-12 bg-black dark:bg-white text-white dark:text-black rounded-lg flex items-center justify-center mb-6">
                     <svg class="w-8 h-8" viewBox="0 0 180 180" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M18 84.8528L85.8822 16.9706C95.2548 7.59798 110.451 7.59798 119.823 16.9706V16.9706C129.196 26.3431 129.196 41.5391 119.823 50.9117L68.5581 102.177" stroke="currentColor" stroke-width="12" stroke-linecap="round"/>
                        <path d="M69.2652 101.47L119.823 50.9117C129.196 41.5391 144.392 41.5391 153.765 50.9117L154.118 51.2652C163.491 60.6378 163.491 75.8338 154.118 85.2063L92.7248 146.6C89.6006 149.724 89.6006 154.789 92.7248 157.913L105.331 170.52" stroke="currentColor" stroke-width="12" stroke-linecap="round"/>
                        <path d="M102.853 33.9411L52.6482 84.1457C43.2756 93.5183 43.2756 108.714 52.6482 118.087V118.087C62.0208 127.459 77.2167 127.459 86.5893 118.087L136.794 67.8822" stroke="currentColor" stroke-width="12" stroke-linecap="round"/>
                     </svg>
                 </div>
                 <h3 class="text-2xl font-bold mb-4">MCP Server</h3>
                 <p class="text-gray-500 dark:text-gray-400 mb-8">
                     Connect MemWyre directly to Claude Desktop or any MCP-compliant client. Give your AI assistant direct access to your second brain.
                 </p>
                 <div class="bg-gray-50 dark:bg-gray-900 rounded-lg p-4 font-mono text-xs text-gray-600 dark:text-gray-400">
                     $ mcp-server-brain-vault start
                 </div>
             </div>

             <div class="p-10 border border-gray-200 dark:border-gray-800 rounded-3xl hover:border-black dark:hover:border-white transition-colors duration-300">
                 <div class="w-12 h-12 bg-black dark:bg-white text-white dark:text-black rounded-lg flex items-center justify-center mb-6 font-bold text-xl">
                      <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" /></svg>
                 </div>
                 <h3 class="text-2xl font-bold mb-4">Browser Extension</h3>
                 <p class="text-gray-500 dark:text-gray-400 mb-8">
                     Capture the web as you browse. Save articles, documentation, or code snippets instantly without breaking your flow.
                 </p>
                 <div class="flex items-center gap-2 text-sm font-bold">
                     <span>Available for Chrome & Edge</span>
                     <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" /></svg>
                 </div>
             </div>
        </div>
    </div>



    <!-- FAQ Section -->
    <div id="faq" class="py-16 px-6 lg:px-8 max-w-3xl mx-auto">
        <div class="text-center mb-16">
             <h2 class="text-sm font-bold uppercase tracking-widest text-gray-400 mb-4">FAQ</h2>
             <p class="text-4xl font-extrabold tracking-tight">Common questions.</p>
        </div>

        <div class="space-y-4">
            <div v-for="(faq, index) in faqs" :key="index" class="border-b border-gray-200 dark:border-gray-800 pb-4">
                <button @click="toggleFaq(index)" class="flex justify-between items-center w-full text-left py-4 group">
                    <span class="text-lg font-bold group-hover:text-gray-600 dark:group-hover:text-gray-300 transition-colors">{{ faq.question }}</span>
                    <span class="ml-4 flex-shrink-0">
                        <svg v-if="faq.isOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4" /></svg>
                        <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
                    </span>
                </button>
                <div v-show="faq.isOpen" class="text-gray-500 dark:text-gray-400 pb-4 leading-relaxed">
                    {{ faq.answer }}
                </div>
            </div>
        </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const faqs = ref([
    {
        question: "What exactly is a 'Second Brain'?",
        answer: "A Second Brain is a personal system for recording, organizing, and retrieving the information that matters to you. MemWyre automates this process using AI to link and surface relevant info when you need it.",
        isOpen: false
    },
    {
        question: "What kind of content can I add?",
        answer: "MemWyre supports a wide range of formats. You can upload PDF documents, text files, markdown notes, and even ingest content directly from YouTube videos and web pages.",
        isOpen: false
    },
    {
        question: "How does the AI Chat work?",
        answer: "We use Retrieval-Augmented Generation (RAG). When you ask a question, MemWyre searches your documents for relevant context and feeds it to the AI, ensuring the answer is grounded in your actual data.",
        isOpen: false
    },
     {
        question: "Can I use MemWyre offline?",
        answer: "The local version of MemWyre can run entirely on your machine. However, certain AI features may require an internet connection depending on your configuration (e.g., using OpenAI vs local LLMs).",
        isOpen: false
    }
]);

const toggleFaq = (index) => {
    faqs.value[index].isOpen = !faqs.value[index].isOpen;
};

// --- Animations ---
onMounted(() => {
    // Start Typing Effect
    typeWriter();
});


// 2. Typing Effect
const typedText = ref('');
const fullText = "> How do I implement the new auth flow?";
const typingSpeed = 50;

const typeWriter = () => {
    let i = 0;
    typedText.value = ''; // Reset
    
    const type = () => {
        if (i < fullText.length) {
            typedText.value += fullText.charAt(i);
            i++;
            setTimeout(type, typingSpeed);
        } else {
             // Optional: Loop animation after a delay
             setTimeout(() => {
                 typedText.value = '> ';
                 i = 2; 
                 type();
             }, 5000);
        }
    };
    
    // Initial delay before starting
    setTimeout(type, 1000); 
};

</script>

<style scoped>
html {
  scroll-behavior: smooth;
}

/* Typing Cursor */
.cursor {
    display: inline-block;
    width: 8px;
    background-color: currentColor;
    animation: blink 1s step-end infinite;
}

@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
}
</style>
