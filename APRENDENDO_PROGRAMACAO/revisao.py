'''metros = float(input("Digite um valor em metros: "))

centimetros = metros * 100

print(centimetros)


largura = float(input("Digite a largura do retangulo: "))
altura = float(input("Digite a altura do retangulo: "))

area = largura * altura

print(area)

while True:
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))
    imc = peso / (altura * altura) 
    print (f"O seu peso é: {peso} sua altura é: {altura} ")
    
    if imc < 17:
        print(f"Seu IMC é: {imc:.2f} você está muito abaixo do peso")
    elif imc >= 17 and imc < 25:
        print(f"Seu IMC é: {imc:.2f} você está com o peso normal")
    elif imc >= 25 and imc < 30:
        print(f"Seu IMC é: {imc:.2f} você está acima do peso")
    elif imc >= 30 and imc < 35:
        print(f"Seu IMC é: {imc:.2f} você está com obesidade gral 1")
    elif imc >= 35 and imc < 40:
        print(f"Seu IMC é: {imc:.2f} você está com obesidade gral 2")
    elif imc > 40:
        print(f"Seu IMC é: {imc:.2f}  você está com obesidade gral 3")
    else:
        print("Ops!!! Algo deu errado.")


while True:
    idade = int(input("Digite sua idade: "))

    if idade <= 12:
        print(f"Você só tem {idade} anos e ainda é criança")
    elif idade > 12 and idade < 18:
        print(f"Você tem {idade} anos e adolecente")
    elif idade >= 18 and idade < 60:
        print(f"Você tem {idade} anos e adulto")
    elif idade > 60:
        print(f"Você tem {idade} anos e idoso")
    else:
        print("Ops!!! Algo deu errado.")


'''

cont = 10

while cont >= 1:
    print(cont)
    cont-=1
print("Feliz ano novo!!!")
