matriz = [[0,0,0],[0,0,0],[0,0,0]]
valor = soma_par = soma_terceira = mai = men = 0

for l in range(0,3):
  for c in range(0,3):
    matriz[l][c] = int(input((f'Digite um valor para [{l} , {c}] ...: ')))
    if matriz[l][c] % 2 == 0:
      soma_par += matriz[l][c]
    if l ==2:
      soma_terceira += matriz[2][c]
    if l == 1:
      if matriz[1][c]> mai:
        mai = matriz[1][c]
      if matriz[1][c] < men:
        men = matriz[1][c]


    


for l in range(0,3):
  for c in range(0,3):
    print(f'[{ matriz[l][c] :^4}]', end='' )
  print()

print(f'A soma dos valores pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_terceira}')      
print(f'o maior valor da segunda linha é {mai}')