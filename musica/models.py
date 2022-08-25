from django.db import models

# Create your models here.
class Musica(models.Model):
    nome = models.CharField(max_length=150)
    duracao = models.CharField(max_length=5)
    file_arquivo = models.FileField(upload_to='test/')