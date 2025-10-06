class Viagem():
    def __init__(self):
        self.distancia = 0
        self.tempo = 0

    def set_distancia(self, d):
        if d < 0:
            print('Distância Inválida')
        else:
            self.distancia = d
    

    def set_tempo(self, t):
        if t < 0:
            print('Tempo Inválido')
        else:
            self.tempo = t


    def get_distancia(self):
        return self.distancia


    def get_tempo(self):
        return self.tempo


    def velocidade_media(self):
        return self.distancia // self.tempo


r = Viagem()
r.set_distancia(50)
r.set_tempo(5) #não pode esquecer, pois sem ele, não funcionar, pois ficou sem input

print(f"Distância: {r.get_distancia()}")
print(f"Tempo em horas: {r.get_tempo()}")
print(f"Velocidade média: {r.velocidade_media()}")

