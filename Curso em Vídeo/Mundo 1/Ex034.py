salario = float(input('Qual é o valor do seu salario? '))

if salario > 1250:
    print('Seu novo salario será de {}'.format(salario*1.1))
else:
    print('Seu novo salario será de {}'.format(salario*1.15))