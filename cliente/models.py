from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length= 100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    