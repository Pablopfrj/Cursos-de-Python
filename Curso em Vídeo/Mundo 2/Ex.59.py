from time import sleep

opçao1 = Soma = Multi = 0
x1 = int(input(' Primeiro valor: '))
x2 = int(input(' Segundo valor: '))
while opçao1 != '5':
    print('[ 1 ] Somar ')
    print('[ 2 ] Multipicar ')
    print('[ 3 ] Maior ')
    print('[ 4 ] Novos números ')
    print('[ 5 ] Sair do programa ')
    opçao1 = str(input('>>> Qual opçao deseja usar?  '))
    print('=-' * 30)
    if opçao1 == '1':
        Soma = x1 + x2
        print('A soma dos dois numeros é {}'.format(Soma))
    elif opçao1 == '2':
        Multi = x1 * x2
        print('A multiplicaçao dos dois numeros é {}'.format(Multi))
    elif opçao1 == '4':
        print('Ok,estamos resentando as informaçoes,tente com outros números agora!')
        sleep(1.23)
        x1 = int(input(' Primeiro valor: '))
        x2 = int(input(' Segundo valor: '))
    elif opçao1 == '3' and x1 > x2:
        print('O maior é {}'.format(x1))
    elif opçao1 == '3' and x1 < x2:
        print('O maior é {}'.format(x2))
    else:
        print('Número Inválido!!')
    print('=-' * 30)
    sleep(1.5)
print('Finalizando...')
sleep(0.75)
print('O programa foi finalizado,volte sempre!!!')
