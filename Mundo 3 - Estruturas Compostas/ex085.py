valores = [[], []]
for p in range(0,7):
    num = int(input(f'Digite o {p+1}° valor: '))
    valores[0].append(num) if num % 2 == 0 else valores[1].append(num)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares {valores[0]}')
print(f'Os valores ímpares {valores[1]}')
