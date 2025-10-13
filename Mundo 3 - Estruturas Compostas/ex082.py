lista = []
par = []
impar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).upper().strip()[0]
    if resp == 'N':
        break
print('-='*15)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')