from random import randint
valor = (randint (1,10), 
         randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Eu sortiei os valores {valor}')
print(f'O maior valor sorteado foi {max(valor)}')
print(f'O menor valor sorteado foi {min(valor)}')
