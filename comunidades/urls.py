from django.urls import path, include
from rest_framework import routers
from comunidades import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'c', views.ComunidadViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('docs', include_docs_urls(title='Comunidad API'))
]
