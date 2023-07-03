
<script>
</script>

<template>
    <div class="sidebar d-flex flex-column flex-shrink-0 bg-body-tertiary" style="width: 280px;">
        <form class="needs-validation" novalidate>
                    <input type="text" class="form-control" id="firstName" placeholder="Nombre de tarea" value="" required>
                    <div class="invalid-feedback">
                        Ingrese un nombre válido.
                    </div>
                
                <div class="col-12">
                    <label for="lastName" class="form-label">Descripción</label>
                    <textarea class="form-control" placeholder="Descripción de tarea" id="floatingTextarea2" style="height: 100px"></textarea>
                    <div class="invalid-feedback">
                        Una descripciòn es necesaria.
                    </div>
                </div>

                <div class="col-md-12">
                    <label for="country" class="form-label">Día</label>
                    <select class="form-select" id="country" required>
                        <option value="">Choose...</option>
                        <option>Lunes</option>
                        <option>Martes</option>
                        <option>Miércoles</option>
                        <option>Jueves</option>
                        <option>Viernes</option>
                        <option>Sábado</option>
                        <option>Domingo</option>
                    </select>
                    <div class="invalid-feedback">
                        Please select a valid country.
                    </div>
                </div>

            

            <hr class="my-4">

            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="same-address">
                <label class="form-check-label" for="same-address">Tarea terminada</label>
            </div>

            <hr class="my-4">

            <button class="btn btn-primary btn-lg">Guardar cambios</button>
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
.sidebar{
    margin: 0;
    padding: 3%;
}
</style>