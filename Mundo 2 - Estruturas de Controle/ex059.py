opcao = 1
while opcao != 5:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
   
    print('=--='*7)
    print('=============MENU============')
    print('=--='*7)
    
    print('### ESCOLHA UMA OPÇÃO ###')
    print('[1] - SOMAR')
    print('[2] - MULTIPLICAR')
    print('[3] - MAIOR')
    print('[4] - NOVOS NÚMEROS')
    print('[5] - SAIR DO PROGRAMA')

    opcao = int(input('>>>>>>> '))
    if opcao == 1:
        totalsoma = n1 + n2
        print(f'>>> {n1} + {n2} = {totalsoma} <<<')
    elif opcao == 2:
        totalmulti = n1 * n2
        print(f'>>> {n1} x {n2} = {totalmulti} <<<')
    elif opcao == 3:
        if n1 > n2:
            print(f'>>> {n1} é maior que {n2} <<<')
        else:
            print(f'>>> {n2} é maior que {n1} <<<')
    elif opcao == 4:
        print('=-==-=Escolha novos valores=-==-=')
    else:
        print('Opçao inválida! Tente novamente!')
    
print('SAINDO DO PROGRAMA...')