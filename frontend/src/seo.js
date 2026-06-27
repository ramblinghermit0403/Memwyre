export const SITE_URL = 'https://memwyre.tech';
export const SITE_NAME = 'Memwyre';
export const DEFAULT_SOCIAL_IMAGE_PATH = '/sequence/ezgif-frame-015.png';
export const PRERENDER_ROUTES = [
  '/', '/use-cases', '/pricing', '/privacy-policy', '/terms', '/connectors', '/mcp', '/plugins', '/rag', '/memory-graph', '/personal', '/extension',
  '/blog',
  '/blog/mcp-persistent-memory',
  '/blog/cursor-vs-claude-code-context',
  '/blog/rag-vs-memory-long-term-knowledge',
  '/blog/vscode-mcp-persistent-memory',
  '/blog/claude-code-memory-ingestion',
  '/blog/openclaw-autonomous-memory'
];

export const DEFAULT_SEO = {
  title: 'Memwyre | AI Memory Vault — Stop repeating to every AI tool',
  description:
    'Memwyre turns your prompts, conversations, and research into a persistent memory layer you can reuse anywhere you work with AI. Connect to Cursor, VS Code, ChatGPT, Claude, and more.',
  ogType: 'website',
  twitterCard: 'summary_large_image',
};

export const PUBLIC_ROUTE_SEO = {
  '/': {
    title: 'Memwyre | AI Memory Vault — Stop repeating to every AI tool',
    description:
      'Memwyre turns your prompts, conversations, and research into a persistent memory layer you can reuse anywhere you work with AI. Connect to Cursor, VS Code, ChatGPT, Claude, and more.',
  },
  '/use-cases': {
    title: 'Memwyre Use Cases | AI Workflow Memory for Teams and Builders',
    description:
      'See how engineers, researchers, students, and product teams use Memwyre to retain AI context, reduce repeated work, and move faster.',
  },
  '/pricing': {
    title: 'Memwyre Pricing | Plans for Individuals and Teams',
    description:
      'Find the plan that fits your AI workflow. Generous free tier with 50 memories and MCP support. Pro includes VS Code, Notion, Google Drive, Claude Code, and Claude Desktop integrations.',
  },
  '/privacy-policy': {
    title: 'Memwyre Privacy Policy | Data Handling, Security, and Retention',
    description:
      'Read how Memwyre collects, processes, secures, and deletes data across the web app, extension, and MCP integrations.',
  },
  '/terms': {
    title: 'Memwyre Terms of Service | Platform Rules and Responsibilities',
    description:
      'Review Memwyre Terms of Service, including account use, acceptable behavior, billing expectations, and service limitations.',
  },
  '/connectors': {
    title: 'Connectors — Memwyre | Real-time Data Sync for AI Agents',
    description:
      'Pull context automatically from Notion, Google Drive, Gmail, GitHub, S3, and more. Configure once and keep your AI agent\'s context fresh in real time.',
  },
  '/mcp': {
    title: 'MCP — Memwyre | Universal Model Context Protocol Integrations',
    description:
      'Connect Memwyre memory layers directly to Claude, Cursor, Windsurf, VS Code, and any Model Context Protocol (MCP) client. Your context follows you everywhere.',
  },
  '/plugins': {
    title: 'Plugins — Memwyre | Persistent Project Memory for Developer Tools',
    description:
      'Memwyre developer plugins for Claude Code, OpenClaw, OpenCode, and Hermes. One-click memory save, automatic context injection, and project-scoped knowledge.',
  },
  '/rag': {
    title: 'RAG — Memwyre | Latency-optimized Hybrid Search & Retrieval',
    description:
      'Sub-300ms retrieval using advanced Hybrid Search. Multi-modal RAG support for PDFs, markdown, videos, audio, and web pages with context-aware reranking.',
  },
  '/memory-graph': {
    title: 'Memory Graph — Memwyre | Living Connected Knowledge Graphs',
    description:
      'An evolving knowledge graph where memories build relationships. Features automatic entity extraction, Updates/Extends/Derives connections, and built-in forgetting.',
  },
  '/personal': {
    title: 'Personal App — Memwyre | Stretched Cross-Platform AI Memory',
    description:
      'A single context layer for all the AI you use. Save memory once and query it directly using Memwyre inside Claude, Cursor, ChatGPT, and your workspace.',
  },
  '/extension': {
    title: 'Chrome Extension — Memwyre | Capture Web Context Instantly',
    description:
      'Save AI chats, reusable prompts, code snippets, and webpage content directly from ChatGPT, Claude, and any site with a single click.',
  },
  '/blog': {
    title: 'Memwyre Blog | Guides, Updates & AI Memory Engineering Insights',
    description:
      'Explore deep dives on Model Context Protocol (MCP), developer tools integration, vector databases, and workflow optimization from the Memwyre team.',
  },
  '/blog/mcp-persistent-memory': {
    title: 'How to Give Claude Desktop Persistent Memory using MCP | Memwyre Blog',
    description:
      'Connect Memwyre to Claude Desktop as a Model Context Protocol (MCP) server. Give your local Claude assistant a persistent long-term memory vault.',
  },
  '/blog/vscode-mcp-persistent-memory': {
    title: 'How to Enable Persistent Codebase Memory in VS Code | Memwyre Blog',
    description:
      'Configure remote MCP memory gateway for VS Code agentic extensions like Cline, Roo-Code, and Devins. Stop starting from scratch each session.',
  },
  '/blog/claude-code-memory-ingestion': {
    title: 'Building Persistent Terminal Sessions: Claude Code Memory | Memwyre Blog',
    description:
      'Integrate Memwyre lifecycle hooks into Anthropic\'s Claude Code CLI. Inject workspace context on startup and automatically ingest terminal chats on exit.',
  },
  '/blog/openclaw-autonomous-memory': {
    title: 'Persistent Memory for Autonomous Agents: OpenClaw | Memwyre Blog',
    description:
      'Load the Memwyre plugin for OpenClaw autonomous coding agents. Enable long-term memory query tools and persistent inbox updates across agent runs.',
  },
  '/blog/cursor-vs-claude-code-context': {
    title: 'Cursor AI vs Claude Code: Managing Context and Memory | Memwyre Blog',
    description:
      'Compare workspace indexing and memory management between Cursor AI and Claude Code CLI. Learn how to plug both into a unified memory layer.',
  },
  '/blog/rag-vs-memory-long-term-knowledge': {
    title: 'RAG vs. AI Memory: Choosing the Right Approach | Memwyre Blog',
    description:
      'Analyze why basic RAG fails for developer workflows due to chunk fragmentation, and why entity-profile routing provides better context.',
  },
  '/blog/:slug': {
    title: 'Memwyre Blog | Engineering Insights & Developer Guides',
    description:
      'Latest guides, insights, and updates on building persistent AI workflows from the Memwyre engineering team.',
  },
};

