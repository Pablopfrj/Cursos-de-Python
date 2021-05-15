y = n = cont = 0

n = int(input('Digite um número [999 para o sistema]:  '))

while True:
    n += y
    y = n
    n = int(input('Digite um número [999 para o sistema]:  '))
    cont += 1
    if n == 999:
        break
print('Acabou!!!')
print('O resultado da soma é {} e foi adicionado {} números.'.format(y, cont))
