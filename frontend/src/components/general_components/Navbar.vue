<template>
    <div>
        <section>
        <nav class="navbar bg-body-tertiary d-flex justify-content-between">
            <div class="container-fluid">
                <form class="d-flex" role="search" @submit.prevent="busquedaTarea">
                    <input class="form-control me-2" type="search" placeholder="Filtrar tarea" aria-label="Search" v-model="busqueda"/>
                    <button class="btn btn-outline-success" type="submit">Buscar</button>
                </form>
                <!-- Boton de crear tarea (Modal) -->
                <article class="d-flex align-items-center">
                    <article v-if="error">
                        <Modal :is_login="true" id_modal="registerModal"/>
                    </article>
                    <!-- Iniciar sesion -->
                    <article v-if="token && !error">
                        <Modal id_modal="loginModal"/>
                    </article>
                    <article v-if="token && !error">

                        <Boton msg="Cerrar sesion" color="danger" tipo="button" @funcion_btn="cerrarSesion" icono="fa-solid fa-right-from-bracket"/>
                    </article>
                    <!-- Redirigir a la pagina de crear usuario -->
                    <Boton msg="Crear usuario" color="primary" tipo="button" @funcion_btn="()=>{$router.push('/crear-usuario')}" icono="fa-solid fa-user-plus"/>
                </article>
            </div>
        </nav>
        </section>
    </div>
</template>

<script setup lang="ts">
import Modal from './Modal.vue'
import Boton from './Boton.vue'
import { useTodoStore } from '../../stores/todoStore';
import {computed, ref, onMounted} from 'vue';
import { useUserStore } from '../../stores/userStore';
import { useAlertStore } from '../../stores/alertStore';

const token = ref<string>("");
onMounted(() => {
    token.value = localStorage.getItem("access_token") as string;
})

const busqueda = ref<string>(""); // Variable para el dato de busqueda

const dataLogout = ref<object>([]);

const apiUsuarios = useUserStore(); // Utilizar el api context
const alertas = useAlertStore(); // Alertas swal

const axiosError = ref<string>("AxiosError");
// Validar si no hay error en axios
const error = computed(() => {
    axiosError.value = JSON.stringify(apiTodos.todoStoreData);
    return axiosError.value.includes("AxiosError"); // Validar si la respuesta tiene AxiosError incluido
});

const apiTodos = useTodoStore();

// Funcion para cerrar la sesion
const cerrarSesion = async() => {
    dataLogout.value = await apiUsuarios.apiUsuarios("http://localhost:8000/api/users/logout", "GET");
    console.log(dataLogout.value);
    if(dataLogout.value.logout === true){
        localStorage.removeItem("access_token"); // Eliminar el token de la sesion
        alertas.mostrarAlerta("Éxito", "Sesión cerrada con éxito", "success", "#0c64b7",true)
    }else{
        alertas.mostrarAlerta("Error", "No se ha podido cerrar la sesión", "error", "#0c64b7",true)
    }
    // Esperar a que se muestre el mensaje para cerrar sesion
    setTimeout(() => {
        window.location.reload()
    }, 1500)
}

// Funcion para ejecutar alguna busqueda
const busquedaTarea = async() => {
    apiTodos.todoStoreData = await apiUsuarios.apiUsuarios("http://localhost:8000/api/todos/?search="+busqueda.value, "GET");
}

</script>

<style scoped>
    
</style>