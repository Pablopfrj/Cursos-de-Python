#Acima de 7 é aprovado menor é reprovado

aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['nota'] = float(input('Nota: ')) 

print(f'O é igual a {aluno["nome"]}')

print(f'Média igual a {aluno["nota"]}')

if aluno["nota"] >= 7:
  print(f'Situação é igual a Aprovado')
else:
  print(f' Situação é igual a Reprovado')
