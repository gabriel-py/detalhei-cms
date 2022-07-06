from rest_framework.serializers import ModelSerializer
from blog.models import *

        
class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class PostReportSerializer(ModelSerializer):

    class Meta:
        model = PostReport
        fields = '__all__'

class ComentarioSerializer(ModelSerializer):

    class Meta:
        model = Comentario
        fields = '__all__'