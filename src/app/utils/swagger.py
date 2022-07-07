import rest_framework
from rest_framework_simplejwt import authentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentação - API VP6",
      default_version='v1',
      description="Documentação das APIs Django REST Framework \
      criada pela VP6 Consultoria em T.I",
      terms_of_service="#",
      contact=openapi.Contact(email="contato@vp6.com.br"),
   ),
   public=False,
   url='https://victa-api.vp6.com.br/', 
   permission_classes=[rest_framework.permissions.IsAuthenticatedOrReadOnly],
   authentication_classes=[authentication.JWTAuthentication,
                           rest_framework.authentication.SessionAuthentication]
)