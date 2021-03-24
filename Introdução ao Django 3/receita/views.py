from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Receita
# Create your views here.


def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    dados = {
        'receita': receita
    }

    return render(request, 'receita.html', dados)


def buscar(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    if 'buscar' in request.GET:
        query = request.GET['buscar']
        if query:
            receitas = receitas.filter(nome__icontains=query)
    print(receitas)
    dados = {
        'receitas': receitas
    }
    return render(request, 'buscar.html', dados)
