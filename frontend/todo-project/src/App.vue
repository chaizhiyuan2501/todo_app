<template>
  <div class="app-container">
    <TodoList />
  </div>
</template>

<script setup lang="ts">
import TodoList from "./components/TodoList.vue";
</script>

<style scoped>
.app-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>
