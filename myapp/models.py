
# Create your models here.

from django.contrib.auth.models import User
from django.db import models


#Criando a classe Pessoa
class Pessoa(models.Model):
    altura =  models.DecimalField(max_digits=10, decimal_places=2,default=0)
    peso =  models.DecimalField(max_digits=10, decimal_places=2,default=0)
    usuario = models.ForeignKey(User, models.CASCADE)


    def __str__(self):
        return (f'{self.usuario}')