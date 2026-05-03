import { defineConfig } from 'vitepress'

export default defineConfig({
  outDir: '../dist/docs',
  base: '/docs/',
  title: "MemWyre Docs",
  description: "Official documentation for MemWyre - Your Second Brain.",
  themeConfig: {
    logo: '/image.svg', // Assuming we copy the logo to docs/public later or point to absolute url
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Integrations', link: '/integrations/' }
    ],
    sidebar: [
      {
        text: 'Platform Features',
        items: [
          { text: 'YouTube Ingestion', link: '/features/youtube-ingestion' },
          { text: 'Web Page Ingestion', link: '/features/web-ingestion' }
        ]
      },
      {
        text: 'Integrations',
        items: [
          { text: 'Browser Extension', link: '/integrations/browser-extension' },
          { text: 'IDEs & Agents (MCP)', link: '/integrations/mcp-server' },
          { text: 'OpenClaw Plugin', link: '/integrations/openclaw-plugin' }
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/memwyre' }
    ]
  }
})
