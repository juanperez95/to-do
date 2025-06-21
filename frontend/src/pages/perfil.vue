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
                        <article class="justify-self-end">
                            <Boton msg="Actualizar datos" color="dark" icono="fa-solid fa-save" @funcion_btn="datos_basicos"/>
                        </article>
                    </section>
                </form>
                <!-- datos de email y contraseña -->
                <legend class="legend-form text-center mt-5">Datos de acceso</legend>
                <hr>
                <section class="row">
                    <article class="col">
                        <!-- Datos del correo electronico -->
                        <section>
                            <article class="grid grid-cols-2 gap-4">
                                <label for="email" class="form-label col-span-2">Datos del email </label>
                                <article>                                   
                                    <label for="email" class="form-label">Email actual:</label>
                                    <input type="email" name="email" id="" class="form-control" :value="correo_actual" disabled>
                                    <input type="email" name="email" id="email" class="form-control mt-2" v-model="dataUsuario.email" placeholder="Email nuevo">
                                </article>
                                <article class="justify-self-center">
                                    <Boton msg="Cambiar correo" color="dark" icono="fa-solid fa-envelope" @funcion_btn="cambiar_correo"/>
                                </article>
                            </article>
                        </section>
                    </article>
                    <article class="col">
                        <!-- Datos de contraseña -->
                        <section>
                            <article class="grid grid-cols-2 gap-4">
                                <label for="password" class="form-label col-span-2">Contraseña</label>
                                <article>
                                    <label for="password" class="form-label">Actualizar contraseña:</label>
                                    <input :type="tipo_input" name="password" id="password1" class="form-control" placeholder="Nueva contraseña">
                                    <input :type="tipo_input" name="password" id="password" class="form-control mt-2" v-model="dataUsuario.password" placeholder="Confirme la contraseña nueva">
                                </article>
                                <article class="justify-self-center">
                                    <Boton msg="Cambiar contraseña" color="dark" icono="fa-solid fa-key" @funcion_btn="cambiar_contrasena"/>
                                    <!-- Mostrar la contraseña-->
                                    <Boton msg="Mostrar contraseña" color="dark" :icono="tipo_input === 'password' ? 'fa-solid fa-eye' : 'fa-solid fa-eye-slash'" @funcion_btn="mostrar_contrasena"/>
                                </article>
                            </article>
                        </section>
                    </article>
                </section>
            </article>
        </section>
    </div>
</template>

<script setup lang="ts">
import Boton from '../components/general_components/Boton.vue';
import {onMounted,ref,reactive} from 'vue';
import { useUserStore } from '../stores/userStore';
import { Usuario, Perfil } from '../interfaces/interfaces';
import {useAlertStore} from '../stores/alertStore';


const userStore = useUserStore(); // API context
const alertas = useAlertStore(); // Uso global de alertas
const correo_actual =ref<String>(""); // Mantener el correo actual y no mezclado v-model de 'dataUsuario.email'
const tipo_input = ref<String>("password"); // Variable encargada de cambiar el tipo de input en la contraseña para poderla validar.

// Datos de usuario para formulario
const dataUsuario = ref<Usuario>({
    username: "",
    first_name: "",
    last_name: "",
    email: "",
    password: ""
});

// Datos para actualizar el perfil
const datos_perfil = reactive<Perfil>({
    info_basica:false,
    basico:dataUsuario.value,
    clave:false,
    correo:false
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
        correo_actual.value = response.usuario.email; // Correo actual
    }
})

// Funcion para cambiar la contraseña
const cambiar_contrasena = async() => {   
    datos_perfil.clave = true; // Cambiar contraseña
    datos_perfil.correo = false; 
    datos_perfil.info_basica = false; 
    let response = await userStore.apiUsuarios("http://localhost:8000/api/users/actualizar-perfil", "PATCH",datos_perfil);

    if(response['update-password']){
        alertas.mostrarAlerta("Éxito", "Contraseña actualizada con éxito", "success", "#0c64b7",true);
    }else{
        alertas.mostrarAlerta("Error", "No se ha podido actualizar la contraseña", "error", "#0c64b7",true);
    }
}

// Funcion para actualizar el correo electronico
const cambiar_correo = async() => {
    datos_perfil.clave = false; 
    datos_perfil.correo = true; // Cambiar correo
    datos_perfil.correo_antiguo = correo_actual.value; // Guardar correo antiguo
    datos_perfil.info_basica = false; 
    let response = await userStore.apiUsuarios("http://localhost:8000/api/users/actualizar-perfil", "PATCH",datos_perfil);
    console.log(response);
}

// Funcion para cambiar los datos basicos del usuario
const datos_basicos = async() => {
    datos_perfil.clave = false; 
    datos_perfil.correo = false; 
    datos_perfil.info_basica = true; // Cambiar los datos basicos
    let response = await userStore.apiUsuarios("http://localhost:8000/api/users/actualizar-perfil", "PATCH",datos_perfil);

    if(response['update-basico']){
        alertas.mostrarAlerta("Éxito", "Datos actualizados con éxito", "success", "#0c64b7",true)
    }else{
        alertas.mostrarAlerta("Error", "No se ha podido actualizar los datos", "error", "#0c64b7",true)
    }
}

// Funcion para mostrar la contreseña
const mostrar_contrasena = () => {
    return tipo_input.value === "text" ? tipo_input.value = "password" : tipo_input.value = "text";
}



</script>

<style scoped>
    
</style>