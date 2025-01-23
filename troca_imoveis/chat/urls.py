from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_chats, name='lista_chats'),
    path('<int:chat_id>/', views.chat_room, name='chat_room'),
    path('iniciar/<int:imovel_id>/', views.iniciar_chat, name='iniciar_chat'),

]
