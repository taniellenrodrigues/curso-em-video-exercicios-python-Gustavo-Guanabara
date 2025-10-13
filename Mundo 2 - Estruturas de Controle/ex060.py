'''from math import factorial
num = int(input('Digite um nÚmero para calcular sua fatorial: '))
f = factorial(num)
print(f'O fatorial de {num} é {f}')'''

'''num = int(input('Digite um número para calcular sua fatorial:'))
c = num
f = 1
while c > 0:
    print(f'{ c}', end=' ')
    print('x' if c >1 else '=', end=' ')
    f *= c
    c -= 1
print(f'{f}')'''

num = int(input('Digite um número para calcular sua fatorial:'))
f = 1
for c in range(num, 0, -1):
    print(f'{c} ', end='')
    print('x' if c >1 else '=', end=' ')
    f = f * c
    c = c - f
   
print(f'{f}')