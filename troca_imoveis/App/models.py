from django.db import models
from django.contrib.auth.models import User
from imoveis.models import Imovel

class InteracaoImovel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    curtido = models.BooleanField(default=False)
    descartado = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'imovel')
