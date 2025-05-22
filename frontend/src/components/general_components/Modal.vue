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
                    <form @submit.prevent method="post" v-if="is_login">
                        <article class="mt-3">
                            <label for="email">Usuario</label>
                            <input type="email" class="form-control" id="email" placeholder="Email" required>
                        </article>
                        <article class="mt-3">
                            <label for="password">Contraseña</label>
                            <input type="password" class="form-control" id="password" placeholder="Contraseña" required>
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

// Interface para definir los datos de la propiedad
interface Login{
    is_login?: Boolean,
    // Manejar diferente IDS para los modales
    id_modal:String
}

const props = defineProps<Login>();



</script>

<style scoped>
    
</style>