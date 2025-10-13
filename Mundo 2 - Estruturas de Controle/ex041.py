from datetime import date
ano = int(input('Qual o seu ano de nascimento?'))
atual = date.today().year
idade = atual - ano
print(f'O atleta tem {idade}.')

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')