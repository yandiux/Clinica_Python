from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('editar-historial/', views.editar_historial, name='editar_historial'),
    path('buscar-pacientes/', views.buscar_pacientes, name='buscar_pacientes'),
    path('', lambda request: redirect('login/')),
]
