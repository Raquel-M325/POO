import json

z = {"RN": "Natal", "PB": "João Pessoa", 1: 'Teste'}

#um dicionário
print(z["RN"])
print(z[1])
print(z) 

#-------------------------------------------------------------------------------------------------------------------
class Aluno:
    def __init__(self, nome, matricula, idade):
        self.nome = nome 
        self.matricula = matricula
        self.idade = idade

a = Aluno("Raquel", "2025101400000", 20)
b = Aluno("Nicolas", "2022101400000", 18)

print(a.__dict__) #é mesma coisa do outro, só que uma é de função do vars e esse dict é atributo
print(vars(b))


#-------------------------------------------------------------------------------------------------------------------


y = {"a": "POO", "B": "Redes"} #Lexicográfica, ele irá ver pelo ASCII de MAIOR valor, o que for menor, não sai!
print(max(y))

z = ["Gustavo", "andré"]
z.sort()
print(z)

z = ["Gustavo", "andré"]
z_ordenado = sorted(z, key=str.lower)
print(z_ordenado)


x = vars(b)
for item in x.items():
    print(item, type(item)) #vai separar cada caracteristica da definição das chaves em cada paragráfo

#-------------------------------------------------------------------------------------------------------------------

x = {"RN" : "Natal"}
y = x
y["PB"] = "João Pessoa"
z = x.copy() #a ordem importa a operação


print(x)
print(z)

#-------------------------------------------------------------------------------------------------------------------
class Cliente:
    def __init__(self, nome, id, idade):
        self.nome = nome 
        self.id = id      #TÁ INCOMPLETO
        self.idade = idade

 
a = Cliente(1, "Douglas")
b = Cliente(2, "Jon")
c = Cliente(3, "Willam")

print(vars(a))

clientes = [a, b, c]

with open('clientes.json', mode="w") as arquivo:
    json.dump(clientes, arquivo, default = vars)

   
