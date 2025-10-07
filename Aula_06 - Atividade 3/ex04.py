class Cinema():
    def __init__(self):
        self.ingresso = 0
        self.acrescimo = 0        

    def set_ingresso(self, i):
        if i < 0:
            print('Valor Inválido')
        else:
            self.ingresso = i

    def set_acrescimo(self, a):
        if a < 0:
            print('Valor Inválido')
        else:
            self.acrescimo = a

    def get_ingresso(self):
        return self.ingresso

    def get_acrescimo(self):
        return self.acrescimo

    def calc_agendamento(self):
        self.acrescimo = 0.5 * self.ingresso
        return self.ingresso + self.acrescimo


c = Cinema()

#----------------INTERFACE DO USUÁRIO----------------------- 
noite = []

for i in range(17, 25):
    noite.append(i)
    
dias = str(input('Qual dia você quer ver o filme, seguindo nesse formato [seg, ter, qua, qui, sex, sab, dom]: '))
horario = int(input('Qual horário: '))
if dias == 'sex' or dias == 'sab' or dias == 'dom':
    c.set_ingresso(18)
    if horario in noite:
        print(f'Ingresso com acréscimo: R$ {c.calc_agendamento():.2f}')
    else:
        print(f'Ingresso: R$ {c.get_ingresso():.2f}')


elif dias == 'seg' or dias == 'ter' or dias == 'qui':
    c.set_ingresso(16)
    if horario in noite:
        print(f'Ingresso com acréscimo: R$ {c.calc_agendamento():.2f}')
    else:
        print(f'Ingresso: R$ {c.get_ingresso():.2f}')


elif dias == 'qua':
    c.set_ingresso(8)
    print(f'Ingresso de meia entrada: R$ {c.get_ingresso():.2f}, lembrando que não tem acréscimo nas quartas!')


