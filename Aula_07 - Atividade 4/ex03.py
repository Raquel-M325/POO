class Conversor():
    def __init__(self, num):
        if num <= 0:
            raise ValueError('Erro: Valor deve ser positivo')
        elif num == float:
            raise ValueError('Erro: Tem que ser valor inteiro')
        
        self.num = num

    def SetNum(self, num):
        if num <= 0:
            print('Valor Inválido')
        elif num == float:
            print('Tipo de número Inválido')

        self.num = num

    def GetNum(self):
        return self.num
    
    def Binario(self):

        
    def ToString(self):


c = Conversor(5)
print(c.ToString())
        