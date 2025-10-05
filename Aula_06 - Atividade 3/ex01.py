class Circulo():
    def __init__(self): #colocar as variaveis
        self.raio = 0
        self.pi = 3.14

    def set_raio(self, v): #é o que colocamos as condições, esse v serve como input fixo já definido
        if v < 0:
            print('Valor inválido')
        else:
            self.raio = v

    def get_raio(self):
        return self.raio #o retorno depois da condição

    def calc_area(self):
        return self.pi * (self.raio ** 2) #o calc serve para as operações

    def calc_circunferencia(self):
        return 2 * self.pi * self.raio 


c = Circulo()
c.set_raio(10)

print(f'Raio: {c.get_raio()}')
print (f'Circunferencia: {c.calc_circunferencia()}')
print (f'Area: {c.calc_area()}')

