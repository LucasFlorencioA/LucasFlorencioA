class Reserva:
    def __init__(self, cliente, quarto, data_checkin, data_checkout):
        self.cliente = cliente
        self.quarto = quarto
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.status = "Confirmada"

    def cancelar(self):
        self.status = "Cancelada"
        self.quarto.liberar()
