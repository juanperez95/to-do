<template>
    <div>
        <section>
            <article class="card p-3">
                <!-- Titulo de la tarea -->
                <article :class="['card-title p-2 m-3 text-center',clases]"><h3>{{ props.titulo }}</h3></article>
                <section class="card-body">
                    <article class="card-text">
                        <!-- Descripción de la tarea -->
                        <p>{{ props.descripcion ? props.descripcion : 'Descripción de la tarea' }}</p>
                        <!-- no mostrar los botones si la tarea ya se completo-->
                        <article class="d-flex justify-content-between" v-if="props.cumplido">
                            <Boton msg="Hecha" color="success" tipo="button" @funcion_btn="console.log('Boton hecha')" />
                            <Boton msg="Editar" color="primary" tipo="button" @funcion_btn="console.log('Boton editar')" />
                            <Boton msg="Eliminar" color="danger" tipo="button" @funcion_btn="console.log('Boton eliminar')" />
                        </article>
                    </article>
                </section>
                <!-- Prioridad de la tarea -->
                <section class="card-header">
                    <article class="card-text">
                        <span class="badge text-bg-primary">Cumplido</span>
                    </article>
                </section>
                <!-- Pie de card -->
                <section class="card-footer">
                    <article class="card-text d-flex justify-content-between">
                        <p>Fecha de creación: 2023-01-01</p>
                        <p>Fecha de modificación: 2023-01-01</p>
                    </article>
                </section>
            </article>
        </section>
    </div>
</template>

<script setup lang="ts">
import {ref, defineProps, computed} from 'vue'
// Importar los componente generales
import Boton from './Boton.vue'

const claseText = ref<String>("text-decoration-line-through");

type Property = {
    titulo: String,
    descripcion: String,
    fecha_creacion?: String,
    fecha_modificacion?: String,
    estado?: String,
    // Especiicar si la tarea se completo
    cumplido?: Boolean,
}

// Propiedad computada
const clases = computed(() => {
    if(props.cumplido){
        claseText.value = "text-decoration-none";
    }
    else{
        claseText.value = "text-decoration-line-through";
    }
    return claseText.value
})

// Definir las propiedades del componente
const props = defineProps<Property>();


</script>

<style scoped>
    
</style>