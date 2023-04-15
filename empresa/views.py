from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from empresa.models import Departamento, Funcionario, Projeto
from empresa.serializer import DepartamentoSerializer, FuncionarioSerializer, FuncionarioSerializerV2, ProjetoSerializer, ProjetoGetSerializer, ListaFuncionariosDepartamentoSerializer, ListaProjetoDepartamentoSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os departamentos"""
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']
    
class FuncionarioViewSet(viewsets.ModelViewSet):
    """Exibindo todos os funcionários"""
    queryset = Funcionario.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', 'salario']
    search_fields = ['nome', 'cpf', 'rg']
    filterset_fields = ['habilitacao']
    
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return FuncionarioSerializerV2
        else:
            return FuncionarioSerializer
                     
    
class ProjetoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os projetos"""
    queryset = Projeto.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', 'horas_necessarias']
    search_fields = ['nome']
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProjetoGetSerializer
        else:
            return ProjetoSerializer
    
class ListaFuncionariosDepartamento(generics.ListAPIView):
    """Listando funcionários de um departamento"""
    def get_queryset(self):
        queryset = Funcionario.objects.filter(func_departamento_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaFuncionariosDepartamentoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', 'salario']

class ListaProjetosDepartamento(generics.ListAPIView):
    """Listando projetos de um departamento"""
    def get_queryset(self):
        queryset = Projeto.objects.filter(departamento_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaProjetoDepartamentoSerializer
    