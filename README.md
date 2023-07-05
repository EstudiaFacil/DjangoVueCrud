# DjangoVueCrud

## Requisitos para correr el Proyecyo
- Tener Docker instalado es su computadora. [link al instalador Docker](https://www.docker.com/)
- Instalar Visual Studio Code. [link al instalador VSCode](https://code.visualstudio.com/)
- (Opcional) Instalar Git en su computadora. [link al instalador Git](https://git-scm.com/)

> <b>Nota</b>: Estos requisitos son para correr los servidores en un contenedor de Docker.

## Instalación del proyecto
Clona el proyecto en una carpeta del sistema.
> <b>Nota</b>: Si no instalaste Git puede descargar directamente el zip, desde el boton Code en GitHub seleciona la ultima opcíon, <b>Download ZIP</b> y extrae la carpeta en tu computadora. Luego abre el proyecto desde VSCode.

Abre una terminal en la carpeta donde deseas descargar el repositorio y ejecuta:
```bash
git clone https://github.com/EstudiaFacil/DjangoVueCrud.git
```

Luego ejecuta los comandos para ingresar a la carpeta generada e ingresar a la carpeta con VSCode:
```bash
cd DjangoVueCrud
code .
```

Una vez finalizado esto se abrira en tu VSCode la carpeta que contiene el proyecto.
> <b>Nota</b>: Puedes abrir manualmente la carpeta desde VSCode si tienes alguna dificultad.

## Ejecutar proyecto
Dentro de VSCode abre una terminal, para abrir una terminal ingresa a *Terminal* en el menú superior luego seleciona *Nueva Terminal*.

Una vez ya se habra la terminal, ejecuta el siguiente comando.
```bash
docker-compose up
```

Con esto docker creara los 2 contenedores que funcionaran como servidores de la app.

Espera a que se ejecute, esto puede tardar algunos minutos.

## Ingresar a los servidores
### Frontend
Para ingresar al Frontend es el siguiente link: [https://localhost:8080](https://localhost:8080)
### Backend
Para ingresar al Backend es el siguiente link: [https://localhost:8000](https://localhost:8000)

