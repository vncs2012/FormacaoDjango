from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receita.models import Receita
# Create your views here.


def cadastro(request):
    """ Cadastro Uma nova Pessoa no Sistema"""
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, 'Nome Vazio')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request, 'E-mail nao pode ser em branco')
            return redirect('cadastro')

        if verifica_senhas_sao_iguais(pass1, pass2):
            messages.error(request, 'Senhas diferentes')
            return redirect('cadastro')

        if verifique_user_existe(email, nome):
            messages.error(request, 'Usuario ja cadastrado')
            return redirect('cadastro')
        else:
            user = User.objects.create_user(
                username=nome, email=email, password=pass1)
            user.save()
            messages.success(request, 'Usuario Cadastrado com Sucesso')

        return redirect('login')

    return render(request, 'usuarios/cadastro.html')


def login(request):
    """ Realiza uma Pessoa no Sistema"""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'E-mail ou senha não pode ficar em Branco')
            return redirect('login')

        if verifique_user_existe(email):
            nome = get_user(email)
            usuario = auth.authenticate(request, username=nome, password=senha)

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, 'Login realizado com Sucesso')
                return redirect('dashboard')
            else:
                messages.error(request, 'Usuario ou Senha incorreto')

    return render(request, 'usuarios/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('index')

    receitas = Receita.objects.order_by(
        '-data_receita').filter(pessoa=request.user.id)
    dados = {
        'receitas': receitas
    }

    return render(request, 'usuarios/dashboard.html', dados)

def campo_vazio(campo):
    return not campo.strip()


def verifique_user_existe(email, nome=None):
    if nome:
        return User.objects.filter(email=email, username=nome).exists()

    return User.objects.filter(email=email).exists()


def verifica_senhas_sao_iguais(senha, senha2):
    return senha != senha2

def get_user(email):

    return User.objects.filter(email=email).values_list(
        'username', flat=True).get()

