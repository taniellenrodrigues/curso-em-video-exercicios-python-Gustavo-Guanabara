t = int(input('Digite um termo:'))
r = int(input('Digite uma razão:'))
decimo = t + (10-1) * r
for c in range(t, decimo+r, r):
    print(c, end='-')