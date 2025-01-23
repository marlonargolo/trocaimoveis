from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path('cadastro/', views.createPerfil, name='cadastro'),
    path('create_imovel/', views.create_imovel, name='create_imovel'),
    path('documentacao/', views.adicionar_documentacao, name='adicionar_documentacao'),

]
