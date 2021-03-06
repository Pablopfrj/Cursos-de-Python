num1 = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
b = num1 + 10*razao
for c in range(num1,b,razao):
    print(c,end=' ')
