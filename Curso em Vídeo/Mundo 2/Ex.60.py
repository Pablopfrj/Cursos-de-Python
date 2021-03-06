from time import sleep

c = int(input('Digite o número que deseja: '))
f = 1
print('Calculando...')
sleep(0.73)
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print('{}'.format(f), end='')