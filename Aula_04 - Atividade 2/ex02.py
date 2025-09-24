class Viagem():
    def __init__(self):
        self.distancia = int(input('Digite a distancia em Km: '))
        self.tempo = int(input('Digite o tempo gasto em hora: '))

    def velocidade(self):
        return self.distancia // self.tempo
    
Classe = Viagem()
print(f'Sua velocidade media foi {Classe.velocidade()} km/h' )