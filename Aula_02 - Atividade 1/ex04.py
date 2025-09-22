print('Digite uma data no formato dd/mm/aaaa')
data = str(input())

parte = data.split('/')
d = int(parte[0])
m = int(parte[1])
a = int(parte[2])

if a < 1900 or a > 2100:
    if m < 1 or m > 12:
        if d < 1 or d > 31:
            print('A data informada não é válida')
else:
    print('É uma data válida')