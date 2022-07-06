from django.contrib.auth.models import Group, User
from django.db import models


class Menu(models.Model):
    TYPE = (
        ('MODULE', 'Módulo'),
        ('MENU', 'Menu'),
        ('PAGE', 'Página'),
    )
    name = models.CharField(max_length=64)
    path = models.CharField(max_length=64, unique=True)
    menu_type = models.CharField(max_length=6, choices=TYPE, default='PAGE')
    groups = models.ManyToManyField(Group, blank=True, verbose_name="Grupos")
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('path',)
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
