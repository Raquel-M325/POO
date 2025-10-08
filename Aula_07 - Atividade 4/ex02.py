class Frete():
    def __init__(self, d, p):
        if d <= 0 or p <= 0:
            raise ValueError('Erro: Valores devem serem positivos')
        self.d = d
        self.p = p

    def SetDistancia(self, d):
        if d <= 0:
            print('Valor Inválido')
        
        self.d = d

    def SetPeso(self, p):
        if p <= 0:
            print('Valor Inválido')

        self.p = p
    
    def GetDistancia(self):
        return self.d
    
    def GetPeso(self):
        return self.p
    
    def CalcFrete(self):
        return 0.01 * self.p * self.d

    def ToString(self):
        return f'Valor do Frete: R$ {self.CalcFrete():.2f}'

f = Frete(5, 20)
print(f.ToString())      
