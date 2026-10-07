from django.db import models
from django.contrib.auth.models import User


class Videojuego(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Publicacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Publicación de {self.usuario.username}"


class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Amigo(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="amistades"
    )
    amigo = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="amigos"
    )
    fecha_amistad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.amigo.username}"