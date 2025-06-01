<template>
    <div class="">
        <section>
            <article class="d-flex justify-content-between">
                <h3>Registrase</h3>
                <!-- Boton de atras -->
                <Boton msg="Atras" color="secondary" tipo="button" @funcion_btn="()=>{$router.push('/')}" icono="fa-solid fa-arrow-left"/>
            </article>
            <article class="p-3 container">
                <!-- Formulario para crear usuarios -->
                <form @submit.prevent="enviarRegistroUsuario" method="post">
                    <!-- Nombres del usuario -->
                    <section class="row">
                        <h6 class="text-center">Nombres del usuario</h6>
                        <hr>
                        <article class="col">
                            <label for="username" class="form-label" >Nombre de usuario:</label><br>
                            <input class="form-control mt-3" type="text" name="username" id="username" required v-model="datosFormulario.username">
                        </article>
                        <article class="col">
                            <label class="form-label" for="first_name">Nombres: </label><br>
                            <input class="form-control mt-3" type="text" name="first_name" id="first_name" v-model="datosFormulario.first_name">
                        </article>
                        <article class="col">
                            <label for="last_name" class="form-label" >Apellidos: </label><br>
                            <input class="form-control mt-3" type="text" name="last_name" id="last_name" v-model="datosFormulario.last_name">
                        </article>
                    </section>
                    <!-- Email y contraseñas -->
                    <section class="row mt-3">
                        <h6 class="text-center">Email y contraseña</h6>
                        <hr>
                        <article class="col">
                            <label for="email" class="form-label" >Email: </label><br>
                            <input class="form-control mt-3" type="email" name="email" id="email" required v-model="datosFormulario.email">
                        </article>
                        <article class="col">
                            <label for="password" class="form-label" >Contraseña: </label><br>
                            <input class="form-control mt-3" type="password" name="password" id="password" required v-model="datosFormulario.password">
                        </article>
                        <article class="col">
                            <label for="password_confirmation" class="form-label" >Confirmar contraseña:</label><br>
                            <input class="form-control mt-3" type="password" name="password_confirmation" id="password_confirmation" required>
                        </article>
                    </section>
                    <!-- Boton de crear usuario -->
                    <section class="row mt-4 p-3">
                        <article class="col d-flex justify-content-end">
                            <Boton msg="Crear usuario" color="primary" tipo="submit" icono="fa-solid fa-user-plus"/>
                        </article>
                    </section>
                </form>
            </article>
        </section>
    </div>
</template>

<script setup lang="ts">
import Boton from '../components/general_components/Boton.vue'
import { useUserStore } from '../stores/userStore'
import { reactive, computed } from 'vue';
import { ref } from 'vue';
import { useAlertStore } from '../stores/alertStore';
import { Usuario } from '../interfaces/interfaces';


const userStore = useUserStore(); // Usar api
const alertStore = useAlertStore(); // Usar alertas

// Validar que las contraseñas coincidan
const passwordConfirmation = computed(() => {
    return datosFormulario.password === document.getElementById('password_confirmation')?.value
})

// Datos del formulario
const datosFormulario = reactive<Usuario>({
    username: "",
    first_name: "",
    last_name: "",
    email: "",
    password: "",
});

// Datos de usuarios y validaciones de registro
const datosUsers = ref<object>([]);

// Funcion para registrar un usuario
const enviarRegistroUsuario = async() => {
    if(passwordConfirmation.value){
        // Enviar datos al servidor para registrar el usuario
        datosUsers.value = await userStore.apiUsuarios("http://localhost:8000/api/users/", "POST", datosFormulario);
        if(datosUsers.value.status === true){
            alertStore.mostrarAlerta("Éxito", "El usuario se ha registrado correctamente", "success", "#0c64b7",true)
            // Limpiar el formulario
            datosFormulario.username = "";
            datosFormulario.first_name = "";
            datosFormulario.last_name = "";
            datosFormulario.email = "";
            datosFormulario.password = ""; 
            // Limpiar el campo de confirmacion
            let password = document.getElementById('password_confirmation');
            password.value = "";
        }else{
            alertStore.mostrarAlerta("Error", "El usuario no se ha registrado", "error", "#0c64b7",true)
        }
    }else{
        alertStore.mostrarAlerta("Error", "Las contraseñas no coinciden", "error", "#0c64b7",true)
    }
}



</script>

<style scoped>
    
</style>