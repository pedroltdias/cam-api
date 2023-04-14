from rest_framework import serializers
from empresa.models import Departamento, Funcionario, Projeto

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['id', 'nome']

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'cpf', 'rg', 'sexo', 'data_nascimento', 'habilitacao', 'salario', 'carga_horaria_semanal']

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = ['id', 'horas_necessarias', 'prazo_estimado', 'horas_realizadas', 'ultima_atualizacao']