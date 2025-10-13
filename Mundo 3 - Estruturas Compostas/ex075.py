n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
n = (n1, n2, n3, n4)
print(f'Você digitou os números {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 aparaceu na {n.index(3)+1}° posição')
else:
    print('Não há nenhum valor 3 na lista!')
print('Os valores pares digitados foram ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=', ')