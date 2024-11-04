
class Calculadora:
    def __init__(self):
        pass

    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            print('Não é possível dividir por zero.')
        else:
            return a / b
        
calculadora = Calculadora()

print(calculadora.somar(34,56))

print(calculadora.subtrair(100,56))

print(calculadora.multiplicar(456,2))

print(calculadora.dividir(56,7))