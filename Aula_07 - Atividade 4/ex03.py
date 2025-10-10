class Conversor:
    def __init__(self, num):
        if num <= 0:
            raise ValueError('Erro: Valor deve ser positivo')
        
        elif num == float:
            raise ValueError('Erro: Tem que ser valor inteiro')
        
        self.num = num

    def SetNum(self, num):
        if num <= 0:
            print('Valor Inválido')
        elif num == float:
            print('Tipo de número Inválido')

        self.num = num

    def GetNum(self):
        return self.num
    
    def Binario(self):


    def __str__(self): #ToString
        return f'Número Binário: {}/n Número Decimal: {self.num}'


c = Conversor(5)
print(c.ToString())
        

# class Conversor:
#     def __init__(self, num):
#         self.set_num(num) 

#     def set_num(self, num):
#         self.__num = num
#     def get_num(self):
#         return self.__num
    
#     def binario(self):
#         restos = []              # pilha
#         n = self.__num
#         while n > 0:
#             restos.append(n % 2) # push - coloca na pilha
#             n = n // 2
#         bin = ""
#         while len(restos) > 0:
#             bin = bin + str(restos.pop()) # pop - retira da pilha
#         return bin
#     def binario2(self):
#         bin = ""
#         n = self.__num
#         while n > 0:
#             bin = str(n % 2) + bin 
#             n = n // 2            
#         return bin
#     def __str__(self):
#         return f"Decimal = {self.__num}, Binário = {self.binario()} {self.binario2()}"

# x = Conversor(14)
# print(x)
