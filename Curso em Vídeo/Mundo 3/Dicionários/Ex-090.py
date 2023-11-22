#Acima de 7 é aprovado menor é reprovado

'''aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['nota'] = float(input('Nota: ')) 

print(f'O é igual a {aluno["nome"]}')

print(f'Média igual a {aluno["nota"]}')

if aluno["nota"] >= 7:
  print(f'Situação é igual a Aprovado')
else:
  print(f' Situação é igual a Reprovado')'''

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno["media"] >= 7:
  aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
  aluno['Situação'] = 'Recuperação'
else:
  aluno['Situação'] = 'Reprovado'

for k,v in aluno.items():
  print(f' - {k} é igual a {v}')
