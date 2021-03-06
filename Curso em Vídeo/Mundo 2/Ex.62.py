print('Gerador de P.A')
print('=-=' * 7)
x1 = int(input('Primeiro termo: '))
r = int(input('Razão da P.A: '))
n = total = 0
mais = 10
while mais != 0:
    total += mais
    while n < total:
        n += 1
        x1 += r
        print('{}'.format(x1), end='')
        print(' ↠ ' if n < total else '↠ Pausa', end='')
    mais = int(input('\nQuantos números deseja acrescentar: '))
print('Finalizando...')
print('Finalizado!! e o total de números foi {}.'.format(total))

