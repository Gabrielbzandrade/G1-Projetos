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
        'entrar': 'inicio' # Mudar para portalpadrinhos
    }
    return render(request, 'apps/baselogin.html', context)

def loginfuncionarios(request):
    return render(request, 'apps/baselogin.html')

def cadastropadrinhos(request):
    context = {
        'title': 'Cadastro Padrinhos',
        'texts': ['Informe se E-mail'],
        'passwords': ['Informe sua Senha', 'Confirme sua Senha'],
        'links': [{'title': 'Login', 'ref': 'loginpadrinhos'}],
        'entrar': 'inicio'
    }
    return render(request, 'apps/baselogin.html', context)