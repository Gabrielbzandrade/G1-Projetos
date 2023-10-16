from django.shortcuts import render

def inicio(request):
    return render(request, 'apps/inicio.html')

def transparencia(request):
    return render(request, 'apps/transparencia.html')

def portalpadrinhos(request):
    return render(request, 'apps/portalpadrinhos.html')

def portalfuncionarios(request):
    return render(request, 'apps/portalfuncionarios.html')
