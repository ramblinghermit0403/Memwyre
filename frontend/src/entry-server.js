import { renderToString } from '@vue/server-renderer';
import { createMemwyreApp } from './app';

export async function render(url) {
    const { app, router } = createMemwyreApp({ ssr: true });

    await router.push(url);
    await router.isReady();

    const appHtml = await renderToString(app);
    return { appHtml };
}
