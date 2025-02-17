// src/services/diagramService.js
import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

export const getDiagrams = () => axios.get(`${API_URL}/diagrams/`);
export const getDiagram = (id) => axios.get(`${API_URL}/diagrams/${id}/`);
export const createDiagram = (data) => axios.post(`${API_URL}/diagrams/`, data);
// etc.
