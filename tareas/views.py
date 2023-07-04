from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import TareaSerializer
from .models import Tarea

class TareaView(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all()
