def numero_1(numero):
    return numero

def numero_2(numero):
    return numero

def soma():
    num_1 = float(input('Digite o primeiro numero para soma: '))
    num_2 = float(input('Digite o segundo numero para soma: '))

    numero_p_soma_1 = numero_1(num_1)
    numero_p_soma_2 = numero_2(num_2)

    return numero_p_soma_1 + numero_p_soma_2

print(soma())