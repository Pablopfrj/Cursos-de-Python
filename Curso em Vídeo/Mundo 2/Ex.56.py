maiorhomen = 0
nomevelho = ''

media = 0
for c in range(1, 5):
    print('------- {}º PESSOA -------'.format(c))
    nome = str(input('NOME: ')).strip()
    idade = input('IDADE: ').strip()
    idade = int(idade)
    sexo = str(input('Sexo [F/M]: ')).strip()
    media += idade
    if c == 1 and sexo in 'Mn':
        maiorhomen = idade
    nomevelho = nome
    if sexo in 'Mn' and idade > maiorhomen:
        maiorhomen = idade
    nomevelho = nome
    if sexo in 'Fr' and idade < 20:
        idademulher += 1
mediatot = media / 4
print('A média da idade desses pessoas é {} anos.'.format(mediatot))
print('O homen mais velho se chama {} e tem {} anos.'.format(nomevelho, maiorhomen))
print('Tem {} menores de 20 anos'.format(idademulher))
