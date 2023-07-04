<script>
import Sidebar from './components/sidebar.vue';
import DiaSemana from './components/diaSemana.vue';

export default {
  components: {
    Sidebar,
    DiaSemana
  },
  data() {
    return {
      diasSemana: ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
      nombreTarea: '',
      desTarea: '', // Agrega esta línea
      diaTarea: 0,
      tareaTerminada: false, // Agrega esta línea
    };
  },
  methods: {
    actualizarNombreTarea(nuevaTarea) {
      this.nombreTarea = nuevaTarea.texto;
    },
    actualizarDatos(datos) {
      // Actualizar los datos en el componente padre
      this.nombreTarea = datos.nombreTarea;
      this.desTarea = datos.desTarea;
      this.diaTarea = datos.diaSemana;
      this.tareaTerminada = datos.tareaTerminada;

      // Mostrar los datos en la consola
      console.log('Nombre de tarea:', this.nombreTarea);
      console.log('Descripción:', this.desTarea);
      console.log('Día de la semana:', this.diaTarea);
      console.log('Tarea terminada:', this.tareaTerminada);

      // Limpiar los campos en el componente padre
      // this.nombreTarea = '';
      // this.desTarea = '';
      // this.diaTarea = 0;
      // this.tareaTerminada = false;
    },
  },
};
</script>

<template>
  <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#"></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse"
        aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav me-auto mb-2 mb-md-0">
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>

  <main class="d-flex flex-nowrap">
    <div class="col-4">
      <Sidebar :nombre-tarea="nombreTarea" :des-tarea="desTarea" :dia-semana="diaTarea" :tarea-terminada="tareaTerminada"
        @guardar-cambios="actualizarDatos"></Sidebar>
    </div>
    <div class="col-8 panelSemana d-flex flex-nowrap overflow-auto">
      <ul class="dias d-flex flex-row">
        <li v-for="dia in diasSemana" :key="dia">
          <DiaSemana :nombre="dia" @tarea-creada="actualizarNombreTarea"></DiaSemana>
        </li>
      </ul>
    </div>
  </main>
</template>

<style scoped>
* {
  box-sizing: border-box;
  padding: 0;
}

nav {
  padding: 10px 0;
}

body {
  text-align: center;
  width: 100%;
  height: 100%;
}

main {
  height: 90vh;
  margin-top: 4%;
}

.panelSemana {
  overflow-x: scroll;
  width: 800px;
  height: 100%;
}

.panelSemana::-webkit-scrollbar {
  /* Opcional: Para ocultar la barra de desplazamiento horizontal */
  display: auto;
}

.dias {
  list-style-type: none;
  padding: 0;
  margin: 0;
  height: 100%;
}

.dias li {
  margin: 7px;
}
</style>