cont1 = cont2 = cont3 = 0
while True:
    print('-'*35)
    print('CADASTRE UMA PESSOA'.center(35))
    print('-'*35)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('--- PESSOA CADASTRADA ---')
    print('')
    if idade >= 18:
            cont1 += 1
    if sexo == 'M':
        cont2 += 1
    if sexo == 'F' and idade < 20:
        cont3 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {cont1}')
print(f'Ao todo temos {cont2} homem cadastrado')
print(f'E temos {cont3} mulher com menos de 20 anos')