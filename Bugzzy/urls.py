
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/usuario/', include('usuarios.urls')), 
    path('api/v1/comunidad/', include('comunidades.urls')),
    path('api/v1/publicacion/', include('publicacion.urls')),

    path('api/v1/', include('escuela.urls')),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
