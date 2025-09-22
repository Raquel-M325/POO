print('Digite uma frase:')
escrita = str(input())


while True:
    parte = escrita.split(' ', 1) #tem que estar dentro para funcionar, se estiver fora, ele só faz uma vez e quebra, sendo que quero que ele funcione até o final

    if len(parte) > 1:
        escrita = parte[1] #com dois pontos não funciona por ser um string e não int
        print(escrita)
    elif len(parte) == 1:
        break #não pode esquecer, senão fica infinito










