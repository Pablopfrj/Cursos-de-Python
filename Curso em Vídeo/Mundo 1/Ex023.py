'''separador1 = str(input('Digite o numero que quer separar: '))

separador1 = str (separador1)

print('Unidade = {} '.format(separador1[3]))
print('Dezena = {}'.format(separador1[2]))
print('Centena = {}'.format(separador1[1]))
print('Milhar = {}'.format(separador1[0]))'''


separador = int(input('Digite o numero que quer separar: '))

u = (separador % 10)
d = (separador //10) % 10
c = (separador//100) % 10
m = (separador // 1000) % 10


print('Unidade = {} '.format(u))
print('Dezena = {}'.format(d))
print('Centena = {}'.format(c))
print('Milhar = {}'.format(m))