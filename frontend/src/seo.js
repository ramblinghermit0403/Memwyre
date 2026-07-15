export const SITE_URL = 'https://memwyre.tech';
export const SITE_NAME = 'Memwyre';
export const DEFAULT_SOCIAL_IMAGE_PATH = '/sequence/ezgif-frame-015.png';
export const PRERENDER_ROUTES = [
  '/', '/use-cases', '/pricing', '/privacy-policy', '/terms', '/connectors', '/mcp', '/plugins', '/extension',
  '/blog',
  '/blog/mcp-persistent-memory',
  '/blog/cursor-vs-claude-code-context',
  '/blog/rag-vs-memory-long-term-knowledge',
  '/blog/vscode-mcp-persistent-memory',
  '/blog/claude-code-memory-ingestion',
  '/blog/openclaw-autonomous-memory',
  '/blog/state-of-ai-memory-2026',
  '/research/what-is-ai-memory',
  '/ai-memory-benchmark-locomo',
  '/research',
  '/memwyre-vs-mem0', '/memwyre-vs-supermemory', '/memwyre-vs-zep',
  '/chatgpt-memory', '/claude-memory', '/cursor-memory', '/mcp-memory',
  '/contact',
  '/login',
  '/signup',
  '/dashboard',
  '/forgot-password'
];

export const DEFAULT_SEO = {
  title: 'Memwyre | AI Memory Platform — Persistent Shared Memory for Every AI',
  description:
    'Memwyre is the AI Memory Platform that gives every AI tool, agent, and conversation a persistent, shared memory. Connect to Cursor, VS Code, ChatGPT, Claude, and more.',
  ogType: 'website',
  twitterCard: 'summary_large_image',
};

