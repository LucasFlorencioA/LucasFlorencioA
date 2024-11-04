def validar_positivo(funcao):
    def wrapper(self, valor):
        if valor >= 0:
            return funcao(self, valor)
        else:
            print(f'Erro: o valor para {funcao.__name__[4:]} não pode ser negativo.')
    return wrapper

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco if preco >= 0 else 0
        self.__quantidade = quantidade if quantidade >= 0 else 0

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco
    
    @validar_positivo
    def set_preco(self, preco):
        self.__preco = preco

    def get_quantidade(self):
        return self.__quantidade
    
    @validar_positivo
    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade


    def exibir(self):
        print(f'Produto: {self.__nome} | Preço: {self.__preco:.2f} | Quantidade em estoque: {self.__quantidade}')


produto = Produto('Caneta', 2.50, 100)
produto.exibir()


print('---------------------')

produto_2 = Produto('Skate', -100, 1)
produto_2.exibir()

print('---------------------')

produto_3 = Produto('Long-board', 200, -5)
produto_3.exibir()