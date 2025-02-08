import axios from "axios"

const API_URL = "http://localhost:8000/api/todos/"

export const getTodos = () => axios.get(API_URL)
export const addTodos = () => axios.post(API_URL, todo)
export const deleteTodos = () => axios.delete(`${API_URL}${id}/`)
export const updateTodos = () => axios.put(`${API_URL}${id}/`, todo)
