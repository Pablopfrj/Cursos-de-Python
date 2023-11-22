jogador = dict()
gols = list()
c = x = 0
jogador['Nome'] = str(input('Nome do jogador: '))
c = int(input(f'Quantas partidas {jogador["Nome"]} fez? '))

for i in range(0,c):
  gols.append(int(input(f'Quantos gols na partida {i+1} ? ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)

print('-='*20)
print(jogador)
print('-='*20)
for v,k in jogador.items():
  print(f'O campo {v} tem valor {k}.')
print('-='*20)

print(f'O jogador {jogador["Nome"]} jogou {c} partidas.')

for c in jogador['gols']:
  print(f'=> Na partida {x+1}, fez {c}')
  x+=1
print(f'Foi um total de {jogador["total"]} gols')







