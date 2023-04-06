from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('buscador_de_colectivos/', views.buscador_de_colectivos, name='buscador_de_colectivos'),
    path('registro_de_colectivos/', views.registro_de_colectivos, name='registro_de_colectivos'),
    path('colectivos/<int:colectivo_id>/eliminar_colectivo', views.eliminar_colectivo, name='eliminar_colectivo'),
    path('colectivos/', views.colectivos, name='colectivos'),
    path('registro_de_usuarios/', views.registro_de_usuarios, name='registro_de_usuarios'),
    path('inicio_de_seccion/', views.inicio_de_seccion, name='inicio_de_seccion'),
    path('cerrar_seccion/', views.cierre_de_seccion, name='cierre_de_seccion'),
]