n = s = c = 0
while True:
    n = int(input('Digite um número: [999 para parar]'))
    if n == 999:
        break
    c += 1
    s = s + n
print(f'Você digitou {c} números e a soma entre os valores é igual a {s}')