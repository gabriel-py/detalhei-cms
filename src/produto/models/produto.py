from django.db import models
from .categoria import Categoria


class Produto(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        related_name='produtos',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return f'{self.titulo}'