export const SITE_URL = 'https://memwyre.tech';
export const SITE_NAME = 'Memwyre';
export const DEFAULT_SOCIAL_IMAGE_PATH = '/sequence/ezgif-frame-015.png';
export const PRERENDER_ROUTES = ['/', '/use-cases', '/pricing', '/privacy-policy', '/terms'];

export const DEFAULT_SEO = {
  title: 'Memwyre | AI Memory Vault for ChatGPT, Claude and More',
  description:
    'Capture prompts, conversations, and research context across AI tools. Memwyre helps your knowledge compound so you can reuse insights faster.',
  ogType: 'website',
  twitterCard: 'summary_large_image',
};

export const PUBLIC_ROUTE_SEO = {
  '/': {
    title: 'Memwyre | AI Memory Vault for ChatGPT, Claude and More',
    description:
      'Capture prompts, conversations, and research context across AI tools. Memwyre helps your knowledge compound so you can reuse insights faster.',
  },
  '/use-cases': {
    title: 'Memwyre Use Cases | AI Workflow Memory for Teams and Builders',
    description:
      'See how engineers, researchers, students, and product teams use Memwyre to retain AI context, reduce repeated work, and move faster.',
  },
  '/pricing': {
    title: 'Memwyre Pricing | Plans for Individuals and Teams',
    description:
      'Choose the plan that fits your AI workflow. Free for personal use, Pro for teams needing persistent memory and advanced integrations.',
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
    jsonLd: JSON.stringify(getDefaultJsonLd(), null, 2),
  };
}
