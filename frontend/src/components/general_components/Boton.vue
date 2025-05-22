<template>
  <div>
    <section>
      <button @click="click" :class="'p-2 m-3 btn btn-'+color" :type="tipo ? tipo : 'button'">{{ msg ? msg : 'Colocar mensaje' }}</button>
    </section>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from 'vue'

// Declarar un emit para la funcion del boton
const emit = defineEmits(['funcion_btn'])

const props = defineProps({
  // Mensaje a mostrar en el boton
  msg: String,
  color:{
    type: String,
    required: true,
  },
  tipo:String|undefined
})

// Funcion para ejecutar el evento de click
function click(){
  emit('funcion_btn')
}

</script>

<style scoped>
  
</style>