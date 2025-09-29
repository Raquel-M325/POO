class Conta():     
    
    def __init__(self):
        self.titular = str(input('seu titular: '))
        self.numero = int(input('sua identidade: '))
        self.saldo = float(input('saldo: '))
        

    def saldo_antigo(self):
        return self.saldo
    
    def bancario(self):
        self.ganho = 0
        self.tirada = 0
        
        self.pergunta = str(input('Quer sacar: '))
        if self.pergunta == 'Sim':
            self.sacar = int(input('Digite o quanto você quer sacar: '))
            self.tirada = self.saldo - self.sacar
        else:
            self.perguntad = str(input('Quer depositar: '))
            if self.perguntad == 'Sim':
                self.deposito = int(input('Digite o quanto você quer depositar: '))
                self.ganho = self.saldo + self.deposito
            else:
                pass
            
        self.saldonovo = self.ganho - self.tirada
        return self.saldonovo


#OBS: preciso saber é como atualizar o valor do saldo sem ficar separado e colocar as condições

classe = Conta() 

print(f'Seu saldo anterior: {classe.saldo_antigo()} R$')
print(f'Seu saldo atual: {classe.bancario()} R$')



#saque é o que eu tiro, ou seja, eu subtraio com saldo
#já o depositorio é o que acrescento o dinheiro, entao eu somo com o saldo