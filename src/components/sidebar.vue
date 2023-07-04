<script>
export default {
    props: {
        diaSemana: {
            type: String,
            required: true
        },
        nombreTarea: {
            type: String,
            required: true
        }
    },
    setup(props) {
        // setup() receives props as the first argument.
        console.log(props.diaSemana,props.nombreTarea);
    },
    data() {
        return {
            descripcion: '',
            tareaTerminada: false,
            dia: ''
        };
    },
    methods: {
        guardarCambios() {
            this.nombreTarea = '';
            this.descripcion = '';
            this.diaSemana = '';
            this.tareaTerminada = false;
        }
    }
}
</script>

<template>
    <div class="sidebar d-flex flex-column flex-shrink-0 bg-body-tertiary" style="width: 280px;">
        <form class="needs-validation" novalidate>
            <input type="text" class="form-control" id="firstName" placeholder="Nombre tarea" :value="nombreTarea" required>

            <div class="invalid-feedback">
                Ingrese un nombre válido.
            </div>

            <div class="col-12">
                <label for="lastName" class="form-label">Descripción</label>
                <textarea class="form-control" placeholder="Descripción de tarea" id="floatingTextarea2"
                    style="height: 100px"></textarea>
                <div class="invalid-feedback">
                    Una descripciòn es necesaria.
                </div>
            </div>

            <div class="col-md-12">
                <label for="country" class="form-label">Día</label>
                <select class="form-select" :value=diaSemana required>
                    <option value="Lunes">Lunes</option>
                    <option value="Martes">Martes</option>
                    <option value="Miércoles">Miércoles</option>
                    <option value="Jueves">Jueves</option>
                    <option value="Viernes">Viernes</option>
                    <option value="Sábado">Sábado</option>
                    <option value="Domingo">Domingo</option>
                </select>
                <div class="invalid-feedback">
                    Selecciona un dia.
                </div>
            </div>



            <hr class="my-4">

            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="same-address">
                <label class="form-check-label" for="same-address">Tarea terminada</label>
            </div>

            <hr class="my-4">

            <button class="btn btn-primary" @click="guardarCambios">Guardar cambios</button>
            <button class="btn btn-danger" @click="eliminarTarea">Eliminar</button>

        </form>

        <hr>
        <div class="dropdown">
            <a href="#" class="d-flex align-items-center link-body-emphasis text-decoration-none dropdown-toggle"
                data-bs-toggle="dropdown" aria-expanded="false">
                <img src="https://github.com/mdo.png" alt="" width="32" height="32" class="rounded-circle me-2">
                <strong>mdo</strong>
            </a>
            <ul class="dropdown-menu text-small shadow">
                <li><a class="dropdown-item" href="#">New project...</a></li>
                <li><a class="dropdown-item" href="#">Settings</a></li>
                <li><a class="dropdown-item" href="#">Profile</a></li>
                <li>
                    <hr class="dropdown-divider">
                </li>
                <li><a class="dropdown-item" href="#">Sign out</a></li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
body {
    text-align: center;
}

.sidebar {
    margin: 0;
    padding: 3%;
}
button{
    margin-right: 5px;
}
</style>
