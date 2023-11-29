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
    path('Calendario/', views.calendario, name="Calendario"),
    path('Adicionareventos/', views.adicionarevento, name="Adicionarevento"),
    path('relato/', views.relato, name="relato"),
    path('acesso_relatos/', views.acesso_relatos, name="acesso_relatos"),
    path ('criar_perfil/', views.criar_perfil, name='criar_perfil'),
    path ('acessar_perfil/', views.acessar_perfil, name='acessar_perfil'),
    path('Afilhados_padrinhos/', views.Afilhados_padrinhos, name='Afilhados_padrinhos'),
    path('Afilhados_funcionarios/', views.Afilhados_funcionarios, name='Afilhados_funcionarios'),
    path('perfil_afilhado/<int:id_afilhado>/', views.perfil_afilhado, name='perfil_afilhado'),
    path('excluir_perfil/', views.excluir_perfil, name='excluir_perfil'),
    path('atualizar_status/', views.atualizar_status, name="atualizar_status"),
    path('acessar_status/', views.acessar_status, name="acessar_status"),
    path('feedback/', views.feedback, name="feedback"),
    path('acessar_feedback/', views.acessar_feedback, name="acessar_feedback"),
]