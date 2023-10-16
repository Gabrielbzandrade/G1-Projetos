from django.shortcuts import render

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
        'entrar': 'inicio' # Mudar para portalfuncionários
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

def portalpadrinhos(request):
    context = {
        'lista': [i for i in range(12)],
        'afilhados': ['Superman', 'Ariel', 'Batman', 'Cinderela']
    }
    return render(request, 'apps/portalpadrinhos.html', context)

def superman(request):
    context = {

    }
    return render(request, 'apps/baseafilhados.html', context)

def ariel(request):
    context = {
        
    }
    return render(request, 'apps/baseafilhados.html', context)

def batman(request):
    context = {
        
    }
    return render(request, 'apps/baseafilhados.html', context)

def cinderela(request):
    context = {
        
    }
    return render(request, 'apps/baseafilhados.html', context)