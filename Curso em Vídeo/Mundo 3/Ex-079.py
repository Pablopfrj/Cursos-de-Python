# list(range(x,y))  ➞ cria uma lista de x a y-1
# .append() ➞ Adiciona elementos na lista
# .sort() ➞ Coloca a lista em ordem crescente
# .sorte(reverse=True)  ➞ Coloca a lista em ordem decrescente
# .insert(x,y)  ➞ Adiciona o valor y na posição x
# del x[y]  ➞ Na lista x elimina o parametro y.
# .pop() ou .pop(x) ➞ Eliminha o ultimo valou ou o valor que foi dado como parametro x.
# .remove(x)  ➞ Elimina a primeira ocorrencia do parametro dado.
# enumerate()  ➞ Pega tanto a chave quanto o valor
# Igual uma lista, o py cria uma ligação entre elas, logo se muda alguma coisa em uma muda na outra.
# x = y[:]  ➞ Faz uma copia entre as listas.
lista = []
'''
c = 0
while True:
    valor = lista.append(int(input("Digite um valor: ")))
    conti = input("Deseja continuar? [S/N] ")
    if conti in 'Nn':
     break
    while c < len(lista):
        j = c + 1
        while j < len(lista):
            if lista[j] == lista[c]:    
                print("Valor Duplicado, não adicionado!!!")
                del(lista[j])
            else:
                print('Valor adicionado com sucesso...')
                j += 1
            c += 1
print(f"Sua lista completa adicionados foi {lista}")'''

'''conti = 's'
while conti in 'Ss':
    valor = lista.append(int(input("Digite um valor: ")))
    conti = str(input("Deseja continuar? [S/N] ")).lower()
    if conti == 'n':
        break
lista = set(lista)
lista = list(lista)
lista.sort()
print(f"Sua lista completa adicionados foi {lista}.")'''

numeros = list()
while True:
    valor = int(input("Digite um valor: "))
    if valor not in numeros:
        numeros.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print("Valor Duplicado, não adicionado!!!")
    conti = str(input("Deseja continuar? [S/N] ")).lower()
    if conti == 'n':
        break
numeros.sort()
print(f"Sua lista é {numeros}")
