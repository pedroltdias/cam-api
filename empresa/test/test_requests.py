from rest_framework.test import APITestCase
from empresa.models import Departamento, Funcionario
from django.urls import reverse
from rest_framework import status

class DepartamentoTestCase(APITestCase):
    
	def setUp(self):
		self.list_url = reverse('Departamentos-list')
		self.departamento_1 = Departamento.objects.create(
			nome="DepartamentoTesteUm"
		)

		self.departamento_2 = Departamento.objects.create(
			nome="DepartamentoTesteDois"
		)

	def test_requisicao_get_para_listar_departamentos(self):
		"""Teste para verificar a requisicao GET para listar departamentos"""
		response = self.client.get(self.list_url)
		self.assertEquals(response.status_code, status.HTTP_200_OK)

	def test_requisicao_post_para_criar_departamento(self):
		"""Teste para verificar a requisicao POST para criar um departamento"""
		data = {
			'nome': 'DepartamentoTeste'
		}

		response = self.client.post(self.list_url, data=data)
		self.assertEquals(response.status_code, status.HTTP_201_CREATED)

	def test_requisicao_delete_para_deletar_departamentos(self):
		"""Teste para verificar a requisicao DELETE para criar um departamento"""
		response = self.client.delete('/departamentos/1/')
		self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
	
	def test_requisicao_put_para_alterar_departamentos(self):
		"""Teste para verificar a requisicao PUT para atualizar um departamento"""
		data = {
			'nome': 'DepTest'
		}

		response = self.client.put('/departamentos/2/', data=data)
		self.assertEquals(response.status_code, status.HTTP_200_OK)

class FuncionarioTestCase(APITestCase):
    
	def setUp(self):
		self.list_url = reverse('Funcionarios-list')
		self.departamento_1 = Departamento.objects.create(
			nome="DepartamentoTesteUm"
		)
		self.departamento_2 = Departamento.objects.create(
			nome="DepartamentoTesteDois"
		)
		self.funcionario_1 = Funcionario.objects.create(
			nome="FuncionarioUm",
			cpf="13020844029",
			rg="12345610",
			telefone="61123456789",
			sexo="M",
			data_nascimento="2023-04-17",
			habilitacao=True,
			salario=550,
			carga_horaria_semanal=40,
			func_departamento=self.departamento_1,
		)

		self.funcionario_2 = Funcionario.objects.create(
			nome="FuncionarioDois",
			cpf="31517448000",
			rg="12345611",
			telefone="61123456788",
			sexo="F",
			data_nascimento="2023-04-18",
			habilitacao=False,
			salario=600,
			carga_horaria_semanal=40,
			func_departamento=self.departamento_2,
		)

	def test_requisicao_get_para_listar_funcionarios(self):
		"""Teste para verificar a requisicao GET para listar funcionarios"""
		response = self.client.get(self.list_url)
		self.assertEquals(response.status_code, status.HTTP_200_OK)

	def test_requisicao_post_para_criar_funcionario(self):
		"""Teste para verificar a requisicao POST para criar um funcionario"""
		data = {
			'nome': "FuncionarioPost",
			'cpf': "93082727042",
			'rg': "12345612",
			'telefone': "61123456888",
			'sexo': "O",
			'data_nascimento': "2023-03-18",
			'habilitacao': True,
			'salario': 600,
			'carga_horaria_semanal': 40,
			'func_departamento': self.departamento_1,
		}

		response = self.client.post(self.list_url, data=data)
		self.assertEquals(response.status_code, status.HTTP_201_CREATED)

	def test_requisicao_delete_para_deletar_funcionario(self):
		"""Teste para verificar a requisicao DELETE para criar um funcionario"""
		response = self.client.delete('/funcionarios/1/')
		self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
	
	def test_requisicao_put_para_alterar_funcionario(self):
		"""Teste para verificar a requisicao PUT para atualizar um funcionario"""
		data = {
			'nome': "FuncionarioUpdate",
			'cpf': "28354017095",
			'rg': "12345612",
			'telefone': "61123456888",
			'sexo': "Outro",
			'data_nascimento': "2023-03-18",
			'habilitacao': True,
			'salario': 600,
			'carga_horaria_semanal': 40,
			'func_departamento': self.departamento_2,
		}

		response = self.client.put('/funcionario/1/', data=data)
		self.assertEquals(response.status_code, status.HTTP_200_OK)