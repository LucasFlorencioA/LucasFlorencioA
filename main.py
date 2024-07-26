inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

soma_pares = 0
tem_par = False

for num in range(inicio, fim + 1):
    if num % 2 == 0:
        soma_pares += num
        tem_par = True

if tem_par:
    print(f"A soma dos números pares no intervalo de {inicio} a {fim} é: {soma_pares}")
else:
    print(f"Não há números pares no intervalo de {inicio} a {fim}.")
