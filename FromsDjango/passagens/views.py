from django.shortcuts import render
from passagens.forms import PassagemForms


def index(request):
    form = PassagemForms()
    contexto = {'from': form}
    return render(request, 'index.html', contexto)
