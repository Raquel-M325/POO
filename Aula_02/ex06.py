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

for num in lista:
    if num < 0:
        valor = abs(num)
        lista1.append(valor)
        
    else: 
         lista1.append(num)

lista1.sort()
print('Resultado:', end=' ')

for num in lista1:
    if -num in lista:
        print(f'-{num}', end=' ')
    else:
        print(num, end=' ')
print()