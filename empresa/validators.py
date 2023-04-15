from validate_docbr import CPF

def nome_valido(nome):
    return nome.isalpha()

def cpf_valido(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)

def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9
