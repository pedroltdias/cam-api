from rest_framework import viewsets, generics
from empresa.models import Departamento, Funcionario, Projeto
from empresa.serializer import DepartamentoSerializer, FuncionarioSerializer, ProjetoSerializer, ListaFuncionariosDepartamentoSerializer, ListaProjetoDepartamentoSerializer

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
    
class ListaFuncionariosDepartamento(generics.ListAPIView):
    """Listando funcionários de um departamento"""
    def get_queryset(self):
        queryset = Funcionario.objects.filter(func_departamento_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaFuncionariosDepartamentoSerializer
    

class ListaProjetosDepartamento(generics.ListAPIView):
    """Listando projetos de um departamento"""
    def get_queryset(self):
        queryset = Projeto.objects.filter(departamento_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaProjetoDepartamentoSerializer
    