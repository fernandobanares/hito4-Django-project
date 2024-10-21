# web/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # Ruta para "índice"
    path('acerca/', views.acerca, name='acerca'), # Ruta para "acerca"
    path('bienvenido/', views.bienvenido, name='bienvenido'), # Ruta para "bienvenido"
]
