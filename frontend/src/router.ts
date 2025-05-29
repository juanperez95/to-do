import { createRouter, createWebHistory } from "vue-router";
import Main from "./pages/main.vue";
import Todos from "./pages/todos.vue";
import ActualizarTodo from "./pages/actualizar_todo.vue";


// Rutas del aplicativo
const routes = [
    { path: "/", component: Todos },
    { path: "/crear-usuario", component: Main },
    { path: "/actualizar-todo/:id",component:ActualizarTodo , meta: { requiresAuth: true } }, // Ruta protegida debe estar autenticado
];

const router = createRouter({
    history: createWebHistory(),
    routes,
})

// guardia para validar los rutas protegidas
router.beforeEach(async(to, from, next) => {

    // Validar si existe el token de acceso
    let token = localStorage.getItem("access_token");
    if(to.meta.requiresAuth && !token){
        next("/");
    }else{
        next();
    }
});

// Exportar router
export default router;