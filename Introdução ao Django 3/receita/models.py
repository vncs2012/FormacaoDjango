from django.db import models
from datetime import datetime
from pessoas.models import Pessoa


class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, verbose_name=(
        "nome"), on_delete=models.CASCADE)
    nome = models.CharField(
        'Nome Receita', max_length=200, blank=False, null=True)
    ingredientes = models.TextField('Ingredientes')
    modo_preparo = models.TextField('Modo Preparo')
    tempo_preparo = models.IntegerField('Tempo Preparo')
    redimento = models.CharField("Rendimento", max_length=100)
    categoria = models.CharField("Categoria", max_length=100)
    data_receita = models.DateTimeField(
        default=datetime.now, blank=True, null=True)
    foto = models.ImageField(
        upload_to='fotos/%d/%m/%Y/', blank=True, null=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome
