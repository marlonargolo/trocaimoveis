from django.shortcuts import render, get_object_or_404
from .models import Chat
from imoveis.models import Imovel

def chat_room(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    return render(request, 'chat_room.html', {'chat': chat})
