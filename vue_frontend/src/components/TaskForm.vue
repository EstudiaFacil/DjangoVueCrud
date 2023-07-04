<template>
  <div class="todo">
    <div class="encabezado">
      <h1>{{ encabezado }}</h1>
    </div>

    <form @submit.prevent="guardarTarea">
      <div class="campo">
        <label for="titulo" class="tarea-label">Título
          <input type="text" class="tarea-input" id="titulo" name="titulo" placeholder="Título de tarea"
            v-model="tarea.titulo" required>
        </label>
      </div>

      <div class="campo">
        <label for="descripcion" class="tarea-label">Descripción
          <textarea rows="3" cols="10" class="tarea-input" placeholder="Descripción de tarea" id="descripcion"
            name="descripcion" v-model="tarea.descripcion"></textarea>
        </label>
      </div>

      <div class="campo">
        <label for="dia" class="tarea-label">Día
          <select class="tarea-input" id="dia" name="dia" v-model="tarea.dia" required>
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
      </div>

      <div class="campo">
        <div class="form-check">
          <label for="terminada" class="tarea-label">
            <input type="checkbox" class="tarea-check" id="terminada" name="terminada" v-model="tarea.completada"> Tarea
            terminada
          </label>
        </div>
      </div>

      <div class="campo">
        <button class="tarea-btn">Guardar Cambios</button>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { Tarea } from '@/interfaces/Tarea';
import { createTarea } from '@/services/TareaService';

export default defineComponent({
  props: {
    encabezado: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      tarea: {
        titulo: '',
        descripcion: '',
        dia: 0,
        completada: false,
      } as Tarea,
    };
  },
  methods: {
    async guardarTarea() {
      const res = await createTarea(this.tarea);
      console.log(res);

      this.tarea =  {
        titulo: '',
        descripcion: '',
        dia: 0,
        completada: false,
      } as Tarea;

      // Emitir el evento "formularioCompletado"
      this.$emit('formularioCompletado');
    },
  },
});

</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Open Sans', sans-serif;
}

.todo {
  display: block;
  flex-direction: column;
  align-items: center;
  margin: 10px 10px;
  width: 100%;
  height: 95vh;
  background-color: rgb(195, 205, 204);
  border-radius: 12px;
}

.encabezado {
  text-align: center;
  margin: 10px auto;
  /* Espacio entre el encabezado y el formulario */
}

.encabezado h1 {
  font-size: 24px;
}

.form-check {
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}

.campo {
  margin: 0 auto;
  width: 90%;
}

.tarea-label {
  margin-bottom: 10px;
  /* Espacio entre cada campo del formulario */
  margin-top: 10px;
  /* Espacio entre cada campo del formulario */
}

form {
  font-family: 'Open Sans', sans-serif;
  /* Cambio de fuente */
  font-size: 16px;
  color: #333;
  margin: 0;
  padding: 0;
}

.tarea-input {
  font-family: 'Open Sans', sans-serif;
  display: block;
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 10px;
}

textarea {
  resize: vertical;
  height: 150px;
}

.tarea-label {
  display: block;
}

.tarea-btn {
  width: 80%;
  display: block;
  margin: 0 auto;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: rgb(68, 143, 179);
  color: white;
  font-weight: bold;
}

.tarea-btn:hover {
  background-color: #8eb9b9;
  cursor: pointer;
}

.tarea-btn:active {
  background-color: #cacbf5;
}
</style>