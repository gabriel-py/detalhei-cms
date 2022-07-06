from rest_framework.routers import DefaultRouter
from django.urls import path, include
from detalhei.api.viewsets import CategoriaViewSet, DepartamentoViewSet, AreaViewSet,\
    ProdutoViewSet, OfertaViewSet, LojaViewSet, OpiniaoViewSet,\
    AvaliacaoViewSet, DescricaoViewSet, RevisaoViewSet, ComentarioViewSet,\
    ComentarioEngajamentoViewSet, PostEngajamentoViewSet, SeguidoresViewSet

router = DefaultRouter()
router.register(r'categoria', CategoriaViewSet)
router.register(r'departamento', DepartamentoViewSet)
router.register(r'area', AreaViewSet)
router.register(r'produto', ProdutoViewSet)
router.register(r'oferta', OfertaViewSet)
router.register(r'loja', LojaViewSet)
router.register(r'opiniao', OpiniaoViewSet)
router.register(r'avaliacao', AvaliacaoViewSet)
router.register(r'descricao', DescricaoViewSet)
router.register(r'revisao', RevisaoViewSet)
router.register(r'comentario', ComentarioViewSet)
router.register(r'comentario-engajamento', ComentarioEngajamentoViewSet)
router.register(r'post-engajamento', PostEngajamentoViewSet)
router.register(r'seguidores', SeguidoresViewSet)

urlpatterns = [
    path('', include(router.urls)),
]