print('Digite três valores: ')
a = int(input())
b = int(input())
c = int(input())


lista1 = [a,b,c]

menor = 100000000000
maior = 0
meio = 0

for i in range(3):
    if lista1[i] > maior:
        maior = lista1[i]
    if lista1[i] < menor:
        menor = lista1[i]
            
for j in range(3):
    if lista1[j] != maior and lista1[j] != menor:
        meio = lista1[j]


lista = [menor, meio, maior]
print(*lista)