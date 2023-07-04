import axios from './axios';
import { AxiosResponse } from 'axios';
import { Tarea } from '@/interfaces/Tarea';

export const getTareas = async (): Promise<AxiosResponse<Tarea[]>> => 
    await axios.get('/tareas/');

export const createTarea = async (tarea: Tarea) => 
    await axios.post('/tareas/', tarea);