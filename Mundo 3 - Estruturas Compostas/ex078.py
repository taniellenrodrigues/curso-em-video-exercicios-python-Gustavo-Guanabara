num = []
cont = 0
for n in range (0,5):
    num.append(int(input(f'Digite um valor para a posição {n}: ')))
print('=-'*20)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {max(num)} na posição', end='')
for c, v in enumerate(num):
    if v == max(num):
        print(f' {c}...', end='')
print(f'\nO menor valor digitado foi {min(num)} na posição', end='')
for c, v in enumerate(num):
    if v == min(num):
        print(f' {c}...', end='')