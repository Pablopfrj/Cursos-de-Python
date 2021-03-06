frase = str(input('Digite uma frase: ')).strip()

print(frase.upper().count('A'))
print('A letra A apareceu primeiramente em {}'.format(frase.find('A')+1))
print('A ultima vez que a porra do A apareceu é {}'.format(frase.rfind('A')+1))

