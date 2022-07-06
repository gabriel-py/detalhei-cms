from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.api.serializers import *
from blog.models import *


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = None
    permission_classes = [IsAuthenticatedOrReadOnly]

class PostReportlViewSet(ModelViewSet):
    serializer_class = PostReportSerializer
    queryset = PostReport.objects.all()
    pagination_class = None

class ComentarioViewSet(ModelViewSet):
    serializer_class = ComentarioSerializer
    queryset = Comentario.objects.all()
    pagination_class = None
    permission_classes = [IsAuthenticatedOrReadOnly]
    
# class ProFaseViewSet(ModelViewSet):
#     serializer_class = ProFaseSerializer
#     queryset = ProFase.objects.all()
#     pagination_class = None

#     @action(methods=['post'], detail=False)
#     def save(self, request, *args, **kwargs):
#         empreendimento = ProEmpreendimento.objects.get(id=request.data["empreendimento"])

#         lista_de_ids = []
#         response = []

#         for item in request.data["fases"]:
#             if "id" in item:
#                 obj = ProFase.objects.get(id=item["id"])
#             else:
#                 if item['id_contrato_pai'] == None and item['nome'] == None and item['codigo'] == None and item['tipo_fase'] == None:
#                     continue
#                 obj = ProFase.objects.create(empreendimento=empreendimento)

#             obj.id_contrato_pai = item['id_contrato_pai']
#             obj.nome = item["nome"]
#             obj.codigo = item["codigo"]
#             obj.tipo_fase_id = item["tipo_fase"]
#             obj.save()
#             item["id"] = obj.id

#             lista_de_ids.append(item["id"])
#             response.append(item)

#         fases = ProFase.objects.filter(empreendimento=empreendimento).exclude(id__in=lista_de_ids)
#         ProConta.objects.filter(fase_id__in=[fase.id for fase in fases]).delete()
#         fases.delete()

#         return Response(response)
