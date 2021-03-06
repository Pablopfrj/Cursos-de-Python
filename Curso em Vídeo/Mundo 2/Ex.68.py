from random import randint

b = randint(0, 10)

cont = 0
print('=-' * 20)
print('VAMO JOGAR PAR OU ÍMPAR')
print('=-' * 20)
while True:
    a = int(input('Digite um valor: '))
    paridade = str(input('Escolha par ou ímpar [P/I]')).strip().upper()[0]
    c = a + b
    while paridade not in 'PI':
        paridade = str(input('Escolha par ou ímpar [P/I]')).strip().upper()[0]
    if paridade == 'P':
        if c % 2 == 0:
            print('--' * 20)
            print(f'Você jogou {a} e o computador jogou {b}.Total DEU {c}, logo é PAR!!')
            print('--' * 20)
            print('Você VENCEU!!!')
            print('Vamos jogar novamente!!')
            cont += 1
        else:
            print(f'Você jogou {a} e o computador jogou {b}.Total DEU {c},logo é IMPAR!!')

            break
    if paridade == 'I':
        if c % 2 != 0:
            print('--' * 20)
            print(f'Você jogou {a} e o computador jogou {b}.Total DEU {c}, logo é ÍMPAR!!')
            print('--' * 20)
            print('Você VENCEU!!!')
            print('Vamos jogar novamente!!')
            cont += 1
        else:
            print(f'Você jogou {a} e o computador jogou {b}.Total DEU {c}!!')
            break
print('Você PERDEU!!!')
print('=-' * 20)
print(f'GAME OVER!!! Você venceu {cont} partidas.')
print('=-' * 20)