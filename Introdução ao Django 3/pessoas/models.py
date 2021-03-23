from django.db import models

# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField("Criador", max_length=120)
    email = models.EmailField("E-mail", max_length=254)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.email
