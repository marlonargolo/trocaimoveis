from django.shortcuts import render
from imoveis.models import Imovel, Imagens

def lista_imoveis(request):
    imoveis = Imovel.objects.all()
    return render(request, 'lista_imoveis.html', {'imoveis': imoveis})
