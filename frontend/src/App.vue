<script setup lang="ts">
import Navbar from './components/general_components/Navbar.vue'
import { useThemeStore } from './stores/themeStore';
import {onMounted} from 'vue';

const theme = useThemeStore(); // Variable global para el tema

onMounted(() => {
    // Obtener el tema
    theme.validarTheme();
})

</script>

<template>
  <div :class="[theme.theme]">
    <!-- Navbar -->
    <Navbar />

    <!-- Se refleja el contenido de SPA -->
    <section :class="['p-3 m-3',theme.theme]">
      <router-view class=""></router-view>
    </section>
    
  </div>

</template>

<style scoped>

</style>
