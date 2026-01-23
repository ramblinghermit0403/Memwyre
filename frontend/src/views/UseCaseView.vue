<template>
  <div class="min-h-screen bg-white dark:bg-black text-black dark:text-white pt-24 pb-20 font-sans selection:bg-gray-200 dark:selection:bg-gray-800">
    
    <!-- 1. HERO SECTION -->
    <div class="max-w-7xl mx-auto px-6 lg:px-8 mb-32">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            <div class="space-y-8">
                <h1 class="text-6xl font-black tracking-tighter leading-none">
                    Your AI Forgets.<br>
                    <span class="text-gray-400">Memwyre Remembers.</span>
                </h1>
                <p class="text-xl text-gray-500 dark:text-gray-400 leading-relaxed max-w-lg">
                    Memwyre captures everything your team does with AI—research, code, decisions—and turns it into persistent, shareable knowledge.
                </p>
                <div class="flex flex-col sm:flex-row gap-4">
                    <router-link to="/register" class="px-8 py-4 bg-black dark:bg-white text-white dark:text-black text-lg font-bold rounded-full hover:opacity-90 transition-opacity text-center">
                        See How It Works
                    </router-link>
                    <a href="mailto:sales@memwyre.com" class="px-8 py-4 border border-gray-200 dark:border-gray-800 text-black dark:text-white text-lg font-bold rounded-full hover:bg-gray-50 dark:hover:bg-gray-900 transition-colors text-center">
                        Talk to Us
                    </a>
                </div>
            </div>
            
            <!-- Visual Diagram -->
            <div class="relative p-1 bg-gradient-to-br from-gray-200 to-gray-100 dark:from-gray-800 dark:to-gray-900 rounded-3xl overflow-hidden border border-gray-200 dark:border-gray-800">
                <div class="bg-white dark:bg-black p-8 rounded-[22px] flex flex-col items-center justify-center space-y-6">
                    <div class="flex items-center gap-4">
                        <div class="w-16 h-16 bg-gray-100 dark:bg-gray-900 rounded-full flex items-center justify-center font-bold">User</div>
                        <div class="h-0.5 w-8 bg-gray-300 dark:bg-gray-700"></div>
                        <div class="px-4 py-2 border border-gray-300 dark:border-gray-700 rounded-lg text-sm">AI Tools</div>
                    </div>
                    <div class="h-8 w-0.5 bg-gray-300 dark:bg-gray-700"></div>
                    <div class="w-full p-6 bg-black text-white dark:bg-white dark:text-black rounded-xl text-center font-bold text-xl shadow-xl">
                        Memwyre Inbox
                    </div>
                    <div class="h-8 w-0.5 bg-gray-300 dark:bg-gray-700"></div>
                    <div class="flex gap-4 w-full">
                        <div class="flex-1 p-4 bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 rounded-xl text-center text-sm font-medium">Teams</div>
                        <div class="flex-1 p-4 bg-gray-50 dark:bg-gray-900 border border-gray-100 dark:border-gray-800 rounded-xl text-center text-sm font-medium">Future Sessions</div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- 2. THE PROBLEM -->
    <div class="bg-gray-50 dark:bg-gray-900/30 py-32 border-y border-gray-100 dark:border-gray-900">
        <div class="max-w-4xl mx-auto px-6 lg:px-8 text-center">
             <h2 class="text-sm font-bold uppercase tracking-widest text-gray-400 mb-8">The Disconnect</h2>
             <blockquote class="text-4xl md:text-5xl font-bold leading-tight mb-16">
                “AI is everywhere in our workflow — <span class="bg-black text-white dark:bg-white dark:text-black px-2">but none of it sticks.</span>”
            </blockquote>
             
             <div class="grid grid-cols-1 md:grid-cols-2 gap-8 text-left">
                 <div class="p-6 border-l-4 border-black dark:border-white">
                     <div class="font-bold text-lg mb-2">Ephemeral Interactions</div>
                     <p class="text-gray-500 dark:text-gray-400">Employees use AI across dozens of tools, but sessions vanish when tabs close.</p>
                 </div>
                 <div class="p-6 border-l-4 border-gray-300 dark:border-gray-700">
                     <div class="font-bold text-lg mb-2">Locked Insights</div>
                     <p class="text-gray-500 dark:text-gray-400">Valuable context lives inside chat logs, prompts, and half-written docs.</p>
                 </div>
                 <div class="p-6 border-l-4 border-gray-300 dark:border-gray-700">
                     <div class="font-bold text-lg mb-2">Context Reset</div>
                     <p class="text-gray-500 dark:text-gray-400">After a few days, the reasoning is gone. You start from zero.</p>
                 </div>
                 <div class="p-6 border-l-4 border-black dark:border-white">
                     <div class="font-bold text-lg mb-2">Redundant Work</div>
                     <p class="text-gray-500 dark:text-gray-400">Teams repeat the same research again and again, unaware it was already solved.</p>
                 </div>
             </div>
        </div>
    </div>

    <!-- 3. THE USE CASE -->
    <div class="py-32 max-w-7xl mx-auto px-6 lg:px-8">
        <div class="flex flex-col md:flex-row gap-16">
            <div class="md:w-1/3">
                 <h2 class="text-4xl font-black mb-6">Enterprise Research &<br>Knowledge Continuity</h2>
                 <p class="text-gray-500 dark:text-gray-400 text-lg">
                     For Strategy teams, engineers, consultants, and analysts doing market research, system design, or compliance analysis.
                 </p>
            </div>
            <div class="md:w-2/3 grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="p-8 bg-gray-50 dark:bg-gray-900 rounded-2xl">
                    <div class="text-4xl mb-4">🔄</div>
                    <h3 class="font-bold mb-2">Knowledge Resets</h3>
                    <p class="text-sm text-gray-500 dark:text-gray-400">Every session starts fresh, losing prior depth.</p>
                </div>
                <div class="p-8 bg-gray-50 dark:bg-gray-900 rounded-2xl">
                    <div class="text-4xl mb-4">🥶</div>
                    <h3 class="font-bold mb-2">Cold Starts</h3>
                    <p class="text-sm text-gray-500 dark:text-gray-400">New hires can't tap into the team's past AI work.</p>
                </div>
                <div class="p-8 bg-gray-50 dark:bg-gray-900 rounded-2xl">
                    <div class="text-4xl mb-4">🧱</div>
                    <h3 class="font-bold mb-2">Siloed Effort</h3>
                    <p class="text-sm text-gray-500 dark:text-gray-400">One person's breakthrough doesn't help the team.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- 4. HOW MEMWYRE FITS (Steps) -->
    <div class="bg-black text-white py-32">
        <div class="max-w-4xl mx-auto px-6 lg:px-8">
            <h2 class="text-3xl font-bold mb-16 text-center">Knowledge Flow</h2>
            <div class="space-y-16 relative before:absolute before:left-8 before:top-0 before:bottom-0 before:w-0.5 before:bg-gray-800">
                
                <!-- Step 1 -->
                <div class="relative pl-24">
                    <div class="absolute left-4 top-0 w-8 h-8 rounded-full bg-white text-black flex items-center justify-center font-bold z-10">1</div>
                    <h3 class="text-2xl font-bold mb-2">Work With AI As Usual</h3>
                    <p class="text-gray-400 mb-4">Employees use ChatGPT, Copilot, internal LLMs, or custom agents.</p>
                    <div class="text-sm border border-gray-700 inline-block px-3 py-1 rounded text-gray-300">Nothing new to learn. No workflow changes.</div>
                </div>

                <!-- Step 2 -->
                 <div class="relative pl-24">
                    <div class="absolute left-4 top-0 w-8 h-8 rounded-full bg-gray-800 text-white border border-gray-600 flex items-center justify-center font-bold z-10">2</div>
                    <h3 class="text-2xl font-bold mb-2">Memwyre Captures the Signal</h3>
                    <p class="text-gray-400 mb-4">Usually lost questions, reasoning paths, and conclusions automatically flow into a <strong>personal knowledge inbox</strong>.</p>
                </div>

                <!-- Step 3 -->
                <div class="relative pl-24">
                    <div class="absolute left-4 top-0 w-8 h-8 rounded-full bg-gray-800 text-white border border-gray-600 flex items-center justify-center font-bold z-10">3</div>
                    <h3 class="text-2xl font-bold mb-2">Knowledge Becomes Durable</h3>
                    <p class="text-gray-400 mb-4">Links related work across sessions. Preserves timelines and decisions.</p>
                    <div class="text-sm text-gray-500 italic">"What your team learns today is still usable next quarter."</div>
                </div>

                 <!-- Step 4 -->
                <div class="relative pl-24">
                    <div class="absolute left-4 top-0 w-8 h-8 rounded-full bg-gray-800 text-white border border-gray-600 flex items-center justify-center font-bold z-10">4</div>
                    <h3 class="text-2xl font-bold mb-2">Cold Start Is Eliminated</h3>
                    <p class="text-gray-400">Restores context upon return. Surfaces prior conclusions. Shows what’s unresolved.</p>
                </div>

                 <!-- Step 5 -->
                <div class="relative pl-24">
                    <div class="absolute left-4 top-0 w-8 h-8 rounded-full bg-white text-black flex items-center justify-center font-bold z-10">5</div>
                    <h3 class="text-2xl font-bold mb-2">Knowledge Is Shared (Safely)</h3>
                    <p class="text-gray-400">Share research internally. Build on each other’s work. Avoid duplicating effort.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- 5. BEFORE vs AFTER -->
    <div class="py-32 px-6 lg:px-8 max-w-7xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-2">
            <div class="p-12 bg-gray-100 dark:bg-gray-900 border-r border-gray-200 dark:border-gray-800">
                <h3 class="text-xl font-bold uppercase tracking-widest text-gray-400 mb-8">Before Memwyre</h3>
                <ul class="space-y-6 text-lg text-gray-500 dark:text-gray-400">
                    <li class="flex items-center gap-3"><span class="text-red-400">×</span> AI usage is ephemeral</li>
                    <li class="flex items-center gap-3"><span class="text-red-400">×</span> Knowledge is siloed</li>
                    <li class="flex items-center gap-3"><span class="text-red-400">×</span> Context is lost</li>
                    <li class="flex items-center gap-3"><span class="text-red-400">×</span> Rework is constant</li>
                </ul>
            </div>
            <div class="p-12 bg-gray-50 dark:bg-black">
                <h3 class="text-xl font-bold uppercase tracking-widest text-black dark:text-white mb-8">After Memwyre</h3>
                 <ul class="space-y-6 text-lg font-medium">
                    <li class="flex items-center gap-3"><span class="text-green-400">✓</span> AI work compounds</li>
                    <li class="flex items-center gap-3"><span class="text-green-400">✓</span> Knowledge is reusable</li>
                    <li class="flex items-center gap-3"><span class="text-green-400">✓</span> Context persists</li>
                    <li class="flex items-center gap-3"><span class="text-green-400">✓</span> Teams move faster</li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 6. BUSINESS IMPACT -->
    <div class="py-20 bg-gray-50 dark:bg-white/5 border-y border-gray-200 dark:border-gray-900">
         <div class="max-w-5xl mx-auto px-6 lg:px-8 text-center">
            <h2 class="text-3xl font-bold mb-12">Why This Matters To Enterprises</h2>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8 mb-16">
                <div>
                     <div class="text-2xl font-bold mb-2">Faster</div>
                     <div class="text-sm text-gray-500">Onboarding</div>
                </div>
                <div>
                     <div class="text-2xl font-bold mb-2">Fewer</div>
                     <div class="text-sm text-gray-500">Repeated Analyses</div>
                </div>
                <div>
                     <div class="text-2xl font-bold mb-2">Stronger</div>
                     <div class="text-sm text-gray-500">Decision Trails</div>
                </div>
                <div>
                     <div class="text-2xl font-bold mb-2">Lasting</div>
                     <div class="text-sm text-gray-500">Institutional Memory</div>
                </div>
            </div>
            <div class="inline-block p-6 border-2 border-black dark:border-white rounded-xl text-xl font-bold">
                Memwyre turns AI spend from an operating cost into a knowledge asset.
            </div>
         </div>
    </div>

    <!-- 7. WHO THIS IS FOR -->
    <div class="py-32 max-w-7xl mx-auto px-6 lg:px-8">
        <h2 class="text-3xl font-bold mb-16 text-center">Who This Is For</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div class="p-6 border border-gray-100 dark:border-gray-800 rounded-xl">
                <h3 class="font-bold mb-2">Strategy & Research</h3>
                <p class="text-sm text-gray-500">Preserve and reuse AI-assisted insights.</p>
            </div>
             <div class="p-6 border border-gray-100 dark:border-gray-800 rounded-xl">
                <h3 class="font-bold mb-2">Engineering Teams</h3>
                <p class="text-sm text-gray-500">Keep architectural and debugging context alive.</p>
            </div>
             <div class="p-6 border border-gray-100 dark:border-gray-800 rounded-xl">
                <h3 class="font-bold mb-2">Consultants</h3>
                <p class="text-sm text-gray-500">Compound firm-wide intelligence.</p>
            </div>
             <div class="p-6 border border-gray-100 dark:border-gray-800 rounded-xl">
                <h3 class="font-bold mb-2">Leadership</h3>
                <p class="text-sm text-gray-500">Know what the organization actually knows.</p>
            </div>
        </div>
    </div>

    <!-- 8. DIFFERENTIATION -->
     <div class="bg-gray-100 dark:bg-gray-900 py-32">
        <div class="max-w-4xl mx-auto px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
                 <div class="space-y-6">
                     <h3 class="text-xl font-bold text-gray-400 uppercase tracking-widest">Memwyre is NOT</h3>
                     <ul class="space-y-4 text-gray-500 text-lg">
                         <li>• Chat history</li>
                         <li>• A vector database</li>
                         <li>• A note-taking tool</li>
                     </ul>
                 </div>
                 <div class="space-y-6">
                     <h3 class="text-xl font-bold text-black dark:text-white uppercase tracking-widest">Memwyre IS</h3>
                      <ul class="space-y-4 text-black dark:text-white font-medium text-lg">
                         <li>• A persistent knowledge buffer</li>
                         <li>• A memory layer between humans and AI</li>
                         <li>• A system of record for AI-assisted thinking</li>
                     </ul>
                 </div>
            </div>
        </div>
     </div>

     <!-- 9. CLOSING CTA -->
    <div class="py-32 text-center px-6 lg:px-8">
         <h2 class="text-4xl lg:text-5xl font-extrabold tracking-tight mb-4">Your team already uses AI.</h2>
         <p class="text-2xl text-gray-500 dark:text-gray-400 mb-12">Make sure it actually remembers.</p>
         
         <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <router-link to="/register" class="px-10 py-5 bg-black dark:bg-white text-white dark:text-black text-xl font-bold rounded-full hover:scale-105 transition-transform">
                Get a Demo
            </router-link>
            <a href="mailto:sales@memwyre.com" class="px-10 py-5 border border-gray-200 dark:border-gray-800 text-black dark:text-white text-xl font-bold rounded-full hover:bg-gray-50 dark:hover:bg-gray-900 transition-colors">
                Contact Sales
            </a>
        </div>
    </div>

  </div>
</template>
