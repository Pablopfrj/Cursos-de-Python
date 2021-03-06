ano = int(input('Em que ano você nasceu??  '))

idade = 2017-ano

if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('JUVENIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SÊNIOR')
else:
    print('SENIOR')
