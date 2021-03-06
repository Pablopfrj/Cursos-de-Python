cont = cont1 = cont2 = total = 0
while True:
    print('--' * 20)
    print('CADASTRO DE PESSOAS')
    print('--' * 20)
    idade = int(input('Idade:  '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        cont1 += 1
    if sexo == 'F' and idade < 20:
        cont2 += 1
    continualidade = ' '
    while continualidade not in 'SN':
        continualidade = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if continualidade == 'N':
            break
print(f'Total de pessoas cadastradas {total}.')
print(f'Total de pessoas cadastradas com menos de 18 anos: {cont}')
print(f'Ao todo temos {cont1} homens cadastrado(s)')
print(f'E temos {cont2} mulher(s) com menos de 20 anos. ')
