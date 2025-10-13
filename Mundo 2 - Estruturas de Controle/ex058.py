from random import randint
from time import sleep
comp = randint(0, 10) #faz o computador "pensar"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*20)
num = 0
soma = 0
while not comp == num:
    num = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
    print('PROCESSANDO....')
    sleep(1)
    if comp != num:
            if num > comp:
                  print('Menos... tente mais uma vez')
            else:
                  print('Mais... tente mais uma vez')
    soma += 1
print(f'Parabéns, os valores finais são {comp} x {num}. VOCÊ GANHOU! ')
print(f'Foram necessárias {soma} jogadas para você finalmente vencer')