from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# cpf do usuario
class Cpf(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, blank=True, null=False)

    def __str__(self):
        if self.cpf:
            return f"cpf de {self.user.username}"
        return f"cpf sem usuario"
    
# cnpj do usuario se aplicavel    
class Cnpj(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=14, blank=True, null=True)

    def __str__(self):
        if self.cnpj:
            return f"cnpj de {self.user.username}"
        else:
            return f"cnpj sem usuário"

# informacoes pessoais de cadastro do usuario se aplicavel
class CadastroCliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=60, blank=False, null=False)
    apelido = models.CharField(max_length=20, blank=False, null=False)
    data_nascimento = models.DateField(blank=True, null=True)
    cpf = models.OneToOneField(Cpf, on_delete=models.CASCADE, blank=True, null=True)
    cnpj = models.OneToOneField(Cnpj, on_delete=models.CASCADE, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    cep = models.CharField(max_length=8, null=False, blank=False)
    telefone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=True)
    foto_perfil = models.ImageField(upload_to="fotos", blank=True, null=True)

    def __str__(self):
        cpf_value = self.cpf.cpf if self.cpf else "No CPF"
        return f"cadastro de {self.user.username} / nome: {self.nome_completo} / cpf: {cpf_value}"



class Imovel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cliente = models.ForeignKey(CadastroCliente, on_delete=models.CASCADE, null=True)
    tipo_imovel = models.CharField(max_length=30, blank=False, null=True)
    endereco = models.CharField(max_length=80, blank=False, null=True)
    cidade = models.CharField(max_length=25, blank=False, null=True)
    estado = models.CharField(max_length=12, blank=False, null=True)
    cep = models.CharField(max_length=8, blank=False, null=True)
    metro_total = models.FloatField(blank=False, null=True)
    metro_area_construida = models.FloatField(null=True)
    quartos = models.IntegerField(null=True)
    banheiros = models.IntegerField(null=True)
    garagem = models.IntegerField(null=True)
    ano_construcao = models.IntegerField(null=True)
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="imoveis", null=True, blank=True)
    relacao = models.CharField(max_length=80, null=True)

def __str__(self):
    return f"imovel do usuario {self.user.username}"


class Imagens(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="fotos", blank=False, null=True)
    descricao_imagem = models.CharField(max_length=20)

def __str__(self):
    return f"imagem de: {self.user.username} cpf: {self.cpf.cpf} "

class Documentacao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(CadastroCliente, on_delete=models.CASCADE)
    imovel = models.OneToOneField(Imovel, on_delete=models.CASCADE)
    escritura = models.BooleanField(default=False, null=False, blank=False)
    troca_menor = models.BooleanField(default=False, null=False, blank=False)
    troca_maior = models.BooleanField(default=False, null=False, blank=False)
    divida = models.BooleanField(default=False, null=False, blank=False)
    detalhes = models.CharField(max_length=100, null=True, blank=True)
    rg_img = models.ImageField(upload_to="docs", blank=False, null=False)
    cpf_img = models.ImageField(upload_to="docs", blank=False, null=False)
    comprovante_residencia = models.ImageField(upload_to="docs", blank=False, null=False)
    rosto = models.ImageField(upload_to="docs", blank=False, null=False)

def __str__(self):
    return f"documentacao de {self.user.username} / cpf: {self.cpf.cpf}"


class caracteristicas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imovel = models.OneToOneField(Imovel, on_delete=models.CASCADE)
    piscina = models.BooleanField(default=False, blank=False, null=False)
    churrasqueira = models.BooleanField(default=False, blank=False, null=False)
    jardim = models.BooleanField(default=False, blank=False, null=False)
    varanda = models.BooleanField(default=False, blank=False, null=False)
    armario = models.BooleanField(default=False, blank=False, null=False)
    elevador = models.BooleanField(default=False, blank=False, null=False)
    outros = models.CharField(max_length=50, blank=False, null=False)
    descricao_imovel = models.CharField(max_length=100, blank=False, null=False)
    imagens = models.ManyToManyField(Imagens, blank=False)
    valor = models.FloatField(null=False, blank=False)
    documentacao = models.ManyToManyField(Documentacao, blank=False)

def __str__(self):
    return self.cliente 











