lista = []
dados = []
max = min = rept = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    lista.append(dados[:])
    rept+=1
    if rept == 1:
        max = min = dados[1]
    else:
        if dados[1] > max :
            max = dados[1]
        if dados[1] < min:
            min = dados[1]
    dados.clear()
    perg = ' '
    while perg not in "SN" and ' ':
        perg = str(input('Deseja continuar? ')).upper().strip()[0]
    if perg == 'N':
        break
print(f'Ao todo {len(lista)} pessoas foram cadastradas!')
print(f'O maior peso foi de {max} de', end=' ')
for p in lista:
    if p[1]==max:
        print(p[0], end=' ')
print(f'\nO menor peso foi de {min} de', end=' ')
for p in lista:
    if p[1]==min:
        print(p[0], end=' ')
