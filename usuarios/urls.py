from django.urls import path, include
from rest_framework import routers
from usuarios import views
from rest_framework.documentation import include_docs_urls
from .views import get_usuarios_estudiantes, get_usuarios, get_usuario_especifico, get_usuarios_profesores, get_usuarios_coordinador, estudianteEspecifico


urlpatterns = [ 
    path('get_usuarios/', get_usuarios, name='api usuarios'),
    path('get_usuarios/<int:pk>/', get_usuario_especifico, name = 'Buscar por cedula'),
    
    path('perfil_estudiante', get_usuarios_estudiantes, name='Obtener los perfiles de los usuarios'),
    path('perfil_estudiante/<int:pk>/', estudianteEspecifico, name='Acceder a un estudiante especifico'),

    path('perfil_profesor', get_usuarios_profesores, name='Obtener los perfiles de los profesores' ),
    path('perfil_coordinador', get_usuarios_coordinador, name='Obtener los perfiles de los coordinadores' ),
    
    path('docs', include_docs_urls(title='USUARIOS API')),
]
