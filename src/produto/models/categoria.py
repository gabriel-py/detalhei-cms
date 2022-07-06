from django.db import models


class Categoria(models.Model):
    titulo = models.CharField(max_length=100)

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return f'{self.titulo}'