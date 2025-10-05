class Cinema():
    def __init__(self):
        self.dia = str(input('Qual dia para ver o filme, escolha e digite desse formato [seg, ter, qua, qui, sex, sab, dom]: '))
        self.horario = int(input('Que horas: '))
        self.valor = 0
        self.acrescimo = 0 

    def noite(self):
        self.horarios = []
        for i in range(17, 25):
            self.horarios.append(i)
        return self.horarios

    def tempo(self):
        if self.dia == "seg" or self.dia == "ter" or self.dia == "qui":
            self.valor = 16
            if self.horario in self.noite():
                self.acrescimo = 0.50 * self.valor
                self.preco_final = self.acrescimo + self.valor
                return f'O ingresso custa {self.preco_final:.2f} R$'
            else:
                return f'O ingresso custa {self.valor:.2f} R$'
         

        elif self.dia == "sex" or self.dia == "sab" or self.dia == "dom":
            self.valor = 20
            if self.horario in self.noite():
                self.acrescimo = 0.50 * self.valor
                self.preco_final = self.acrescimo + self.valor
                return f'O ingresso custa {self.preco_final:.2f} R$'
            else:
                return f'O ingresso custa {self.valor:.2f} R$'
         
        elif self.dia == "qua":
            self.valor = 8
            if self.horario in self.noite():
                self.acrescimo = 0.50 * self.valor
                self.preco_final = self.acrescimo + self.valor
                return f'O ingresso custa {self.preco_final:.2f} R$ de meia-entrada com acréscimo'
            else:
                return f'O ingresso custa {self.valor:.2f} R$ de meia-entrada'
         
    
C = Cinema()

print(C.tempo())


        