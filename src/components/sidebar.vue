<script>
export default {
  props: ['nombreTarea', 'desTarea', 'diaSemana', 'tareaTerminada'],
  data() {
    return {
      diasSemana: ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
    };
  },
  methods: {
    guardarCambios() {
      const datos = {
        nombreTarea: this.nombreTarea,
        desTarea: this.desTarea,
        diaSemana: this.diaSemana,
        tareaTerminada: this.tareaTerminada,
      };
      this.$emit('guardar-cambios', datos);
    },
  },
};
</script>

<template>
    <div class="sidebar d-flex flex-column flex-shrink-0 bg-body-tertiary">

        <h1>Tarea</h1>

        <form class="needs-validation" novalidate>
            <label for="titulo" class="form-label">Título</label>
            <input type="text" class="form-control" id="titulo" name="titulo" placeholder="Título de tarea"
              :value="nombreTarea" @input="$emit('update:nombre-tarea', $event.target.value)" required>

            <div class="invalid-feedback">
                Ingrese un nombre válido.
            </div>

            <div class="col-md-12">
                <label for="descripcion" class="form-label">Descripción</label>
                <textarea class="form-control" placeholder="Descripción de tarea" id="descripcion" name="descripcion"
                  style="height: 100px" @input="$emit('update:des-tarea', $event.target.value)"></textarea>

                <div class="invalid-feedback">
                    Una descripción es necesaria.
                </div>
            </div>

            <div class="col-md-12">
                <label for="country" class="form-label">Día</label>
                <select class="form-select" :value="diaSemana"
                  @input="$emit('update:dia-semana', parseInt($event.target.value))" required>
                    <option disabled selected value="0">Selecciona un día</option>
                    <option value="1">Lunes</option>
                    <option value="2">Martes</option>
                    <option value="3">Miércoles</option>
                    <option value="4">Jueves</option>
                    <option value="5">Viernes</option>
                    <option value="6">Sábado</option>
                    <option value="7">Domingo</option>
                </select>
                <div class="invalid-feedback">
                    Selecciona un dia.
                </div>
            </div>

            <hr class="my-4">

            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="tarea-terminada" :checked="tareaTerminada"
                  @change="$emit('update:tarea-terminada', $event.target.value)">
                <label class="form-check-label" for="tarea-terminada">Tarea terminada</label>
            </div>

            <hr class="my-4">

            <button class="btn btn-primary btn-lg" @click.prevent="guardarCambios">Guardar cambios</button>

        </form>

        <hr>
        <div class="dropdown">
            <a href="#" class="d-flex align-items-center link-body-emphasis text-decoration-none dropdown-toggle"
              data-bs-toggle="dropdown" aria-expanded="false">
                <img src="./icons/perfil-del-usuario.png" alt="" width="32" height="32" class="rounded-circle me-2">
                <strong>mdo</strong>
            </a>
            <ul class="dropdown-menu text-small shadow">
                <li><a class="dropdown-item" href="#">Sign out</a></li>
            </ul>
        </div>

    </div>
</template>

<style scoped>
body {
    text-align: center;
}

h1 {
    font-size: 2em;
    margin: 0 auto 8px;
    padding: 0;
}

label {
    display: block;
    margin-top: 4px;
}

.sidebar {
    margin: 0;
    padding: 3%;
    height: 100%;
    width: 280px;
}
</style>