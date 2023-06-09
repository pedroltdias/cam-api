from django.db import models
from datetime import date, timedelta

class Departamento(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    SEXOS = [('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')]

    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=20, unique=True)
    rg = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=20, default="")
    sexo = models.CharField(max_length=1, choices=SEXOS)
    data_nascimento = models.DateField()
    habilitacao = models.BooleanField(default=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2, default=550)
    carga_horaria_semanal = models.PositiveIntegerField(default=40)
    func_departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, related_name='funcionarios', verbose_name='Departamento')
    
    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    horas_necessarias = models.IntegerField(default=120)
    prazo_estimado = models.DateField(default=date.today)
    horas_realizadas = models.IntegerField(default=0)
    ultima_atualizacao = models.DateField(default=date.today)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, related_name='projetos')
    supervisor = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, related_name='projeto_supervisor')
    funcionarios = models.ManyToManyField(Funcionario, related_name='projeto_funcionarios')

    class Meta:
        unique_together = ('nome', 'departamento')

    def __str__(self):
        return self.nome