class Conta():     
    
    def __init__(self):
        self.titular = str(input('seu titular: '))
        self.numero = int(input('sua identidade: '))
        self.saldo = int(input('saldo: '))
        

    def __saldo_antigo(self):
        return self.saldo
    
    def __bancario(self): #a operação terá que ser tudo junto para ele trabalhar, senão ele separa e dá erro
        self.deposito = 0 #tem que definir os objetos antes
        self.sacar = 0
        
        self.pergunta = str(input('Quer sacar: ').strip().lower()) #strip remove os espaços; lower converte ao minusculo
        if self.pergunta == 'sim':
            self.sacar = int(input('Digite o quanto você quer sacar: '))
            self.perguntad = str(input('Quer depositar: ').strip().lower())
            if self.perguntad == 'sim':
                self.deposito = int(input('Digite o quanto você quer depositar: '))
            else:
                pass

        self.saldo = (self.saldo + self.deposito) - self.sacar
        return self.saldo

classe = Conta() 

print(f'Seu saldo anterior: {classe._Conta__saldo_antigo()} R$')
print(f'Seu saldo atual: {classe._Conta__bancario()} R$')



#saque é o que eu tiro, ou seja, eu subtraio com saldo
#já o depositorio é o que acrescento o dinheiro, entao eu somo com o saldo