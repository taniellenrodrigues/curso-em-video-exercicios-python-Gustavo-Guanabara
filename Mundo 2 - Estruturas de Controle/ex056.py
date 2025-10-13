somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for c in range(1,5):
    print(f'-----{c}° PESSOA-----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    somaidade = somaidade + idade
    
    if c == 1 and sexo == 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

    
    
media = somaidade / 4
print(f'A média de idade do grupo é de {media}')
print(f'O homem mais velho do grupo tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')