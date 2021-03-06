merda = int(input('Digite a quantidade de dias que utlizou o carro: '))
dias = float(input('Digite a quantidade de Km que utlizou o carro: '))

preço1 = merda * 60
preço2 = dias * 0.15

preçoT = preço1 + preço2

print('O valor total a se pagar é {:.2f}'.format(preçoT))
