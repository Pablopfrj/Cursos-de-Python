import random

from time import sleep

print('-=-'*20)
print('VOU PENSAR NUM NUMERO DE 1 A 5.TENTE ADIVINHAR...')
print('-=-'*20)

numero = int(input('Escolha um número de 0 á 5 : '))


numero2 = int(random.choice('012345'))

print('PROCESSANDO...')
sleep(2)
if numero > 5:
    print('Claro que perdeu,A mula nao sabe ler nao ? \nO numero é de 0 á 5.')
else:
    if numero2 == numero:
        print('Parabens vc ganhou!!! ')
    else:
        print('Errou rude,errou feio!!')
        print('O valor que eu escolhi é {} !,mais sorte na próxima.'.format(numero2))
