nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'{media:.1f} REPROVADO!!!')
elif media >= 5.0 and media < 6.9:
    print(f'{media:.1f} RECUPERAÇÃO!!!')
elif media >= 7.0:
    print(f'{media:.1f} APROVADO!!!')