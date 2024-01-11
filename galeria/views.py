from django.shortcuts import render


def index(request):
    return render(request, 'templates/galeria/index.html')


def imagem(request):
    return render(request, 'templates/galeria/imagem.html')
''' 

Quando requerido o servidor de alura space será vizualizado no servidor o que tem em index.html 

'''

