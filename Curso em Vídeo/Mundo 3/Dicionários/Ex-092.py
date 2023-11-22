from datetime import datetime
cadastro = dict()

cadastro['nome'] = str(input('Nome: '))
cadastro['idade'] = (datetime.now().year - int(input('Nascimento: ')))
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem):'))

if cadastro['ctps'] != 0:
  cadastro['contratação'] = int(input('Ano da Contratação: '))
  cadastro['Salário'] = int(input('Salário R$: '))
  cadastro['Aposentadoria'] = cadastro['idade'] + ((cadastro['contratação'] + 35) - datetime.now().year)

for k, v in cadastro.items():
  print(f'- {k} tem valor de {v}')

