from django.db import models

class Calendario(models.Model):
    data = models.DateField()
    evento = models.CharField(max_length=1000)

    def __str__ (self):
        return self.evento

class Relatos(models.Model):
    FELIZ = 'Feliz'
    NORMAL = 'Normal'
    TRISTE = 'Triste'

    STATUS_CHOICES = [
        (FELIZ, 'Feliz'),
        (NORMAL, 'Normal'),
        (TRISTE, 'Triste'),
    ]

    titulo = models.TextField(max_length=1000)
    texto = models.TextField(max_length=10000)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=FELIZ,  
    )

class Perfil(models.Model):
    nome = models.TextField(max_length=300)
    padrinho = models.TextField(max_length=300)
    data_nascimento = models.TextField(max_length=100)
    caracteristicas = models.TextField(max_length=1000)
    historia = models.TextField(max_length=5000)
    sobre_mim = models.TextField(max_length=5000)

class Status(models.Model):
    status = models.CharField(max_length=15, choices=[('Feliz', 'F'), ('Normal', 'N'), ('Triste', 'T')])

class Feedback(models.Model):
    texto = models.TextField(max_length=1500)
    feedback = models.CharField(max_length=15, choices=[('Feliz', 'F'), ('Normal', 'N'), ('Triste', 'T')])