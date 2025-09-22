n = int(input())
n1 = int(input())
n2 = int(input())
n3 = int(input())

lista = [n,n1,n2,n3]
parcontagem = 0
imparcontagem = 0
for i in range(4):
    if lista[i] % 2 == 0:
        parcontagem += lista[i]
    else:
        imparcontagem += lista[i]

print("Soma dos pares = ",parcontagem )
print("Soma dos ímpares = ",imparcontagem )

#o número par é aquele que divide por ele mesmo e mais de um número, diferente do impar que é somente 1 e ele mesmo

