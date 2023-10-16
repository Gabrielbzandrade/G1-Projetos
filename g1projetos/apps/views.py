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
        'links': [{'title': 'Esqueceu sua senha?', 'ref': 'inicio'}],
        'entrar': 'inicio' # Mudar para portalfuncionários
    }
    return render(request, 'apps/baselogin.html', context)

def cadastropadrinhos(request):
    context = {
        'title': 'Cadastro Padrinhos',
        'texts': ['Informe se E-mail'],
        'passwords': ['Informe sua Senha', 'Confirme sua Senha'],
        'links': [{'title': 'Login', 'ref': 'loginpadrinhos'}],
        'entrar': 'inicio'
    }
    return render(request, 'apps/baselogin.html', context)

def portalpadrinhos(request):
    context = {
        'lista': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'afilhados': ['Superman', 'Ariel', 'Batman', 'Cinderela']
    }
    return render(request, 'apps/portalpadrinhos.html', context)