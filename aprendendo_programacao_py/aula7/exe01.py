import funcoes as f

while True:
    f.menu()
    opcao = int(input('Escolha a opção desejada: '))

    if opcao == 0:
        print('Saindo do programa...')
        break

    elif opcao == 1:
        num1 = float(input('Digite o primeiro número.'))
        num2 = float(input('Digite o segundo número.'))
        print(f'A soma de {num1} + {num2} é {f.soma(num1,num2)}')

    elif opcao == 2:
        num1 = float(input('Digite o primeiro número.'))
        num2 = float(input('Digite o segundo número.'))
        print(f'A divisão entre {num1} e {num2} é {f.divisao(num1,num2)}')

    elif opcao == 3:
        num1 = float(input('Digite o primeiro número.'))
        num2 = float(input('Digite o segundo número.'))
        print(f'A subtração de {num1} - {num2} é {f.subtracao(num1,num2)}')

    elif opcao == 4:
        num1 = float(input('Digite o primeiro número.'))
        num2 = float(input('Digite o segundo número.'))
        print(f'A Multiplicação de {num1} x {num2} é {f.multiplicacao(num1,num2)}')

    else:
        print('Opção Inválida.')