import { createApp as createClientApp, createSSRApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router, { createAppRouter } from './router';

export function createMemWyreApp({ ssr = false } = {}) {
    const app = ssr ? createSSRApp(App) : createClientApp(App);
    const pinia = createPinia();
    const appRouter = ssr ? createAppRouter({ ssr: true }) : router;

    app.use(pinia);
    app.use(appRouter);

    return { app, pinia, router: appRouter };
}
