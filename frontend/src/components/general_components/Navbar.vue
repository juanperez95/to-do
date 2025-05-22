<template>
    <div>
        <section>
        <nav class="navbar bg-body-tertiary d-flex justify-content-between">
            <div class="container-fluid">
                <form class="d-flex" role="search" @submit.prevent>
                    <input class="form-control me-2" type="search" placeholder="Filtrar tarea" aria-label="Search"/>
                    <button class="btn btn-outline-success" type="submit">Buscar</button>
                </form>
                <!-- Boton de crear tarea (Modal) -->
                <article class="d-flex align-items-center">
                    <Modal :is_login="true" id_modal="registerModal"/>
                    <!-- Iniciar sesion -->
                    <Modal id_modal="loginModal"/>
                    <!-- Redirigir a la pagina de crear usuario -->
                    <Boton msg="Crear usuario" color="primary" tipo="button" @funcion_btn="()=>{$router.push('/crear-usuario')}" />
                </article>
            </div>
        </nav>
        </section>
    </div>
</template>

<script setup lang="ts">
import Modal from './Modal.vue'
import Boton from './Boton.vue'

</script>

<style scoped>
    
</style>