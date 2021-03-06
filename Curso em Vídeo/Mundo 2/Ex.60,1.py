n = int(input('Digite o número que desejar calcular o fatorial: '))
f = 1
c = 1
for c in range(n,1,-1):
    f *= c
print('o fatorial de {} é {}'.format(n,f))

