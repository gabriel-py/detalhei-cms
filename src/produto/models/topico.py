from django.db import models
from .sub_categoria import Subcategoria

class Topico(models.Model):
    titulo = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # noqa E501
    subcategoria = models.ForeignKey(
        Subcategoria,
        on_delete=models.SET_NULL,
        related_name='topicos',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'tópico'
        verbose_name_plural = 'tópicos'

    def __str__(self):
        return f'{self.titulo}'