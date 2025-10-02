class Cinema():
    def __init__(self):
        self.dia = str(input('Qual dia para ver o filme, escolha e digite desse formato [seg, ter, qua, qui, sex, sab, dom]: '))
        self.horario = int(input('Que horas: '))
        self.valor = 0
        self.acrescimo = 0 

    def noite(self):
        self.listadehora= []
        for i in range(17, 24):
            self.listadehora.append(i)
            return [i + 1]
        return self.listadehora 
        #Precisa ajeitar em relação das horas do desconto que ainda não está funcionando       
    

    def tempo(self):
        if self.dia == "seg" or self.dia == "ter" or self.dia == "qui":
            self.valor = 16
            if self.horario == self.noite:
                self.acrescimo = (50/100) * self.valor
                return f'O ingresso custa {self.acrescimo:.2f} R$'
            else:
                return f'O ingresso custa {self.valor:.2f} R$'
         

        elif self.dia == "sex" or self.dia == "sab" or self.dia == "dom":
            self.valor = 20
            if self.horario == self.noite:
                self.acrescimo = (50/100) * self.valor
                return f'O ingresso custa {self.acrescimo:.2f} R$'
            else:
                return f'O ingresso custa {self.valor:.2f} R$'
         
        elif self.dia == "qua":
            self.valor = 8
            if self.horario == self.noite:
                self.acrescimo = (50/100) * self.valor
                return f'O ingresso custa {self.acrescimo:.2f} R$ de meia-entrada com acréscimo'
            else:
                return f'O ingresso custa {self.valor:.2f} R$ de meia-entrada'
         
    
C = Cinema()

print(C.tempo())


        