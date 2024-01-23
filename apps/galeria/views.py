from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    return render(request, 'templates/galeria/index.html', {"cards": fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'templates/galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    #garante que para acessar as fotos o usuário precisa estar logado 
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, 'templates/galeria/buscar.html', {"cards": fotografias})

def searchtag(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    if request.method == 'GET':
        tag_id = request.GET.get('tag_id').upper()
        if tag_id:
            fotografias = fotografias.filter(tag=tag_id)
    return render(request, 'galeria/buscar.html', {'cards': fotografias})

''' 

Quando requerido o servidor de alura space será vizualizado no servidor o que tem em index.html 

'''
