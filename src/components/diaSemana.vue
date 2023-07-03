<script>
export default {
    data() {
        return {
            nuevaTareaTexto: '',
            tareas: []
        };
    },
    methods: {
        añadirTarea() {
            if (this.nuevaTareaTexto) {
                this.tareas.push({ id: Date.now(), texto: this.nuevaTareaTexto });
                this.nuevaTareaTexto = '';
            }
        }
    }
};
</script>

<template>
    <div class="panelTareas">
        <h3 class="dia">LUNES</h3>
        <br>
        <div class="nuevaTarea">
            <input class="form-control" type="text" placeholder="Nueva tarea" v-model="nuevaTareaTexto">
            <button class="añadirTarea btn btn-primary d-inline-flex align-items-center" @click="añadirTarea">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-lg"
                    viewBox="0 0 16 16">
                    <path fill-rule="evenodd"
                        d="M8 2a.5.5 0 0 1 .5.5v5h5a.5.5 0 0 1 0 1h-5v5a.5.5 0 0 1-1 0v-5h-5a.5.5 0 0 1 0-1h5v-5A.5.5 0 0 1 8 2Z" />
                </svg>
            </button>
        </div>
        <div class="tareas">
            <ul class="listaTareas">
                <div v-for="tarea in tareas" :key="tarea.id">
                    <div class="tarea">
                        <p>{{ tarea.texto }}</p>
                        <button class="btn btn-secondary d-inline-flex align-items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                class="bi bi-three-dots-vertical" viewBox="0 0 16 16">
                                <path d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z" />
                            </svg>
                        </button>
                    </div>
                </div>
            </ul>
        </div>
    </div>
</template>

<style scoped>
body {
    text-align: center;
}

.panelTareas {
    background-color: rosybrown;
    margin: 3%;
    padding: 5% 3%;
}

.tarea {
    background-color: aliceblue;
    margin: 3%;
}

.listaTareas {
    padding: 0;
}
</style>