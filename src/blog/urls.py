from rest_framework.routers import DefaultRouter
from django.urls import path, include
from blog.api.viewsets import PostViewSet, PostReportlViewSet, ComentarioViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'post-report', PostReportlViewSet)
router.register(r'comentario', ComentarioViewSet)
# router.register(r'post-report', PostReportlViewSet)
# router.register(r'comentario', ComentarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]