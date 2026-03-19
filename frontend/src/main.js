import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './style.css'
import App from './App.vue'
import router from './router'

import Toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'

// Force light mode globally, independent of browser/system preference.
document.documentElement.classList.remove('dark')
document.documentElement.style.colorScheme = 'light'
localStorage.setItem('theme', 'light')

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(Toast, {
    position: "bottom-right",
    timeout: 3000,
    toastClassName: "brain-vault-toast",
})

// Inject Plausible Analytics
if (import.meta.env.VITE_PLAUSIBLE_DOMAIN) {
    const script1 = document.createElement('script')
    script1.async = true
    script1.setAttribute('src', 'https://plausible.io/js/pa-fZ5pVYBXSKSV46Szlu3S4.js')
    document.head.appendChild(script1)

    const script2 = document.createElement('script')
    script2.innerHTML = `window.plausible=window.plausible||function(){(plausible.q=plausible.q||[]).push(arguments)},plausible.init=plausible.init||function(i){plausible.o=i||{}};plausible.init()`
    document.head.appendChild(script2)
}

app.mount('#app')
