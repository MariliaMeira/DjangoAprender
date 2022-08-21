from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ahahaha", views.funcao_views),
    path("passo3", views.funcao2)]