from django.urls import path, include
from rest_framework import routers

from tareas import views

router = routers.DefaultRouter()
router.register(r'tareas', views.TareaView, 'tareas')
router.register(r'usuarios', views.UsuarioView, 'usuarios')

urlpatterns = [
    path('api/', include(router.urls)),
]