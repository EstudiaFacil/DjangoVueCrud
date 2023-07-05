<template>
  <div id="window">
    <div id="home-container">
      <TaskFormVue :encabezado="from_enc" @formularioCompletado="tareaCreada"/>
      <TaskList ref="taskList" @editar="editarTarea" @eliminar="eliminarTarea"/>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import TaskList from '@/components/TaskList.vue';
import TaskFormVue from '@/components/TaskForm.vue';

export default defineComponent({
  name: 'App',
  components: {
    TaskList,
    TaskFormVue,
  },
  data() {
    return {
      from_enc: 'Nueva Tarea',
    };
  },
  mounted() {
    this.refrescarLista();
  },
  methods: {
    refrescarLista() {
      (this.$refs.taskList as typeof TaskList)?.cargarTareas();
    },
    tareaCreada() {
      this.refrescarLista();
    },
    editarTarea(id: number) {
      console.log('Editar tarea con ID:', id);
      // Agrega aquí el código para editar la tarea correspondiente
    },
    eliminarTarea(id: number) {
      console.log('Eliminar tarea con ID:', id);
      // Agrega aquí el código para eliminar la tarea correspondiente
    },
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

#window {
  width: 100%;
  height: 100vh;
  max-height: 100vh;
}

#home-container {
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-columns: 2fr 8fr;
}

</style>
