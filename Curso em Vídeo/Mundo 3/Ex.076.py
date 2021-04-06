print('-'*50)
print(f'{"LISTA DE COMPRAS":^50}')
print('-'*50)

lista = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25,'Transferidor',4.20,
         'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livros',34.90)
for itens in range(0,len(lista)):
    if itens % 2 == 0:
        print(f'{lista[itens]:.<40}', end='')
    else:
        print(f' RS {lista[itens]:>8.2f}')