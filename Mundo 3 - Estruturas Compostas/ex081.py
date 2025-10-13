lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).upper().strip()[0]
    if resp == 'N':
        break

print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem descrescente são {lista}') 
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')