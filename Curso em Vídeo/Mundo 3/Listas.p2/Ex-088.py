import random
from time import sleep

num = []
jogos = list()
titulo = ' JOGA NA MEGA SENA'
print('--'*18)
print(titulo.center(36))
print('--'*18)
cont = 0
tot = 1
quant = int(input('Quantos jogos você quer que eu sorteie? '))
'''
while True:
  cont += 1
  print(f'Jogo {cont}:', end=' ')
  num = sorted([random.randint(0, 60) for _ in range(6)])
  print(num)
  sleep(0.75)
  num.clear()
  if cont == quant:
      break
'''
while tot <= quant:
  cont = 0
  while True:
    n = random.randint(1,60)
    if n not in num:
      num.append(n)
      cont += 1
    if cont>=6:
      break
  num.sort()
  jogos.append(num[:])
  num.clear()
  tot+=1
print('-+'*3 , f'SORTEANDO {quant} JOGOS', '-='*3)
for i,l in enumerate(jogos):
  print(f'Jogo {i+1}: {l}')
  sleep(1)
print('-+'*5, '<BOA SORTE!!>', '-+'*5,)
