from django.shortcuts import render, redirect

from myapp.models import Pessoa

def cadastrar_submit(request):
    if request.POST:
        peso = float(request.POST.get('peso').replace(",","."))
        altura = float(request.POST.get('altura').replace(",","."))
        usuario = request.user
        pessoa = verificarSeUsuarioJaTemCadastradoSeuPesoeAltura(usuario,peso,altura)

        return redirect('/verIMC')

def verificarSeUsuarioJaTemCadastradoSeuPesoeAltura(usuario,peso,altura):
    try:
        pessoa = Pessoa.objects.get(usuario = usuario)

        pessoa.peso = peso
        pessoa.altura = altura
        pessoa.save()
    except:
        pessoa = Pessoa.objects.create(usuario = usuario,
                           peso= peso,
                           altura=altura)
    return pessoa
def home(request):
    return render(request, 'myapp/home.html')
def cadastrar_altura_peso(request):
    return render(request, 'myapp/cadastrar.html')

def excluir(request):
    usuario = request.user
    pessoa = Pessoa.objects.get(usuario=usuario)
    pessoa.delete()
    return redirect('/')


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
