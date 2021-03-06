velo = float(input('Digite a velocidade do seu carro: '))
if velo > 80 :
     print('Fez merda cria,foi multado, \nA multa é {:.2f} reais.'.format((velo - 80)*7.00))
else:
    print('Nao foi multado,parabens nao fez merda')

