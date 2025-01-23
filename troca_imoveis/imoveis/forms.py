from django import forms
from .models import Imovel, caracteristicas, Imagens, Documentacao

class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = '__all__' 
        exclude = ('user', 'cliente')  # Excluir o campo 'user' do formulário

class CaracteristicasForm(forms.ModelForm):
    class Meta:
        model = caracteristicas
        fields = '__all__'
        exclude = ('user', 'imovel', 'imagens', 'documentacao', 'cliente') 

class ImagensForm(forms.ModelForm):
    class Meta:
        model = Imagens
        fields = '__all__'
        exclude = ('user',)

class DocumentacaoForm(forms.ModelForm):
    class Meta:
        model = Documentacao
        fields = [
            'escritura',
            'troca_menor',
            'troca_maior',
            'divida',
            'detalhes',
            'rg_img',
            'cpf_img',
            'comprovante_residencia',
            'rosto',
        ]
        