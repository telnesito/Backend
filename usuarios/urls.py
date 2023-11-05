from django.urls import path, include
from rest_framework import routers
from usuarios import views
from rest_framework.documentation import include_docs_urls
from .views import get_usuarios_estudiantes, get_usuarios, get_usuario_especifico


urlpatterns = [ 
    path('get_usuarios/', get_usuarios, name='api usuarios'),
    path('get_usuarios/<int:pk>/', get_usuario_especifico, name = 'Buscar por cedula'),
    path('perfil_estudiante', get_usuarios_estudiantes),
    path('docs', include_docs_urls(title='Usuarios API'))
    
]
