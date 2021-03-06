print('-' * 30)
print('LOJA QUE VENDE COISAS')
print('-' * 30)
conti = ' '
soma = cont = cont2 = menor = 0
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('RS '))
    soma += preço
    conti = ' '
    cont2 += 1
    while conti not in 'SN':
        conti = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
    if preço > 1000:
        cont += 1
    if cont2 == 1 or preço < menor:
        menor = preço
        nome = produto
    if conti == 'N':
        break
print('--------- FIM DO PROGRAMA ---------')
print(f'O total da compra foi {soma}')
print(f'Tem {cont} produto(s) custando mais de RS 1000,00')
print(f'O produto mais barato é {nome} que custa {menor}')
