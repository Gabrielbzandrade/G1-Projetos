from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('transparencia/', views.transparencia, name="transparencia"),
    path('portalpadrinhos/', views.portalpadrinhos, name="portalpadrinhos"),
    path('portalfuncionarios/', views.portalfuncionarios, name="portalfuncionarios"),
]