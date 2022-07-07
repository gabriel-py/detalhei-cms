from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import filters

from detalhei.api.serializers import CategoriaSerializer, DepartamentoSerializer, AreaSerializer,\
    ProdutoSerializer, OfertaSerializer, LojaSerializer, OpiniaoSerializer,\
    AvaliacaoSerializer, DescricaoSerializer, RevisaoSerializer, ComentarioSerializer,\
    ComentarioEngajamentoSerializer, PostEngajamentoSerializer, SeguidoresSerializer, \
        SetorSerializer, TopicoSerializer

from detalhei.models import Categoria, Departamento, Area, Produto, Oferta, Loja,\
    Opiniao, Avaliacao, Descricao, Revisao, Comentario, ComentarioEngajamento, PostEngajamento,\
        Seguidores, Setor, Topico

class SetorViewSet(ModelViewSet):
    serializer_class = SetorSerializer
    queryset = Setor.objects.all()
    pagination_class = None
    
class DepartamentoViewSet(ModelViewSet):
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all()
    pagination_class = None
    
    def get_queryset(self):
        queryParams = self.request.GET.get('setor')
        if queryParams is None:
            return Departamento.objects.all()
        return Departamento.objects.filter(setor__id=queryParams)

class AreaViewSet(ModelViewSet):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()
    pagination_class = None
    
    def get_queryset(self):
        queryParams = self.request.GET.get('departamento')
        if queryParams is None:
            return Area.objects.all()
        return Area.objects.filter(departamento__id=queryParams)
    
class CategoriaViewSet(ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
    pagination_class = None
    
    def get_queryset(self):
        queryParams = self.request.GET.get('area')
        if queryParams is None:
            return Categoria.objects.all()
        return Categoria.objects.filter(area__id=queryParams)
    
class TopicoViewSet(ModelViewSet):
    serializer_class = TopicoSerializer
    queryset = Topico.objects.all()
    pagination_class = None
    
    def get_queryset(self):
        queryParams = self.request.GET.get('categoria')
        if queryParams is None:
            return Topico.objects.all()
        return Topico.objects.filter(categoria__id=queryParams)
    
class ProdutoViewSet(ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()
    pagination_class = None
    
    def get_queryset(self):
        queryParams = self.request.GET.get('area')
        if queryParams is None:
            return Produto.objects.all()
        return Produto.objects.filter(area__id=queryParams)
    
class OfertaViewSet(ModelViewSet):
    serializer_class = OfertaSerializer
    queryset = Oferta.objects.all()
    pagination_class = None
    
class LojaViewSet(ModelViewSet):
    serializer_class = LojaSerializer
    queryset = Loja.objects.all()
    pagination_class = None
    
class OpiniaoViewSet(ModelViewSet):
    serializer_class = OpiniaoSerializer
    queryset = Opiniao.objects.all()
    pagination_class = None
    
class AvaliacaoViewSet(ModelViewSet):
    serializer_class = AvaliacaoSerializer
    queryset = Avaliacao.objects.all()
    pagination_class = None
    
class DescricaoViewSet(ModelViewSet):
    serializer_class = DescricaoSerializer
    queryset = Descricao.objects.all()
    pagination_class = None
    
class RevisaoViewSet(ModelViewSet):
    serializer_class = RevisaoSerializer
    queryset = Revisao.objects.all()
    pagination_class = None
    
class ComentarioViewSet(ModelViewSet):
    serializer_class = ComentarioSerializer
    queryset = Comentario.objects.all()
    pagination_class = None
    
class ComentarioEngajamentoViewSet(ModelViewSet):
    serializer_class = ComentarioEngajamentoSerializer
    queryset = ComentarioEngajamento.objects.all()
    pagination_class = None
    
class PostEngajamentoViewSet(ModelViewSet):
    serializer_class = PostEngajamentoSerializer
    queryset = PostEngajamento.objects.all()
    pagination_class = None
    
class SeguidoresViewSet(ModelViewSet):
    serializer_class = SeguidoresSerializer
    queryset = Seguidores.objects.all()
    pagination_class = None
