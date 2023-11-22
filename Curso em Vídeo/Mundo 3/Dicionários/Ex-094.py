
#Cadastrar num dicionario e desse dicionario jogar na lista

cadastro = dict()
info = list()
c = ''
soma = media = 0
while True:
  #CADASTRANDO O NOME
  cadastro['Nome'] = str(input('Nome: '))
    #CADASTRANDO O SEXO
  while True:
    cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper()
    if cadastro['sexo']  in 'MF':
      break
    else:
      print('ERROR: Invalid cadastro')
  #CADASTRANDO A IDADE
  cadastro['idade'] = int(input('Idade: '))
  soma += cadastro['idade']
  info.append(cadastro.copy())
  while True:
    c = str(input('Quer continuar? [S/N] ')).upper()
    if c in 'SN':
      break
    else:
      print('ERROR: Entrada inválida')
  if c == 'N':
    break
print('-='*30)
print(f'A) Ao todo {len(info)} pessoas cadastradas')
media = soma/len(info)
print(f'B) A média da idade é de {media:5.1f}')
print('As mulheres cadastradas foram ', end='')
for p in info:
  if p['sexo'] == 'F':
    print(f'{p["Nome"]}', end=' ')
print()
print('Lista das pessoas que estão acima da média')
for p in info:
  if p['idade'] >= media:
    print('  ')
    for k,v in p.items():
      print(f'{k} = {v}')
print('<<ENCERRADO>>')







  
      
