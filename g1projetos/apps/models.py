from django.db import models

class Calendario(models.Model):
    data = models.DateField()
    evento = models.CharField(max_length=1000)

    def __str__ (self):
        return self.evento
