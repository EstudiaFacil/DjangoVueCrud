from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

from tareas import views

router = routers.DefaultRouter()
router.register(r'tareas', views.TareaView, 'tareas')
router.register(r'usuarios', views.UsuarioView, 'usuarios')

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='Tareas API'))
]