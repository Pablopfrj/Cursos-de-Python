k=0
num = int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite mais um valor: ')), int(input('Digite o ultimo valor: '))

print(f'Você digitou os seguinte números: {num}')

print(f'O valor 9 apareceu {num.count(9)}')

if num == 3:
    print(f'O valor 3 apareceu na posição {num.index(3)+1}')
else:
    print('Não possue valor 3.')
print('Os valores pares são ', end='')
for n in num:
    if n % 2 ==0:
        k+=1
        print(n, end=' ')
    
print(f'apareceram {k} vezes')
