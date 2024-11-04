import random

def jogar_adivinhacao():
    print('Bem-vindo ao jogo da adivinhação!')
    numero_secreto = random.randint(1,100)
    tentativas = 0

    while True:
        palpite = int(input('Digite o seu palpite (entre 1 e 100): '))
        tentativas += 1

        if palpite == numero_secreto:
            print(f'Você acertou em {tentativas} tentativas!')
            break
        elif palpite < numero_secreto:
            print('Digite um número maior!')
        else:
            print('Digite um número menor!')

jogar_adivinhacao()