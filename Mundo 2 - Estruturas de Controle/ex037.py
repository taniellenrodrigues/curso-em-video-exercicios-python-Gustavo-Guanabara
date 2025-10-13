num = int(input('Digite um número: '))
print('Escolha qual será a base de conversão: ')

base = int(input('1- BINÁRIO, 2- OCTAL, 3-HEXADECIMAL: '))

binario = num 

if  base == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif base == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif base == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')