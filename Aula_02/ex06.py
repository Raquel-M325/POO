a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
j = int(input())


lista = [a, b, c, d, e, f, g, h, i, j]
lista1 = []

for i in range(10):
    if lista[i] < 0:
        valor = lista[i] * (-1)
        lista1.append(f"-{valor}")
        #preciso resolver essa parte da conversão.
        
    else: 
         lista1.append(lista[i])

lista1.sort()
print('Resultado: ', *lista1)