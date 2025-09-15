print("Digite quatro valores inteiros")
n = int(input())
n1 = int(input())
n2 = int(input())
n3 = int(input())

lista = [n,n1,n2,n3]
maior = 0
menor = 1000000000000

for i in range(4):
    if lista[i] > maior:
        maior = lista[i]
    elif lista[i] < menor:
        menor = lista[i]



print('Maior valor = ', maior)
print('Menor valor = ', menor)
print('A soma do segundo maior valor com o segundo menor = ', soma)
