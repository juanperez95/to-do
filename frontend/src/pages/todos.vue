<template>
    <div>
        <section>
            <h3>Tus tareas</h3>
            <article>
                <Card titulo="Tarea 1" descripcion="Descripción de la tarea" cumplido />
            </article>
        </section>
    </div>
</template>

<script setup lang="ts">
import Card from '../components/general_components/Card.vue';
import { useUserStore } from '../stores/userStore'

const userStore = useUserStore();

    
</script>

<style scoped>
    
</style>