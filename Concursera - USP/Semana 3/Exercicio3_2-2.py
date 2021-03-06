Nqualquer = int(input('Digite o número desejado : '))

if (Nqualquer % 3) == 0 :
    print('Fizz')

else :
    if (Nqualquer % 5) == 0:
        print('Buzz')
    else :
        print(Nqualquer)