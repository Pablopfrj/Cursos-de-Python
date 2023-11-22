cadastro = dict()
info = list()

while True:
    # CADASTRANDO O NOME
    cadastro['Nome'] = str(input('Nome: '))
    
    # CADASTRANDO O SEXO
    while True:
        cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper()
        if cadastro['sexo'] in 'MF':
            break
        else:
            print('ERROR: Sexo inválido')

    # CADASTRANDO A IDADE
    cadastro['idade'] = int(input('Idade: '))

    while True:
        c = str(input('Quer continuar? [S/N] ')).upper()
        if c in 'SN':
            break
        else:
            print('ERROR: Entrada inválida')
    
    if c == 'N':
        break

# O restante do código continua aqui, se houver alguma ação que você deseja executar após o cadastro.
