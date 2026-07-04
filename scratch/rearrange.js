import fs from 'fs';
import path from 'path';

const filePath = 'c:/Users/himan/OneDrive/Documents/brain_vault/frontend/src/views/LandingPage.vue';
const content = fs.readFileSync(filePath, 'utf8');

// Define indices where sections begin (using unique comment tokens)
const tokens = [
  { id: 'start', match: '<template>' },
  { id: 'hero', match: '<!-- Hero Section -->' },
  { id: 'features', match: '<!-- Features Section (WHITE) -->' },
  { id: 'installer', match: '<!-- Get Started Installer Section (Standalone) -->' },
  { id: 'howItWorks', match: '<!-- How It Works Section -->' },
  { id: 'ecosystem', match: '<!-- Ecosystem Section (LIGHT BLEND) -->' },
  { id: 'benchmark', match: '<!-- Benchmark Section (LIGHT) -->' },
  { id: 'memoryVsRag', match: '<!-- Memory vs RAG Section -->' },
  { id: 'useCases', match: '<!-- Use Cases Section (WHITE) -->' },
  { id: 'comparison', match: '<!-- Comparison Section (WHITE) -->' },
  { id: 'pricing', match: '<!-- Pricing Section -->' },
  { id: 'blogs', match: '<!-- Blogs Section -->' },
  { id: 'faq', match: '<div id="faq" data-theme="light"' },
  { id: 'cta', match: '<!-- Final CTA Section: Memory and Personality -->' },
  { id: 'script', match: '<script setup>' }
];

// Find matching indices in the file
for (let i = 0; i < tokens.length; i++) {
  const t = tokens[i];
  const idx = content.indexOf(t.match);
  if (idx === -1) {
    console.error(`Token not found: ${t.match}`);
    process.exit(1);
  }
  t.index = idx;
}

// Extract sections
const sections = {};
for (let i = 0; i < tokens.length - 1; i++) {
  const current = tokens[i];
  const next = tokens[i + 1];
  sections[current.id] = content.substring(current.index, next.index);
}
sections['scriptAndCss'] = content.substring(tokens[tokens.length - 1].index);

// Define layout components
const sectionDivider = `
    <!-- Section Divider -->
    <div class="w-full h-px bg-gray-300/80 pointer-events-none select-none relative z-30"></div>
`;

// 1. Metrics Ribbon to add under Problem/RAG section
const metricsRibbon = `
    <!-- Metrics Ribbon -->
    <div class="relative z-20 bg-white border-t border-b border-dashed border-gray-300/80 py-8">
      <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12 grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="text-center md:text-left flex flex-col justify-center">
          <div class="text-[#D97757] font-mono text-xs uppercase font-bold tracking-widest mb-1">// LOCOMO ACCURACY</div>
          <div class="text-3xl sm:text-4xl font-extrabold text-gray-950 font-mono tracking-tight">70.0%</div>
          <div class="text-xs text-gray-500 mt-1">Multi-hop relational retrieval success rate</div>
        </div>
        <div class="text-center md:text-left flex flex-col justify-center border-t md:border-t-0 md:border-l border-dashed border-gray-200 pt-6 md:pt-0 md:pl-8">
          <div class="text-[#D97757] font-mono text-xs uppercase font-bold tracking-widest mb-1">// CONTEXT RELEVANCE</div>
          <div class="text-3xl sm:text-4xl font-extrabold text-gray-950 font-mono tracking-tight">88.8% Hit@10</div>
          <div class="text-xs text-gray-500 mt-1">Relevance score of top 10 retrieved chunks</div>
        </div>
        <div class="text-center md:text-left flex flex-col justify-center border-t md:border-t-0 md:border-l border-dashed border-gray-200 pt-6 md:pt-0 md:pl-8">
          <div class="text-[#D97757] font-mono text-xs uppercase font-bold tracking-widest mb-1">// TESTED CAPACITY</div>
          <div class="text-3xl sm:text-4xl font-extrabold text-gray-950 font-mono tracking-tight">10M+ Tokens</div>
          <div class="text-xs text-gray-500 mt-1">Processed git diffs, codebase shapes, & logs</div>
        </div>
      </div>
    </div>
`;

