<template>
  <div>
    <!-- Recuadro modal -->
    <div v-if="mostrar" class="modal">
      <div class="modal-content">
        <div class="encabezado">
          <h1> ¿Desea eliminar esta tarea?</h1>
          <hr>
        </div>

        <h2 class="title">{{ tarea.titulo }}</h2>
        <p class="description">{{ tarea.descripcion }}</p>
        <hr>
        <!-- Botones dentro del recuadro modal -->
        <div class="tarea-form">
          <button class="button delete" @click.prevent="eliminarTarea">Eliminar</button>
          <button class="button edit" @click.prevent="cerrarModal">Cancelar</button>
        </div>

      </div>
    </div>

  </div>
</template>

<script lang="ts">
import { Tarea } from '@/interfaces/Tarea';
import { getTarea, deleteTarea } from '@/services/TareaService';
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    return {
      mostrar: false,
      tarea: {} as Tarea,
      id: '',
    };
  },
  methods: {
    async mostrarModal(id: number) {
      const res = await getTarea(id.toString());
      this.tarea = res.data;

      this.mostrar = true;
    },
    cerrarModal() {
      this.mostrar = false;
    },
    async eliminarTarea() {
      try {
        const res = await deleteTarea(this.tarea.id.toString());
        console.log(res);
      } catch (error: any) {
        console.log('Error al eliminar la tarea:', error.message);
      }
      this.cerrarModal();
      this.$emit('tareaEliminada');
    },
  },
});
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Open Sans', sans-serif;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 20px;

  /* Transparencia para oscurecer el fondo */
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  width: 500px;
  background-color: #fff;
  padding: 20px;
  border-radius: 20px;
}

.encabezado {
  text-align: center;
  margin: 10px auto;
}

.encabezado h1 {
  font-size: 24px;
}

.title {
  text-align: left;
  margin: 0;
  font-size: 20px;
}

.description {
  color: #888888;
  margin: 6px 0;
  padding: 5px;
}

.tarea-form {
  margin-top: 10px;
  display: flex;
  justify-content: flex-end;
}

.button {
  color: #fff;
  border-radius: 20px;
  border: none;
  padding: 5px 10px;
  font-weight: bold;
  margin: 0 5px;
}

.edit {
  background-color: rgb(34, 72, 138);
}

.delete {
  background-color: rgb(187, 61, 30);
}

.edit:hover {
  background-color: darkblue;
  cursor: pointer;
}

.delete:hover {
  background-color: rgb(139, 0, 0);
  cursor: pointer;
}
</style>