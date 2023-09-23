'''linha1 = []
linha2 = []
linha3 = []
valor = 0
for c in range(1,4):
  for i in range(1,4):
    valor = int(input((f'Adicione os numeros na posição {[c,i]} ...: ')))
    if c == 1:
      linha1.append(valor)
    if c == 2:
      linha2.append(valor)
    if c == 3:
      linha3.append(valor)


print(linha1)
print(linha2)
print(linha3)'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
  for c in range(0,3):
    matriz[l][c] = int(input((f'Digite um valor para [{l} , {c}] ...: ')))

for l in range(0,3):
  for c in range(0,3):
    print(f'[{ matriz[l][c] :^4}]', end='' )
  print()
