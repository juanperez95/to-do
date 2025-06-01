<template>
    <div>
        <section class="p-3">    
            <article>
                <article class="d-flex justify-content-between">
                    <h3>¡Actualizacion de tarea! : {{ tarea.titulo.toUpperCase() }}</h3>
                    <Boton msg="< Atras" color="secondary" tipo="button" @funcion_btn="$router.push('/')" icono="fa-solid fa-arrow-left"/>
                </article>
                <article>
                    <form @submit.prevent="enviarDatos" method="patch">
                        <article class="form-group">
                            <label for="titulo" class="form-label">Titulo tarea</label>
                            <input name="titulo" class="form-control" id="titulo" placeholder="Titulo" v-model="tarea.titulo"/>
                        </article>
                        <article class="form-group">
                            <label for="descripcion" class="form-label">Descripción</label>
                            <textarea name="descripcion" class="form-control" id="descripcion" placeholder="Descripción" v-model="tarea.descripcion">{{ tarea.descripcion }}</textarea>
                        </article>
                        <article class="form-group">
                            <label for="estado" class="form-label">Estado tarea</label>
                            <select name="estado" class="form-select" id="estado" v-model="tarea.estado">
                                <option value="HECHO" :selected="tarea.estado === 'HECHO'">Tarea hecha</option>
                                <option value="EN_PROGRESO" :selected="tarea.estado === 'EN_PROGRESO'">Tarea en progreso</option>
                                <option value="TODO" :selected="tarea.estado === 'TODO'">Tarea pendiente</option>
                            </select>
                        </article>
                        <article class="form-group">
                            <Boton msg="Actualizar" color="success" tipo="button" @funcion_btn="enviarDatos" icono="fa-solid fa-check"/>
                        </article>
                    </form>
                </article>
            </article>       
        </section>
    </div>
</template>

<script setup lang="ts">
import Boton from '../components/general_components/Boton.vue';
import { useUserStore } from '../stores/userStore';
import { useRoute } from 'vue-router';
import { onMounted, reactive } from 'vue';
import {Todo} from '../interfaces/interfaces';
import { useAlertStore } from '../stores/alertStore';

const api = useUserStore(); // Utilizar el api context
const route = useRoute(); // Utilizar ruta y recoger los parametros
const id = route.params.id; // Obtener el id de la tarea
const alertas = useAlertStore(); // Utilizar alertas

// Crear una tarea para almacenar los datos de la peticion
const tarea = reactive<Todo>({
    titulo: "",
    descripcion: "",
    estado: "",
})

// Al renderizar el componente se realiza la peticion para trar la tarea
onMounted(async() => {
    let response = await api.apiUsuarios("http://localhost:8000/api/todos/actualizar/"+id, "GET");
    if(response.todo){
        // Asignar los datos a la tarea
        tarea.titulo = response.todo.titulo;
        tarea.descripcion = response.todo.descripcion;
        tarea.estado = response.todo.estado;
    }
})

// Enviar datos a la api con los datos actualizados
const enviarDatos = async() => {
    let response = await api.apiUsuarios("http://localhost:8000/api/todos/actualizar/"+id, "PATCH", tarea);
    if(response.updatedTodo === true){
        alertas.mostrarAlerta("Exito", "Tarea actualizada con éxito", "success", "#0c64b7",true);
    }else{
        alertas.mostrarAlerta("Error", "No se ha podido actualizar la tarea", "error", "#0c64b7",true);
    }
}




</script>

<style scoped>
    
</style>