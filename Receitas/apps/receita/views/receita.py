from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from receita.models import Receita
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    paginator = Paginator(receitas, 3)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    dados = {
        'receitas': receitas_por_pagina
    }
    return render(request, 'receitas/index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    dados = {
        'receita': receita
    }

    return render(request, 'receitas/receita.html', dados)


def cria_receita(request):
    if request.method == 'POST':
        receita = Receita()
        receita.pessoa = request.user
        receita.nome = request.POST['nome_receita']
        receita.ingredientes = request.POST['ingredientes']
        receita.modo_preparo = request.POST['modo_preparo']
        receita.tempo_preparo = request.POST['tempo_preparo']
        receita.redimento = request.POST['rendimento']
        receita.categoria = request.POST['categoria']
        receita.foto = request.FILES['foto_receita']
        receita.save()
        messages.success(request, 'Receita Criada com Sucesso')
        redirect('dashboard')

    return render(request, 'receitas/cria_receita.html')


def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    dados = {
        'receita': receita
    }
    return render(request, 'receitas/edita_receita.html', dados)


def atualiza_receita(request):
    if request.method == 'POST':
        receita = Receita.objects.get(pk=request.POST['receita_id'])
        receita.pessoa = request.user
        receita.nome = request.POST['nome_receita']
        receita.ingredientes = request.POST['ingredientes']
        receita.modo_preparo = request.POST['modo_preparo']
        receita.tempo_preparo = request.POST['tempo_preparo']
        receita.redimento = request.POST['rendimento']
        receita.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            receita.foto = request.FILES['foto_receita']
        receita.save()
    return redirect('dashboard')


def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')
