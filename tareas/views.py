from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import TareaSerializer, UsuarioSerializer
from .models import Tarea, Usuario

class TareaView(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all()

class UsuarioView(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        # Verificar si se proporcionó una contraseña en la solicitud
        contrasenia = request.data.get('contrasenia')
        if contrasenia:
            instance.set_contrasenia(contrasenia)
        
        self.perform_update(serializer)
        
        return Response(serializer.data)