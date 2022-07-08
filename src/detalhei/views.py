from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from detalhei.models import Post, Produto, Avaliacao, NotaAvaliacao, Topico, Area, Categoria, \
    NormalizacaoBacklog, Sumario, SumarioNormalizado
import pandas as pd
import numpy as np
import json

{
    "produto": 1,
    "notas": [
        {"topico": 6, "nota": 7.5},
        {"topico": 7, "nota": 7.5},
        {"topico": 8, "nota": 7.5},
        {"topico": 9, "nota": 7.5},
        {"topico": 10, "nota": 7.5},
    ]
}

@api_view(['POST'])
def createAvaliacao(request):
    body = json.loads(request.body)
    produto = Produto.objects.get(id=body["produto"])
    notas = body["notas"]
    
    post = Post.objects.create(produto=produto, created_by=request.user)
    avaliacao = Avaliacao.objects.create(post=post)
    
    objs = []
    for nota in notas:
        topico = Topico.objects.get(id=nota["topico"])
        obj = NotaAvaliacao(
            topico=topico,
            avaliacao=avaliacao,
            nota=nota["nota"]
        )
        objs.append(obj)
    
    NotaAvaliacao.objects.bulk_create(objs, batch_size=1000)
    
    NormalizacaoBacklog.objects.create(
        avaliacao=avaliacao
    )
    return JsonResponse({'success': True}, safe=False)

@api_view(['POST'])
def getRanking(request):
    body = json.loads(request.body)
    area = Area.objects.get(id=body["area"])
    
    produtos = Produto.objects.filter(area=area).all()
    
    result = {}
    for produto in produtos:
        ranking = NormalizacaoRanking.objects.filter(avaliacao__post__produto=produto).all()
        result["produto"] = produto.nome
        result["overall_score_normalizado"] = ranking.overall_score_normalizado

        notas = []
        sumarios = SumarioNormalizado.objects.filter(produto=produto).all()
        for s in sumarios:
            notas.append({
                s.categoria: s.nota
            })
        result["categoria"] = notas
            
    return JsonResponse({'success': True}, safe=False)

def calculoSumario(obj):
    avaliacao = obj.avaliacao
    produto = avaliacao.post.produto
    area = produto.area
    categorias = Categoria.objects.filter(area=area).all()
    
    objs_sumarios = []
    total_score = 0
    total_max_score = 0
    sum_scores = 0
    i = 0
    for categoria in categorias:
        topicos_da_categoria = Topico.objects.filter(categoria=categoria).all()
        
        somatorio_notas_topicos = 0
        max_score = 0
        for topico in topicos_da_categoria:
            notaAvObj = NotaAvaliacao.objects.filter(avaliacao=avaliacao, topico=topico).all()
            somatorio_notas_topicos = somatorio_notas_topicos + notaAvObj.nota
            max_score = max_score + (notaAvObj.topico.peso)*10
        
        total_score = total_score + somatorio_notas_topicos
        total_max_score = total_max_score + max_score
        score = somatorio_notas_topicos/max_score * 100
        sum_scores = sum_scores + score
        i = i + 1
        
        objSum = Sumario(
            produto=produto,
            categoria=categoria,
            nota=score
        )
        objs_sumarios.append(objSum)
        
    NormalizacaoRanking.objects.create(
        avaliacao=avaliacao,
        average_score=sum_scores/i,
        overall_score=total_score/total_max_score*100
    )
    
    Sumario.objects.bulk_create(objs_sumarios, batch_size=1000)
    updateProdutos(area)


def updateProdutos(area):
    categorias = Categoria.objects.filter(area=area).all()
    produtos_to_recalculate = Produto.objects.filter(area=area).all()
    ids_produtos = [p.id for p in produtos_to_recalculate]
    SumarioNormalizado.objects.filter(produto_id__in=ids_produtos).delete()
    
    for categoria in categorias:
        sumarios = Sumario.objects.filter(produto__area=area, categoria=categoria).all()
        
        max_note = -1
        for s in sumarios:
            if s.nota > max_note:
                max_note = s.nota
        
        objs = []        
        for s in sumarios:
            nota_normalizada = s.nota / max_note * 100
            obj = SumarioNormalizado(
                produto=s.produto,
                categoria=categoria,
                nota=nota_normalizada
            )
            objs.append(obj)
            
        SumarioNormalizado.objects.bulk_create(objs, batch_size=1000)
    
    ranking_to_update = NormalizacaoRanking.objects.filter(avaliacao__post__produto__area=area).all()
    max_average_score = -1
    max_overall_score = -1
    for r in ranking_to_update:
        if r.average_score > max_average_score:
            max_average_score = r.average_score
        if r.overall_score > max_overall_score:
            max_overall_score = r.overall_score
    
    to_update = []        
    for r in ranking_to_update:
        r.average_score_normalizado = r.average_score / max_average_score * 100
        r.overall_score_normalizado = r.overall_score / max_overall_score * 100
        to_update.append(r)
    
    NormalizacaoRanking.objects.bulk_update(to_update, batch_size=1000)

@api_view(['GET'])
def consultaBacklog(request):
    objs = NormalizacaoBacklog.objects.all()
    
    for obj in objs:
        calculoSumario(obj)

