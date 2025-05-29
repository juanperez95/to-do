<template>
    <div>
        <section>
            <h3>Tus tareas</h3>
            <!-- Mostrar todos las tareas -->
            <section class="grid grid-cols-2 gap-3">
                <article v-if="todos.todoStoreData.length !== 0 && !error" v-for="tarea in todos.todoStoreData" :key="tarea.id">
                    <Card :titulo="tarea.titulo" :descripcion="tarea.descripcion" class="col" v-if="tarea.estado === 'TODO' || tarea.estado === 'EN_PROGRESO'" :estado="tarea.estado" :cumplido="true"  :id="tarea.id"/>
                    <Card :titulo="tarea.titulo" :descripcion="tarea.descripcion" :fecha_creacion="tarea.fecha_creacion" :fecha_modificacion="tarea.fecha_modificacion" :estado="tarea.estado" class="col" v-else :id="tarea.id"/>
                </article>
            </section>
            <!-- Mostrar mensaje para que inicie sesion-->
            <article v-if="error">
                <h4 class="text-center">¡Inicia sesion para ver tus tareas!</h4>
            </article>
            <article v-else-if="todos.todoStoreData.length === 0">
                <h4 class="text-center">¡No tienes tareas pendientes!</h4>
            </article>
        </section>
    </div>
</template>

<script setup lang="ts">
import Card from '../components/general_components/Card.vue';
import { useUserStore } from '../stores/userStore'
import { onMounted,computed, ref } from 'vue';
import { useTodoStore } from '../stores/todoStore'

const userStore = useUserStore();

// Recibir todas las tareas de la api
const todos = useTodoStore();

const axiosError = ref<string>("AxiosError");

// Cuando inicia el componente
onMounted(async() => {
    // Obtener todos los usuarios
    todos.todoStoreData = await userStore.apiUsuarios("http://localhost:8000/api/todos/", "GET");
})

// Validar si no hay error en axios
const error = computed(() => {
    axiosError.value = JSON.stringify(todos.todoStoreData);
    return axiosError.value.includes("AxiosError"); // Validar si la respuesta tiene AxiosError incluido
});

    
</script>

<style scoped>
    
</style>