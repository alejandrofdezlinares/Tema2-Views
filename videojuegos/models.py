from django.core.exceptions import ValidationError
from django.db import models


class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Videojuego"
        verbose_name_plural = "Videojuegos"

    def __str__(self):
        return self.titulo


class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    creador = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="grupos_creados"
    )
    miembros = models.ManyToManyField(
        "auth.User", related_name="grupos_miembros", blank=True
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"

    def __str__(self):
        return self.nombre


class Amigo(models.Model):
    usuario = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="usuario_amigos"
    )
    amigo = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="amigos_de"
    )
    fecha_amistad = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Amigo"
        verbose_name_plural = "Amigos"

    def __str__(self):
        return f"{self.usuario} - {self.amigo}"

    def clean(self):
        super().clean()
        if hasattr(self, "usuario") and hasattr(self, "amigo"):
            if self.usuario == self.amigo:
                raise ValidationError(
                    "Un usuario no puede añadirse a sí mismo como amigo."
                )