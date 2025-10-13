velo = int(input('Qual é a velocidade atual do carro? '))
multa = (velo - 80) * 7
if velo <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você vai precisar pagar uma multa de R${multa:.2f}!')
    print('Tenha um bom, dia! Dirija com segurança!')