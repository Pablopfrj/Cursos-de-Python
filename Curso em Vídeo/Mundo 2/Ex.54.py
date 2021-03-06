from datetime import date
hj = date.today().year
idademaior = 0
idademenor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {} nasceu? '.format(c)))
    idade = hj - ano
    if idade < 18:
        idademenor += 1
    else:
        idademaior += 1
print('Ao todo tem {} de maior e {} de menor !!'.format(idademaior, idademenor))