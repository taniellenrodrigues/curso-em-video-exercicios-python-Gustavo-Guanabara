v = 0
soma = 0
cont = -1
while v != 999:
    v = int(input('Digite um número [999 para parar]'))
    soma = soma + v
    cont += 1

print(f'Você digitou {cont} números e a soma entre eles foi {soma-999}')