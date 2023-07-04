<template>
  <h1>Tarea</h1>
  <form @submit.prevent="guardarTarea">
    <label for="titulo" class="tarea-label">Título
      <input type="text" class="tarea-input" id="titulo" name="titulo" placeholder="Título de tarea"
        v-model="tarea.titulo" required>
    </label>

    <label for="descripcion" class="tarea-label">Descripción
      <textarea rows="3" class="tarea-textarea" placeholder="Descripción de tarea" id="descripcion"
        v-model="tarea.descripcion" name="descripcion"></textarea>
    </label>

    <label for="dia" class="tarea-label">Día
      <select class="tarea-select" id="dia" name="dia" v-model="tarea.dia" required>
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
        <input type="checkbox" class="tarea-input tarea-check" id="terminada" name="terminada" v-model="tarea.completada"
          required>
        Tarea terminada
      </label>
    </div>

    <button class="tarea-btn">Guardar cambios</button>
  </form>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { Tarea } from '@/interfaces/Tarea';
import { createTarea } from '@/services/TareaService';

export default defineComponent({
  data() {
    return {
      tarea: {} as Tarea,
    };
  },
  methods: {
    async guardarTarea() {
      const res = await createTarea(this.tarea);
      console.log(res);
      this.$router.push({name: 'tasks'});
    },
  },
});

</script>