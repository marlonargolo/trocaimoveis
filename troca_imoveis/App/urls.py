from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_imoveis, name='lista_imoveis'),
    path('descartar/<int:imovel_id>/', views.descartar_imovel, name='descartar_imovel'),
    path('troca/', views.troca, name='troca'),
    path('curtir-imovel/<int:imovel_id>/', views.curtir_imovel, name='curtir_imovel'),
    
]
