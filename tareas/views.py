from rest_framework import viewsets

from .serializer import TareaSerializer, UsuarioSerializer
from .models import Tarea, Usuario

class TareaView(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all()
