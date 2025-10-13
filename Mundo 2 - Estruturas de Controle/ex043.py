peso = float(input('Qual seu peso atual? '))
altura = float(input('Qual a sua altura atual? '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'{imc:.1f}=ABAIXO DO PESO')
elif imc <= 25.0:
    print(f'{imc:.1f}=PESO IDEAL')
elif imc <= 30.0:
    print(f'{imc:.1f}=SOBREPESO')
elif imc <= 40.0:
    print(f'{imc:.1f}=OBESIDADE')
else:
    print(f'{imc:.1f}=OBESIDADE ÓRBIDA')