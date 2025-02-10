import axios from "axios";

// 使用环境变量，确保在 Docker 里可以访问后端
const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000/api/todos/";

export const getTodos = () => axios.get(API_URL);
export const addTodo = (todo) => axios.post(API_URL, todo);
export const deleteTodo = (id) => axios.delete(`${API_URL}${id}/`);
export const updateTodo = (id, todo) => axios.put(`${API_URL}${id}/`, todo);
