from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExcluirPerfilForm, CalendarioForm
from .models import Calendario, Relatos, Perfil, Status

def inicio(request):
    return render(request, 'apps/inicio.html')

def transparencia(request):
    return render(request, 'apps/transparencia.html')

def loginpadrinhos(request):
    context = {
        'title': 'Login Padrinhos',
        'texts': ['E-mail'],
        'passwords': ['Senha'],                          # Mudar para pagina de esquecimento de senha
        'links': [{'title': 'Esqueceu sua senha?', 'ref': 'inicio'}, {'title': 'Criar Conta', 'ref': 'cadastropadrinhos'}],
        'entrar': 'portalpadrinhos' # Mudar para portalpadrinhos
    }
    return render(request, 'apps/baselogin.html', context)

def loginfuncionarios(request):
    context = {
        'title': 'Login Funcionários',
        'texts': ['E-mail'],
        'passwords': ['Senha'],                   # Mudar para pagina de esquecimento de senha
        'links': [{'title': 'Esqueceu sua senha?', 'ref': 'inicio'}, {'title': 'Criar Conta Institucional', 'ref': 'cadastrofuncionarios'}],
        'entrar': 'portalfuncionarios' 
    }
    return render(request, 'apps/baselogin.html', context)

def cadastropadrinhos(request):
    context = {
        'title': 'Cadastro Padrinhos',
        'texts': ['Informe seu E-mail'],
        'passwords': ['Informe sua Senha'],
        'links': [{'title': 'Login', 'ref': 'loginpadrinhos'}],
        'entrar': 'inicio'
    }
    return render(request, 'apps/baselogin.html', context)

def cadastrofuncionarios(request):
    context = {
        'title': 'Cadastro Funcionários',
        'texts': ['Informe seu E-mail institucional'],
        'passwords': ['Informe sua Senha'],
        'links': [{'title': 'Login', 'ref': 'loginfuncionarios'}],
        'entrar': 'inicio'
    }
    return render(request, 'apps/baselogin.html', context)

def portalfuncionarios(request):
    return render(request, 'apps/portalfuncionarios.html')


def portalpadrinhos(request):
    context = {
        'lista': [i for i in range(12)],
        'afilhados': ['Superman', 'Ariel', 'Batman', 'Cinderela']
    }
    return render(request, 'apps/portalpadrinhos.html', context)

def adicionarevento (request):
    if request.method == 'POST':
        form = CalendarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Calendario')
    else:
        form = CalendarioForm()
    return render(request, 'apps/adicionareventos.html', {'form': form})

def calendario (request):
    eventos = Calendario.objects.order_by('data')
    return render(request, 'apps/calendario.html', {'eventos': eventos})

def relato(request):
    return render(request,'apps/relato.html')

def acesso_relatos(request):
    if request.method == 'POST':
        novo_relato = Relatos()
        novo_relato.titulo = request.POST.get('titulo')
        novo_relato.texto = request.POST.get('texto')

        if novo_relato.titulo and novo_relato.texto:
            novo_relato.save()

    relatos = {
        'relatos': Relatos.objects.all()
    }
    return render(request,'apps/acesso_relatos.html', relatos)

def criar_perfil(request):
    return render(request,'apps/criar_perfil.html')

def acessar_perfil(request):
    if request.method == 'POST':
        novo_perfil = Perfil()
        novo_perfil.nome = request.POST.get('nome')
        novo_perfil.padrinho = request.POST.get('padrinho')
        novo_perfil.data_nascimento = request.POST.get('data_nascimento')
        novo_perfil.caracteristicas = request.POST.get('caracteristicas')
        novo_perfil.historia = request.POST.get('historia')
        novo_perfil.sobre_mim = request.POST.get('sobre_mim')

        if novo_perfil.nome and novo_perfil.data_nascimento and novo_perfil.caracteristicas and novo_perfil.historia and novo_perfil.sobre_mim and novo_perfil.padrinho:
            novo_perfil.save()

    perfils = {
        'perfils': Perfil.objects.all()
    }
    return render(request,'apps/acessar_perfil.html', perfils)

def Afilhados_padrinhos(request):
    Afilhados = Perfil.objects.all()
    return render(request, 'apps/Afilhados_padrinhos.html', {'afilhados': Afilhados})

def Afilhados_funcionarios(request):
    Afilhados = Perfil.objects.all()
    return render(request, 'apps/Afilhados_funcionarios.html', {'afilhados': Afilhados})

def perfil_afilhado(request, id_afilhado):
    afilhado = get_object_or_404(Perfil, id=id_afilhado)
    nome_afilhado = afilhado.nome
    return render(request, 'apps/perfil_afilhado.html', {'afilhado': afilhado, 'nome_afilhado': nome_afilhado})

def excluir_perfil(request):
    erro = False
    if request.method == 'POST':
        form = ExcluirPerfilForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            try:
                perfil = get_object_or_404(Perfil, nome=nome)
                perfil.delete()
                return redirect('Afilhados_funcionarios')
            except:
                erro = True
                return render(request, 'apps/excluir_perfil.html', {'form': form, "erro": erro})
        else:
            return redirect('excluir_perfil')
    else:
        form = ExcluirPerfilForm()

    return render(request, 'apps/excluir_perfil.html', {'form': form})

def atualizar_status(request):
    return render(request, 'apps/atualizar_status.html')

def acessar_status(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        if status:
            novo_status = Status(status=status)
            novo_status.save()
    
    status = {
        'status': Status.objects.last()
    }

    return render(request, 'apps/acessar_status.html', status)