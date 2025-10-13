frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Você digitou a frase {frase}')
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('Temos um palídromo')
else:
    print('Não temos um palídromo')  
    