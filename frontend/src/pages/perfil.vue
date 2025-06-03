<template>
    <div>
        <section class="d-flex justify-content-between align-items-center">
            <h3>Perfil de usuario</h3>
            <Boton msg="Atras" color="secondary" tipo="button" @funcion_btn="()=>{$router.push('/')}" icono="fa-solid fa-arrow-left"/>
        </section>
        <!-- formulario con datos cargados del usuario para actualizar-->
        <section>
            <article>
                <form @submit.prevent method="PATCH" >
                    <legend class="legend-form text-center">Datos de usuario</legend>
                    <hr>
                    <section class="row">
                        <article class="col">
                            <label for="username" class="label-form mb-2">Nombre de usuario:</label>
                            <input type="text" name="username" id="username"  class="form-control" required>
                        </article>
                        <article class="col">
                            <label for="first_name" class="label-form mb-2">Primer nombre:</label>
                            <input type="text" name="first_name" id="first_name"  class="form-control" required>
                        </article>
                        <article class="col">
                            <label for="last_name" class="label-form mb-2">Segundo nombre:</label>
                            <input type="text" name="last_name" id="last_name"  class="form-control" required>
                        </article>
                    </section>
                    <!-- datos de email y contraseña -->
                    <legend class="legend-form text-center mt-5">Datos de acceso</legend>
                    <hr>
                    <section class="row">
                        <article class="col">
                            <label for="email" class="label-form mb-2">Email:</label>
                            <input type="email" name="email" id="email"  class="form-control" required>
                        </article>
                        
                        <article class="col">
                            <label for="password" class="label-form mb-2">Contraseña:</label>
                            <input type="password" name="password" id="password"  class="form-control" required>
                        </article>
                    </section>
                </form>
            </article>
        </section>
    </div>
</template>

<script setup lang="ts">
import Boton from '../components/general_components/Boton.vue';

</script>

<style scoped>
    
</style>