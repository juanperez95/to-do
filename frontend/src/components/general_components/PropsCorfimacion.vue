<template>
    <div>
        <section>
            <article class="grid grid-cols-2 gap-4">
                <label for="email" class="form-label col-span-2">{{ msg_label }}: </label>
                <article>
                    <!-- Mostrar el dato actual si se define en True el valor en el componente-->
                    <label v-show="mostrar_actual" for="email" class="form-label">{{ (dato.charAt(0).toUpperCase() + dato?.slice(1)) }} actual:</label>
                    <input v-show="mostrar_actual" type="email" name="" id="" class="form-control" :value="valor_actual" disabled>
                    <input :type="input_type" :name="dato" :id="dato" class="form-control mt-2" v-model="dato_actualizado" :placeholder="dato + ' a cambiar'">
                    <!-- Mostrar una entrada para que el usuario escriba la confirmacion de una contraseña o algun otro dato sensible-->
                    <input :type="input_type" :name="dato" :id="dato+'2'" class="form-control mt-2" :placeholder="'Confirmar '+dato + ' a cambiar'" v-show="confirmar_input">
                </article>
                <article class="justify-self-center">
                    <!-- Cambiar icono del boton ver si el tipo de input es password -->
                    <Boton v-show="tipo_input === 'password'" msg="Ver contraseña" color="dark" :icono="input_type === 'password' ? 'fa-solid fa-eye' : 'fa-solid fa-eye-slash'" @funcion_btn="showPass"/>
                    <Boton :msg="mensaje_btn" color="dark" :icono="icono" @funcion_btn="funcion"/>
                </article>
            </article>
        </section>
    </div>
</template>

<script setup lang="ts">
import Boton from './Boton.vue'
import {ref, onMounted} from 'vue'

const dato_actual = ref<String>("")
const dato_actualizado = ref<String>("");
const input_type = ref<String>("text"); // Mantener el tipo de input ya que el prop solo es lectura y no deja asignar mas valor.

const props = defineProps({
    mensaje_btn:String,
    msg_label:String,
    funcion:Function,
    dato:String,
    icono:String,
    tipo_input:String,
    valor_actual:String,
    mostrar_actual:Boolean,
    confirmar_input:Boolean
});

// Asignar valor actual al renderizar componente
onMounted(()=>{
    dato_actual.value = props.valor_actual as String;
    input_type.value = props.tipo_input as String;
})


// Funcion para mostrar la contraseña cambiando el tipo de input
const showPass = () => {
    // Cambiar el tipo de input al hacer click en el boton de mostrar clave
    if(input_type.value === "password"){
        input_type.value = "text";
    }else{
        input_type.value = "password";
    }
}

</script>

<style scoped>
    
</style>