from django import forms


class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100, required=True)
    destino = forms.CharField(label='Destino', max_length=100, required=True)
    data_ida = forms.DateField(label='Ida', required=True)
    data_volta = forms.DateField(label='Volta', required=True)
