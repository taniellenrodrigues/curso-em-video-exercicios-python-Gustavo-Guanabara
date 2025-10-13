t = int(input('Digite um termo:'))
r = int(input('Digite uma razão:'))
termo = t
cont = 1
while cont <= 10:
    print(f'{termo}-', end='')
    termo+= r
    cont += 1
print('FIM')