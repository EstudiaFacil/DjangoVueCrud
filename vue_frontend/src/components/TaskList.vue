<template>
  <h1>Tareas</h1>
  <div>
    <div v-for="(tarea, index) in tareas" :key="index">
      <h2>{{ tarea.titulo }}</h2>
      <p>{{ tarea.descripcion }}</p>
      <p>{{ tarea.dia }}</p>
      <p>{{ tarea.completada }}</p>
      <button @click="$router.push(`/tasks/${tarea.id}`)">Editar</button>
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
  },
  mounted() {
    this.cargarTareas();
  },
});
</script>