<template>
    <div>
        <Boton tipo="button" color="success" data-bs-toggle="modal" :data-bs-target="'#'+props.id_modal" :msg=" !is_login ? 'Crear tarea' : 'Iniciar sesion'"/>

        <!-- Modal -->
        <div class="modal fade" :id="props.id_modal.toString()" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">{{ !is_login ? 'Crear tarea' : 'Iniciar sesion' }}</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <!-- Campos de la tarea si la opcion is_login esta activo -->
                    <form @submit.prevent method="post" v-if="!is_login">
                        <article class="mt-3">
                            <label for="titulo">Titulo</label>
                            <input type="text" class="form-control" id="titulo" placeholder="Titulo de la tarea" required>
                        </article>
                        <article class="mt-3">
                            <label for="descripcion">Descripción</label>
                            <textarea class="form-control" id="descripcion" rows="3" required></textarea>
                        </article>
                        <article class="mt-3">
                            <label for="estado">Estado</label>
                            <select class="form-control" id="estado" required>
                                <option value="TODO">Pendiente de realizar</option>
                                <option value="EN_PROGRESO">En progreso</option>
                                <option value="HECHO">Realizado</option>
                            </select>
                        </article>
                        <!-- Boton de crear tarea -->
                        <div class="modal-footer">
                            <Boton tipo="button" color="secondary" data-bs-dismiss="modal" msg="Cerrar"/>
                            <Boton tipo="submit" color="primary" msg="Guardar tarea"/>
                        </div>
                    </form>

                    <!-- Mostrar formualrio de login -->
                    <form @submit.prevent="inicioSesion" method="post" v-if="is_login">
                        <article class="mt-3">
                            <label for="username">Usuario</label>
                            <input type="text" class="form-control" id="username" placeholder="Nombre de usuario" required v-model="dataSesion.username">
                        </article>
                        <article class="mt-3">
                            <label for="password">Contraseña</label>
                            <input type="password" class="form-control" id="password" placeholder="Contraseña" required v-model="dataSesion.password">
                        </article>
                        <!-- Boton de crear tarea -->
                        <div class="modal-footer">
                            <Boton tipo="button" color="secondary" data-bs-dismiss="modal" msg="Cerrar"/>
                            <Boton tipo="submit" color="primary" msg="Entrar"/>
                        </div>
                    </form>

                </div>
                </div>
            </div>
        </div>        
    </div>
</template>

<script setup lang="ts">
import Boton from './Boton.vue'
import {defineProps} from 'vue'
import { useUserStore } from '../../stores/userStore' // Api de la aplicacion
import { Login, Usuario } from '../../interfaces/interfaces'
import { reactive } from 'vue'
import { useAlertStore } from '../../stores/alertStore'


const alertas = useAlertStore();


const props = defineProps<Login>();

// Deinir la api
const apiModal = useUserStore();

// Datos para iniciar la sesion
const dataSesion = reactive<Usuario>({
    username: "",
    password: "",
});

// Funcion para validar he iniciar sesion con el token
const inicioSesion = async() => {
    // Obtener el token en el store de la aplicacion
    let response = await apiModal.apiUsuarios("http://localhost:8000/api/users/login", "POST", dataSesion);
    if(response.status){
        alertas.mostrarAlerta("Éxito", "Sesión iniciada con éxito", "success", "#0c64b7",true)
        apiModal.access_token = response.access; // Guardar el token
    }else{
        alertas.mostrarAlerta("Error", "No se ha podido iniciar sesión", "warning", "#0c64b7",true)
    }
}
</script>

<style scoped>
    
</style>