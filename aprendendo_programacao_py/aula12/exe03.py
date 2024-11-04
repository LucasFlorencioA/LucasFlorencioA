class Veiculo:
    def __init__(self):
        self.cor = None
        self.modelo = None

    def set_color(self, cor):
        self.cor = cor
        return self
    
    def set_model(self, modelo):
        self.modelo = modelo
        return self
    
class Carro(Veiculo):
    def __init__(self):
        super().__init__()
        
        
    def set_num_portas(self, num_portas):
        self.num_portas = num_portas
        return self
    
    def descricao(self):
        return f'Carro - Modelo: {self.modelo}, Cor: {self.cor}, Portas: {self.num_portas}'
    
class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__()
        self.tipo = None

    def set_tipo(self, tipo):
        self.tipo = tipo
        return self
    
    def descricao(self):
        return f'Bicicleta - Modelo: {self.modelo}, Cor: {self.cor}, Tipo: {self.tipo}'


carro = Carro().set_color('vermelha').set_model('Celta').set_num_portas(2)

bike = Bicicleta().set_color('azul').set_model('Caloi').set_tipo('Montanha')

print(carro.descricao())

print(bike.descricao())