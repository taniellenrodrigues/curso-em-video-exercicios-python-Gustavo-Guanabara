import random #ou usar o 'from random import shuffle'

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))

lista = [n1, n2, n3, n4]
re = random.shuffle(lista)

print('A ordem de apresentação será:')
print(lista)