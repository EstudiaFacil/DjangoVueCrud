<template>
  <h1>Tareas</h1>
  <div class="container">
    <div v-for="(tarea, index) in tareas" :key="index" class="task">
      <h2 class="title">{{ tarea.titulo }}</h2>
      <p class="description">{{ tarea.descripcion }}</p>
      <div class="day">{{ getDayName(tarea.dia) }}</div>
      <div class="task-footer">
        <div class="completed-pill" :class="{ 'completed': tarea.completada, 'not-completed': !tarea.completada }">
          {{ tarea.completada ? 'Completado' : 'No completado' }}
        </div>
        <button class="edit-button" @click="$router.push(`/tasks/${tarea.id}`)">Editar</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Tarea } from '@/interfaces/Tarea';
import { getTareas } from '@/services/TareaService';
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    return {
      tareas: [] as Tarea[],
    };
  },
  methods: {
    async cargarTareas() {
      const res = await getTareas();
      this.tareas = res.data;
    },
    getDayName(dayNumber: number) {
      const days = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
      return days[dayNumber];
    },
  },
  mounted() {
    this.cargarTareas();
  },
});
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Open Sans', sans-serif;
}

.container {
  width: 100%;
  height: 80vh;
  overflow-y: scroll;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.task {
  width: 100%;
  margin: 10px 0;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  position: relative;
}

.task-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.title {
  text-align: left;
  margin: 0;
}

.description {
  color: #888888;
  margin: 6px 0;
  padding: 5px;
}

.day {
  position: absolute;
  top: 15px;
  right: 15px;
}

.completed-pill {
  display: inline-block;
  padding: 5px 10px;
  border-radius: 20px;
  color: #fff;
  font-weight: bold;
}

.completed {
  background-color: rgb(60, 210, 98);
}

.not-completed {
  background-color: rgb(187, 61, 30);
}

.edit-button {
  background-color: rgb(34, 72, 138);
  color: #fff;
  border-radius: 20px;
  border: none;
  padding: 5px 10px;
  font-weight: bold;
}

.edit-button:hover {
  background-color: darkblue;
}
</style>