export function normalizePath(path = '/') {
  if (!path || path === '/') return '/';
  return path.endsWith('/') ? path.slice(0, -1) : path;
}

export function buildCanonicalUrl(path = '/') {
  const normalizedPath = normalizePath(path);
  return normalizedPath === '/' ? `${SITE_URL}/` : `${SITE_URL}${normalizedPath}`;
}

export function getDefaultJsonLd() {
  return [
    {
      '@context': 'https://schema.org',
      '@type': 'Organization',
      name: SITE_NAME,
      url: `${SITE_URL}/`,
      logo: `${SITE_URL}/image.svg`,
      sameAs: ['https://x.com/Memwyre'],
    },
    {
      '@context': 'https://schema.org',
      '@type': 'WebSite',
      name: SITE_NAME,
      url: `${SITE_URL}/`,
      potentialAction: {
        '@type': 'SearchAction',
        target: `${SITE_URL}/?q={search_term_string}`,
        'query-input': 'required name=search_term_string',
      },
    },
  ];
}

export function getSeoForPath(path = '/') {
  const normalizedPath = normalizePath(path);
  const isIndexable = PRERENDER_ROUTES.includes(normalizedPath);
  const routeSeo = PUBLIC_ROUTE_SEO[normalizedPath] || {};
  const canonical = buildCanonicalUrl(normalizedPath);
  const socialImageUrl = `${SITE_URL}${DEFAULT_SOCIAL_IMAGE_PATH}`;

  const jsonLdData = getDefaultJsonLd();

  if (normalizedPath === '/') {
    // Add FAQPage Schema
    jsonLdData.push({
      '@context': 'https://schema.org',
      '@type': 'FAQPage',
      'mainEntity': [
        {
          '@type': 'Question',
          'name': 'What exactly is Memwyre?',
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': 'Memwyre is a unified AI memory vault that captures your context across tools (browser, ChatGPT, Claude, Cursor) so you never lose an insight, code snippet, or research finding. It then makes this knowledge instantly searchable and reusable.'
          }
        },
        {
          '@type': 'Question',
          'name': 'Is there a free plan?',
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': 'Yes! Memwyre has a generous free tier that includes up to 50 memories, 10 document uploads, 30 AI chat messages, and full IDE integration via MCP. No credit card required — just sign up and start building your brain.'
          }
        },
        {
          '@type': 'Question',
          'name': 'How do I connect Memwyre to Cursor or VS Code?',
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': 'You can connect Memwyre to Cursor, VS Code, or Claude Desktop using our official Model Context Protocol (MCP) server. This gives your AI assistant direct, real-time access to your entire personal knowledge base.'
          }
        },
        {
          '@type': 'Question',
          'name': 'Do you offer a browser extension?',
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': 'Yes! The Memwyre browser extension (available for Chrome and Edge) lets you instantly clip text, articles, and code snippets directly into your vault without breaking your flow.'
          }
        },
        {
          '@type': 'Question',
          'name': 'Is my data private and secure?',
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': 'Absolutely. Your memory vault is fully private and encrypted. Your data is only accessible to you via authenticated sessions and your personal API keys.'
          }
        },
        {
          '@type': 'Question',
          'name': 'What is the OpenClaw plugin?',
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': 'The OpenClaw plugin allows autonomous AI agents to read from and write to your Memwyre vault. This gives agents persistent memory across runs, letting them build on past debugging sessions and research.'
          }
        }
      ]
    });

    // Add SoftwareApplication Schema
    jsonLdData.push({
      '@context': 'https://schema.org',
      '@type': 'SoftwareApplication',
      'name': 'Memwyre',
      'applicationCategory': 'DeveloperApplication',
      'operatingSystem': 'Windows, macOS, Linux, ChromeOS',
      'offers': {
        '@type': 'Offer',
        'price': '0',
        'priceCurrency': 'USD',
        'category': 'Free'
      },
      'description': 'Memwyre is a unified AI memory vault that captures your context across tools (browser, ChatGPT, Claude, Cursor) so you never lose an insight, code snippet, or research finding. It then makes this knowledge instantly searchable and reusable.'
    });
  }

  return {
    title: routeSeo.title || DEFAULT_SEO.title,
    description: routeSeo.description || DEFAULT_SEO.description,
    canonical,
    ogTitle: routeSeo.title || DEFAULT_SEO.title,
    ogDescription: routeSeo.description || DEFAULT_SEO.description,
    ogType: DEFAULT_SEO.ogType,
    ogUrl: canonical,
    ogImage: socialImageUrl,
    ogImageWidth: '1280',
    ogImageHeight: '720',
    twitterCard: DEFAULT_SEO.twitterCard,
    twitterTitle: routeSeo.title || DEFAULT_SEO.title,
    twitterDescription: routeSeo.description || DEFAULT_SEO.description,
    twitterImage: socialImageUrl,
    robots: isIndexable ? 'index, follow' : 'noindex, nofollow',
    jsonLd: JSON.stringify(jsonLdData, null, 2),
  };
}
