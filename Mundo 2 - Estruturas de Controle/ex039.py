from datetime import date
ano = int(input('Qual o ano do seu nascimento? '))
atual = date.today().year
idade = atual - ano
restante = idade - 18
restante2 = 18 - idade

if 18 > idade:
    print(f'Faltam {restante2} anos para voce se alistar.!')
elif 18 < idade:
    print(f'Você já passou {restante} anos do tempo de se alistar!')
else:
    print('Está na hora de se alistar!')