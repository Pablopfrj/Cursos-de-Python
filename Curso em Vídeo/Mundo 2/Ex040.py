nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

print ('Sua média é igual à {}'.format(media))

if media >= 7.0:
    print('Tá aprovado!!!')
elif 5 < media <= 6.9:
    print('Tá de recuperação!!')
else:
    print('Tá reprovado!!')