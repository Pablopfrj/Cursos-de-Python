from random import randint

computador = randint(0, 10)
tentativas=0
print('Sou seu pc...')
print('Pensei num número entre 0 e 10')
print('Tenta adivinhar ai corno')

N_aleatorio = int(input('Qual número vc acha q é ?? '))
while not computador == N_aleatorio:
    if computador > N_aleatorio:
        print('Mais...Tente outra vez')
    elif computador < N_aleatorio:
        print('Menos...Tente outra vez')
    N_aleatorio = int(input('Qual número vc acha q é ?? '))
    tentativas += 1
if computador == N_aleatorio:
    print('Parabéns... Ganhou saporra com {} tentativas.'.format(tentativas))

