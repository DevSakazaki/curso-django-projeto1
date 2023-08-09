from django.shortcuts import render  # Le arquivo e renderiza arquivo

# Http Request


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'testes'
    })
    # Tem que retornar HTTP Response
