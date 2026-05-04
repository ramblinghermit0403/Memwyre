import { defineConfig } from 'vitepress'

export default defineConfig({
  outDir: '../dist/docs',
  base: '/docs/',
  appearance: false,
  title: 'Memwyre',
  titleTemplate: ':title — Memwyre Docs',
  description: 'Official documentation for Memwyre — the universal memory layer for AI.',

  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/docs/image.svg' }],
    ['meta', { name: 'theme-color', content: '#111111' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:site_name', content: 'Memwyre Docs' }],
  ],

  themeConfig: {
    logo: '/image.svg',
    siteTitle: 'Memwyre',

    nav: [
      { text: 'Home', link: '/' },
      { text: 'Features', link: '/features/web-ingestion' },
      { text: 'Integrations', link: '/integrations/' },
      { text: 'GitHub', link: 'https://github.com/ramblinghermit0403/Memwyre' },
      { text: '← Back to App', link: 'https://memwyre.tech/' }
    ],

    sidebar: [
      {
        text: 'Getting Started',
        items: [
          { text: 'Overview', link: '/' },
          { text: 'Introduction', link: '/introduction' }
        ]
      },
      {
        text: 'Platform Features',
        items: [
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
      { icon: 'github', link: 'https://github.com/ramblinghermit0403/Memwyre' }
    ],

    footer: {
      message: 'Built with ❤️ by the Memwyre team.',
      copyright: `Copyright © ${new Date().getFullYear()} Memwyre. All rights reserved.`
    },

    search: {
      provider: 'local'
    },

    editLink: false,

    lastUpdated: false
  }
})
