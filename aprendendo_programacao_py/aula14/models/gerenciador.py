from models.reserva import Reserva


class GerenciadorDeReservas:
    def __init__(self):
        self.reservas = []
        self.quartos = []

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def verificar_disponibilidade(self, data_checkin, data_checkout):
        return [quarto for quarto in self.quartos if quarto.disponivel]

    def criar_reserva(self, cliente, quarto, data_checkin, data_checkout):
        if quarto.disponivel:
            reserva = Reserva(cliente, quarto, data_checkin, data_checkout)
            self.reservas.append(reserva)
            quarto.reservar()
            cliente.adicionar_reserva(reserva)
            return reserva
        return None
    
    def listar_reservas(self):
        """Retorna uma lista de todas as reservas feitas."""
        return self.reservas
