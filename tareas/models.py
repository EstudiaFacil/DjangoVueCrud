from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, unique=True)
    contrasenia_hash = models.CharField(max_length=128)

    def set_contrasenia(self, contrasenia):
        self.contrasenia_hash = make_password(contrasenia)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    dia = models.IntegerField(default=1)
    completada = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
