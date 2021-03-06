y = n = cont = 0

n = int(input('Digite um número [999 para o sistema]:  '))

while n != 999:
    n += y
    y = n
    n = int(input('Digite um número [999 para o sistema]:  '))
    cont += 1
print('Acabou!!!')
print('O resultado da soma é {} e foi adiconado {} números.'.format(y,cont))

