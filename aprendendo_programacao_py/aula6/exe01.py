
##Exemplo de args com listas
numeros = [1,2,3,4,5,6,7,8,9,10]
def somar(*args):
    resultado = []
    for num in args:
        resultado.append(num)
    resultado = sum(resultado)
    return resultado
somatorio_2 = somar(*numeros)
print(somatorio_2)
