from rest_framework.test import APITestCase
from empresa.models import Departamento
from django.urls import reverse

class DepartamentoTestCase(APITestCase):
    
	def setUp(self):
		self.list_url = reverse('Departamentos-list')
		self.departamento_1 = Departamento.objects.create(
			nome="DepartamentoTesteUm"
		)

		self.departamento_2 = Departamento.objects.create(
			nome="DepartamentoTesteDois"
		)