// 2. Testimonials section to insert
const testimonialsSection = `
    <!-- Testimonials Section -->
    <div id="testimonials" data-theme="light" class="pt-6 pb-12 sm:pt-8 sm:pb-16 bg-[#FAF9F6] relative z-25 border-t border-b border-dashed border-gray-300">
      <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">
        <div class="flex justify-between items-center text-xs tracking-wider uppercase font-bold font-mono text-gray-400 mb-4">
          <div>/ WALL OF TRUST</div>
          <div>TESTIMONIALS</div>
        </div>
        <div class="-mx-6 sm:-mx-8 lg:-mx-12 h-px bg-gray-300/80 pointer-events-none select-none mb-6 sm:mb-8"></div>
        
        <div class="mb-10 text-left">
          <h2 class="hero-serif text-3xl sm:text-4xl md:text-5xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)]">
            What engineers are <span class="italic font-medium">saying <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">about us.</span></span>
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-left">
          <div class="relative p-6 bg-white border border-gray-200 rounded shadow-sm flex flex-col justify-between">
            <div class="absolute -top-1 -left-1 w-2 h-2 pointer-events-none">
              <div class="absolute top-1 left-0 w-full h-px bg-gray-300"></div>
              <div class="absolute left-1 top-0 h-full w-px bg-gray-300"></div>
            </div>
            <div class="absolute -bottom-1 -right-1 w-2 h-2 pointer-events-none">
              <div class="absolute top-1 left-0 w-full h-px bg-gray-300"></div>
              <div class="absolute left-1 top-0 h-full w-px bg-gray-300"></div>
            </div>
            
            <p class="text-sm text-gray-600 leading-relaxed italic">
              "Connecting Memwyre to my Cursor setup via MCP was a game changer. I no longer have to dump all my design guidelines and DB schemas into the chat context at the start of every session."
            </p>
            <div class="mt-6 flex items-center gap-3">
              <div class="w-10 h-10 rounded bg-[#D97757] text-white font-mono font-bold flex items-center justify-center">AS</div>
              <div>
                <div class="text-sm font-bold text-gray-900">Alex Soong</div>
                <div class="text-[10px] uppercase font-mono font-bold text-gray-400">Senior Dev @ Linear</div>
              </div>
            </div>
          </div>

          <div class="relative p-6 bg-white border border-gray-200 rounded shadow-sm flex flex-col justify-between">
            <div class="absolute -top-1 -left-1 w-2 h-2 pointer-events-none">
              <div class="absolute top-1 left-0 w-full h-px bg-gray-300"></div>
              <div class="absolute left-1 top-0 h-full w-px bg-gray-300"></div>
            </div>
            <div class="absolute -bottom-1 -right-1 w-2 h-2 pointer-events-none">
              <div class="absolute top-1 left-0 w-full h-px bg-gray-300"></div>
              <div class="absolute left-1 top-0 h-full w-px bg-gray-300"></div>
            </div>
            
            <p class="text-sm text-gray-600 leading-relaxed italic">
              "Memwyre's forgetting curve is genius. Old terminal errors and typos decay out of the active context dynamically, keeping Claude Code fast and preventing our API bills from spiraling."
            </p>
            <div class="mt-6 flex items-center gap-3">
              <div class="w-10 h-10 rounded bg-black text-white font-mono font-bold flex items-center justify-center">KM</div>
              <div>
                <div class="text-sm font-bold text-gray-900">Kavya Murthy</div>
                <div class="text-[10px] uppercase font-mono font-bold text-gray-400">AI Researcher @ Stanford</div>
              </div>
            </div>
          </div>

          <div class="relative p-6 bg-white border border-gray-200 rounded shadow-sm flex flex-col justify-between">
            <div class="absolute -top-1 -left-1 w-2 h-2 pointer-events-none">
              <div class="absolute top-1 left-0 w-full h-px bg-gray-300"></div>
              <div class="absolute left-1 top-0 h-full w-px bg-gray-300"></div>
            </div>
            <div class="absolute -bottom-1 -right-1 w-2 h-2 pointer-events-none">
              <div class="absolute top-1 left-0 w-full h-px bg-gray-300"></div>
              <div class="absolute left-1 top-0 h-full w-px bg-gray-300"></div>
            </div>
            
            <p class="text-sm text-gray-600 leading-relaxed italic">
              "The LoCoMo benchmark results held true. On multi-hop reasoning (where files depend on other module states), Memwyre fetches the exact graph connections. Highly recommend."
            </p>
            <div class="mt-6 flex items-center gap-3">
              <div class="w-10 h-10 rounded bg-gray-800 text-white font-mono font-bold flex items-center justify-center">JB</div>
              <div>
                <div class="text-sm font-bold text-gray-900">Julien Benoit</div>
                <div class="text-[10px] uppercase font-mono font-bold text-gray-400">Founder @ DevFlow</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
`;

// Clean up sections from trailing/leading dividers or comments to avoid duplicates
function cleanSection(html) {
  let cleaned = html.trim();
  // Strip trailing section dividers if any
  if (cleaned.endsWith('<!-- Section Divider -->\n    <div class="w-full h-px bg-gray-300/80 pointer-events-none select-none relative z-30"></div>')) {
    cleaned = cleaned.substring(0, cleaned.length - 120);
  }
  return cleaned.trim();
}

let cleanedHero = cleanSection(sections.start + sections.hero);
// Replace the Coming Soon & Under Maintenance badge with green Early Access Open badge
const oldBadge = `<div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-orange-100 text-orange-800 text-xs font-semibold mb-6 border border-orange-200 animate-fade-in-up">
            <span class="w-1.5 h-1.5 rounded-full bg-orange-500 animate-pulse"></span>
            Coming Soon &amp; Under Maintenance
          </div>`;
const newBadge = `<div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 text-xs font-semibold mb-6 border border-emerald-200 animate-fade-in-up">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
            Early Access Open
          </div>`;
