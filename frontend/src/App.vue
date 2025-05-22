<script setup lang="ts">
import Navbar from './components/general_components/Navbar.vue'

</script>

<template>
  <div>
    <!-- Navbar -->
    <Navbar />

    <!-- Se refleja el contenido de SPA -->
    <section class="p-3 m-3">
      <router-view></router-view>
    </section>
    
  </div>

</template>

<style scoped>

</style>
