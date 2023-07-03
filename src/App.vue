<script>
import Sidebar from './components/sidebar.vue';
import DiaSemana from './components/diaSemana.vue';

export default {
    components: {
        Sidebar,
        DiaSemana
    }, data() {
        return {
      diasSemana: ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
      diaTarea: '',
      nombreTarea: ''
    };
    },
    methods: {
        updateDiaSemana(dia) {
    this.diaTarea = dia;
  },
    updateNombreTarea(nombre) {
      this.nombreTarea = nombre;
    },
    actualizarNombreTarea(nuevaTarea) {
      this.nombreTarea = nuevaTarea.texto;
    }
  }
}

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
    <Sidebar :dia-semana="diaTarea" :nombre-tarea="nombreTarea" @update:dia-semana="updateDiaSemana" @update:nombre-tarea="updateNombreTarea"></Sidebar>
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
body {
    text-align: center;
}

.panelSemana {
    overflow-x: scroll;
    width: 800px;
}

.panelSemana::-webkit-scrollbar {
    /* Opcional: Para ocultar la barra de desplazamiento horizontal */
    display: auto;
}

main {
    margin-top: 4%;
}

.dias {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

.dias li {
    margin: 7px;
}
</style>