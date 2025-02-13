<template>
    <div class="todo-container">
        <h1>Todo List</h1>

        <!-- 输入框 -->
        <div class="todo-input">
            <input v-model="newTodo" placeholder="新しいタスクを追加する">
            <button @click="addNewTodo">追加</button>
        </div>

        <!-- 任务列表 -->
        <ul>
            <li v-for="todo in todoStore.todos" :key="todo.id">
                <input type="checkbox" :checked="todo.completed" @change="toggleTodo(todo)">
                {{ todo.title }}
                <button @click="removeTodo(todo.id)">削除</button>
            </li>
        </ul>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useTodoStore } from "../stores/todoStore";
import type { Todo } from "../types/Todo";

const todoStore = useTodoStore();
const newTodo = ref("");

const addNewTodo = async () => {
    if (newTodo.value.trim() !== "") {
        await todoStore.createTodo(newTodo.value);
        newTodo.value = "";
    }
};

const removeTodo = async (id: number) => {
    await todoStore.removeTodo(id);
};

const toggleTodo = async (todo: Todo) => {
    await todoStore.toggleTodo(todo);
};

onMounted(todoStore.fetchTodos);
</script>

<style scoped>
.todo-container {
    text-align: center;
    padding: 20px;
}

.todo-input {
    display: flex;
    gap: 10px;
    justify-content: center;
    margin-bottom: 10px;
}

input {
    padding: 5px;
}
</style>