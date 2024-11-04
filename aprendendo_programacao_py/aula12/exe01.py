 # Crie uma classe Hotel que permita gerenciar
 # funcionários, reservas e quartos de hotel. Os
 # funcionários devem ter informações como nome,
 # função e salário. O hotel deve ser capaz de
 # receber reservas, atribuí-las a quartos e
 # calcular a conta final


class Funcionario:
    def __init__(self, nome, funcao, salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario


    def exibir_funcionarios(self):
        return f"Nome: {self.nome}, Função: {self.funcao}, Salário: {self.salario}"
    
class Quarto:
    def __init__(self, numero, preco_diaria, ocupado=False):
        self.numero = numero
        self.preco_diaria = preco_diaria
        self.ocupado = ocupado

    def exibir_quartos(self):
        return f"Número: {self.numero}, Preço da diária: R${round(self.preco_diaria, 2)}, Vago ?: {self.ocupado}"

class Reserva:
    def __init__(self, nome_hospede, dias, quarto):
        self.nome_hospede = nome_hospede
        self.dias = dias
        self.quarto = quarto
        self.valor_total = 0

    def calcular_valor_total(self):
        self.valor_total = self.dias * self.quarto.preco_diaria
        self.valor_total = round(self.valor_total, 2)

    def exibir_reserva(self):
        return (
            f"Hospede: {self.nome_hospede}\n"
            f"Número de diárias: {self.dias} diárias.\n"
            f"Quarto Nº: {self.quarto.numero}\n"
            f"Valor Total: R${self.valor_total}\n"
        )
    
class Hotel:
    def __init__(self, nome_hotel):
        self.nome_hotel = nome_hotel
        self.funcionarios = []
        self.reservas = []
        self.quartos = []

    def add_funcionarios(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f'Funcionário {funcionario.nome} adicionado com sucesso.')

    def remover_funcionarios(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                self.funcionarios.remove(funcionario)
                print(f'O Funcionário {funcionario.nome} foi removido.')
                return
        print(f'Funcionário {nome} não encontrado.')

    def listar_funcionarios(self):
        if not self.funcionarios:
            print('Nenhum funcionário cadastro.')
        else:
            print(f'Funcionários do Hotel {self.nome_hotel}')
            for funcionario in self.funcionarios:
                print(funcionario.exibir_funcionarios())

    def reservar_quarto(self, nome_hospede, dias, numero_quarto):
        for quarto in self.quartos:
            if quarto.numero == numero_quarto and not quarto.ocupado:
                reserva = Reserva(nome_hospede, dias, quarto)
                reserva.calcular_valor_total()
                self.reservas.append(reserva)
                quarto.ocupado = True
                print(f'Reserva do quarto nº {numero_quarto} para o hospede {nome_hospede} efetuada com sucesso.')
                print(f'Valor da reserva: R${reserva.valor_total}')
                return
        print(f'Quarto {numero_quarto} não está disponível.')

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)
        print(f'Quarto Nº {quarto.numero} adicionado com sucesso.')

    def listar_quartos(self):
        if not self.quartos:
            print('Nenhum quarto existente.')

        else:
            print(f'Quartos do Hotel {self.nome_hotel}')
            for quarto in self.quartos:
                print(quarto.exibir_quartos())

    def listar_reservas(self):
        if not self.reservas:
            print('Nenhuma reserva feita.')
        else:
            print(f'Reservas do Hotel {self.nome_hotel}')
            for reserva in self.reservas:
                print(reserva.exibir_reserva())

    def calcular_conta_final(self, nome_hospede):
        for reserva in self.reservas:
            if reserva.nome_hospede == nome_hospede:
                return f'Conta final para {nome_hospede}: R${reserva.valor_total}'
        return f'Nenhuma conta para {nome_hospede} encontrada.'
    

hotel = Hotel('Infinity Hotel')

funcionario_1 = Funcionario('Bruno', 'Gerente', 10000)
funcionario_2 = Funcionario('Wilkson', 'Auxiliar de serviços gerais', 1412)

hotel.add_funcionarios(funcionario_1)
hotel.add_funcionarios(funcionario_2)    

quarto_1 = Quarto(1, 150)
quarto_2 = Quarto(2, 1000)

hotel.adicionar_quarto(quarto_1)
hotel.adicionar_quarto(quarto_2)


hotel.reservar_quarto('João', 7, 1)
hotel.reservar_quarto('Bruno', 3, 2)

hotel.listar_funcionarios()
hotel.listar_quartos()
hotel.listar_reservas()