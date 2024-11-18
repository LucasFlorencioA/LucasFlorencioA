class Quarto:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.disponivel = True

    def reservar(self):
        self.disponivel = False

    def liberar(self):
        self.disponivel = True