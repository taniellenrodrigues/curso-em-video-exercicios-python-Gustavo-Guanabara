num = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in num:
        num.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Não vou adicionar!')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
    
print('=-'*25)
num.sort()
print(f'Você digitou os valores {num}')