Ds = float(input('Qual é a distancia que vc percorreu? : '))

if Ds < 200:
    print('O valor da sua passagem é {:.1f}'.format(Ds*0.50))

else :
    print('O valor da sua passagem é {:.2f} ,porque é mais longa'.format(Ds*0.45))