export const PUBLIC_ROUTE_SEO = {
  '/contact': {
    title: 'Contact Us | Memwyre — Support, Sales & Partnerships',
    description:
      'Get in touch with the Memwyre team. Reach out directly to himansh@memwyre.tech or submit a message for developer support and sales inquiries.',
  },
  '/': {
    title: 'Memwyre | AI Memory Platform — Persistent Shared Memory for Every AI',
    description:
      'Memwyre is the AI Memory Platform that gives every AI tool, agent, and conversation a persistent, shared memory. Connect to Cursor, VS Code, ChatGPT, Claude, and more.',
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
      'Connect Memwyre to Claude Desktop as a Model Context Protocol (MCP) server. Give your local Claude assistant a persistent long-term memory layer.',
    ogImage: '/blog-covers/mcp-persistent-memory.png',
  },
  '/blog/vscode-mcp-persistent-memory': {
    title: 'How to Enable Persistent Codebase Memory in VS Code | Memwyre Blog',
    description:
      'Configure remote MCP memory gateway for VS Code agentic extensions like Cline, Roo-Code, and Devins. Stop starting from scratch each session.',
    ogImage: '/blog-covers/vscode-mcp-persistent-memory.png',
  },
  '/blog/claude-code-memory-ingestion': {
    title: 'Building Persistent Terminal Sessions: Claude Code Memory | Memwyre Blog',
    description:
      'Integrate Memwyre lifecycle hooks into Anthropic\'s Claude Code CLI. Inject workspace context on startup and automatically ingest terminal chats on exit.',
    ogImage: '/blog-covers/claude-code-memory-ingestion.png',
  },
  '/blog/openclaw-autonomous-memory': {
    title: 'Persistent Memory for Autonomous Agents: OpenClaw | Memwyre Blog',
    description:
      'Load the Memwyre plugin for OpenClaw autonomous coding agents. Enable long-term memory query tools and persistent inbox updates across agent runs.',
    ogImage: '/blog-covers/openclaw-autonomous-memory.png',
  },
  '/blog/cursor-vs-claude-code-context': {
    title: 'Cursor AI vs Claude Code: Managing Context and Memory | Memwyre Blog',
    description:
      'Compare workspace indexing and memory management between Cursor AI and Claude Code CLI. Learn how to plug both into a unified memory layer.',
    ogImage: '/blog-covers/cursor-vs-claude-code-context.png',
  },
  '/blog/rag-vs-memory-long-term-knowledge': {
    title: 'RAG vs. AI Memory: Choosing the Right Approach | Memwyre Blog',
    description:
      'Analyze why basic RAG fails for developer workflows due to chunk fragmentation, and why entity-profile routing provides better context.',
    ogImage: '/blog-covers/rag-vs-memory-long-term-knowledge.png',
  },
  '/blog/state-of-ai-memory-2026': {
    title: 'State of AI Memory 2026: Shift from Stateless to Stateful | Memwyre Blog',
    description:
      'An inspection of context window explosion and why stateless attention buffers create substantial financial and latency overheads for enterprise codebase scale.',
    ogImage: '/blog-covers/state-of-ai-memory-2026.png',
  },
  '/blog/:slug': {
    title: 'Memwyre Blog | Engineering Insights & Developer Guides',
    description:
      'Latest guides, insights, and updates on building persistent AI workflows from the Memwyre engineering team.',
  },
  '/research/:slug': {
    title: 'Memwyre Research | AI Memory & Retrieval Studies',
    description:
      'Deep dives, evaluations, and benchmarks from the Memwyre Research Lab on long-term AI memory architectures.',
  },
  '/research/what-is-ai-memory': {
    title: 'What is AI Memory? Long-Term Persistent Context for AI Agents',
    description: 'Learn the architectural principles of long-term AI memory, comparing entity memory graphs, vector databases, and forgetting decay curves for agentic workflows.',
  },
  '/ai-memory-benchmark-locomo': {
    title: 'LoCoMo Benchmark Report | Evaluating AI Memory Networks',
    description: 'Read the LoCoMo Benchmark Report: methodology, datasets, competitors, findings, and conclusions comparing Memwyre, Mem0, Zep, and Supermemory.',
    ogImage: '/blog-covers/ai-memory-benchmark-locomo.png',
  },
  '/research': {
    title: 'Memwyre Research Hub | Advancing AI Long-Term Context Retention',
    description: 'Explore studies, whitepapers, and experiments on context density, memory graphs, and RAG retrieval optimizations by the Memwyre Research Lab.',
  },
  '/memwyre-vs-mem0': {
    title: 'Memwyre vs Mem0 | Graph Memory vs Flat Vector Lists',
    description: 'Compare Memwyre and Mem0: side-by-side feature comparison, latency benchmarks, and client-side developer integration support.',
  },
  '/memwyre-vs-supermemory': {
    title: 'Memwyre vs Supermemory | Developer Context vs Personal Bookmarks',
    description: 'Analyze differences between developer-first memory layers and personal search engines. Compare latency, MCP configs, and workspace tools.',
  },
  '/memwyre-vs-zep': {
    title: 'Memwyre vs Zep | Active Workspace Graph vs Session Chat History',
    description: 'Compare Memwyre and Zep: active developer client integrations and entity mapping vs backend database session history logs.',
  },
  '/chatgpt-memory': {
    title: 'ChatGPT Memory | Persistent Context & Long-Term Memory for OpenAI',
    description: 'Connect ChatGPT to a unified, long-term memory graph. Save developer guidelines, schemas, and context across all your browser chat sessions.',
  },
  '/claude-memory': {
    title: 'Claude Memory | Persistent long-term memory for Claude Desktop & Code',
    description: 'Setup persistent long-term memory for Anthropic Claude Desktop and Claude Code CLI. Secure, private context updates via remote MCP server gateway.',
  },
  '/cursor-memory': {
    title: 'Cursor Memory | Long-Term Codebase Context for Cursor AI IDE',
    description: 'Enable sub-300ms persistent memory for Cursor Composer and Chat. Save developer rules and databases context to avoid index rebuilding.',
  },
  '/mcp-memory': {
    title: 'MCP Memory Server | Universal Context Layer for All MCP Clients',
    description: 'Link any Model Context Protocol (MCP) client to your personal memory layer. Secure, remote context gateway supporting Cursor, Claude, VS Code, and Windsurf.',
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
  const defaultImageUrl = `${SITE_URL}${DEFAULT_SOCIAL_IMAGE_PATH}`;
  const socialImageUrl = routeSeo.ogImage ? `${SITE_URL}${routeSeo.ogImage}` : defaultImageUrl;

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
            'text': 'Memwyre is a unified AI memory platform that captures your context across tools (browser, ChatGPT, Claude, Cursor) so you never lose an insight, code snippet, or research finding. It makes this knowledge instantly searchable and reusable by any tool.'
          }
        },
        {
          '@type': 'Question',
          'name': 'Is there a free plan?',
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': 'Yes! Memwyre has a generous free tier that includes up to 50 memories, 10 document uploads, 30 AI chat messages, and full IDE integration via MCP. No credit card required — just sign up and start building your memory layer.'
          }
        },
        {
          '@type': 'Question',
          'name': 'How do I connect Memwyre to Cursor or VS Code?',
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': 'You can connect Memwyre to Cursor, VS Code, or Claude Desktop using our official Model Context Protocol (MCP) server. This gives your AI assistant direct, real-time access to your entire shared memory layer.'
          }
        },
        {
          '@type': 'Question',
          'name': 'Do you offer a browser extension?',
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': 'Yes! The Memwyre browser extension (available for Chrome and Edge) lets you instantly clip text, articles, and code snippets directly into your memory layer without breaking your flow.'
          }
        },
        {
          '@type': 'Question',
          'name': 'Is my data private and secure?',
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': 'Absolutely. Your memory layer is fully private and encrypted. Your data is only accessible to you via authenticated sessions and your personal API keys.'
          }
        },
        {
          '@type': 'Question',
          'name': 'What is the OpenClaw plugin?',
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': 'The OpenClaw plugin allows autonomous AI agents to read from and write to your Memwyre memory layer. This gives agents persistent memory across runs, letting them build on past debugging sessions and research.'
          }
        },
        {
          '@type': 'Question',
          'name': 'Why not just use ChatGPT\'s built-in memory?',
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': 'ChatGPT memory is locked entirely inside ChatGPT. It cannot be accessed by Claude, Cursor, your terminal agents, or other LLMs. Memwyre acts as a universal, shared memory layer that works across all of these tools simultaneously.'
          }
        },
        {
          '@type': 'Question',
          'name': 'How is this different from traditional RAG?',
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': 'Traditional RAG search takes static documents, chunks them, and searches for matches. Memwyre builds active, connected semantic profiles of your project guidelines, API models, and style rules, updating them dynamically in the background.'
          }
        },
        {
          '@type': 'Question',
          'name': 'How does Memwyre compare to Mem0 or Zep?',
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': 'Mem0 and Zep are developer databases designed as backend infrastructure for teams building custom agents. Memwyre is a ready-to-use memory platform that connects directly to everyday consumer tools.'
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
      'description': 'Memwyre is a unified AI memory platform that captures your context across tools (browser, ChatGPT, Claude, Cursor) so you never lose an insight, code snippet, or research finding. It then makes this knowledge instantly searchable and reusable.'
    });
  }

  // Dynamic Schema Injection
  if (normalizedPath.startsWith('/blog/') && normalizedPath !== '/blog') {
    const slug = normalizedPath.split('/').pop();
    const blogDates = {
      'mcp-persistent-memory': '2026-06-15T08:00:00Z',
      'vscode-mcp-persistent-memory': '2026-06-02T08:00:00Z',
      'claude-code-memory-ingestion': '2026-05-18T08:00:00Z',
      'openclaw-autonomous-memory': '2026-05-04T08:00:00Z',
      'cursor-vs-claude-code-context': '2026-04-22T08:00:00Z',
      'state-of-ai-memory-2026': '2026-04-18T08:00:00Z',
      'rag-vs-memory-long-term-knowledge': '2026-04-09T08:00:00Z'
    };
    const pubDate = blogDates[slug] || '2026-03-01T08:00:00Z';
    jsonLdData.push({
      '@context': 'https://schema.org',
      '@type': 'BlogPosting',
      'headline': routeSeo.title || DEFAULT_SEO.title,
      'description': routeSeo.description || DEFAULT_SEO.description,
      'image': socialImageUrl,
      'datePublished': pubDate,
      'dateModified': pubDate,
      'author': {
        '@type': 'Person',
        'name': 'Himansh Shivhare'
      },
      'publisher': {
        '@type': 'Organization',
        'name': SITE_NAME,
        'logo': {
          '@type': 'ImageObject',
          'url': `${SITE_URL}/image.svg`
        }
      },
      'url': canonical
    });
  } else if (normalizedPath === '/what-is-ai-memory' || normalizedPath === '/ai-memory-benchmark-locomo') {
    const techDates = {
      '/what-is-ai-memory': '2026-03-10T08:00:00Z',
      '/ai-memory-benchmark-locomo': '2026-03-25T08:00:00Z'
    };
    const pubDate = techDates[normalizedPath] || '2026-03-01T08:00:00Z';
    jsonLdData.push({
      '@context': 'https://schema.org',
      '@type': 'TechArticle',
      'headline': routeSeo.title || DEFAULT_SEO.title,
      'description': routeSeo.description || DEFAULT_SEO.description,
      'image': socialImageUrl,
      'datePublished': pubDate,
      'dateModified': pubDate,
      'author': {
        '@type': 'Organization',
        'name': 'Memwyre Research Lab'
      },
      'publisher': {
        '@type': 'Organization',
        'name': SITE_NAME,
        'logo': {
          '@type': 'ImageObject',
          'url': `${SITE_URL}/image.svg`
        }
      },
      'url': canonical
    });
  } else if (['/chatgpt-memory', '/claude-memory', '/cursor-memory', '/mcp-memory'].includes(normalizedPath)) {
    jsonLdData.push({
      '@context': 'https://schema.org',
      '@type': 'SoftwareApplication',
      'name': `${SITE_NAME} Integration`,
      'applicationCategory': 'DeveloperApplication',
      'operatingSystem': 'Windows, macOS, Linux, ChromeOS',
      'image': socialImageUrl,
      'offers': {
        '@type': 'Offer',
        'price': '0',
        'priceCurrency': 'USD',
        'availability': 'https://schema.org/InStock'
      },
      'description': routeSeo.description || DEFAULT_SEO.description
    });
  } else if (['/memwyre-vs-mem0', '/memwyre-vs-supermemory', '/memwyre-vs-zep'].includes(normalizedPath)) {
    jsonLdData.push({
      '@context': 'https://schema.org',
      '@type': 'Product',
      'name': routeSeo.title || DEFAULT_SEO.title,
      'image': socialImageUrl,
      'description': routeSeo.description || DEFAULT_SEO.description,
      'brand': {
        '@type': 'Brand',
        'name': SITE_NAME
      },
      'offers': {
        '@type': 'Offer',
        'price': '0',
        'priceCurrency': 'USD',
        'availability': 'https://schema.org/InStock'
      }
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
    ogSiteName: SITE_NAME,
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
