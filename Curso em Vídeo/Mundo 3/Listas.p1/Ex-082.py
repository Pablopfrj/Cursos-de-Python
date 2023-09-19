completa = []
impares = []
pares = []
cont = 's'
while cont in 'Ss':
  num = int(input('Digite um número: '))
  completa.append(num)
  if num % 2 == 0:
    pares.append(num)
  else:
    impares.append(num)
  cont = str(input('Quer continuar? [S/N]'))

print('-=-'*20)
print(f'A lista completa é {completa}')
print(f'A lista de pares é {sorted(pares)}')
print(f'A lista de impares é {sorted(impares)}')


