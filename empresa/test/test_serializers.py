from django.test import TestCase
from empresa.models import Departamento, Funcionario, Projeto
from empresa.serializer import DepartamentoSerializer, FuncionarioSerializer, ProjetoSerializer, ListaFuncionariosDepartamentoSerializer, ListaProjetoDepartamentoSerializer

class DepartamentoSerializerTestCase(TestCase):
    
	def setUp(self):
		self.departamento = Departamento(
			nome = 'DepartamentoTeste'
		)

		self.serializer = DepartamentoSerializer(instance=self.departamento)

	def test_verifica_campos_serializados(self):
		"""Teste que verifica os campos que estao sendo serializados"""
		data = self.serializer.data
		self.assertEqual(set(data.keys()), set(['id', 'nome']))


	def test_verifica_conteudo_dos_campos_serializados(self):
		"""Teste que verifica o conteudo dos campos serializados"""
		data = self.serializer.data
		self.assertEqual(data['nome'], self.departamento.nome)