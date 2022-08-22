from django.shortcuts import render

from myapp.models import Pessoa
def index(request):
    nome_value = request.user
    id_value = request.user.id

    #dicionario exemplo
    #dados = {"chave":"valor","key":"value"}


    dados = {"nome":nome_value,"id":id_value}
    print(type(dados))
    return render(request, "myapp/home.html",dados)
def funcao_views(request):
    return render(request, 'myapp/passo2.html')
def funcao2(request):
    idade=22
    nome='marilia'
    dados={"anos":idade,'nome':nome}
    return render(request, 'passo3.html',dados)
def funcao3(request):
    return render(request, 'passo4.html')

def verIMC(request):
    usuario = request.user
    pessoa = Pessoa.objects.get(usuario = usuario)

    valor =  pessoa.peso / (pessoa.altura * pessoa.altura)
    classificacao = ""
    if valor < 18.5:
        classificacao = "MAGREZA"


    if valor >= 18.5 and valor <=25:
        classificacao = "NORMAL"

    if valor >= 25 and valor <= 30:
        classificacao = "SOBREPESO"

    if valor >= 30 and valor < 40:
        classificacao = "SOBREPESO"

    if valor >= 40:
        classificacao = "OBESIDADE GRAVE"

    dados = {"pessoa":pessoa,"imc":valor,"classificacao":classificacao}
    return render(request, 'myapp/visualizador_de_imc.html',dados)

"""
def soma(a,b):
    return a+b
"""