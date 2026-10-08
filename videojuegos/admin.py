from django.contrib import admin
from .models import Amigo, Grupo, Videojuego


@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo")


@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "creador", "fecha_creacion")
    filter_horizontal = ("miembros",)


@admin.register(Amigo)
class AmigoAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "amigo", "fecha_amistad")