import axios from './axios';
import { Tarea } from '@/interfaces/Tarea';

export const createTarea = async (tarea: Tarea) => {
    await axios.post('/tareas/', tarea);
};