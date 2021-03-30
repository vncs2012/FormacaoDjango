from django.shortcuts import get_object_or_404, render, redirect
from receita.models import Receita

def buscar(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    if 'buscar' in request.GET:
        query = request.GET['buscar']
        receitas = receitas.filter(nome__icontains=query)

    dados = {
        'receitas': receitas
    }
    return render(request, 'receitas/buscar.html', dados)