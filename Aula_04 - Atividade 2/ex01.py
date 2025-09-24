class Circulo:
    def __init__(self):
        self.pi = 3.14
        self.raio = int(input('Digite o raio: 5'))
       
    def area(self):
        return self.pi * (self.raio ** 2)

    def circunferencia(self):
        return 2 * self.pi * self.raio

classe = Circulo()
print('Área do círculo:', classe.area())
print('Circunferência:', classe.circunferencia())
