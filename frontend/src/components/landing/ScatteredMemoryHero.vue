<template>
  <div class="relative w-full max-w-xl mx-auto overflow-visible group">
    <!-- SVG Canvas -->
    <svg class="w-full h-auto z-10 overflow-visible scale-150 origin-center" viewBox="-30 0 560 520" fill="none" xmlns="http://www.w3.org/2000/svg">
      <!-- Concentric Rings (Semi-Circles) -->
      <path d="M 130,450 A 120,120 0 0,1 370,450" stroke="#D97757" stroke-width="1.5" stroke-dasharray="4 6" opacity="0.6" fill="none" />
      <path d="M 10,450 A 240,240 0 0,1 490,450" stroke="#D97757" stroke-width="1.5" stroke-dasharray="4 6" opacity="0.6" fill="none" />

      <!-- Radial Lines to Inner Ring Nodes -->
      <line x1="250" y1="450" x2="146" y2="390" stroke="#D97757" stroke-width="1" stroke-dasharray="3 3" opacity="0.2" />
      <line x1="250" y1="450" x2="250" y2="330" stroke="#D97757" stroke-width="1" stroke-dasharray="3 3" opacity="0.2" />
      <line x1="250" y1="450" x2="354" y2="390" stroke="#D97757" stroke-width="1" stroke-dasharray="3 3" opacity="0.2" />

      <!-- Radial Lines to Outer Ring Nodes -->
      <line x1="250" y1="450" x2="18" y2="388" stroke="#D97757" stroke-width="1" stroke-dasharray="3 3" opacity="0.2" />
      <line x1="250" y1="450" x2="80" y2="280" stroke="#D97757" stroke-width="1" stroke-dasharray="3 3" opacity="0.2" />
      <line x1="250" y1="450" x2="250" y2="210" stroke="#D97757" stroke-width="1" stroke-dasharray="3 3" opacity="0.2" />
      <line x1="250" y1="450" x2="420" y2="280" stroke="#D97757" stroke-width="1" stroke-dasharray="3 3" opacity="0.2" />
      <line x1="250" y1="450" x2="482" y2="388" stroke="#D97757" stroke-width="1" stroke-dasharray="3 3" opacity="0.2" />

      <!-- Trailing dots traveling along radial paths towards center -->
      <circle r="4" fill="#D97757" opacity="0.8">
        <animateMotion dur="2.5s" repeatCount="indefinite" begin="0s" path="M146,390 L250,450" />
        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="2.5s" repeatCount="indefinite" begin="0s" />
      </circle>
      <circle r="4" fill="#D97757" opacity="0.8">
        <animateMotion dur="2.5s" repeatCount="indefinite" begin="0.3s" path="M250,330 L250,450" />
        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="2.5s" repeatCount="indefinite" begin="0.3s" />
      </circle>
      <circle r="4" fill="#D97757" opacity="0.8">
        <animateMotion dur="2.5s" repeatCount="indefinite" begin="0.6s" path="M354,390 L250,450" />
        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="2.5s" repeatCount="indefinite" begin="0.6s" />
      </circle>
      <circle r="4" fill="#D97757" opacity="0.8">
        <animateMotion dur="2.5s" repeatCount="indefinite" begin="0.9s" path="M18,388 L250,450" />
        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="2.5s" repeatCount="indefinite" begin="0.9s" />
      </circle>
      <circle r="4" fill="#D97757" opacity="0.8">
        <animateMotion dur="2.5s" repeatCount="indefinite" begin="1.2s" path="M80,280 L250,450" />
        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="2.5s" repeatCount="indefinite" begin="1.2s" />
      </circle>
      <circle r="4" fill="#D97757" opacity="0.8">
        <animateMotion dur="2.5s" repeatCount="indefinite" begin="1.5s" path="M250,210 L250,450" />
        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="2.5s" repeatCount="indefinite" begin="1.5s" />
      </circle>
      <circle r="4" fill="#D97757" opacity="0.8">
        <animateMotion dur="2.5s" repeatCount="indefinite" begin="1.8s" path="M420,280 L250,450" />
        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="2.5s" repeatCount="indefinite" begin="1.8s" />
      </circle>
      <circle r="4" fill="#D97757" opacity="0.8">
        <animateMotion dur="2.5s" repeatCount="indefinite" begin="2.1s" path="M482,388 L250,450" />
        <animate attributeName="opacity" values="0;0.9;0.9;0" dur="2.5s" repeatCount="indefinite" begin="2.1s" />
      </circle>

      <!-- Central Node: Memwyre (Bottom Centered) -->
      <g class="transition-transform duration-500 hover:scale-105 origin-[250px_450px]">
        <image href="/image.svg" x="225" y="425" width="50" height="50" />
        <text x="250" y="506" font-family="monospace" font-size="12" font-weight="bold" fill="#111827" letter-spacing="1.5" text-anchor="middle">MEMWYRE</text>
      </g>

      <!-- Outer Nodes: Concentric Distribution -->
      <!-- INNER RING NODES -->
      <!-- 1. Inner Left (Gemini) -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -6; 0 0" dur="4s" repeatCount="indefinite" begin="0s" />
        <image :href="geminiLogo" x="128" y="372" width="36" height="36" />
        <text x="146" y="422" font-family="monospace" font-size="10" font-weight="bold" fill="#111827" text-anchor="middle">Gemini</text>
      </g>
      <!-- 2. Inner Top (Antigravity) -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -6; 0 0" dur="5s" repeatCount="indefinite" begin="0.3s" />
        <image :href="antigravityLogo" x="232" y="312" width="36" height="36" />
        <text x="250" y="362" font-family="monospace" font-size="10" font-weight="bold" fill="#111827" text-anchor="middle">Antigravity</text>
      </g>
      <!-- 3. Inner Right (Perplexity) -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -6; 0 0" dur="6s" repeatCount="indefinite" begin="0.6s" />
        <image :href="perplexityLogo" x="336" y="372" width="36" height="36" />
        <text x="354" y="422" font-family="monospace" font-size="10" font-weight="bold" fill="#111827" text-anchor="middle">Perplexity</text>
      </g>

      <!-- OUTER RING NODES -->
      <!-- 4. Outer Far Left (OpenClaw) -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -6; 0 0" dur="4s" repeatCount="indefinite" begin="0.9s" />
        <image :href="openclawLogo" x="0" y="370" width="36" height="36" />
        <text x="18" y="420" font-family="monospace" font-size="10" font-weight="bold" fill="#111827" text-anchor="middle">OpenClaw</text>
      </g>
      <!-- 5. Outer Mid Left (Notion) -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -6; 0 0" dur="5s" repeatCount="indefinite" begin="1.2s" />
        <image :href="notionLogo" x="62" y="262" width="36" height="36" />
        <text x="80" y="312" font-family="monospace" font-size="10" font-weight="bold" fill="#111827" text-anchor="middle">Notion</text>
      </g>
      <!-- 6. Outer Top (Claude) -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -6; 0 0" dur="6s" repeatCount="indefinite" begin="1.5s" />
        <image :href="claudeLogo" x="232" y="192" width="36" height="36" />
        <text x="250" y="242" font-family="monospace" font-size="10" font-weight="bold" fill="#111827" text-anchor="middle">Claude</text>
      </g>
      <!-- 7. Outer Mid Right (Chrome) -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -6; 0 0" dur="4s" repeatCount="indefinite" begin="1.8s" />
        <image :href="chromeLogo" x="402" y="262" width="36" height="36" />
        <text x="420" y="312" font-family="monospace" font-size="10" font-weight="bold" fill="#111827" text-anchor="middle">Chrome</text>
      </g>
      <!-- 8. Outer Far Right (ChatGPT) -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0 0; 0 -6; 0 0" dur="5s" repeatCount="indefinite" begin="2.1s" />
        <image :href="openaiLogo" x="464" y="370" width="36" height="36" />
        <text x="482" y="420" font-family="monospace" font-size="10" font-weight="bold" fill="#111827" text-anchor="middle">ChatGPT</text>
      </g>
    </svg>
  </div>
</template>

<script setup>
import geminiLogo from '@/assets/gemini-color.svg';
import antigravityLogo from '@/assets/Google-Antigravity-Icon-Full-Color.png';
import perplexityLogo from '@/assets/perplexity-color.svg';
import openclawLogo from '@/assets/openclaw-color.svg';
import notionLogo from '@/assets/notion-svgrepo-com.svg';
import claudeLogo from '@/assets/claude-color.svg';
import chromeLogo from '@/assets/chrome-logo-svgrepo-com.svg';
import openaiLogo from '@/assets/openai.svg';
</script>

