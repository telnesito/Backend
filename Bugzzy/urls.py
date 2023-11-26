
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/usuario/', include('usuarios.urls')), 
    path('api/v1/comunidad/', include('comunidades.urls')),
    path('api/v1/publicacion/', include('publicacion.urls')),

    path('api/v1/', include('escuela.urls')),
    
    
]
