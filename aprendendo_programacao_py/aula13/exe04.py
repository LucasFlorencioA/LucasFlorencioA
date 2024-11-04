class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.pedidos = []

    def fazer_pedido(self,pedido):
        if isinstance(pedido, Pedido):
            pedido.cliente = self
            self.pedidos.append(pedido)
            print(f'O pedido {pedido.produto} foi adicionado para o cliente {self.nome}.')
        else:
            print('Apenas pedidos da classe Pedido podem ser adicionados.')

    def listar_pedidos(self):
        if not self.pedidos:
            print(f'O cliente {self.nome} não realizou nenhum pedido.')
        else:
            print(f'Pedidos realizados pelo cliente {self.nome}: ')
            for pedido in self.pedidos:
                print(f'- {pedido.produto}')

    def __str__(self):
        return f'Cliente: {self.nome} | E-mail: {self.email} | Nº de pedidos {len(self.pedidos)} |'
    
class Pedido:
    def __init__(self, produto, quantidade, preco_unitario):
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.cliente = None

    def calcular_total(self):
        preco_total = self.quantidade * self.preco_unitario
        print(f'O pedido feito por {self.cliente} totalizou em R${preco_total:.2f}')
    
    def __str__(self):
        return (f'Produto: {self.produto} | Quantidade: {self.quantidade}'
                f'Preço Unitário: {self.preco_unitario} | '
                f'Total: R%{self.calcular_total():.2f}' 
        )
    
cliente_1 = Cliente('Lucas', 'lokao_sk8_589@hotmail.com')
cliente_2 = Cliente('Anderson', 'gatinho69@mirc.com')
cliente_3 = Cliente('Gabriel', 'gabgoldatuf@bol.com.br')


pedido_1 = Pedido('Skate',1, 200)
pedido_1_5 = Pedido('Long-board',1, 400)
pedido_2 = Pedido('Oculos escuros', 2, 200)
pedido_3 = Pedido('Camisa do Fortaleza', 1, 350)

cliente_1.fazer_pedido(pedido_1)
cliente_1.fazer_pedido(pedido_1_5)
pedido_1.calcular_total()
pedido_1_5.calcular_total()

cliente_2.fazer_pedido(pedido_2)
pedido_2.calcular_total()

cliente_3.fazer_pedido(pedido_3)
pedido_3.calcular_total()



cliente_1.listar_pedidos()

print('#####################')

cliente_2.listar_pedidos()    

print('#####################')

cliente_3.listar_pedidos() 