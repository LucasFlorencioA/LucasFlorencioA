#Exemplos de Funções lambda

pares = [1,2,3,4,5,6]
encontrar_pares = list(map(lambda x: 'Par' if x % 2 == 0 else 'Impar', pares))
print(encontrar_pares)


numeros = [1,2,1,4,1,6]
filtro = list(filter(lambda x: x if x == 1 else False,numeros))
print(filtro)


compras = ('vassoura','maçã','carne','pipoca')
def lista_compras(*args):
    lista_compras = []
    for compra in args:
        lista_compras.append(compra)
    print('LISTA DE COMPRAS')
    for i in lista_compras:
        print(f'produto: {i}')

        
lista_compras(*compras)


from functools import reduce

lista_strings = ['barro','retas']
maior_string = reduce(lambda x, y: x if len(x) > len(y) else y, lista_strings)
print(maior_string)