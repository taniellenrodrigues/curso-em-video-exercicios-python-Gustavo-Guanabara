lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    
    if c == 0 or n > lista[-1]: #appende se ele for o primeiro valor[0], ou se ele for o último valor da lista
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos+=1
print('=-'*30)

print(lista, )
