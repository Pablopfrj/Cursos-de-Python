num = int(input('Digite um numero inteiro: '))

print('''Digite qual base deseja converter
[ 1 ] Para base BINÁRIA
[ 2 ] Para base HEXADECIMAL
[ 3 ] Para base OCTAL ''')

opçao = int(input('Sua opção: '))

if opçao == 1 :
    print('{} convertido para numero binário é {}'.format(num,bin(num)[2:]))
elif opçao == 2:
    print('{} convertido para numero hexadecimal é {}'.format(num, hex(num)[2:]))
elif opçao == 3:
    print('{} convertido para numero octal é {}'.format(num, oct(num)[2:]))
else:
    print('Número inválido.Tente novamente')
