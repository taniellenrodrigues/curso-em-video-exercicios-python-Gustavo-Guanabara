print('-='*20)
print('        Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3< r1 + r2:
    print('Os segmentos acima podem formar triângulos')
else:
    print('Os segmentos acima não podem formar triângulos')