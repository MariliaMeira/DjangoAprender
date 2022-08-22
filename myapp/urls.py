from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ahahaha", views.funcao_views),
    path("passo3", views.funcao2),
    path("passo4", views.funcao3),
    path("verIMC", views.verIMC),

]