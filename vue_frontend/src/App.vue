<template>
  <div id="window">
    <div id="home-container">
      <TaskFormVue ref="formTarea" :encabezado="form_enc" :editar="form_edi" @formularioCompletado="tareaCreada" @salirEditar="cancelarEditar"/>
      <TaskList ref="taskList" @editar="editarTarea" @eliminar="eliminarTarea"/>

      <!-- Recuadro modal -->
      <EliminarTarea ref="elimTarea" rea="tareaSeleccionada" @tareaEliminada="refrescarLista"></EliminarTarea>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import TaskList from '@/components/TaskList.vue';
import TaskFormVue from '@/components/TaskForm.vue';
import EliminarTarea from '@/components/EliminarTarea.vue';

export default defineComponent({
  name: 'App',
  components: {
    TaskList,
    TaskFormVue,
    EliminarTarea,
  },
  data() {
    return {
      form_enc: 'Nueva Tarea',
      form_edi: false,
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
      this.form_enc = 'Editar Tarea';
      this.form_edi = true;

      (this.$refs.formTarea as typeof TaskFormVue)?.cargarTarea(id);
    },
    eliminarTarea(id: number) {
      (this.$refs.elimTarea as typeof EliminarTarea)?.mostrarModal(id);
    },
    cancelarEditar() {
      this.form_enc = 'Nueva Tarea';
      this.form_edi = false;
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
