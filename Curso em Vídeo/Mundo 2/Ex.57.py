sexo = str(input('DIGITE QUAL É O SEU SEXO [F\M]: ')).strip().upper()[0]

while sexo not in 'FMmf' and not '':
    sexo = str(input('Dados inválidos!! Digite novamente o seu sexo [F\M]: ')).strip()[0]
print('fim')
