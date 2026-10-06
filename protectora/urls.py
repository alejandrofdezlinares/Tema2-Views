from django.urls import path
from . import views

urlpatterns = [
    path('animales/', views.animales, name='animales'),
    path('protectoras/', views.protectoras, name='protectoras'),
    path('colaboradores/', views.colaboradores, name='colaboradores'),
]