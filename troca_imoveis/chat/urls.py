from django.urls import path
from . import views

urlpatterns = [
    path('<int:chat_id>/', views.chat_room, name='chat_room'),
]
