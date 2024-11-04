class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.historico = []


    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f'+ R${valor:.2f}')
            print(f'O valor de R${valor:.2f} foi depositado com sucesso.')
        else:
            print(f'Valor inválido. Refaça a operação.')

    def sacar(self, valor, limite_saque = 1000):
        if valor > limite_saque:
            print(f'O valor excede o limite permitido de R${limite_saque:.2f}')
            return
        
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f'- R${valor:.2f}')
            print(f'Saque de R${valor:.2f} efetuado com sucesso.')
        else:
            print('Saldo insuficiente.')

    def exibir_saldo(self):
        return f'Seu saldo atual é de R${self.saldo:.2f}.'
    
    def resumo(self):
        print(f'Tipo da Conta: {self.__class__.__name__}')
        print(f'Conta Nº:{self.numero}')
        print(f'Titular: {self.titular}')
        print(self.exibir_saldo())
    
    def transferir(self, valor, conta_destino):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.historico.append(f'- R${valor:.2f}')
            conta_destino.historico.append(f'+ R${valor:.2f}')
            print('Transferência realizada com sucesso.')
        else:
            print('Saldo insuficiente.')

    def exibir_historico(self):
        print(f'Histórico da Conta Nº {self.numero}')
        for transacao in self.historico:
            print(transacao)

class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0, taxa_manutencao = 10, limite_cheque = 500):
        super().__init__(numero, titular, saldo)
        self.taxa_manutencao = taxa_manutencao
        self.limite_cheque = limite_cheque

    def sacar(self, valor, limite_saque=1000):
        if valor <= self.saldo + self.limite_cheque:
            super().sacar(valor, limite_saque)
        else:
            print('Saldo insuficiente.')

    def depositar(self, valor):
        return super().depositar(valor)
    
    def cobrar_taxa_manutencao(self):
        if self.saldo + self.limite_cheque >= self.taxa_manutencao:
            self.saldo -= self.taxa_manutencao
            self.historico.append(f'- R${self.taxa_manutencao:.2f}')
            print('Taxa de manutenção deduzida com sucesso.')
        else:
            print('Saldo insuficiente.')

class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0, taxa_juros = 0.02):
        super().__init__(numero, titular, saldo)
        self.taxa_juros = taxa_juros

    def sacar(self, valor, limite_saque=1000):
        if valor <= self.saldo:
            super().sacar(valor, limite_saque)
        else:
            print('Saldo insuficiente.')

    def depositar(self, valor):
        return super().depositar(valor)
    
    def add_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        self.historico.append(f' + R${juros:.2f} ')

conta_corrente = ContaCorrente(numero='12345', titular='Bruno', saldo=10000)
conta_poupanca = ContaPoupanca(numero='789456', titular='Will', saldo=10000)


conta_corrente.depositar(500)
conta_corrente.sacar(200)
conta_corrente.cobrar_taxa_manutencao()
conta_corrente.resumo()
conta_corrente.exibir_historico()

print('------------------------------')

conta_poupanca.depositar(1000)
conta_poupanca.sacar(500)
conta_poupanca.add_juros()
conta_poupanca.resumo()
conta_poupanca.exibir_historico()