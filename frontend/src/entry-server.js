import { renderToString } from '@vue/server-renderer';
import { createMemWyreApp } from './app';

export async function render(url) {
    const { app, router } = createMemWyreApp({ ssr: true });

    await router.push(url);
    await router.isReady();

    const appHtml = await renderToString(app);
    return { appHtml };
}
