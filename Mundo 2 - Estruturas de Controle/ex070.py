tot = maiorM = menorV = cont = 0 
barato = ''
print('-'*40)
print('LOJA SUPER BARATÃO'.center(40))
while True:
    print('-'*40)
    prod = str(input('Nome do produto:'))
    preco = float(input('Preço do produto: R$ '))
    cont += 1
    tot += preco
    if preco >= 1000:
        maiorM += 1
    if cont == 1:
        menorV = preco 
        barato = prod
    else:
       if preco < menorV:
        menorV = preco
        barato = prod   
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('----------FIM DO PRAGRAMA----------')
print(f'O total da compra foi {tot}')
print(f'Temos {maiorM} produtos custando mais de R$1.000 ')
print(f'O produto mais barato foi {barato} que custa R${menorV}')