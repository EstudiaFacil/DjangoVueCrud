<script>
import Sidebar from './components/sidebar.vue';
import DiaSemana from './components/diaSemana.vue';

export default {
    components: {
        Sidebar,
        DiaSemana
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
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Mis Tareas</a>
                    </li>
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
                <Sidebar></Sidebar>
            </div>
            <div class="col-8 panelSemana d-flex flex-nowrap overflow-auto">
                        <DiaSemana class ="Lunes"></DiaSemana>
                        <DiaSemana></DiaSemana>
                        <DiaSemana></DiaSemana>
                        <DiaSemana></DiaSemana>
                        <DiaSemana></DiaSemana>
                        <DiaSemana></DiaSemana>
                        <DiaSemana></DiaSemana>
            </div>
        
    </main>
</template>

<style scoped>
body {
    text-align: center;
}
.panelSemana{
    overflow-x: scroll;
    width: 800px;
}
.panelSemana::-webkit-scrollbar {
  /* Opcional: Para ocultar la barra de desplazamiento horizontal */
  display: none;
}
main{
    margin-top: 4%;
}
</style>