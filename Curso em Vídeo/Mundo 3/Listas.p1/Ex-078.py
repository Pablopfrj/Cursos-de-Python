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
# .index(x) ➞ Acha a posição do x.
# .count(x) ➞ Conta quantos x's teve.
maior = min = 0
lista = []
for c in enumerate(range(0, 6)):
    lista.append(int(input(f"Digite um valor para a Posição {c}: ")))
    if c == 0:
        maior = min = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < min:
            min = lista[c]

print(f"Vc digitou os valores: {lista}")
print(f"O maior numero é {maior}")
print(f"O menor numero é {min}")
