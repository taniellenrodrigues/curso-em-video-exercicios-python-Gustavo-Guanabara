from datetime import date
data = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input(f'{c}°-Qual o seu ano de nascimento?' ))
    idade = data - nasc
    print(f'Você nasceu em {nasc} e tem {idade} anos!')
    if idade >= 18:
        totmaior += 1
    else:
        totmenor +=1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'E também tivemos {totmenor} pessoas menores de idade')