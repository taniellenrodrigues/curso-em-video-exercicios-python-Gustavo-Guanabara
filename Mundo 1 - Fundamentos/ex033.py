num1 = int(input('Primeiro valor:'))
num2 = int(input('Segundo valor:'))
num3 = int(input('Terceiro valor:')) 
# verificando quem é o menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
#verificando quem é o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'O menor valor digitado foi: {menor}!')
print(f'O maior valor digitado foi:{maior}!')