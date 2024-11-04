class Fatura:
    def __init__(self, nome_item, preco_unitario, quantidade):
        self.nome_item = nome_item
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.valor_total = 0

    def gerar_fatura(self):
        self.valor_total = self.preco_unitario * self.quantidade
        return self.valor_total
    
    def exibir_fatura(self):
        print(f'Item: {self.nome_item}')
        print(f'Preço Unitário: R${self.preco_unitario:.2f}')
        print(f'Quantidade: {self.quantidade}')
        print(f'Valor Total da Fatura: R${self.valor_total:.2f}')


boleto_infinity = Fatura('Curso de Python',300, 6)


boleto_infinity.gerar_fatura()

boleto_infinity.exibir_fatura()
