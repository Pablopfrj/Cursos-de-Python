lista_de_material = ('Lápis',1.75,
'Borracha',2,
'Caderno',15.9,
'Estojo',25,
'Transferidor',4.2,
'Compasso',9.99,
'Mochila',120.32,
'Canetas',22.3,
'Livro',34.8)

print('-'*40)
print (f'{"LISTA DE PREÇO":^40}')
print('-'*40)
for pos in range (0,len(lista_de_material)):
    if pos % 2 ==0  :
        print(f'{lista_de_material[pos]:.<30}', end='')
    else:
        print(f'RS {lista_de_material[pos]:>7.2f}')

print('_'*40)