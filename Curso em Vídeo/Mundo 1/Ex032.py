from datetime import date

ano = int(input('Digite o ano.Se colocar 0,será considerado o ano atual: ' ))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and (ano % 100 == 0 or ano % 400 == 0):
    print('Esse ano é bissexto')
else:
    print('Esse ano é bissexto')