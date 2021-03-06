print('Gerador de P.A')
print('=-=' * 7)
x1 = int(input('Primeiro termo: '))
r = int(input('Razão da P.A: '))

n = 0

while n < 10:
    n += 1
    x1 += r
    print('{}'.format(x1), end='')
    print(' ↠ ' if n < 10 else ' ↠ FIM', end='')
