import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
// Importar bootstrap
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap'
import router from './router.ts'

// Importar pinia para manejar el estado de la aplicacion
import { createPinia } from 'pinia'
const pinia = createPinia()

createApp(App).
use(router). // Agregar las rutas del router
use(pinia). // Agregar pinia
mount('#app');
