a = float(input('Digite o valor do primeiro segmento de reta: '))

b = float(input('Digite o valor do segundo segmento de reta: '))

c = float(input('Digite o valor do terceiro segmento de reta: '))

if a < b + c and b < a + c and c < a + b:
    print('Pode se fazer um triangulo ',end='')
    if a == b == c:
        print('e o triangulo é equilátero.')
    elif a == b != c or a == c != b or c == b != a:
        print('e o triangulo é isosceles.')
    else:
        print('e o triangulo é escaleno.')
else:
    print('O triangulo nao existe.')
