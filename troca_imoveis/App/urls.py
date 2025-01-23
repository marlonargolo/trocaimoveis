from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_imoveis, name='lista_imoveis'),
]
