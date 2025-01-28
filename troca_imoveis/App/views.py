from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import InteracaoImovel
from imoveis.models import Imovel

def lista_imoveis(request):
    imoveis = Imovel.objects.all()
    return render(request, 'lista_imoveis.html', {'imoveis': imoveis})

from django.shortcuts import get_object_or_404, redirect
from .models import InteracaoImovel
from imoveis.models import Imovel

def curtir_imovel(request, imovel_id):
    if request.method == 'POST':
        imovel = get_object_or_404(Imovel, id=imovel_id)
        interacao, created = InteracaoImovel.objects.get_or_create(user=request.user, imovel=imovel)
        interacao.curtido = True
        interacao.descartado = False
        interacao.save()
        return redirect('lista_imoveis')  # Redireciona de volta para a lista de imóveis

def descartar_imovel(request, imovel_id):
    imovel = get_object_or_404(Imovel, id=imovel_id)
    interacao, created = InteracaoImovel.objects.get_or_create(user=request.user, imovel=imovel)
    interacao.curtido = False
    interacao.descartado = True
    interacao.save()
    return JsonResponse({'success': True})

def troca(request):
    trocas = InteracaoImovel.objects.filter(user=request.user, curtido=True).select_related('imovel')
    return render(request, 'troca.html', {'trocas': trocas})
