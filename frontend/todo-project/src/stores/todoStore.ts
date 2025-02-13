import { defineStore } from "pinia";
import { ref } from "vue";
import { getTodos, addTodo, deleteTodo, updateTodo } from "../api/todoApi";
import type { Todo } from "../types/Todo";

export const useTodoStore = defineStore("todo", () => {
    const todos = ref<Todo[]>([]);

    // 获取任务
    const fetchTodos = async () => {
        const response = await getTodos();
        todos.value = response.data;
    };

    // 添加任务
    const createTodo = async (title: string) => {
        await addTodo({ title, completed: false });
        fetchTodos();
    };

    // 删除任务
    const removeTodo = async (id: number) => {
        await deleteTodo(id);
        fetchTodos();
    };

    // 切换任务状态
    const toggleTodo = async (todo: Todo) => {
        await updateTodo(todo.id, { completed: !todo.completed });
        fetchTodos();
    };

    return { todos, fetchTodos, createTodo, removeTodo, toggleTodo };
});
