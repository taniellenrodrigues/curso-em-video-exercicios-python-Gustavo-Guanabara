print('-'*25)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*25)
n = int(input('Quantos termos você quer mostrar? '))
v1 = 0
v2 = 1
c = 3
print(f'{v1} - {v2} ', end='')

while c <= n:
    v3 = v1 + v2
    print(f'- {v3}', end=' ')
    v1 = v2
    v2 = v3
    c += 1
    
print('FIM')
    