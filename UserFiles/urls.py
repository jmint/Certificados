from django.urls import path
from .views import Files, filtrarCertificados

urlpatterns = [
    path('files/<str:pk>', Files.as_view(), name='files'),
    path('files_ajax/', filtrarCertificados, name='filtrar'),
]