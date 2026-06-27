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
    logo: '/logo.png',
    siteTitle: false,

    nav: [
      { text: '← Dashboard', link: 'https://memwyre.tech/dashboard' },
      { text: 'Blog', link: 'https://memwyre.tech/blog/' }
    ],

    sidebar: {
      '/integrations/mcp-server': [
        {
          text: 'MCP Server',
          items: [
            { text: 'Overview', link: '/integrations/mcp-server' },
            { text: 'CLI Auto-Installer', link: '/integrations/cli-installer' },
            { text: 'Claude Desktop', link: '/integrations/mcp-server/claude' },
            { text: 'Cursor', link: '/integrations/mcp-server/cursor' },
            { text: 'VS Code', link: '/integrations/mcp-server/vscode' }
          ]
        }
      ],
      '/integrations/plugins': [
        {
          text: 'Plugins',
          items: [
            { text: 'OpenClaw Plugin', link: '/integrations/plugins/openclaw' },
            { text: 'Claude Code Plugin', link: '/integrations/plugins/claude' }
          ]
        }
      ],
      '/': [
        {
          text: 'Getting Started',
          items: [
            { text: 'Overview', link: '/' },
            { text: 'Use Cases', link: '/use-cases' },
            { text: 'Self-Hosting', link: '/self-hosting' }
          ]
        },
        {
          text: 'Concepts',
          items: [
            { text: 'How It Works', link: '/how-it-works' },
            { text: 'RAG vs. Memory', link: '/rag-vs-memory' },
            { text: 'Benchmarks', link: '/benchmarks' },
            { text: 'Security & Privacy', link: '/security' }
          ]
        }
      ]
    },

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
