from random import randint
from time import sleep
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))
maquina = randint(0,2)
pedra = 0
papel = 1
tesoura = 2

if jogador == pedra and maquina == tesoura:
    print('PEDRA')
    sleep(2)
    print('o computador escolheu TESOURA. Você ganhou!')
elif jogador == pedra and maquina == papel:
    print('PEDRA')
    sleep(2)
    print('O computador escolheu PAPEL. Você perdeu!')
elif jogador == papel and maquina ==pedra:
    print('PAPEL')
    sleep(2)
    print('O computador escolheu PEDRA. Você ganhou!')
elif jogador == papel and maquina == tesoura:
    print('PAPEL')
    sleep(2)
    print('O computador escolheu TESOURA. Você perdeu!')
elif jogador == tesoura and maquina == pedra:
    print('TESOURA')
    sleep(2)
    print('O computador escolheu PEDRA. Você perdeu!')
elif jogador == tesoura and maquina == papel:
    print('TESOURA')
    sleep(2)
    print('O computador escolheu PAPEL. Você ganhou!')
elif jogador == maquina:
    print('EMPATE!!')
else:
    print('JOGADA INVÁLIDA!')