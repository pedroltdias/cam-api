from django.contrib import admin
from empresa.models import Departamento, Funcionario, Projeto

class Departamentos(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
    ordering = ('nome',)
    
admin.site.register(Departamento, Departamentos)

class Funcionarios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'rg', 'data_nascimento', 'habilitacao', 'salario', 'carga_horaria_semanal')
    list_display_links = ('id', 'nome', 'cpf', 'rg', 'data_nascimento')
    search_fields = ('id', 'nome', 'cpf', 'rg',)
    list_per_page = 20
    ordering = ('nome',)

admin.site.register(Funcionario, Funcionarios)

class Projetos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'horas_necessarias', 'prazo_estimado', 'horas_realizadas', 'ultima_atualizacao')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome',)
    list_per_page = 20
    ordering = ('nome',)

admin.site.register(Projeto, Projetos)