while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*35)
    if t < 0:
        break
    c = 0
    for c in range(1,11):
        print(f'{t} x {c} = {t*c}')
print('PROGRAMA TABUADA ENCERRADO')