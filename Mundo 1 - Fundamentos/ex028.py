from random import randint
from time import sleep
comp = randint(0, 5) #faz o computador "pensar"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
num = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO....')
sleep(3)
print(f'{comp}')
if comp == num:
    print('Parabéns, você venceu!!!')
else:
    print('Que pena, você perdeu!')