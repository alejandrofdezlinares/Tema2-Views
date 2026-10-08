from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Videojuego(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Videojuego"
        verbose_name_plural = "Videojuegos"

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
        related_name="amigos_de"
    )
    fecha_amistad = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Amistad"
        verbose_name_plural = "Amistades"
        unique_together = ('usuario', 'amigo')

    def clean(self):
        if self.usuario == self.amigo:
            raise ValidationError("Un usuario no puede ser amigo de sí mismo.")

    def __str__(self):
        return f"{self.usuario.username} es amigo de {self.amigo.username}"


class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    creador = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="grupos_creados",
        null=True, 
        blank=True
    )
    miembros = models.ManyToManyField(
        User, 
        related_name="grupos_pertenecientes", 
        blank=True
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Grupo de videojuegos"
        verbose_name_plural = "Grupos de videojuegos"

    def __str__(self):
        return self.nombre