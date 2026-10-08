from django.contrib import admin
from .models import Videojuego, Amigo, Grupo


@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'genero', 'plataforma')
    search_fields = ('nombre', 'genero', 'plataforma')
    list_filter = ('genero', 'plataforma')


@admin.register(Amigo)
class AmigoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'amigo', 'fecha_amistad')
    search_fields = ('usuario__username', 'amigo__username')
    list_filter = ('fecha_amistad',)
    raw_id_fields = ('usuario', 'amigo')


@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'creador', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion', 'creador__username')
    list_filter = ('fecha_creacion',)
    filter_horizontal = ('miembros',)