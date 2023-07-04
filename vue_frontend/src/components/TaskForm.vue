<template>
  <div class="todo">
    <div class="encabezado">
      <h1>Tarea</h1>
    </div>
    <form @submit.prevent="guardarTarea">
      <div class="campo">
        <label for="titulo" class="tarea-label">Título</label>
        <input type="text" class="tarea-input" id="titulo" name="titulo" placeholder="Título de tarea" v-model="tarea.titulo" required>
      </div>

      <div class="campo">
        <label for="descripcion" class="tarea-label">Descripción</label>
        <textarea rows="3" class="tarea-input" placeholder="Descripción de tarea" id="descripcion" v-model="tarea.descripcion" name="descripcion"></textarea>
      </div>

      <div class="campo">
        <label for="dia" class="tarea-label">Día</label>
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
      </div>

      <div class="campo">
        <div class="form-check">
          <input type="checkbox" class="tarea-check" id="terminada" name="terminada" v-model="tarea.terminada" required>
          <label for="terminada" >Tarea terminada</label>
        </div>
      </div>

      <button class="tarea-btn">Guardar cambios</button>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { Tarea } from '@/interfaces/Tarea';

export default defineComponent({
  data() {
    return {
      tarea: {} as Tarea,
    };
  },
  methods: {
    guardarTarea() {
      console.log(this.tarea);
    },
  },
});

</script>

<style scoped>
.todo {
  display: block;
  flex-direction: column;
  align-items: center;
  margin: 10px;
  padding: 0;
  width: 100%;
  height: 100%;
  background-color: rgb(25, 199, 190);
  max-width: 250px;
}

.encabezado {
  text-align: center;
  margin-bottom: 20px; /* Espacio entre el encabezado y el formulario */
}

.form-check {
  display: block;
  margin-top: 10px; /* Espacio entre cada campo del formulario */
  margin-bottom: 10px; /* Espacio entre cada campo del formulario */
  margin-left: 25%;
}

.tarea-label {
  text-align: center;
  margin-bottom: 10px; /* Espacio entre cada campo del formulario */
  margin-top: 10px; /* Espacio entre cada campo del formulario */
}

form {
  font-family: 'Montserrat', sans-serif; /* Cambio de fuente */
  font-size: 16px;
  color: #333;
  margin: 0;
  padding: 0;
}

.tarea-input {
  display: block;
  width: 75%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 10px; /* Espacio entre cada campo del formulario */
  box-sizing: border-box;
  margin-left: 12%;
}

.tarea-label {
  display: block;
}

.tarea-btn {
  display: center;
  width: 50%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 10px; /* Espacio entre cada campo del formulario */
  margin-left: 25%;
  box-sizing: border-box;
  background-color: rgb(255, 255, 255);
  color: black;
  font-weight: bold;
}

.tarea-btn:hover {
  background-color: #8eb9b9;
}

.tarea-btn:active {
  background-color: #cacbf5;
}
</style>