
from django.urls import path, include
from . import views

urlpatterns = [
    path('access/', views.Access.as_view(), name='access'),
    path('new-password/', views.NewPassword.as_view(), name='new-password'),
    path('change-password/', views.ChangePassword.as_view(), name='change-password'),
]
