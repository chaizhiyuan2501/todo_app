import { defineStore } from "pinia";
import { ref } from "vue";
import { getTodos, addTodo, deleteTodo, updateTodo } from "../api/todoApi";

export const useTodoStore = defineStore("todo", () => {
  const todos = ref([]);
  
  // 获取任务
  const fetchTodos = async () => {
    const response = await getTodos();
    todos.value = response.data;
  };

  // 添加任务
  const createTodo = async (title) => {
    await addTodo({ title, completed: false });
    fetchTodos();
  };

  // 删除任务
  const removeTodo = async (id) => {
    await deleteTodo(id);
    fetchTodos();
  };

  // 切换任务状态
  const toggleTodo = async (todo) => {
    await updateTodo(todo.id, { ...todo, completed: !todo.completed });
    fetchTodos();
  };

  return { todos, fetchTodos, createTodo, removeTodo, toggleTodo };
});
