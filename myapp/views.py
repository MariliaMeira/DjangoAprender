from django.shortcuts import render

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
    dados={"anos":idade}
    return render(request, 'passo3.html')
def funcao3(request):
    return render(request, 'passo4.html')

"""
def soma(a,b):
    return a+b
"""