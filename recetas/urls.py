# recetas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recetas/', views.lista_recetas, name='lista_recetas'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('<int:receta_id>/', views.detalle_receta, name='detalle_receta'),
    path('pacientes/<int:paciente_id>/', views.detalle_paciente, name='detalle_paciente'),
]
