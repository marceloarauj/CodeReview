from django.db import models
 
# Cria modelo
class Funcionario (models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=19, decimal_places=10)
 
    # Define unicode para o Django Admin
    def __unicode__(self):
        return self.nome