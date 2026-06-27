<template>
  <div class="subnav-wrapper">
    <div class="subnav-container">
      <a 
        v-for="item in items" 
        :key="item.text" 
        :href="withBase(item.link)" 
        class="subnav-item"
        :class="{ active: isActive(item) }"
      >
        <span class="subnav-icon-wrapper">
          <img v-if="item.icon.startsWith('http')" :src="item.icon" class="subnav-icon-img" />
          <span v-else v-html="item.icon" class="subnav-icon-svg-inline"></span>
        </span>
        <span class="subnav-text">{{ item.text }}</span>
      </a>
    </div>
  </div>
</template>

<script setup>
import { useRoute, withBase } from 'vitepress'
import { computed } from 'vue'

const route = useRoute()

const items = [
  {
    text: 'Developer Platform',
    link: '/',
    icon: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>`,
    match: (path) => path === '/' || path === '/index.html' || path.includes('/self-hosting') || path.includes('/security')
  },
  {
    text: 'Workspace Connectors',
    link: '/integrations/connectors',
    icon: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>`,
    match: (path) => path.includes('/connectors')
  },
  {
    text: 'Browser Extension',
    link: '/integrations/browser-extension',
    icon: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="3" y1="9" x2="21" y2="9"/></svg>`,
    match: (path) => path.includes('/browser-extension')
  },
  {
    text: 'MCP Server',
    link: '/integrations/mcp-server',
    icon: 'https://unpkg.com/@lobehub/icons-static-svg@latest/icons/mcp.svg',
    match: (path) => path.includes('/mcp-server') || path.includes('/cli-installer')
  },
  {
    text: 'Plugins',
    link: '/integrations/plugins/openclaw',
    icon: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>`,
    match: (path) => path.includes('/plugins/')
  }
]

const isActive = (item) => {
  let path = route.path
  if (path.startsWith('/docs')) {
    path = path.slice(5)
  }
  return item.match(path)
}
</script>

<style scoped>
.subnav-wrapper {
  position: absolute;
  top: 64px;
  left: 0;
  width: 100%;
  height: 48px;
  background-color: transparent !important;
  border-bottom: none !important;
  z-index: 99;
  pointer-events: auto !important;
  overflow-x: auto;
  scrollbar-width: none;
}

.subnav-wrapper::-webkit-scrollbar {
  display: none;
}

.subnav-container {
  display: flex;
  align-items: center;
  gap: 28px;
  height: 100%;
  padding: 0 24px;
  margin: 0 auto;
  max-width: calc(var(--vp-layout-max-width) - 64px);
  width: 100%;
  box-sizing: border-box;
}

@media (min-width: 768px) {
  .subnav-container {
    padding: 0 32px;
  }
}

/* Align perfectly with the main navbar logo on desktop with sidebar */
@media (min-width: 960px) {
  .VPNavBar.has-sidebar .subnav-container {
    max-width: 100%;
    margin: 0;
    padding-left: 32px;
  }
}

@media (min-width: 1440px) {
  .VPNavBar.has-sidebar .subnav-container {
    padding-left: max(32px, calc((100% - (var(--vp-layout-max-width) - 64px)) / 2));
    padding-right: max(32px, calc((100% - (var(--vp-layout-max-width) - 64px)) / 2));
  }
}

.subnav-item {
  height: 100%;
  display: flex;
  align-items: center;
  gap: 8px;
  color: #475569;
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 500;
  letter-spacing: -0.01em;
  border-bottom: 2px solid transparent;
  transition: color 0.15s ease, border-color 0.15s ease;
  white-space: nowrap;
  cursor: pointer;
}

.subnav-item:hover {
  color: #0f172a;
}

.subnav-item.active {
  color: #0f172a;
  font-weight: 600;
  border-bottom: 2px solid #2563eb;
}

.dark .subnav-item {
  color: #94a3b8;
}

.dark .subnav-item:hover {
  color: #f8fafc;
}

.dark .subnav-item.active {
  color: #f8fafc;
  border-bottom: 2px solid #3b82f6;
}

.subnav-icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  color: #64748b;
  transition: color 0.15s ease;
}

.subnav-item:hover .subnav-icon-wrapper,
.subnav-item.active .subnav-icon-wrapper {
  color: #0f172a;
}

.dark .subnav-icon-wrapper {
  color: #94a3b8;
}

.dark .subnav-item:hover .subnav-icon-wrapper,
.dark .subnav-item.active .subnav-icon-wrapper {
  color: #f8fafc;
}

.subnav-icon-img {
  width: 14px;
  height: 14px;
  object-fit: contain;
}

.subnav-icon-svg-inline {
  display: flex;
  align-items: center;
  justify-content: center;
}

.subnav-item :deep(svg) {
  width: 14px;
  height: 14px;
  stroke-width: 2px;
}
</style>
