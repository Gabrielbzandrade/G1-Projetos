from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('transparencia/', views.transparencia, name="transparencia"),
    path('loginpadrinhos/', views.loginpadrinhos, name="loginpadrinhos"),
    path('loginfuncionarios/', views.loginfuncionarios, name="loginfuncionarios"),
    path('cadastropadrinhos/', views.cadastropadrinhos, name="cadastropadrinhos"),
    path('cadastrofuncionarios/', views.cadastrofuncionarios, name="cadastrofuncionarios"),
    path('portalpadrinhos/', views.portalpadrinhos, name="portalpadrinhos"),
    path('portalfuncionarios/', views.portalfuncionarios, name="portalfuncionarios"),
    path('Superman/', views.superman, name="Superman"),
    path('Ariel/', views.ariel, name="Ariel"),
    path('Batman/', views.batman, name="Batman"),
    path('Cinderela/', views.cinderela, name="Cinderela"),
    path('Calendario/', views.calendario, name="Calendario"),
    path('Adicionareventos/', views.adicionarevento, name="Adicionarevento"),
    path('relato/', views.relato, name="relato"),
    path('acesso_relatos/', views.acesso_relatos, name="acesso_relatos"),
    path ('criar_perfil/', views.criar_perfil, name='criar_perfil'),
    path ('acessar_perfil/', views.acessar_perfil, name='acessar_perfil'),
]