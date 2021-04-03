from django.shortcuts import render
from passagens.forms import PassagemForms, PessoaForms


def index(request):
    form = PassagemForms()
    pessoa_form = PessoaForms()
    contexto = {'form': form,
                'pessoa_form': pessoa_form}
    return render(request, 'index.html', contexto)


def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        pessoaform = PessoaForms(request.POST)
        contexto = {'form': form,
                    'pessoa_form': pessoaform}
        if not form.is_valid():
            return render(request, 'index.html', contexto)

    return render(request, 'minha_consulta.html', contexto)
