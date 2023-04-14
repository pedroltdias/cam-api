from rest_framework import viewsets
from empresa.models import Departamento, Funcionario, Projeto
from empresa.serializer import DepartamentoSerializer, FuncionarioSerializer, ProjetoSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os departamentos"""
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    
class FuncionarioViewSet(viewsets.ModelViewSet):
    """Exibindo todos os funcionários"""
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    
class ProjetoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os projetos"""
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer