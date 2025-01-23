from django.shortcuts import render, get_object_or_404
from .models import Chat
from imoveis.models import Imovel

def chat_room(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    return render(request, 'chat_room.html', {'chat': chat})

from django.shortcuts import redirect, get_object_or_404
from .models import Chat
from imoveis.models import Imovel
from django.contrib.auth.decorators import login_required

@login_required
def iniciar_chat(request, imovel_id):
    imovel = get_object_or_404(Imovel, id=imovel_id)
    owner = imovel.proprietario

    # Verificar se o chat já existe
    chat, created = Chat.objects.get_or_create(
        imovel=imovel,
        user=request.user,
        owner=owner
    )

    # Redirecionar para o chat
    return redirect('chat_room', chat_id=chat.id)

@login_required
def lista_chats(request):
    chats = Chat.objects.filter(user=request.user)
    return render(request, 'lista_chats.html', {'chats': chats})
