import math

angulo1 = int(input('Qual é o angulo que deseja saber ?  '))

angulo = math.radians(angulo1)

print('Seno = {:.2f}'.format(math.sin(angulo)))

print('Cosseno = {:.2f}'.format(math.cos(angulo)))

print('Tangente = {:.2f}'.format(math.tan(angulo)))
