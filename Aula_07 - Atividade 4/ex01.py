import math

class Retangulo():

    def __init__(self, b, h):
        if b <= 0 or h <= 0:
            raise ValueError('Erro: Valores devem ser positivos')
        
        self.b = b
        self.h = h

    def SetBase(self, b):
        if b <= 0:
            print('Valor Inválido')
        else:
            self.b = b
        
    
    def SetAltura(self, h):
        if h <= 0:
            print('Valor Inválido')
        else:
            self.h = h
        

    def GetBase(self):
        return self.b

    def GetAltura(self):
        return self.h

    def CalcArea(self):
        return self.h * self.b

    def CalcDiagonal(self):
        return math.sqrt((self.h ** 2) + (self.b ** 2))

    def ToString(self):
        return f'A Base: {self.b} e a Altura: {self.h}\nÁrea do Retângulo: {self.CalcArea()} \nDiagonal do Retângulo: {self.CalcDiagonal()}'


r = Retangulo(2, 7)
print(r.ToString())

