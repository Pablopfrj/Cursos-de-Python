nome = (input('Digite seu nome completo: ')).strip()

print('Seu nome em maiusculo é {}'.format(nome.upper()))

print('Seu nome em minusculo é {}'.format(nome.lower()))

#print('Seu primeiro nome tem ao todo {} letras '.format(nome.find(' ')))

print('Seu nome tem ao todo {} letras '.format(len(nome)- nome.count(' ')))

primeiro = nome.split()

print('Seu primeiro nome tem {} letras'.format(len(primeiro[0])))
