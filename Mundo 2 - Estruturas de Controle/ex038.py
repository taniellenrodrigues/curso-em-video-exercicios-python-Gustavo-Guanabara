num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print(f'O valor {num1} é maior que {num2}')
elif num1 < num2:
    print(f'O valor {num2} é maior que {num1}')
else:
    print('Não existe valor maior, os dois são iguais!!!')