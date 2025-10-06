class Cinema():
    def __init__(self):
        self.ingresso = 0
        self.acrescimo = 0        

    def set_ingresso(self, i):
        if i < 0:
            print('Valor Inválido')
        return i == self.ingresso

    def set_acrescimo(self, a):
        if a < 0:
            print('Valor Inválido')
        return a == self.acrescimo

    def get_ingresso(self):
        return self.ingresso

    def get_acrescimo(self):
        return self.acrescimo

    def calc_agendamento(self):
        #ainda estou fazendo

c = Cinema()
