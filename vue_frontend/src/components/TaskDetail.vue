<template>
  <form @submit.prevent="actualizarTarea">
    <label for="titulo" class="tarea-label">Título
      <input type="text" class="tarea-input" id="titulo" name="titulo" placeholder="Título de tarea"
        v-model="tareaActual.titulo" required>
    </label>

    <label for="descripcion" class="tarea-label">Descripción
      <textarea rows="3" class="tarea-textarea" placeholder="Descripción de tarea" id="descripcion"
        v-model="tareaActual.descripcion" name="descripcion"></textarea>
    </label>

    <label for="dia" class="tarea-label">Día
      <select class="tarea-select" id="dia" name="dia" v-model="tareaActual.dia" required>
        <option disabled selected value=0>Selecciona un día</option>
        <option value=1>Lunes</option>
        <option value=2>Martes</option>
        <option value=3>Miércoles</option>
        <option value=4>Jueves</option>
        <option value=5>Viernes</option>
        <option value=6>Sábado</option>
        <option value=7>Domingo</option>
      </select>
    </label>

    <div class="form-check">
      <label for="terminada" class="tarea-label">
        <input type="checkbox" class="tarea-input tarea-check" id="terminada" name="terminada"
          v-model="tareaActual.completada" required>
        Tarea terminada
      </label>
    </div>

    <button class="tarea-btn">Actualizar</button>
  </form>

  <button class="eliminar-btn" @click="eliminarTarea">Eliminar</button>
</template>

<script lang="ts">
import { Tarea } from '@/interfaces/Tarea';
import { getTarea, updateTarea, deleteTarea } from '@/services/TareaService';
import { defineComponent, resolveTransitionHooks } from 'vue';

export default defineComponent({
  data() {
    return {
      tareaActual: {} as Tarea,
    };
  },
  methods: {
    async cargarTarea(id: string) {
      if (typeof this.$route.params.id == "string") {
        const res = await getTarea(this.$route.params.id);
        this.tareaActual = res.data
      }
    },
    async actualizarTarea() {
      if (typeof this.$route.params.id == "string") {
        const res = await updateTarea(this.$route.params.id, this.tareaActual);
        console.log(res);
        this.$router.push({ name: 'tasks' });
      }
    },
    async eliminarTarea() {
      if (typeof this.$route.params.id == "string") {
        const res = await deleteTarea(this.$route.params.id);
        console.log(res);
        this.$router.push({ name: 'tasks' });
      }
    },
  },
  mounted() {
    if (typeof this.$route.params.id == "string") {
      this.cargarTarea(this.$route.params.id);
    }
  },
});

</script>
