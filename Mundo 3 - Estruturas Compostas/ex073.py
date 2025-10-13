times = ('Palmeiras','Santos','Vasco da Gama','Grêmio','Flamengo',
'Corinthians','Internacional','Cruzeiro','São Paulo','Atlético Mineiro',
'Botafogo','Fluminense','Coritiba','Bahia','Goiás','Guarani',
'Sport','Portuguesa','Atlético Paranaense','Vitória')
print('### Listas de time brasileirão ###'.center(60))
print(times)
print('###Os cinco primeiros colocados foram...###'.center(60))
print(f'{times[0:5]}\n')
print('### Os últimos quatro colocas da tabela foram... ###'.center(60))
print(f'{times[-4]}\n')
print('### Lista em Ordém Alfabética ###'.center(60))
print(sorted(times))
posicao=' '
while True:
    posicao = str(input('Qual time você deseja saber sua posição? '))
    if posicao in times:
       print(f'O time {posicao} está na posição {times.index(posicao)+1}°')
       break  
    else:
        print('Time não encontrado. Tente novamente!')
    




