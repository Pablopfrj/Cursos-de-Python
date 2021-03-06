from time import sleep

print('VAMOS ANALISAR SEU PEDIDO DE EMPRÉSTIMO...')
sleep(2)
csa = float(input('Qual é o valor da casa que o senhor quer? RS '))
sal = float(input('Qual é o seu salário? RS '))
anos = float(input('Quantos anos deseja pagar? '))

prestaçao_mensal = csa/(anos*12)

if prestaçao_mensal >= (sal*1.3):
    print('Sua prestação será de RS {:.2f}.Sinto muito, mas seu empréstimo foi \033[1;31mNEGADO \033[37m!!!'.format(prestaçao_mensal))
else:
    print('Sua prestação será de RS {:.2f}.Parabéns!!, pois seu empréstimo foi \033[1;32mAPROVADO\033[37m!!'.format(prestaçao_mensal))
