from random import randint
from time import sleep
jogo = dict()
a = 1
print(f'{"== VALORES SORTEADOS ==":^30}')

for c in range(1,5):
  num_jogador = f'jogador {c}'
  for _ in range (0,5):
    jogo[num_jogador] = [randint(1,6)]
  print(f'O {num_jogador}° tirou o número: {jogo[num_jogador]}')
  sleep(0.5)
print(jogo)
print(f'{"== RANKING DOS JOGADORES ==":^30}')
jogos2 = dict(sorted(jogo.items(), key=lambda item: item[1], reverse=True))
for k, v in jogos2.items():
    print(f'{a}° lugar: {k} com {v}.')
    a +=1
    sleep(0.7)
