from rest_framework import serializers
from empresa.models import Departamento, Funcionario, Projeto

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'
        
class ListaFuncionariosDepartamentoSerializer(serializers.ModelSerializer):
    # departamento = serializers.ReadOnlyField(source='departamento.nome')
    # funcionario = serializers.SerializerMethodField()
    class Meta:
        model = Funcionario
        fields = ['nome']
        