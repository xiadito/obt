from django.db import models

# Create your models here.

from django.db import models

class Experimento(models.Model):
    nome = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=[('intacto', 'Intacto'), ('avariado', 'Avariado')])

    def __str__(self):
        return self.nome