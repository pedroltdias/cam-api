from rest_framework import viewsets, generics, filters, status
from rest_framework.response import Response 
from django_filters.rest_framework import DjangoFilterBackend
from empresa.models import Departamento, Funcionario, Projeto
from empresa.serializer import DepartamentoSerializer, FuncionarioSerializer, FuncionarioSerializerV2, ProjetoSerializer, ProjetoGetSerializer, ListaFuncionariosDepartamentoSerializer, ListaProjetoDepartamentoSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from datetime import datetime, timedelta

class DepartamentoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os departamentos"""
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            id = str(serializer.data['id'])
            response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            response['Location'] = self.request.build_absolute_uri() + id

            return response
        
    @method_decorator(cache_page(30)) #30 seg
    def dispatch(self, *args, **kwargs):
        return super(DepartamentoViewSet, self).dispatch(*args, **kwargs)
    
class FuncionarioViewSet(viewsets.ModelViewSet):
    """Exibindo todos os funcionários"""
    queryset = Funcionario.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', 'salario']
    search_fields = ['nome', 'cpf', 'rg']
    filterset_fields = ['habilitacao']
    serializer_class = FuncionarioSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            id = str(serializer.data['id'])
            response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            response['Location'] = self.request.build_absolute_uri() + id
            
            return response
    
    # def get_serializer_class(self):
    #     if self.request.version == 'v2':
    #         return FuncionarioSerializerV2
    #     else:
    #         return FuncionarioSerializer 
   
class ProjetoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os projetos"""
    queryset = Projeto.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', 'horas_necessarias']
    search_fields = ['nome']
    serializer_class = ProjetoSerializer
    
    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return ProjetoGetSerializer
    #     else:
    #         return ProjetoSerializer
        
    #Override
    def perform_create(self, serializer):
        print('hello 1')
        projeto = serializer.save()
        self.calcular_prazo_estimado(projeto)

    #Override
    def perform_update(self, serializer):
        print('hello update')
        projeto = serializer.save()
        self.calcular_prazo_estimado(projeto)

    #Calcular prazo estimado
    def calcular_prazo_estimado(self, projeto):
        print('hello 2')
        horas_gastas = projeto.horas_realizadas
        horas_restantes = projeto.horas_necessarias - horas_gastas
        if horas_restantes <= 0:
            projeto.prazo_estimado = datetime.now().date()
        else:
            semanas_restantes = horas_restantes // 40
            data_atual = datetime.now().date()
            data_estimada = data_atual + timedelta(weeks=semanas_restantes)
            projeto.prazo_estimado = data_estimada
            print(data_estimada)
        projeto.save()

    # def create(self, request):
    #     print('hello 3')
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         headers = self.get_success_headers(serializer.data)
    #         id = str(serializer.data['id'])
    #         response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #         response['Location'] = self.request.build_absolute_uri() + id
            
    #         return response
    
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
    