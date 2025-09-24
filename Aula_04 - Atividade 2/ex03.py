class Conta():     
    
    def __init__(self):
        self.titular = str(input())
        self.numero = int(input())
        self.saldo = float(input())

    def saldo_antigo(self):
        return self.saldo

    def depositorio(self):
        self.deposito = int(input('Digite o quanto você quer depositar: '))
        return self.saldo + self.deposito

    def saque(self):
        self.sacar = int(input('Digite o quanto você quer sacar: '))
        return self.saldo - self.sacar

    def saldo_novo(self):
        return saldo.

#OBS: preciso saber é como atualizar o valor do saldo sem ficar separado

classe = Conta() 

print(f'Você depositou: {classe.depositorio()} R$')
print(f'Você sacou: {classe.saque()} R$')
print(f'Seu saldo anterior: {classe.saldo_antigo()} R$')
print(f'Seu saldo atual: {classe.saldo.novo} R$')



#saque é o que eu tiro, ou seja, eu subtraio com saldo
#já o depositorio é o que acrescento o dinheiro, entao eu somo com o saldo