from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import Group, User
import os
import secrets
import base64
import json
# from django.db.models import JSONField
import jsonfield

class Setor(models.Model):
    nome = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Departamento(models.Model):
    nome = models.CharField(max_length=150)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Area(models.Model):
    nome = models.CharField(max_length=150)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Categoria(models.Model):
    nome = models.CharField(max_length=150)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Topico(models.Model):
    nome = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.TextField()
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    nota = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    # empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Loja(models.Model):
    nome = models.CharField(max_length=50)
    logo = models.TextField()
    url_site_loja = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Oferta(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_creator')
    title = models.CharField(max_length=150, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    # images
    # videos
    video_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    
class Opiniao(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gostei = models.CharField(max_length=180)
    gostaria = models.CharField(max_length=180)
    eh_recomendada = models.BooleanField()
    eh_verificada = models.BooleanField()
    
class Avaliacao(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    pontos_fortes = jsonfield.JSONField(blank=True, null=True)
    pontos_fracos = jsonfield.JSONField(blank=True, null=True)
    nota = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    custo_beneficio = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
class NotaAvaliacao(models.Model):
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
class Descricao(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    caracteristicas = jsonfield.JSONField()

class Revisao(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pontos_fortes = jsonfield.JSONField()
    pontos_fracos = jsonfield.JSONField()

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="criador_comentario")
    response_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    has_the_product = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content

class ComentarioEngajamento(models.Model):
    ACOES = (
        ('like', 'Curtiu o comentário'),
        ('favorito', 'Favoritou o comentário'),
    )
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    acao = models.CharField(max_length=100, choices=ACOES, default='like', db_index=True)
    
class PostEngajamento(models.Model):
    ACOES = (
        ('like', 'Curtiu o post'),
        ('favorito', 'Favoritou o post'),
        ('compartilhar', 'Compartilhou o post'),
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    acao = models.CharField(max_length=100, choices=ACOES, default='like', db_index=True)
    
class Seguidores(models.Model):
    seguidor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_que_segue")
    seguindo = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_que_eh_seguido")
    
class NormalizacaoBacklog(models.Model):
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class NormalizacaoRanking(models.Model):
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, blank=True, null=True)
    average_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    overall_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    average_score_normalizado = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    overall_score_normalizado = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
class Sumario(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
class SumarioNormalizado(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)