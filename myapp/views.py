from django.shortcuts import render

def index(request):
    return render(request, "myapp/home.html")
def funcao_views(request):
    return render(request, 'myapp/passo2.html')
def funcao2(request):
    return render(request, 'passo3.html')