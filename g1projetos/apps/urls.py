from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('transparencia/', views.transparencia, name="transparencia"),
    path('loginpadrinhos/', views.loginpadrinhos, name="loginpadrinhos"),
    path('loginfuncionarios/', views.loginfuncionarios, name="loginfuncionarios"),
    path('cadastropadrinhos/', views.cadastropadrinhos, name="cadastropadrinhos"),
]