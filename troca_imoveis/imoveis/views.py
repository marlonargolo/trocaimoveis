from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import CadastroCliente, Cpf, Cnpj, Imovel, Documentacao, Imagens
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImovelForm, CaracteristicasForm, ImagensForm, DocumentacaoForm
from django.forms import modelformset_factory


# Crie suas visualizações aqui.


def index(request):
    return render(request, 'index.html')

#cadastro de usuario
@login_required(login_url='/accounts/login/')
def createPerfil(request):
    # Garante que o usuário está autenticado
    if not request.user.is_authenticated:
        return render(request, "perfil.html", {"error": "Usuário não autenticado!"})

    # Obtém ou cria o perfil para o usuário atual
    perfil, criado = CadastroCliente.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Atualiza os campos do perfil com base nos dados enviados no formulário
        perfil.nome_completo = request.POST.get("nome", "")
        perfil.apelido = request.POST.get("apelido", "")

        # Verifica e converte a data de nascimento
        data_nascimento_str = request.POST.get("data_de_nascimento", "")
        if data_nascimento_str:
            try:
                perfil.data_nascimento = datetime.strptime(data_nascimento_str, "%d-%m-%y")  # Supondo que o formato seja 'YYYY-MM-DD'
            except ValueError:
                perfil.data_nascimento = None  # Caso a conversão falhe, a data será definida como None
        
        perfil.endereco = request.POST.get("endereco", "")
        perfil.cep = request.POST.get("cep", "")
        perfil.telefone = request.POST.get("telefone", "")
        perfil.whatsapp = request.POST.get("whatsapp", "")
        perfil.email = request.POST.get("email", "")

        # Processa a foto de perfil
        if 'foto_perfil' in request.FILES:
            perfil.foto_perfil = request.FILES['foto_perfil']


        # Atualiza ou cria o CPF
        cpf_valor = request.POST.get("cpf", None)
        if cpf_valor:
            # Tente obter o objeto Cpf do usuário atual, caso não exista, cria um novo
            cpf_obj, created = Cpf.objects.get_or_create(user=request.user)
            cpf_obj.cpf = cpf_valor
            cpf_obj.save()
            perfil.cpf = cpf_obj  # Associa o CPF ao perfil
        else:
            perfil.cpf = None  # Caso o CPF não seja fornecido, desvincula

        # Atualiza o CNPJ de maneira semelhante
        cnpj_valor = request.POST.get("cnpj", None)
        if cnpj_valor:
            cnpj_obj, created = Cnpj.objects.get_or_create(user=request.user)
            cnpj_obj.cnpj = cnpj_valor
            cnpj_obj.save()
            perfil.cnpj = cnpj_obj  # Associa o CNPJ ao perfil
        else:
            perfil.cnpj = None  # Caso o CNPJ não seja fornecido, desvincula

        # Salva as alterações no perfil
        perfil.save()

        return render(request, "perfil.html", {"perfil": perfil})

    return render(request, "perfil.html", {"perfil": perfil})

#cadastro de imovel 
@login_required
def list_imoveis(request):
    imoveis = Imovel.objects.filter(user=request.user)
    return render(request, 'list_imoveis.html', {'imoveis': imoveis})

@login_required
def edit_imovel(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk, user=request.user)
    # ... resto do código para editar o imóvel
    return render(request, 'edit_imovel.html', {'imovel': imovel})

@login_required
def delete_imovel(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk, user=request.user)
    imovel.delete()
    return redirect('list_imoveis')

@login_required(login_url='/accounts/login/')
def create_imovel(request):
    ImagensFormSet = modelformset_factory(Imagens, form=ImagensForm, extra=3)  # Permite o upload de múltiplas imagens
    if request.method == 'POST':
        imovel_form = ImovelForm(request.POST)
        caracteristicas_form = CaracteristicasForm(request.POST)
        imagens_formset = ImagensFormSet(request.POST, request.FILES, queryset=Imagens.objects.none())

        if imovel_form.is_valid() and caracteristicas_form.is_valid() and imagens_formset.is_valid():
            imovel = imovel_form.save(commit=False)
            imovel.user = request.user
            imovel.save()

            caracteristicas = caracteristicas_form.save(commit=False)
            caracteristicas.user = request.user  # Certifique-se de que o campo no modelo seja `user`
            caracteristicas.imovel = imovel
            caracteristicas.save()


            for form in imagens_formset:
                if form.cleaned_data:  # Verifica se há dados válidos no formulário
                    imagem = form.save(commit=False)
                    imagem.user = request.user
                    imagem.save()
                    caracteristicas.imagens.add(imagem)

            messages.success(request, 'Imóvel cadastrado com sucesso!')
            return render (request, 'lista_imoveis.html') # Redirecionar para uma lista de imóveis

    else:
        imovel_form = ImovelForm()
        caracteristicas_form = CaracteristicasForm()
        imagens_formset = ImagensFormSet(queryset=Imagens.objects.none())

    context = {
        'imovel_form': imovel_form,
        'caracteristicas_form': caracteristicas_form,
        'imagens_formset': imagens_formset,
    }
    return render(request, 'create_imovel.html', context)


#documentacao

@login_required(login_url='/accounts/login/')
def adicionar_documentacao(request):
    # Verifica se o usuário já possui uma documentação cadastrada
    documentacao_existente = Documentacao.objects.filter(user=request.user).first()

    if request.method == 'POST':
        if documentacao_existente:
            # Atualiza a documentação existente
            form = DocumentacaoForm(request.POST, request.FILES, instance=documentacao_existente)
        else:
            # Cria uma nova documentação
            form = DocumentacaoForm(request.POST, request.FILES)

        if form.is_valid():
            documentacao = form.save(commit=False)
            documentacao.user = request.user
            documentacao.save()
            messages.success(request, 'Documentação salva com sucesso!')
            return redirect('adicionar_documentacao')
        else:
            messages.error(request, 'Houve um erro ao salvar a documentação. Verifique os campos.')
    else:
        # Mostra o formulário com os dados da documentação, se existir
        form = DocumentacaoForm(instance=documentacao_existente)

    context = {
        'form': form,
        'documentacao_existente': documentacao_existente,
    }
    return render(request, 'adicionar_documentacao.html', context)