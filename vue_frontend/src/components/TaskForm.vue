<template>
  <div class="todo" :class="{ 'nuevo': !editar, 'editar': editar }">
    <div class="encabezado">
      <h1>{{ encabezado }}</h1>
    </div>

    <form @submit.prevent="submitForm">
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

      <div v-if="!editar" class="campo">
        <button class="tarea-btn">Crear Tarea</button>
      </div>

      <div v-if="editar" class="campo">
        <button class="tarea-btn">Guardar Cambios</button>
      </div>

    </form>

    <div v-if="editar" class="campo">
      <button class="tarea-btn" @click.prevent="salirEditar">Cancelar</button>
    </div>

  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { Tarea } from '@/interfaces/Tarea';
import { getTarea, updateTarea } from '@/services/TareaService';
import { createTarea } from '@/services/TareaService';

export default defineComponent({
  props: {
    encabezado: {
      type: String,
      required: true,
    },
    editar: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      tarea: {} as Tarea,
    };
  },
  methods: {
    submitForm() {
      if (this.editar) {
        this.guardarCambios();
      } else {
        this.crearTarea();
      }
    },
    async crearTarea() {
      const res = await createTarea(this.tarea);
      console.log(res);

      this.limpiarTarea();
      this.$emit('tareaCreada');
    },
    async guardarCambios() {
      try {
        const res = await updateTarea(this.tarea.id.toString(), this.tarea);
        console.log(res);
      } catch (error: any) {
        console.log('Error al editar la tarea:', error.message);
      }

      this.limpiarTarea();
      this.$emit('tareaEditada');
    },
    async cargarTarea(id: number) {
      try {
        const res = await getTarea(id.toString());
        this.tarea = res.data;
      } catch (error: any) {
        console.log('Error al cargar la tarea:', error.message);
        this.salirEditar();
      }
    },
    salirEditar() {
      this.limpiarTarea();
      this.$emit('salirEditar');
    },
    limpiarTarea() {
      this.tarea = {
        titulo: '',
        descripcion: '',
        dia: 0,
        completada: false,
      } as Tarea;
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
  border-radius: 12px;
}

.nuevo {
  background-color: #C8DCFA;
}

.editar {
  background-color: #FAE4C8;
}

.encabezado {
  text-align: center;
  margin: 10px auto;
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
  background-color: rgb(128, 174, 196);
  color: white;
  font-weight: bold;
}

.tarea-btn:hover {
  background-color: #8eb9b9;
  cursor: pointer;
}

.tarea-btn:active {
  background-color: #D4D5F1;
}
</style>