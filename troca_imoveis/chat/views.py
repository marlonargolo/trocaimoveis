from django.shortcuts import render, get_object_or_404
from .models import Chat
from imoveis.models import Imovel

def chat_room(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    return render(request, 'chat_room.html', {'chat': chat})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Chat
from django.contrib.auth.decorators import login_required

@login_required
def iniciar_chat(request, imovel_id):
    # Agora você usa 'imovel_id' em vez de 'id_imovel'
    imovel = get_object_or_404(Imovel, id=imovel_id)

    # Atribui o usuário logado ao campo `user`
    chat, created = Chat.objects.get_or_create(
        imovel=imovel,
        owner=request.user,
        user=request.user  # Certifique-se de passar o usuário aqui também
    )

    if created:
        pass

    return render(request, 'chat_room.html', {'chat': chat, 'imovel': imovel})

@login_required
def lista_chats(request):
    chats = Chat.objects.filter(user=request.user)
    return render(request, 'lista_chats.html', {'chats': chats})