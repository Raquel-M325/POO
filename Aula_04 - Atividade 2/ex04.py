class Cinema():
    def __init__(self):
        self.dia = str(input('dia: '))
        self.horario = int(input('hora: '))
        self.valor = 0
        self.listadehora= []
        self.acrescimo = 0 

    def noite(self):
        for i in range(17, 24):
            self.listadehora.append([i])

    def tempo(self):
        if self.dia == "seg" or self.dia == "ter" or self.dia == "qui":
            self.valor = 16
            if self.horario == self.listadehora:
                self.acrescimo = (50/100) * 16

        elif self.dia == "sex" or self.dia == "sab" or self.dia == "dom":
            self.valor = 20
        elif self.dia == "qua":
            self.valor == 8
        

        