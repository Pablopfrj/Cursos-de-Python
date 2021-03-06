'''from math import sqrt

cat_op = int(input('Qual é o valor do cat.oposto: '))

cat_adj = int(input('Qual é o valor do cat.adjacente: '))

hip = sqrt(cat_adj**2 + cat_op**2)

print('A hiponetusa vale {:.0f}'.format(hip))'''


from math import hypot

cat_op = int(input('Qual é o valor do cat.oposto: '))

cat_adj = int(input('Qual é o valor do cat.adjacente: '))

hip = hypot(cat_op,cat_adj)

print('A hiponetusa vale {:.0f}'.format(hip))