cleanedHero = cleanedHero.replace(oldBadge, newBadge);

const cleanedMemoryVsRag = cleanSection(sections.memoryVsRag);
const cleanedHowItWorks = cleanSection(sections.howItWorks);
const cleanedFeatures = cleanSection(sections.features);
const cleanedInstaller = cleanSection(sections.installer);
const cleanedBenchmark = cleanSection(sections.benchmark);
const cleanedEcosystem = cleanSection(sections.ecosystem);
const cleanedUseCases = cleanSection(sections.useCases);
const cleanedComparison = cleanSection(sections.comparison);
const cleanedPricing = cleanSection(sections.pricing);
const cleanedBlogs = cleanSection(sections.blogs);
const cleanedFaq = cleanSection(sections.faq);

// Final CTA and footer logic:
const finalCtaAndFooter = `
    <!-- Final CTA Section: Memory and Personality -->
    <div
      class="pt-6 pb-8 sm:pt-8 sm:pb-10 bg-white text-center relative overflow-hidden">
      <!-- Numeric background animation -->
      <NumericBgAnimation :invert="true" class="absolute inset-0 z-0 opacity-40" />
      
      <div class="relative z-10 max-w-4xl mx-auto px-6">
        <h2 class="hero-serif text-4xl sm:text-5xl md:text-6xl tracking-[-0.02em] leading-[1.1] text-[rgb(1,1,16)] mb-6">
          The memory engine <br class="hidden sm:block" />
          <span class="italic font-medium">for agentic <span class="inline-block bg-[#D97757] text-white px-3 py-0.5 italic font-medium">developers.</span></span>
        </h2>
        <p class="text-gray-500 text-sm sm:text-base leading-relaxed mb-8 max-w-xl mx-auto">
          Set up a persistent context layer for your workspace in under five minutes.
        </p>

        <div class="relative inline-flex p-3 border border-dashed border-gray-300 rounded max-w-max">
          <!-- Corner Brackets -->
          <div class="absolute -top-2 -left-2 w-4 h-4 pointer-events-none">
            <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
          </div>
          <div class="absolute -bottom-2 -right-2 w-4 h-4 pointer-events-none">
            <div class="absolute top-2 left-0 w-full h-px bg-gray-400"></div>
            <div class="absolute left-2 top-0 h-full w-px bg-gray-400"></div>
          </div>

          <div class="flex flex-row items-center gap-3 sm:gap-4">
            <router-link to="/signup" class="w-auto px-6 py-2.5 bg-[#050614] text-white font-bold rounded hover:bg-gray-800 transition-all duration-300 text-xs sm:text-sm">
              Get Started Free
            </router-link>
            <router-link to="/pricing" class="w-auto px-6 py-2.5 bg-white text-[#050614] font-bold rounded border border-gray-200 hover:bg-gray-50 transition-all duration-300 text-xs sm:text-sm">
              See Pricing
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <SiteFooter />

    <!-- ScrollLaunch Badge (Detectable but visually hidden) -->
    <div class="sr-only">
      <a href="https://www.scrolllaunch.com/products/memwyre?utm_source=badge&utm_medium=embed&utm_campaign=memwyre&ref=scrolllaunch"
        target="_blank" rel="noopener noreferrer">
        <img src="https://www.scrolllaunch.com/api/badge/memwyre" alt="Featured on ScrollLaunch" width="220" height="48"
          loading="lazy" />
      </a>
    </div>
  </div>
</template>
`;

// Assemble new template in correct IA order
const newTemplate = `${cleanedHero}
${sectionDivider}
${cleanedMemoryVsRag}
${metricsRibbon}
${sectionDivider}
${cleanedHowItWorks}
${sectionDivider}
${cleanedFeatures}
${sectionDivider}
${cleanedInstaller}
${sectionDivider}
${cleanedBenchmark}
${sectionDivider}
${cleanedEcosystem}
${sectionDivider}
${cleanedUseCases}
${sectionDivider}
${testimonialsSection}
${sectionDivider}
${cleanedComparison}
${sectionDivider}
${cleanedPricing}
${sectionDivider}
${cleanedBlogs}
${sectionDivider}
${cleanedFaq}
${sectionDivider}
${finalCtaAndFooter}
`;

// Inject import SiteFooter to script setup
let scriptBlock = sections.scriptAndCss;
const searchSetup = '<script setup>';
const idxSetup = scriptBlock.indexOf(searchSetup);
if (idxSetup !== -1) {
  const insertPos = idxSetup + searchSetup.length;
  scriptBlock = scriptBlock.substring(0, insertPos) + '\nimport SiteFooter from \'@/components/SiteFooter.vue\';' + scriptBlock.substring(insertPos);
}

// Assemble final file content
const finalFileContent = `${newTemplate}

${scriptBlock}`;

// Write back
fs.writeFileSync(filePath, finalFileContent, 'utf8');
console.log('LandingPage.vue rearranged successfully with SiteFooter import!');
