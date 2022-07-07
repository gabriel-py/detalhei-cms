from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from detalhei.models import Post, Produto, Avaliacao, NotaAvaliacao, Topico, Area, Categoria
import pandas as pd
import numpy as np

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
    
    return JsonResponse({'success': True}, safe=False)

