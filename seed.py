import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random, datetime
from empresa.models import  Funcionario, Departamento, Projeto

def criando_departamentos(quantidade_de_departamentos):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_departamentos):
        nome = fake.job()
        d = Departamento(nome=nome)
        d.save()
        
def criando_funcionarios(quantidade_de_funcionarios):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_funcionarios):
        nome = fake.name()
        cpf = CPF()
        rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) )
        sexo = "Outro"
        data_nascimento = fake.date_between(start_date='-18y', end_date='today')
        f = Funcionario(nome=nome, cpf=cpf, rg=rg, sexo=sexo,data_nascimento=data_nascimento)
        f.save()
        
def criando_projetos(quantidade_de_projetos):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_projetos):
        nome = fake.name()
        p = Projeto(nome=nome)
        p.save()

criando_departamentos(10)
criando_funcionarios(30)
criando_projetos(15)