from django.urls import path, include
from rest_framework import routers
from escuela import views
from rest_framework.documentation import include_docs_urls

router=routers.DefaultRouter()
router.register(r'escuela',views.EscuelaViewSet) 

urlpatterns = [
    path('', include(router.urls)),
    path('docs', include_docs_urls(title='Escuela API'))
]
