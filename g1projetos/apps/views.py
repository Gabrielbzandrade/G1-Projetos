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

def superman(request):
    context = {
        'nome': 'Superman',
        'texto': 'Agora, eu tenho a oportunidade de aprender muitas coisas novas todos os dias. Os professores são atenciosos e sempre me ajudam a entender os assuntos que são mais difíceis para mim. Além disso, a ONG também me proporciona refeições nutritivas, o que me deixa com energia para estudar e brincar. O que eu mais gosto é que, além das aulas, temos muitas atividades divertidas, como jogos, desenhos e até mesmo passeios. Eu fiz muitos amigos aqui e sempre me sinto apoiado por todos. Estar na ONG me faz sentir especial e acreditar que eu posso alcançar meus sonhos no futuro. Estou muito grato por tudo o que a ONG faz por mim e por outras crianças como eu.',
        'imagem': 'https://brandlogos.net/wp-content/uploads/2014/10/Superman-vector.png'

    }
    return render(request, 'apps/baseafilhados.html', context)

def ariel(request):
    context = {
        'nome': 'Ariel',
        'texto': 'Na minha ONG, tenho uma experiência incrível! Todos os dias, sou cercado por pessoas incríveis que me ajudam a aprender, crescer e sonhar alto. Recebo educação de qualidade que me abre portas para um futuro brilhante. Além disso, sempre tenho uma refeição deliciosa para me alimentar e muitos amigos com quem brincar e compartilhar histórias. A ONG é como uma segunda casa para mim, onde sou amado e apoiado, e estou muito agradecido por fazer parte desta família. Juntos, estamos construindo um amanhã melhor.',
        'imagem': 'https://mundodisneyprincess.files.wordpress.com/2014/01/administrar-o-mar.png'
    }
    return render(request, 'apps/baseafilhados.html', context)

def batman(request):
    context = {
        'nome': 'Batman',
        'texto': 'Minha experiência na ONG tem sido incrível! Aqui, eu tenho a oportunidade de aprender muitas coisas novas, brincar com outras crianças e até receber ajuda com meus estudos. Os professores são muito legais e sempre estão dispostos a me ajudar quando eu preciso. Além disso, a comida é deliciosa e me ajuda a ter energia para brincar e aprender. Estou muito feliz por fazer parte dessa ONG, pois sei que ela está me ajudando a crescer e a ter um futuro melhor!',
        'imagem': 'https://static.adecoretecidos.com.br/public/adecoretecidos/imagens/produtos/painel-sublimado-batman-11748.png'
    }
    return render(request, 'apps/baseafilhados.html', context)

def cinderela(request):
    context = {
        'nome': 'Cinderela',
        'texto': 'Na ONG onde estou matriculada, minha experiência tem sido incrível. Eu aprendo muitas coisas interessantes e faço amigos com quem posso brincar e conversar. Os professores são legais e sempre me ajudam quando tenho dificuldades. Além disso, a ONG me oferece alimento gostoso e nutritivo todos os dias. Eu me sinto feliz e cuidada aqui, e sei que essa experiência está me ajudando a crescer e a ser uma pessoa melhor.',
        'imagem': 'https://i.ebayimg.com/images/g/DR4AAOSw8QhgWDtG/s-l1600.png'
    }
    return render(request, 'apps/baseafilhados.html', context)