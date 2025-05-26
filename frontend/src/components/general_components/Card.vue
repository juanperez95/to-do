<template>
    <div>
        <section>
            <article class="card p-3">
                <!-- Titulo de la tarea -->
                <article :class="['card-title p-2 m-3 text-center',clases]"><h3>{{ props.titulo }}</h3></article>
                <section class="card-body">
                    <article class="card-text">
                        <!-- Descripción de la tarea -->
                        <p>{{ props.descripcion ? props.descripcion : 'Descripción de la tarea' }}</p>
                        <!-- no mostrar los botones si la tarea ya se completo-->
                        <article class="d-flex justify-content-between" v-if="props.cumplido">
                            <Boton msg="Hecha" color="success" tipo="button" @funcion_btn="console.log('Boton hecha')" />
                            <Boton msg="Editar" color="primary" tipo="button" @funcion_btn="console.log('Boton editar')" />
                            <Boton msg="Eliminar" color="danger" tipo="button" @funcion_btn="borrarTarea" />
                        </article>
                    </article>
                </section>
                <!-- Prioridad de la tarea -->
                <section class="card-header">
                    <article class="card-text">
                        <span class="badge text-bg-success" v-if="props.estado === 'HECHO'">Cumplido</span>
                        <span class="badge text-bg-primary" v-else-if="props.estado === 'EN_PROGRESO'">En proceso</span>
                        <span class="badge text-bg-danger" v-else>Pendiente</span>
                    </article>
                </section>
                <!-- Pie de card -->
                <section class="card-footer">
                    <article class="card-text d-flex justify-content-between">
                        <!-- Queda pendiente arreglar la fecha-->
                        <p>Fecha de creación: {{ formaterFechaCreacion }}</p>
                        <p>Fecha de modificación: {{ formaterFechaModificacion }}</p>
                    </article>
                </section>
            </article>
        </section>
    </div>
</template>

<script setup lang="ts">
import {ref, defineProps, computed} from 'vue'
// Importar los componente generales
import Boton from './Boton.vue'
import { Todo } from '../../interfaces/interfaces'
import { useAlertStore } from '../../stores/alertStore';
import { useUserStore } from '../../stores/userStore';
import { useTodoStore } from '../../stores/todoStore';

// Para formatear la fecha
import dayjs from 'dayjs';

const alertas = useAlertStore(); // Alertas

const apiTodos = useUserStore(); // Utilizar el api context

const claseText = ref<String>("text-decoration-line-through");

const todos = useTodoStore(); // Utilizar store de tareas



// Propiedad computada
const clases = computed(() => {
    if(props.cumplido){
        claseText.value = "text-decoration-none";
    }
    else{
        claseText.value = "text-decoration-line-through";
    }
    return claseText.value
})

// Definir las propiedades del componente
const props = defineProps<Todo>();

// Formatear fecha
const formaterFechaCreacion = computed(() => {
    return props.fecha_creacion ? dayjs(props.fecha_creacion).format('DD/MM/YYYY') : '---';
})

const formaterFechaModificacion = computed(() => {
    return props.fecha_modificacion ? dayjs(props.fecha_modificacion).format('DD/MM/YYYY') : '----';
})


// ------------------------------------- Funciones de crud en tareas

const borrarTarea = async() => {
    let response = await apiTodos.apiUsuarios("http://localhost:8000/api/todos/"+props.id, "DELETE");
    if(response.deleted === true){
        alertas.mostrarAlerta("Éxito", "Tarea eliminada con éxito", "success", "#0c64b7",true)
        todos.todoStoreData = await apiTodos.apiUsuarios("http://localhost:8000/api/todos/", "GET");
    }else{
        alertas.mostrarAlerta("Error", "No se ha podido eliminar la tarea", "error", "#0c64b7",true)
    }
}

</script>

<style scoped>
    
</style>