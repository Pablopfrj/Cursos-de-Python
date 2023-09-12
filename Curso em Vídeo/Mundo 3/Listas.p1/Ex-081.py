lista = []
c = 0
while True:
    valor = lista.append(int(input('Digite um número: ')))
    cont = str(input('Deseja continuar [S/N]')).lower()
    if cont == 'n':
        break
    c+=1

if c == 0 or c == 1: #PODE SER FEITO COM O COMANDO len() TBM
    print(f'Foram digitados o numero {c} ')
else:
    print(f'Foram digitados {c} numeros')
lista.sort(reverse=True)
print(f'A lista em ordem descrescente é : {lista}')
if lista.count(5) == 0:
    print('Não tem numero 5 na lista')
else:
    print(f'O numero 5 repetiu {lista.count(5)} vez(es).')