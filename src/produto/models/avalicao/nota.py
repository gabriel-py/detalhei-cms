from django.db import models
from ..produto import Produto

class Nota(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    data = models.DateTimeField(auto_now_add=True)
    produto = models.ForeignKey(
        Produto,
        on_delete=models.SET_NULL,
        related_name='produto_itens',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'nota'
        verbose_name_plural = 'notas'

    def __str__(self):
        return f'{self.titulo}'

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Nota)
def update_ranking(sender, instance, created, **Kwargs):
    category_products = instance.produto.categoria.produtos.all()

    for product in category_products:
        product_item = product.produto_itens.first()
        scores = product_item.notas.all()
        
        for score in scores:
            from produto.models import Topico
            topico = Topico.objects.filter(id=score.topico_id).first()
            peso = float(topico.peso)
            score.valor_calculado = float(score.valor) * peso
            score.save()