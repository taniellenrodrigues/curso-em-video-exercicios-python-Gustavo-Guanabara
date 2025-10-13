valor = float(input('Qual o salário do funcionário? R$'))
soma1 = valor + (valor * 10 / 100)
soma2 = valor + (valor * 15 / 100)
if valor <= 1250.00:
    print(f'Quem ganhava R${valor} passa a ganhar R${soma2:.2f}!')
else:
    print(f'Quem ganhava R${valor}, passa a ganhar R${soma1:.2f}')