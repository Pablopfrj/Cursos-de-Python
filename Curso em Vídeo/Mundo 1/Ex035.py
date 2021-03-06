a = float(input('Digite o valor do segemento de reta'))
b = float(input('Digite o valor do segemento de reta'))
c = float(input('Digite o valor do segemento de reta'))
if a < b + c and b < a + c and c < a + b:
    print('Pode se fazer um triangulo')
else:
    print('O triangulo nao existe')