
print('='*30)
print('BANCO CEV'.center(30))
print('='*30)
valor = int(input('Qual o valor que você deseja sacar? '))
total = valor
ced = 50
totalcont = 0
while True:
    if total >= ced:
        total -= ced
        totalcont += 1
        
    else:
        if totalcont > 0:
            print(f'Total de {totalcont} cédulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced ==20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalcont = 0
        if total == 0:
            break
    
