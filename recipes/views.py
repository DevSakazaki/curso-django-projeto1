from django.shortcuts import render  # Le arquivo e renderiza arquivo
from django.http import HttpResponse

# Http Request


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'testes'
    })
    # Tem que retornar HTTP Response


def contato(request):
    return render(request, 'me-apague/temp.html')


def sobre(request):
    return HttpResponse('sobre')
