from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("cadastrar", views.cadastrar_altura_peso),
    path('cadastrar/submit', views.cadastrar_submit),

    path("excluir", views.excluir),
    path("verIMC", views.verIMC),
    path("aluno", views.verIMC2),

]