'''EXERCICIO 1


Implemente uma classe base Veiculo com um método mover() que retorna uma mensagem indicando a velocidade com que o veículo está se movendo.

Depois, crie três subclasses: Carro, Bicicleta, e Aviao, cada uma com suas próprias características:

Cada subclasse deve implementar o método mover() para retornar uma velocidade diferente para cada tipo de veículo (por exemplo, Carro a 60 km/h, Bicicleta a 15 km/h, e Aviao a 900 km/h).
Adicione um método acelerar() na classe base Veiculo que aumenta a velocidade em um valor definido por cada subclasse.
Crie uma lista de diferentes instâncias de veículos e, em um loop, chame os métodos mover() e acelerar() para cada veículo, imprimindo a velocidade após a aceleração.


RESOLUÇÃO'''

class Veiculo:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def mover(self):
        return f'O Veículo está se movendo a {self.velocidade} km/h.'
    
    def acelerar(self, incremento):
        self.velocidade += incremento
        return f'O veículo acelerou em {incremento}, atingindo uma velocidade de {self.velocidade} km/h.'
    
class Carro(Veiculo):
    def __init__(self):
        super().__init__(velocidade=60)

    def mover(self):
        return f'O Carro está se movendo a {self.velocidade} km/h.'
    
    def acelerar(self, incremento):
        return super().acelerar(incremento)
    
class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__(velocidade=15)

    def mover(self):
        return f'A bicicleta está se movendo a {self.velocidade} km/h.'
    
    def acelerar(self, incremento):
        return super().acelerar(incremento)
    
class Aviao(Veiculo):
    def __init__(self):
        super().__init__(velocidade=900)

    def mover(self):
        return f'O avião está se movendo a {self.velocidade} km/h.'
    
    def acelerar(self, incremento):
        return super().acelerar(incremento)
    
veiculos = [Carro(), Bicicleta(), Aviao()]