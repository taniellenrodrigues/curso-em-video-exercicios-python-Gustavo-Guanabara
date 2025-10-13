
n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
     'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 
     'dezenove', 'vinte')

while True:

    valor = int(input('Digite um número entre 0 e 20: '))
    if valor >= 0 and valor <= 20:
        print(f'O valor digitado foi {n[valor]}!')
        
        resp = ' '
        while resp not in 'NS':
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp == 'N':
            break
    else:
        print('Tente novamente.', end=' ')
