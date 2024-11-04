def soma(a,b):
    return a + b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    if b != 0:
        return a/b
    return 'Não é possível dividir por 0.'

def subtracao(a,b):
    return a - b

def menu():
    print('Selecione a operação: ')
    print('1 - Soma: ')
    print('2 - Divisão: ')
    print('3 - Subtracao: ')
    print('4 - Multiplicação: ')
    print('0 - Sair ')

def inverter_strings(string):
    return string[::-1]

def contar_elementos(string):
    return len(string.split())

def palindromo(string):
    string = string.replace(" ","").lower()
    return string == string[::-1]