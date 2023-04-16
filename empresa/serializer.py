from rest_framework import serializers
from empresa.models import Departamento, Funcionario, Projeto
from empresa.validators import *

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['id', 'nome']

    def validate(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError(
                {'nome': 'O nome de um departamento não pode conter números!'})
        return data

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        exclude = ['telefone', 'func_departamento']

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'CPF inválido!'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError(
                {'rg': "O RG deve ter 9 dígitos"})
        return data

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        exclude = ['prazo_estimado', 'horas_realizadas', 'ultima_atualizacao']
        
    def validate(self, data):
        supervisor = data['supervisor']
        horas_necessarias = data['horas_necessarias']
        print(supervisor.carga_horaria_semanal)
        if not (supervisor.carga_horaria_semanal * 4) > horas_necessarias:
            raise serializers.ValidationError("O funcionário não tem carga horária suficiente para supervisionar o projeto!")
        return data
    
class ProjetoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'

class ListaFuncionariosDepartamentoSerializer(serializers.ModelSerializer):
    sexo = serializers.SerializerMethodField()

    class Meta:
        model = Funcionario
        fields = ['nome', 'cpf', 'sexo', 'salario']

    def get_sexo(self, obj):
        return obj.get_sexo_display()

class ListaProjetoDepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = ['nome', 'supervisor', 'horas_necessarias',
                  'horas_realizadas', 'prazo_estimado', 'ultima_atualizacao']

class FuncionarioSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        exclude = ['func_departamento']

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'CPF inválido!'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError(
                {'rg': "O RG deve ter 9 dígitos"})
        return data