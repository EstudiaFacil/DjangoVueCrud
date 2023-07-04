<template>
  <nav>
    <ul>
      <li>
        <router-link to="/">Tareas</router-link>
      </li>
      <li>
        <router-link to="/tasks/new">Crear Tarea</router-link>
      </li>
    </ul>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'NavbarMenu',
});
</script>
