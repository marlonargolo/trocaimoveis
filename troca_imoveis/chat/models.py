from django.db import models
from django.contrib.auth.models import User
from imoveis.models import Imovel

class Chat(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_chats")
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
