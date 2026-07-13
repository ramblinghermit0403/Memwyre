import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { PRERENDER_ROUTES } from './src/seo.js'

export const prerenderRoutes = PRERENDER_ROUTES

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  define: {
    __PRERENDER_ROUTES__: JSON.stringify(prerenderRoutes)
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  ssr: {
    noExternal: ['vue-toastification']
  }
})
