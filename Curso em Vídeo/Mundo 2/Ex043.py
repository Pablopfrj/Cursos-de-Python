altura = int(input('Digite a sua altura: '))
peso = int(input('Digite o seu peso: '))

IMC = peso/altura**2

if IMC < 18.5:
    print('Abaixo do peso')
elif 18.5 < IMC < 25:
    print('Peso ideal')
elif 25 < IMC < 30:
    print('Sobrepeso')
elif 30< IMC < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')

