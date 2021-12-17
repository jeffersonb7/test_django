from django.db import models

# Create your models here.
class Carro(models.Model):
    nome = models.CharField('Nome: ', max_length=150)
    cor = models.CharField('Cor', max_length=150)