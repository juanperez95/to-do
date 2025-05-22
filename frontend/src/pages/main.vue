<template>
    <div>
        <section>
            <article class="d-flex justify-content-between">
                <h3>Registrase</h3>
                <!-- Boton de atras -->
                <Boton msg="< Atras" color="second" tipo="button" @funcion_btn="()=>{$router.push('/')}" />
            </article>
            <article class="p-3 container">
                <!-- Formulario para crear usuarios -->
                <form @submit.prevent method="post">
                    <!-- Nombres del usuario -->
                    <section class="row">
                        <h6 class="text-center">Nombres del usuario</h6>
                        <hr>
                        <article class="col">
                            <label for="username" class="form-label" >Nombre de usuario:</label><br>
                            <input class="form-control mt-3" type="text" name="username" id="username" required>
                        </article>
                        <article class="col">
                            <label class="form-label" for="first_name">Nombres: </label><br>
                            <input class="form-control mt-3" type="text" name="first_name" id="first_name">
                        </article>
                        <article class="col">
                            <label for="last_name" class="form-label" >Apellidos: </label><br>
                            <input class="form-control mt-3" type="text" name="last_name" id="last_name">
                        </article>
                    </section>
                    <!-- Email y contraseñas -->
                    <section class="row mt-3">
                        <h6 class="text-center">Email y contraseña</h6>
                        <hr>
                        <article class="col">
                            <label for="email" class="form-label" >Email: </label><br>
                            <input class="form-control mt-3" type="email" name="email" id="email" required>
                        </article>
                        <article class="col">
                            <label for="password" class="form-label" >Contraseña: </label><br>
                            <input class="form-control mt-3" type="password" name="password" id="password" required>
                        </article>
                        <article class="col">
                            <label for="password_confirmation" class="form-label" >Confirmar contraseña:</label><br>
                            <input class="form-control mt-3" type="password" name="password_confirmation" id="password_confirmation" required>
                        </article>
                    </section>
                    <!-- Boton de crear usuario -->
                    <section class="row mt-4 p-3">
                        <article class="col d-flex justify-content-end">
                            <Boton msg="Crear usuario" color="primary" tipo="submit" />
                        </article>
                    </section>
                </form>
            </article>
        </section>
    </div>
</template>

<script setup lang="ts">
import Boton from '../components/general_components/Boton.vue'

</script>

<style scoped>
    
</style>