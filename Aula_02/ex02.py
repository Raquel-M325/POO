n = int(input("Informe o número do mês: "))

if n == 1:
    mes = str('janeiro')
    ordem = str('primeiro')

elif n == 2:
    mes = str('fevereiro')
    ordem = str('primeiro')

elif n == 3:
    mes = str('marco')
    ordem = str('primeiro')

elif n == 4:
    mes = str('abril')
    ordem = str('segundo')

elif n == 5:
    mes = str('maio')
    ordem = str('segundo')

elif n == 6:
    mes = str('junho')
    ordem = str('segundo')

elif n == 7:
    mes = str('julho')
    ordem = str('terceiro')

elif n == 8:
    mes = str('agosto')
    ordem = str('terceiro')

elif n == 9:
    mes = str('setembro')
    ordem = str('terceiro')

elif n == 10:
    mes = str('outubro')
    ordem = str('quarto')

elif n == 11:
    mes = str('novembro')
    ordem = str('quarto')

elif n == 12:
    mes = str('dezembro')
    ordem = str('quarto')


print('O mês de', mes, 'é do', ordem, 'trimestre do ano')