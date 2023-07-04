<template>
  <div id="window">
    <Navbar />
    <!-- <router-view /> -->
    <div id="home-container">
      <TaskFormVue :encabezado="from_enc"/>
      <TaskList ref="taskList" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Navbar from '@/components/Navbar.vue';
import TaskList from '@/components/TaskList.vue';
import TaskFormVue from '@/components/TaskForm.vue';

export default defineComponent({
  name: 'App',
  components: {
    Navbar,
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
