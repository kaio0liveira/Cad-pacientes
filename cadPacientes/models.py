from django.db import models


class Paciente(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    dataNascimento = models.DateField(max_length=10)
    tipoTeste = models.CharField(max_length=20, blank=False, null=False)
    resultado = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return self.nome
