from rest_framework.serializers import ModelSerializer
from detalhei.models import Categoria, Departamento, Area, Produto, Oferta, Loja,\
    Opiniao, Avaliacao, Descricao, Revisao, Comentario, ComentarioEngajamento, PostEngajamento,\
        Seguidores, Setor, Topico
        
class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class TopicoSerializer(ModelSerializer):
    class Meta:
        model = Topico
        fields = '__all__'

class DepartamentoSerializer(ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class AreaSerializer(ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'
        
class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
        
class OfertaSerializer(ModelSerializer):
    class Meta:
        model = Oferta
        fields = '__all__'
        
class LojaSerializer(ModelSerializer):
    class Meta:
        model = Loja
        fields = '__all__'
        
class OpiniaoSerializer(ModelSerializer):
    class Meta:
        model = Opiniao
        fields = '__all__'
        
class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'
        
class DescricaoSerializer(ModelSerializer):
    class Meta:
        model = Descricao
        fields = '__all__'
        
class RevisaoSerializer(ModelSerializer):
    class Meta:
        model = Revisao
        fields = '__all__'

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
        ref_name = "detalhei_comentario"
        
class ComentarioEngajamentoSerializer(ModelSerializer):
    class Meta:
        model = ComentarioEngajamento
        fields = '__all__'
        
class PostEngajamentoSerializer(ModelSerializer):
    class Meta:
        model = PostEngajamento
        fields = '__all__'
        
class SeguidoresSerializer(ModelSerializer):
    class Meta:
        model = Seguidores
        fields = '__all__'
        
class SetorSerializer(ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'