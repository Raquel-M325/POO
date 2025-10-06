class Conta():
    def __init__(self):
        self.saldo = 0
        self.deposito = 0
        self.saque = 0

    def set_saldo(self, s):
        if s < 0:
            print('Seu saldo está negativo')
        else:
            self.saldo = s

    def set_deposito(self, d):
        if d < 0:
            print('Depósito Inválido')
        else:
            self.deposito = d

    def set_saque(self, m):
        if m < 0:
            print('Saque Inválido')
        else:
            self.saque = m

    def get_saldo(self):
        return self.saldo

    def get_deposito(self):
        return self.deposito

    def get_saque(self):
        return self.saque

    def calc_bancario(self): #somente calculo, sem as enrolações como input
        return (self.saldo + self.deposito) - self.saque

c = Conta()

#INTERFACE COM USUÁRIO

#TITULAR
titular = str(input('Qual seu nome completo: '))


#IDENTIDADE
identidade = int(input('Agora a sua identidade: '))


#SALDO
saldo_atual = float(input('Informe qual seu saldo atual: '))
c.set_saldo(saldo_atual)


#DEPOSITO
perguntar = str(input('Quer depositar [s/n]: ').lower())
if perguntar == 's':
    resposta_deposito = float(input('Quanto: '))
    c.set_deposito(resposta_deposito)


#SAQUE
perguntad = str(input('Quer sacar[s/n]: ').lower())
if perguntad == 's':
    resposta_saque = float(input('Quanto: '))
    c.set_saque(resposta_saque)


print(f'Seu saldo: {c.get_saldo():.2f} R$')
print(f'Depositou: {c.get_deposito():.2f} R$')
print(f'Sacou: {c.get_saque():.2f} R$')
print(f'Seu saldo atual: {c.calc_bancario():.2f} R$')

