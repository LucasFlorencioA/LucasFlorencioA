import funcoes as f
from time import sleep

def menu():
    print('Escolha as operações com strings desejadas.')
    print('1 - Inverter String')
    print('2 - Contar elementos da string')
    print('3 - Verificar se é palindromo')
    print('0 - Sair')

while True:
    menu()
    opcao = int(input("Digite a opção desejada: "))
    sleep(3)

    if opcao == 0:
        print('Saindo do programa...')
        break

    string_usuario = input('Digite uma string: ')
    sleep(3)

    if opcao == 1:
        print(f'String invertida: {f.inverter_strings(string_usuario)}')

    elif opcao == 2:
        print(f'Número de elementos da string: {f.contar_elementos(string_usuario)}')

    elif opcao == 3:
        if f.palindromo(string_usuario) == True:
            print(f'A string {string_usuario} é palindromo.')
        else:
            print(f'A string {string_usuario} não é palindromo.')
    else:
        print('Opção invalida.')