from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import Group, User
import os
import secrets
import base64
import json


class Post(models.Model):
    created_by = models.ForeignKey(User, models.PROTECT)
    title = models.CharField(max_length=150)
    content = models.TextField()
    # images
    # videos
    nota = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    
class PostReport(models.Model):
    REASONS = (
        ('spam', 'Conteúdo sem sentido'),
        ('hate', 'Conteúdo de ódio'),
        ('misinformation', 'Contém informações falsas ou  imprecisas'),
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, models.PROTECT)
    content = models.TextField()
    reason = models.CharField(max_length=100, choices=REASONS, default='spam', db_index=True)

    def __str__(self):
        return self.content

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, models.PROTECT)
    response_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    has_the_product = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content