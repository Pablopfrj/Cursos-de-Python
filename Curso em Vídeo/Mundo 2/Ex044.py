n1 = float(input('Qual é o valor do seu produto? '))
n2 = str(input('Vai paga à vista, cartão ou cheque?  ')).strip()

if n2 == 'cartão':
    n3 = str(input('Quantas vezes quer paga à vista, 2x ou 3x?  ')).upper()
    if n3 == 'À VISTA':
        print('O valor do produto é {:.0f} reais'.format(n1*0.95))
    elif n3 == '2X':
        print('O valor do produto será o preço normal {:.0f} reais.'.format(n1))
    elif n3 == '3X':
        print('O valor do produto é {:.0f} reais.'.format(n1*1.2))
else:
    print('O valor do seu produto será {:.0f} reais.'.format(n1*0.90))