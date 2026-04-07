import './style.css'
import { createMemWyreApp } from './app'

import Toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'

const { app } = createMemWyreApp()
app.use(Toast, {
    position: "bottom-right",
    timeout: 3000,
    toastClassName: "brain-vault-toast",
})

app.mount('#app')
