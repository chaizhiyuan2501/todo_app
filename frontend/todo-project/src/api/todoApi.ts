import axios from "axios";
import type { Todo } from "../types/Todo";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000/api/todos/";

export const getTodos = () => axios.get<Todo[]>(API_URL);
export const addTodo = (todo: Omit<Todo, "id">) => axios.post<Todo>(API_URL, todo);
export const deleteTodo = (id: number) => axios.delete(`${API_URL}${id}/`);
export const updateTodo = (id: number, todo: Partial<Todo>) => axios.put<Todo>(`${API_URL}${id}/`, todo);
