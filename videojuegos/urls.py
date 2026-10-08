from django.urls import path
from . import views

urlpatterns = [
    path("videojuegos/", views.lista_videojuegos, name="lista_videojuegos"),
    path("grupos/", views.lista_grupos, name="lista_grupos"),
    path("amigos/", views.lista_amigos, name="lista_amigos"),
]