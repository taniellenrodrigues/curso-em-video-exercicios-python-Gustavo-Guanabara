num = int(input('Informe um número: '))
un = num // 1 % 10
de = num // 10 % 10
ce = num // 100 % 10
mi = num // 1000 % 10

print('Analisando o número...')
print(f'Unidade: {un}')
print(f'Dezena: {de}')
print(f'Centena: {ce}')
print(f'Milhar: {mi}')