from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=10, unique=True)
    sexo = models.CharField(max_length=1)
    data_nascimento = models.DateField()
    habilitacao = models.BooleanField(default=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    carga_horaria_semanal = models.IntegerField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='funcionarios')

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    horas_necessarias = models.IntegerField()
    prazo_estimado = models.DateField()
    horas_realizadas = models.IntegerField()
    ultima_atualizacao = models.DateField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='projetos')

    def __str__(self):
        return self.nome