from django.contrib import admin
from .models import CadastroCliente, Cpf, Cnpj, Imovel, Imagens, Documentacao, caracteristicas
# Register your models here.


admin.site.register(CadastroCliente)

admin.site.register(Cpf)

admin.site.register(Imovel)

admin.site.register(Imagens)

admin.site.register(Documentacao)

admin.site.register(caracteristicas)

