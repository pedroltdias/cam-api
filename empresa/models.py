from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    lista_funcionarios = models.ManyToManyField('Funcionario',  verbose_name="Lista de Funcionários")
    
    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    SEXOS = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro')
	]

    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=10, unique=True)
    sexo = models.CharField(max_length=1, choices=SEXOS)
    data_nascimento = models.DateField()
    habilitacao = models.BooleanField(default=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    carga_horaria_semanal = models.PositiveIntegerField()
    func_departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, related_name='funcionarios', verbose_name='Departamento')
    
	# projetos_trabalho = models.ManyToManyField('Projeto', through=...)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    horas_necessarias = models.IntegerField()
    prazo_estimado = models.DateField()
    horas_realizadas = models.IntegerField()
    ultima_atualizacao = models.DateField()
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, related_name='projetos')
    supervisor = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, related_name='funcionarios')

    def __str__(self):
        return self.nome