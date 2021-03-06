cont = n = 0
while True:
    print('--' * 10)
    n = int(input('Qual número deseja ver a tabuada: '))
    if n < 0:
        break
    print('--' * 10)
    for c in range(1, 11):
        print(f'{c} X {n} = {c*n}')
print('PROGRAMA FINALIZADO!!!')