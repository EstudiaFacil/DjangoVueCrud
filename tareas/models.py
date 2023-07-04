from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    dia = models.IntegerField(default=1)
    completada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
