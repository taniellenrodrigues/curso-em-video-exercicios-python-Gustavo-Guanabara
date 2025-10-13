print(f'{'LOJA DA ELLEN':=^40}')

valor = float(input('Qual o valor a ser pago? '))
print(f'{'FORMAS DE PAGAMENTO':=^40}')
print('[1] - Á VISTA COM DINHEIRO/CHEQUE')
print('[2] - Á VISTA NO CARTÃO')
print('[3] - 2x NO CARTÃO')
print('[4] - 3x NO CARTÃO')

pagar = int(input('Qual será a forma de pagamento? Escolha o número da opção:'))




if pagar == 1:
    avdin = valor - (valor * 10 / 100)
    print(f'Você pagará R${avdin:.2f}')

elif pagar == 2:
    avcar = valor - (valor * 5 / 100)
    print(f'Você irá pagar R${avcar:.2f}')

elif pagar == 3:
    parcela = valor / 2
    print(f'Você pagará 2x de R${parcela:.2f} sem juros')

elif pagar == 4:
    vezes = int(input('Quantas parcelas? '))
    total = (20 / 100 * valor + valor)
    totalx = total / vezes
    
    print(f'Você pagará {vezes}x de R${totalx:.2f}, num valor total de {total}')
   
else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE!!!')
