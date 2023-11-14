from django.db import models

class Calendario(models.Model):
    data = models.DateField()
    evento = models.CharField(max_length=1000)

    def __str__ (self):
        return self.evento

class Relatos(models.Model):
    titulo = models.TextField(max_length=1000)
    texto = models.TextField(max_length=10000)

class Perfil(models.Model):
    nome = models.TextField(max_length=300)
    data_nascimento = models.TextField(max_length=100)
    caracteristicas = models.TextField(max_length=1000)
    historia = models.TextField(max_length=5000)
    sobre_mim = models.TextField(max_length=5000)