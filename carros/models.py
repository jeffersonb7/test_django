from django.db import models
from musica.models import Musica
# Create your models here.
class Carro(models.Model):
    nome = models.CharField('Nome: ', max_length=150)
    cor = models.CharField('Cor', max_length=150)
    musica = models.ForeignKey(Musica, null=True, blank=True, on_delete=models.CASCADE)