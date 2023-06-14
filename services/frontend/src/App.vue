<template>
  <NavBar></NavBar>
  <div class="container mx-auto px-4">
    <router-view></router-view>
  </div>
</template>

<script setup>
import NavBar from "@/components/NavBar.vue"
</script>

<style src="./assets/tailwind.css"></style>