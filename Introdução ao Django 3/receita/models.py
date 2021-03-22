from django.db import models
from datetime import datetime


class Receita(models.Model):
    nome = models.CharField(
        'Nome Receita', max_length=200, blank=False, null=True)
    ingredientes = models.TextField('Ingredientes')
    modo_preparo = models.TextField('Modo Preparo')
    tempo_preparo = models.IntegerField('Tempo Preparo')
    redimento = models.CharField("Rendimento", max_length=100)
    categoria = models.CharField("Categoria", max_length=100)
    data_receita = models.DateTimeField(
        default=datetime.now, blank=True, null=True)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome
