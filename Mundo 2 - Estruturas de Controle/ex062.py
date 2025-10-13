t = int(input('Digite um termo:'))
r = int(input('Digite uma razão:'))
termo = t
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}-', end='')
        termo+= r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você que mostrar a mais? '))
print(f'temos o total de {total} termos mostrados!')