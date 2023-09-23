num = [[],[]]
valor = 0
for p in range(1,8):
  valor = int(input(f'Digite o {p}ª valor: '))
  if valor % 2 ==0:
    num[0].append(valor)
  else:
    num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os números impares são {num[0]}')
print(f'Os números pares são {num[1]}')
