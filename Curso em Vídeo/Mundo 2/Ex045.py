from random import choice

print('\033[32m='*24)

print('VAMO COMEÇAR O JOGO !!!')

print('\033[32m='*24)

n1 = 'Pedra Papel Tesoura'

n2 = n1.upper().split()

ale = choice(n2)

ale2 = input('Escolha Pedra,Papel ou Tesoura: ').upper()
if ale == ale2:
    print('Parabens você ganhou!!!')
else:
    print('Infelizmente, você perdeu! Eu escolhi {}'.format(ale))