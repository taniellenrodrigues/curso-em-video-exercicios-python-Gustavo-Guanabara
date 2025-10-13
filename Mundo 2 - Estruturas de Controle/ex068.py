from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*15)
cont = 0
while True:
    jogador = int(input('Digite um valor: '))
    pi = str(input('Você quer par ou ímpar [P/I]? ')).strip().upper()[0]
    comp = randint(0,10)
    total = jogador + comp
    print(f'Você jogou {jogador} e o computador {comp}, o total é de {total}!!! ', end='')
    if total % 2 == 0:
        print('DEU PAR') 
        if pi == 'P':
            print('VOCÊ GANHOU!')
        else:
            break
    elif total % 2 == 1:
        print('DEU ÍMPAR')
        if pi == 'I':
            print('VOCÊ GANHOU!!!')
        else:
            break
    cont += 1

    print('Vamos jogar novamente...')
    print('=-'*15)
print('VOCÊ PERDEU')
print(f'GAME OVER! Você venceu {cont} vezes')