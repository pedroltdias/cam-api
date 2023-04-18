from empresa.models import Funcionario, Departamento, Projeto
from django.test import TestCase

class DepartamentoModelTestCase(TestCase):

	def setUp(self):
		self.departamento = Departamento(
			nome = 'DepartamentoTeste'
		)
    
	def test_verifica_atributos_departamento(self):
		"""Teste para verificar atributos de um departamento"""
		self.assertEqual(self.departamento.nome, 'DepartamentoTeste')