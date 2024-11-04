import math

class Forma:
    def area(self):
        raise NotImplementedError('Este método deve ser implementado pela subclasse.')

    def perimetro(self):
        raise NotImplementedError('Este método deve ser implementado pela subclasse.')
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)
    
    def perimetro(self):
        return 2 * math.pi * self.raio
    
class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return (2 * self.base) + (2 * self.altura)
    
circulo = Circulo(5)
print(f'A area do circulo é {circulo.area()}')
print(f'O perimetro do circulo é {circulo.perimetro()}')

retangulo = Retangulo(20,15)
print(f'A area do retangulo é {retangulo.area()}')
print(f'O perimetro do retangulo é {retangulo.perimetro()}')
