class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.historico_reservas = []

    def adicionar_reserva(self, reserva):
        self.historico_reservas.append(reserva)