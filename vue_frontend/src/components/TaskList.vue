<template>
  <div class="tareas">
    <div class="encabezado">
      <h1> Lista de Tareas</h1>
      <hr>
    </div>

    <div class="container">
      <div v-for="(tarea, index) in tareas" :key="index" class="task">
        <h2 class="title">{{ tarea.titulo }}</h2>
        <p class="description">{{ tarea.descripcion }}</p>
        <div class="day">{{ getDayName(tarea.dia) }}</div>
        <div class="task-footer">
          <div class="completed-pill" :class="{ 'completed': tarea.completada, 'not-completed': !tarea.completada }">
            {{ tarea.completada ? 'Completado' : 'No completado' }}
          </div>
          <form class="tarea-form" :id="'form-' + index" action="">
            <button class="button edit" @click.prevent="editar(tarea.id)">Editar</button>
            <button class="button delete" @click.prevent="eliminar(tarea.id)">Eliminar</button>
          </form>
        </div>
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
      id: 0,
    };
  },
  methods: {
    async cargarTareas() {
      const res = await getTareas();
      this.tareas = res.data;
      this.tareas.sort((a: Tarea, b: Tarea) => b.id - a.id);
    },
    getDayName(dayNumber: number) {
      const days = ['','Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo',];
      return days[dayNumber];
    },
    saludo() {
      console.log('Hola');
    },
    editar(id: number) {
      this.$emit('editar', id);
    },
    eliminar(id: number) {
      this.$emit('eliminar', id);
    },
  },
  // mounted() {
  //   this.cargarTareas();
  // },
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

.encabezado {
  text-align: center;
  margin: 10px auto;
}

.encabezado h1 {
  font-size: 24px;
}

.tareas {
  margin: 0 auto;
  width: 90%;
  height: 90vh;
  display: block;
}

.container {
  width: 100%;
  height: 100%;
  overflow-y: scroll;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  border: 1px solid rgb(187, 187, 187);
  border-radius: 12px;
}

.task {
  width: 100%;
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #2e2e2e;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
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
  font-size: 20px;
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
  font-size: 12px;
}

.completed {
  background-color: rgb(60, 210, 98);
}

.not-completed {
  background-color: rgb(187, 61, 30);
}

.tarea-form {
  display: inline-block;
}

.button {
  color: #fff;
  border-radius: 20px;
  border: none;
  padding: 5px 10px;
  font-weight: bold;
  margin: 0 5px;
}

.edit {
  background-color: rgb(34, 72, 138);
}

.delete {
  background-color: rgb(187, 61, 30);
}

.edit:hover {
  background-color: darkblue;
  cursor: pointer;
}

.delete:hover {
  background-color: rgb(139, 0, 0);
  cursor: pointer;
}
</style>