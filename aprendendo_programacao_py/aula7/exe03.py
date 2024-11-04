
from time import sleep
from funcoes import menu, calcular_a_p_circulo, calcular_a_p_quadrado, calcular_a_p_retangulo



while True:
    menu()

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 0:
        print('Encerrando aplicação...')
        break

    elif opcao == 1:
        lado = float(input('Digite o tamanho do lado do quadrado: '))
        print(calcular_a_p_quadrado(lado))

    elif opcao == 2:
        base = float(input('Digite o tamanho da base do retangulo: '))
        altura = float(input('Digite o tamanho da altura do retangulo: '))
        print(calcular_a_p_retangulo(base,altura))

    elif opcao == 3:
        raio = float(input('Digite o raio do circulo: '))
        print({calcular_a_p_circulo(raio)})

    else:
        print('Opção inválida.')


import math

def calcular_a_p_retangulo(base, altura):
    perimetro = 2 * (base + altura)
    area = base * altura
    return f'A area do retangulo é {area} e o perimetro é {perimetro}'

def calcular_a_p_quadrado(lado):
    perimetro = lado * 4
    area = lado**2
    return f'A area do quadrado é {area} e o perimetro é {perimetro}'

def calcular_a_p_circulo(raio):
    perimetro = 2 * math.pi * raio
    area = math.pi * raio**2
    return f'A area do circulo é {round(area,2)} e o perimetro é {round(perimetro,2)}'


def menu():
    print('OPÇÕES GEOMETRICAS')
    print('1 - quadrado')
    print('2 - retangulo')
    print('3 - circulo')
    print('0 - sair')