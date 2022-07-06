from django.db import models
from .nota import Nota
from ..topico import Topico

class NotaItens(models.Model):
    nota = models.ForeignKey(
        Nota,
        on_delete=models.SET_NULL,
        related_name='notas',
        null=True,
        blank=True
    )

    topico = models.ForeignKey(
        Topico,
        on_delete=models.SET_NULL,
        related_name='topico_itens',
        null=True,
        blank=True
    )
    
    valor = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # noqa E501
    valor_calculado = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'item'
        verbose_name_plural = 'itens'

    def __str__(self):
        return f'{self.pk}'

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=NotaItens)
def update_ranking(sender, instance, created, **Kwargs):
    pass