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
                            <input type="text" name="username" id="username" class="form-control" v-model="dataUsuario.username" required>
                        </article>
                        <article class="col">
                            <label for="first_name" class="label-form mb-2">Primer nombre:</label>
                            <input type="text" name="first_name" id="first_name" class="form-control" v-model="dataUsuario.first_name" required>
                        </article>
                        <article class="col">
                            <label for="last_name" class="label-form mb-2">Segundo nombre:</label>
                            <input type="text" name="last_name" id="last_name" class="form-control" v-model="dataUsuario.last_name" required>
                        </article>
                    </section>
                </form>
                <!-- datos de email y contraseña -->
                <legend class="legend-form text-center mt-5">Datos de acceso</legend>
                <hr>
                <section class="row">
                    <article class="col">
                        <Acordion :mensaje_btn="'Cambiar correo electronico'" msg_label='Correo electronico' dato='email' icono='fa-solid fa-envelope' tipo_input='email' :valor_actual="dataUsuario.email" mostrar_actual/>
                    </article>
                    <article class="col">
                        <Acordion :mensaje_btn="'Cambiar la contraseña'" msg_label='Contraseña' dato='contraseña' icono='fa-solid fa-lock' tipo_input='password' confirmar_input :funcion="cambiar_contrasena"/>
                    </article>
                </section>
            </article>
        </section>
    </div>
</template>

<script setup lang="ts">
import Boton from '../components/general_components/Boton.vue';
import {onMounted,ref} from 'vue';
import { useUserStore } from '../stores/userStore'
import { Usuario } from '../interfaces/interfaces';
import Acordion from '../components/general_components/PropsCorfimacion.vue';
import {useAlertStore} from '../stores/alertStore'

const userStore = useUserStore(); // API context
const alertas = useAlertStore(); // Uso global de alertas

const dataUsuario = ref<Usuario>({
    username: "",
    first_name: "",
    last_name: "",
    email: "",
    password: ""
});

// Al redenderizar el componente se realiza la siguiente peticion para traer la informacion del usuario logueado
onMounted(async() => {
    let response = await userStore.apiUsuarios("http://localhost:8000/api/users/", "GET");
    if(response.usuario){
        //Asignar valores
        dataUsuario.value.username = response.usuario.username;
        dataUsuario.value.first_name = response.usuario.first_name;
        dataUsuario.value.last_name = response.usuario.last_name;
        dataUsuario.value.email = response.usuario.email;
    }
})

// Funcion para cambiar la contraseña
const cambiar_contrasena = async() => {
    
    let response = await userStore.apiUsuarios("http://localhost:8000/api/users/actualizar-perfil", "PATCH",{
        info_basica:false, // Solo va a cambiar clave
        basico:dataUsuario.value,
        clave:true,
    });
}

// Funcion para actualizar el correo electronico
const cambiar_correo = () => {

}


</script>

<style scoped>
    
</style>