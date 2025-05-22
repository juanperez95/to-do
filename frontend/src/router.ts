import { createRouter, createWebHistory } from "vue-router";
import Main from "./pages/main.vue";
import Todos from "./pages/todos.vue";

// Rutas del aplicativo
const routes = [
    { path: "/", component: Todos },
    { path: "/crear-usuario", component: Main },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
})
// Exportar router
export default router;