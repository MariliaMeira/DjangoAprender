
# Create your models here.

from django.contrib.auth.models import User
from django.db import models


#Criando a classe Pessoa
class Pessoa(models.Model):
    altura =  models.DecimalField(max_digits=10, decimal_places=2,default=0)
    peso =  models.DecimalField(max_digits=10, decimal_places=2,default=0)
    usuario = models.ForeignKey(User, models.CASCADE)
    idade =models.IntegerField(default=0)


    def __str__(self):
        return (f'{self.usuario}')
class Aluno(models.Model):
    nome= models.CharField(max_length=50)
    usuario = models.ForeignKey(User, models.CASCADE)
    def __str__(self):
        return (f'{self.nome}')