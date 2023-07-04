import axios from './axios';
import { AxiosResponse } from 'axios';
import { Tarea } from '@/interfaces/Tarea';

export const getTareas = async (): Promise<AxiosResponse<Tarea[]>> => 
    await axios.get('/tareas/');

export const getTarea = async (id: string): Promise<AxiosResponse<Tarea>> => 
    await axios.get('/tareas/' + id + '/');

export const createTarea = async (tarea: Tarea) => 
    await axios.post('/tareas/', tarea);

export const updateTarea = async (id: string, tarea: Tarea) =>
    await axios.put('/tareas/' + id + '/', tarea);

export const deleteTarea = async (id: string) =>
    await axios.delete('/tareas/' + id + '/');