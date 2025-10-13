vcasa = float(input('Qual o valor da casa que pretende comprar?'))
salario = float(input('Qual o seu salário mensal?'))
anos = int(input('Em quantos anos pretende pagar?'))

mensal = vcasa / (anos * 12)

if mensal <= 30 / 100 * salario:
    print(f'Parabens! O seu financiamento foi aprovado')
else:
    print('Sinto muito! O seu financiamento foi negado')

print(f'Com a casa no valor de R${vcasa:.3f}, o seu financiamento ficará com parcelas de R${mensal:.2f} mensais por {anos} anos')