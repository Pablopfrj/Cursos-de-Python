nome = str(input('Digite seu nome completo : ')).strip()

nome2 = nome.split()

print('O seu primeiro nome é {}'.format(nome2[0]))

print('Seu ultimo nome é {}'.format(nome2[len(nome2)-1]))
