import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { access, mkdir, readFile, readdir, rm, writeFile } from 'node:fs/promises';
import { getSeoForPath, PRERENDER_ROUTES } from '../src/seo.js';

const currentDir = path.dirname(fileURLToPath(import.meta.url));
const frontendDir = path.resolve(currentDir, '..');
const distDir = path.join(frontendDir, 'dist');
const clientTemplatePath = path.join(distDir, 'index.html');
const serverDir = path.join(distDir, 'server');

function escapeRegExp(value) {
    return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function escapeHtml(value) {
    return String(value)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
}

function replaceMetaTag(html, attrName, attrValue, content) {
    const pattern = new RegExp(
        `<meta\\s+[^>]*${attrName}="${escapeRegExp(attrValue)}"[^>]*>`,
        'i'
    );
    const replacement = `<meta ${attrName}="${attrValue}" content="${escapeHtml(content)}" />`;
    return html.replace(pattern, replacement);
}

function replaceCanonical(html, canonicalUrl) {
    return html.replace(
        /<link\s+rel="canonical"[^>]*>/i,
        `<link rel="canonical" href="${escapeHtml(canonicalUrl)}" />`
    );
}

function replaceJsonLd(html, jsonLd) {
    const escapedJson = jsonLd.replace(/<\/script>/gi, '<\\/script>');
    return html.replace(
        /<script id="seo-ld-json" type="application\/ld\+json">[\s\S]*?<\/script>/i,
        `<script id="seo-ld-json" type="application/ld+json">\n${escapedJson}\n  </script>`
    );
}

function withSeoAndContent(template, seo, appHtml, injectedScript = '') {
    let html = template;

    html = html.replace(/<title>[\s\S]*?<\/title>/i, `<title>${escapeHtml(seo.title)}</title>`);
    html = replaceMetaTag(html, 'name', 'description', seo.description);
    html = replaceMetaTag(html, 'name', 'robots', seo.robots);
    html = replaceCanonical(html, seo.canonical);

    html = replaceMetaTag(html, 'property', 'og:title', seo.ogTitle);
    html = replaceMetaTag(html, 'property', 'og:description', seo.ogDescription);
    html = replaceMetaTag(html, 'property', 'og:type', seo.ogType);
    html = replaceMetaTag(html, 'property', 'og:url', seo.ogUrl);
    html = replaceMetaTag(html, 'property', 'og:image', seo.ogImage);
    html = replaceMetaTag(html, 'property', 'og:image:width', seo.ogImageWidth);
    html = replaceMetaTag(html, 'property', 'og:image:height', seo.ogImageHeight);

    html = replaceMetaTag(html, 'name', 'twitter:card', seo.twitterCard);
    html = replaceMetaTag(html, 'name', 'twitter:title', seo.twitterTitle);
    html = replaceMetaTag(html, 'name', 'twitter:description', seo.twitterDescription);
    html = replaceMetaTag(html, 'name', 'twitter:image', seo.twitterImage);
    html = replaceJsonLd(html, seo.jsonLd);

    if (injectedScript) {
        html = html.replace('<!--app-html-->', `${injectedScript}<!--app-html-->`);
    }

    return html.replace('<!--app-html-->', appHtml);
}

async function resolveServerBundlePath() {
    const candidates = [
        path.join(serverDir, 'entry-server.js'),
        path.join(serverDir, 'entry-server.mjs'),
    ];

    for (const candidate of candidates) {
        try {
            await access(candidate);
            return candidate;
        } catch {
            // Keep searching.
        }
    }

    const files = await readdir(serverDir);
    const fallback = files.find((file) => file.endsWith('.js') || file.endsWith('.mjs'));
    if (!fallback) {
        throw new Error('No SSR server bundle found in dist/server.');
    }

    return path.join(serverDir, fallback);
}

async function prerender() {
    const template = await readFile(clientTemplatePath, 'utf-8');
    const serverBundlePath = await resolveServerBundlePath();
    const serverEntryUrl = `${pathToFileURL(serverBundlePath).href}?v=${Date.now()}`;
    const { render } = await import(serverEntryUrl);

    for (const route of PRERENDER_ROUTES) {
        const { appHtml } = await render(route);
        const seo = getSeoForPath(route);

        let injectedScript = '';
        if (route.startsWith('/blog/') && route !== '/blog') {
            const slug = route.substring('/blog/'.length);
            const mdPath = path.join(frontendDir, 'src', 'assets', 'blog', `${slug}.md`);
            try {
                const content = await readFile(mdPath, 'utf-8');
                const escapedContent = JSON.stringify({ slug, content });
                injectedScript = `<script id="pre-rendered-data">window.__BLOG_POST_DATA__ = ${escapedContent};</script>`;
            } catch (err) {
                console.error(`Failed to read markdown file for route ${route}:`, err);
            }
        }

        const routeHtml = withSeoAndContent(template, seo, appHtml, injectedScript);

        const outputPath = route === '/'
            ? path.join(distDir, 'index.html')
            : path.join(distDir, route.replace(/^\//, ''), 'index.html');

        await mkdir(path.dirname(outputPath), { recursive: true });
        await writeFile(outputPath, routeHtml, 'utf-8');
    }

    await rm(serverDir, { recursive: true, force: true });
}

await prerender();
