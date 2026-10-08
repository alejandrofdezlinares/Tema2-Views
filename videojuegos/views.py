from django.shortcuts import render
from .models import Amigo, Grupo, Videojuego


def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(
        request,
        "videojuegos/lista_videojuegos.html",
        {"videojuegos": videojuegos},
    )


def lista_grupos(request):
    grupos = Grupo.objects.prefetch_related("miembros").select_related("creador").all()
    return render(request, "videojuegos/lista_grupos.html", {"grupos": grupos})


def lista_amigos(request):
    amigos = Amigo.objects.select_related("usuario", "amigo").all()
    return render(request, "videojuegos/lista_amigos.html", {"amigos": amigos})