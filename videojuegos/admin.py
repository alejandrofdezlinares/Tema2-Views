from django.contrib import admin
from .models import Videojuego, Publicacion, Grupo, Amigo

admin.site.register(Videojuego)
admin.site.register(Publicacion)
admin.site.register(Grupo)
admin.site.register(Amigo)