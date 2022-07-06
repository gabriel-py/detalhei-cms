from django.db import models
from .categoria import Categoria

class Subcategoria(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        related_name='subcategorias',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'subcategoria'
        verbose_name_plural = 'subcategorias'

    def __str__(self):
        return f'{self.titulo}'