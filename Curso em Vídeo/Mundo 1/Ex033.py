#Incompleto
a = input('Digite o primeiro numero: ')
b = input('Digite o segundo numero: ')
c = input('Digite o terceiro numero: ')

if a < b < c:
    print('O maior numero é {} \nO menor numero é {}'.format(c, a))
else:
    if a > b > c:
        print('O maior numero é {} \nO menor numero é {}'.format(a, c))
    else:
        if a > c > b:
            print('O maior numero é {} \nO menor numero é {}'.format(a, b))
        else:
            if b > c > a:
                print('O maior numero é {} \nO menor numero é {}'.format(b, a))
            else:
                if c > a > b:
                    print('O maior numero é {} \nO menor numero é {}'.format(c, b))
                else:
                    print('O maior numero é {} \nO menor numero é {}'.format(b, c))
