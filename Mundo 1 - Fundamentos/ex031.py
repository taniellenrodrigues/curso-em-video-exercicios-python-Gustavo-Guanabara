dist = float(input('Qual a distância da sua viagem?'))
print(f'Você está prestes a começar uma viagem de {dist}Km.')
if dist <=  200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print(f'E o preço da sua passagem será de R${preco}!')