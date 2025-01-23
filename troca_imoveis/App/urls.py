from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_imoveis, name='lista_imoveis'),
    path('curtir/<int:imovel_id>/', views.curtir_imovel, name='curtir_imovel'),
    path('descartar/<int:imovel_id>/', views.descartar_imovel, name='descartar_imovel'),
    path('troca/', views.troca, name='troca'),
]
