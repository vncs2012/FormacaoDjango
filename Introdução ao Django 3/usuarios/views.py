from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from receita.models import Receita
# Create your views here.


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password2']
        if not nome.strip():
            print('Nome Vazio')
            return redirect('cadastro')
        if not email.strip():
            print('E-mail nao pode ser em branco')
            return redirect('cadastro')
        if pass1 != pass2:
            print('Senhas diferentes')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('usuarios ja cadastrado')
            return redirect('cadastro')
        else:
            user = User.objects.create_user(
                username=nome, email=email, password=pass1)
            user.save()
            print('usuarios cadastrado com sucesso')

        return redirect('login')

    return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        print('entrou Login')
        email = request.POST['email']
        senha = request.POST['senha']

        if email == "" or senha == "":
            print('E-mail ou senha invalida')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list(
                'username', flat=True).get()
            usuario = auth.authenticate(request, username=nome, password=senha)

            if usuario is not None:
                auth.login(request, usuario)
                print('fazer Login')
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('index')
    
    receitas = Receita.objects.order_by('-data_receita').filter(pessoa=request.user.id)
    dados = {
    'receitas': receitas
    }

    return render(request, 'usuarios/dashboard.html',dados)

def cria_receita(request):
    if request.method == 'POST':
        receita = Receita()
        receita.pessoa = request.user if request.user.is_authenticated else print('usuario nao cadastrado')
        receita.nome = request.POST['nome_receita'] if request.POST['nome_receita'].strip() else print('nome_receita invalido')
        receita.ingredientes =  request.POST['ingredientes'] if request.POST['ingredientes'].strip() else print('ingredientes invalido')
        receita.modo_preparo = request.POST['modo_preparo'] if request.POST['modo_preparo'].strip() else print('modo_preparo invalido')
        receita.tempo_preparo = request.POST['tempo_preparo'] if request.POST['tempo_preparo'].strip() else print('tempo_preparo invalido')
        receita.redimento = request.POST['rendimento'] if request.POST['rendimento'].strip() else print('rendimento invalido')
        receita.categoria =  request.POST['categoria'] if request.POST['categoria'].strip() else print('categoria invalido')
        receita.foto = request.FILES['foto_receita'] if request.FILES['foto_receita'] else print('foto_receita invalido')
        receita.save()
        print('salvo Sucesso')
        redirect('dashboard')

    return render(request,'usuarios/cria_receita.html')

