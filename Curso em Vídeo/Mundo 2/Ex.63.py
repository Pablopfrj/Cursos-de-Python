print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
y = int(input('Quantos termos você que mostrar? '))
t1 = 0
t2 = 1
cont = 3
print('{} -> {} '.format(t1,t2),end='')
while cont <= y:
    t3 = t2 + t1
    cont += 1
    t1 = t2
    t2 = t3
    print(' -> {}'.format(t3),end='')
print(' -> FIM')