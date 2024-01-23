from django.urls import path
from apps.galeria.views import index, imagem, buscar, searchtag

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('searchtag/', searchtag, name='search-tag')
]