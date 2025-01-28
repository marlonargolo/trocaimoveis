import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import database_sync_to_async
from .models import Message, Chat

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.chat_group_name = f'chat_{self.chat_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        sender = self.scope['user']

        # Salvar a mensagem no banco de dados
        chat = await database_sync_to_async(Chat.objects.get)(id=self.chat_id)
        await database_sync_to_async(Message.objects.create)(
            chat=chat, sender=sender, content=message
        )

        # Broadcast message to the group
        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.username,
            }
        )

    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
        }))
