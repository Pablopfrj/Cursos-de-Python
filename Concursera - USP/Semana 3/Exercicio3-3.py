A = int(input('Digite o primeiro numero : '))

B = int(input('Digite o segundo numero : '))

C = int(input('Digite o terceiro numero : '))

if A==B==C:
    print('inválido')
else:
    if A<B<C:
        print('crescente.')
    else: 
        print('Nao é crescente.')