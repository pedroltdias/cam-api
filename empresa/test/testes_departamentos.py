from rest_framework.test import APITestCase
from empresa.models import Departamento
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
			'nome': 'DepartamentoAtualizado'
		}
		response = self.client.put('/departamentos/1/', data=data)
		self.assertEquals(response.status_code, status.HTTP_200_OK)
