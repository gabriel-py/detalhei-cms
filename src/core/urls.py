# from django.contrib import admin
from django_stisla import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/detalhei/', include('detalhei.urls')),
    path('api/blog/', include('blog.urls')),
    path('api/access/', include('access.urls')),
]
